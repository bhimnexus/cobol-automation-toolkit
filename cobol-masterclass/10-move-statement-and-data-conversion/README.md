# Chapter 10 — MOVE Statement, Data Conversion & Truncation Rules  
*(Deep + Tricky + Interview Critical)*

---

## 1. Introduction

The `MOVE` statement is the **most frequently used statement in COBOL**.

It is deceptively simple but responsible for:
- Data conversion
- Data alignment
- Truncation
- Many production defects and abends

📌 A strong understanding of `MOVE` rules is **mandatory** for:
- Production support
- Debugging data issues
- COBOL interviews

---

## 2. Purpose of the MOVE Statement

The `MOVE` statement is used to:

- Transfer data from one field to another
- Assign literal values to variables
- Initialize or reset data items

---

## 3. Basic Syntax

```cobol
MOVE source TO destination
```
Multiple destinations are allowed:
```cobol
MOVE source TO dest-1 dest-2 dest-3
```

## 4. Categories of MOVE Operations

MOVE behavior depends on the **data types involved**:

- Numeric → Numeric
- Alphanumeric → Alphanumeric
- Alphanumeric → Numeric
- Numeric → Alphanumeric
- Group MOVE

📌 Each category follows **different rules**.

---
## 5. Numeric to Numeric MOVE

### Rules

- Decimal points are **aligned**
- Data is copied **right to left**
- Unfilled positions are filled with **zeros**
- Excess digits are **truncated**

---

### Example

```cobol
01 A PIC 9(03)V99 VALUE 12.34.
01 B PIC 9(05)V99.

MOVE A TO B.
```
### Result
```cobol
B = 012.34
```
### Truncation Example
```cobol
01 A PIC 9(05)V99 VALUE 12345.67.
01 B PIC 9(03)V99.

MOVE A TO B.
```
### Result
```
B = 345.67   (Left-side digits truncated)
```


---

## 6. Alphanumeric to Alphanumeric MOVE

### Rules

- Data moves **left to right**
- Unfilled positions are filled with **spaces**
- Excess characters on the right are **truncated**

---

### Example

```cobol
01 A PIC X(10) VALUE 'COBOL'.
01 B PIC X(15).

MOVE A TO B.
```

### Result
```cobol
B = 'COBOL          '
```

### Truncation Example
```cobol
01 A PIC X(10) VALUE 'MAINFRAME'.
01 B PIC X(4).

MOVE A TO B.
```
### Result
```cobol
B = 'MAIN'
```


---

## 7. Numeric to Alphanumeric MOVE

### Rules

- Numeric value is converted to **DISPLAY format**
- Result is **right-justified**
- Left padded with **spaces**

---

### Example

```cobol
01 A PIC 9(04) VALUE 25.
01 B PIC X(6).

MOVE A TO B.
```
### Result
```cobol
B = '    25'
```

---

## 8. Alphanumeric to Numeric MOVE (Very Dangerous)

### Rules

- Source must contain **valid numeric characters only**
- Spaces are ignored
- Any invalid character causes **data exception (S0C7)**

---

### Example (Valid)

```cobol
01 A PIC X(04) VALUE '0123'.
01 B PIC 9(04).

MOVE A TO B.
```
### Result
```cobol
B = 0123
```
### Example (Invalid → ABEND)

```cobol
01 A PIC X(04) VALUE '12A4'.
01 B PIC 9(04).

MOVE A TO B.   *> S0C7 ABEND
```
📌 One of the most common production abends.


---

## 9. Group MOVE

### Rules

- Entire group treated as **alphanumeric**
- No regard for individual field types
- Bytes are copied **as-is**

---

### Example

```cobol
01 A.
   05 A-NUM  PIC 9(04).
   05 A-CHAR PIC X(06).

01 B.
   05 B-NUM  PIC 9(04).
   05 B-CHAR PIC X(06).

MOVE A TO B.
```
📌 No numeric alignment or validation happens in Group MOVE.


---

## 10. MOVE CORRESPONDING

### Purpose

Moves fields with **same names** from one group to another.

---

### Syntax

```cobol
MOVE CORRESPONDING group-1 TO group-2
```
### Example
```cobol
01 EMP-A.
   05 ID   PIC 9(04).
   05 NAME PIC X(10).

01 EMP-B.
   05 ID   PIC 9(04).
   05 NAME PIC X(10).

MOVE CORRESPONDING EMP-A TO EMP-B.
```
📌 Only matching field names are moved.


---

## 11. MOVE and EDITED FIELDS

### Important Rules

- Edited fields must **never** be used in calculations
- MOVE **into** edited fields is allowed
- MOVE **from** edited fields to numeric is risky

---

### Example

```cobol
01 A PIC 9(05)V99 VALUE 123.45.
01 B PIC $ZZZ,ZZ9.99.

MOVE A TO B.
```
### Result
```
B = $  123.45
```

---

## 12. Truncation Rules Summary

| Scenario | What Gets Truncated |
|--------|---------------------|
| Numeric → Numeric | Left-side digits |
| Alphanumeric → Alphanumeric | Right-side characters |
| Group MOVE | Raw bytes |

📌 Truncation **does not raise an error by default**.

---

## 13. ON SIZE ERROR (Protection)

### Purpose

Detects truncation or overflow in **arithmetic operations**.

📌 Not directly applicable to `MOVE`,  
but critical when conversion happens via arithmetic.

---

### Example

```cobol
ADD A TO B
   ON SIZE ERROR
      DISPLAY 'SIZE ERROR'
END-ADD
```

---

## 14. Common Interview Traps

❌ Assuming `MOVE` does validation  
❌ Forgetting numeric alignment rules  
❌ Using alphanumeric → numeric MOVE blindly  
❌ Confusing group MOVE with elementary MOVE  
❌ Ignoring silent truncation  

---
## 15. Best Practices

- Validate data before numeric MOVE
- Avoid alphanumeric → numeric MOVE where possible
- Use group MOVE only when layouts are identical
- Be explicit about field sizes
- Log or handle truncation-sensitive logic

---






