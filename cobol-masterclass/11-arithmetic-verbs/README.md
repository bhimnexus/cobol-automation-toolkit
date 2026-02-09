# Chapter 11 — Arithmetic Verbs
## ADD, SUBTRACT, MULTIPLY, DIVIDE, COMPUTE

Arithmetic verbs in COBOL are used to perform numeric calculations.
They are **highly interview-critical** and **widely used in production systems**.

This chapter explains:
- All arithmetic verbs
- Syntax variants
- Rounding and truncation rules
- ON SIZE ERROR handling
- Common interview traps and best practices

---

## 1. Arithmetic Verbs Overview

COBOL provides the following arithmetic verbs:

- ADD
- SUBTRACT
- MULTIPLY
- DIVIDE
- COMPUTE

📌 These verbs operate **only on numeric data items**.

---

## 2. ADD Statement

### Purpose

Adds one or more values to another value.

---

### Syntax Variants

```cobol
ADD A TO B
ADD A B TO C
```
### Examples
```cobol
01 A PIC 9(02) VALUE 10.
01 B PIC 9(02) VALUE 20.

ADD A TO B.
```

### Result
```cobol
B = 30
```
```cobol
ADD A B GIVING C.
```

📌 GIVING preserves the original operands.

## 3. SUBTRACT Statement

### Purpose

Subtracts one or more values from another value.

---

### Syntax Variants

```cobol
SUBTRACT A FROM B
SUBTRACT A B FROM C
SUBTRACT A B FROM C GIVING D
```

### Example
```cobol
01 A PIC 9(02) VALUE 4.
01 B PIC 9(02) VALUE 20.
```
```cobol
DIVIDE A INTO B.
```
```
Result
B = 5
```

#### Example with REMAINDER
```cobol
DIVIDE 3 INTO 10
   GIVING QUOTIENT
   REMAINDER REM.
```

## 6. COMPUTE Statement

### Purpose

Performs complex arithmetic expressions using operators.

---

### Operators Supported
```
| Operator | Meaning |
|--------|--------|
| + | Addition |
| - | Subtraction |
| * | Multiplication |
| / | Division |
| ** | Exponentiation |
```
---

### Example

```cobol
01 A PIC 9(03) VALUE 10.
01 B PIC 9(03) VALUE 5.
01 C PIC 9(04).

COMPUTE C = (A + B) * 2.

Result
C = 30
```

---

## 7. Operator Precedence (Very Important)

Order of evaluation:

1. Parentheses
2. Exponentiation (`**`)
3. Multiplication and Division
4. Addition and Subtraction

📌 Same as standard mathematics.

---

## 8. ROUNDED Option

### Purpose

Controls rounding of arithmetic results.

---

### Example

```cobol
ADD A TO B ROUNDED.
```
📌 Without ROUNDED, COBOL truncates extra decimal places.

⚠️ Avoid using ROUNDED in intermediate calculations.


---

## 9. Truncation Behavior

- COBOL truncates, **not rounds**, by default
- Truncation occurs **silently**
- Left-side digits are lost if the result exceeds target size

📌 This is a **major source of production defects**.

---

## 10. ON SIZE ERROR

### Purpose

Handles overflow or truncation in arithmetic operations.

---

### Example

```cobol
ADD A TO B
   ON SIZE ERROR
      DISPLAY 'SIZE ERROR OCCURRED'
END-ADD
```

📌 If SIZE ERROR occurs:

Arithmetic operation is not executed

Control transfers to ON SIZE ERROR


---

## 11. Explicit Scope Terminators

Each arithmetic verb has an explicit END form:

- END-ADD
- END-SUBTRACT
- END-MULTIPLY
- END-DIVIDE
- END-COMPUTE

📌 Always preferred over the period (`.`).

---

## 12. Common Interview Traps

❌ Forgetting default truncation  
❌ Using edited fields in arithmetic  
❌ Ignoring `ON SIZE ERROR`  
❌ Misunderstanding operand modification  
❌ Using `COMPUTE` with careless `ROUNDED`

---

## 13. Best Practices

- Use `GIVING` to preserve operands
- Use `COMP-3` for financial arithmetic
- Always consider `ON SIZE ERROR`
- Prefer explicit scope terminators
- Keep arithmetic logic simple and readable

---

## 14. Key Points to Remember

- Arithmetic verbs work only on numeric data
- Default behavior is truncation
- `COMPUTE` is powerful but risky if misused
- `SIZE ERROR` handling is essential
- Arithmetic mastery = **production-ready COBOL skill**

---

