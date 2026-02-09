# Chapter 8 — PICTURE Clause & Data Types  
*(Deep + Interview Critical)*

---

## 1. Introduction

The **PICTURE clause (PIC)** is one of the **most important and most tested** concepts in COBOL.

It defines:
- The **type of data**
- The **size of data**
- The **format of data**
- How data is **stored and displayed**

📌 A strong understanding of PIC clauses is **mandatory** for:
- Production support
- Performance tuning
- Banking and financial applications
- COBOL interviews

---

## 2. Purpose of the PICTURE Clause

The `PICTURE` clause specifies the **characteristics of a data item**, including:

- Whether data is numeric or alphanumeric
- Number of digits or characters
- Presence of sign
- Decimal position (real or implied)
- Editing and formatting rules

---

## 3. Categories of Data Types in COBOL

COBOL data types can be broadly classified into:

1. Numeric
2. Numeric Edited
3. Alphabetic
4. Alphanumeric
5. Alphanumeric Edited

---

## 4. Numeric Data Type

### Definition

Numeric data items:
- Contain **digits only**
- May include a **sign**
- Used for calculations

---

### Common Numeric Picture Symbols

| Symbol | Meaning |
|------|--------|
| `9` | Digit |
| `S` | Sign |
| `V` | Implied decimal point |

---

### Examples

```cobol
05 WS-COUNT    PIC 9(03).
05 WS-AMOUNT   PIC 9(05)V99.
05 WS-BALANCE  PIC S9(07).
```
📌 V does not occupy storage — it is an implied decimal.

## 5. Numeric Edited Data Type

### Purpose

Numeric edited items are used for **displaying numeric data in a readable format**.

📌 They are **not suitable for calculations**.

---

### Common Editing Symbols

| Symbol | Meaning |
|------|--------|
| `Z` | Zero suppression |
| `,` | Comma |
| `.` | Decimal point |
| `$` | Currency symbol |
| `+` | Plus sign |
| `-` | Minus sign |
| `*` | Asterisk fill |
| `CR` / `DB` | Credit / Debit |

---

### Examples

```cobol
05 WS-DISPLAY-AMT PIC $ZZZ,ZZ9.99.
05 WS-DISPLAY-BAL PIC -ZZZ,ZZ9.
```

---

## 6. Alphabetic Data Type

### Definition

Alphabetic data items:

- Contain **only letters and spaces**
- Cannot contain **digits or special characters**

---

### Symbol

| Symbol | Meaning |
|------|--------|
| `A` | Alphabetic character |

---

### Example

```cobol
05 WS-NAME PIC A(20).
```

---

## 7. Alphanumeric Data Type

### Definition

Alphanumeric data items:

- Can contain **letters, digits, spaces, and special characters**
- Are the **most commonly used data type** in COBOL

---

### Symbol

| Symbol | Meaning |
|------|--------|
| `X` | Any character |

---

### Examples

```cobol
05 WS-ADDRESS PIC X(50).
05 WS-STATUS  PIC X.
```

---

## 8. Alphanumeric Edited Data Type

### Purpose

Used to:

- Format alphanumeric output
- Insert spaces or fixed characters

📌 Less commonly used compared to numeric edited fields.

---

### Example

```cobol
05 WS-EMP-CODE PIC XXX-XXXX.
```

---

## 9. Sign Handling (`S` and SIGN Clause)

### Signed Numeric Items

- `S` indicates **signed data**
- Sign can be:
  - Leading
  - Trailing
  - Separate or non-separate

---

### Default Behavior

- Trailing
- Non-separate
- Stored in the **last digit position**

---

### Example

```cobol
05 WS-SIGNED-AMT PIC S9(05).
```
### SIGN Clause Example
```cobol
05 WS-AMT PIC S9(05) SIGN IS LEADING SEPARATE.
```

---

## 10. Storage Considerations (Interview Favorite)

### DISPLAY (Default)

- One byte per character
- Easy to read
- Slower arithmetic

```cobol
PIC 9(05)
```
## COMP (Binary)

### Characteristics

- Uses **binary representation**
- Provides **faster arithmetic** than DISPLAY
- Suitable for counters and calculations
- `PIC` must contain **only `9` and optional `S`**

---

### Storage Requirement

| Digits | Storage |
|------|---------|
| 1–4 | Halfword (2 bytes) |
| 5–9 | Fullword (4 bytes) |
| 10–18 | Doubleword (8 bytes) |

---

### Example

```cobol
05 WS-COUNT PIC S9(09) COMP.
```

---


## COMP-3 (Packed Decimal)

### Characteristics

- Stores **two digits per byte**
- Last nibble stores the **sign**
- Very common in **banking and financial applications**
- More storage-efficient than DISPLAY

---

### Storage Formula

---

### Example

```cobol
05 WS-AMOUNT PIC S9(07) COMP-3.
```

---

## 11. USAGE vs PICTURE (Interview Trap)

- `PICTURE` → Defines the **logical format**
- `USAGE` → Defines the **physical storage**

📌 Both together determine **how data is stored, processed, and displayed**.

## 12. Common Interview Pitfalls

- Using numeric edited fields for calculations ❌
- Forgetting that `V` does **not occupy storage** ❌
- Miscalculating `COMP-3` storage ❌
- Using `DISPLAY` for heavy arithmetic ❌

## 13. Best Practices

- Use `DISPLAY` for input and output fields
- Use `COMP-3` for financial calculations
- Avoid unnecessary numeric editing
- Keep `PIC` definitions simple and readable
- Always align data definitions with business meaning

