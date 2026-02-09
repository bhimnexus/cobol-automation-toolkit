# Chapter 13 — PERFORM Statement & Looping Constructs
IBM Enterprise COBOL (z/OS)

---

## 1. PERFORM Statement — Introduction

### Purpose

The `PERFORM` statement is used to:

- Execute a paragraph or section
- Implement loops
- Reuse logic
- Control program flow without `GO TO`

📌 `PERFORM` is the **foundation of structured programming in COBOL**.

---

## 2. Simple PERFORM

### Purpose

Executes a paragraph once and returns control to the next statement.

---

### Syntax

```cobol
PERFORM paragraph-name
```
## Example

```cobol
PERFORM DISPLAY-MSG
DISPLAY 'END OF PROGRAM'
STOP RUN.

DISPLAY-MSG.
   DISPLAY 'HELLO FROM PERFORM'.
```
## 3. Inline PERFORM (END-PERFORM)

### Purpose

- Groups statements together without using a separate paragraph
- Equivalent to `DO...END` in other languages

---

### Syntax

```cobol
PERFORM
   statement-1
   statement-2
END-PERFORM
```
## 4. PERFORM UNTIL (Looping)

### Purpose

- Repeats execution until a condition becomes true

---

### Syntax

```cobol
PERFORM paragraph-name
   UNTIL condition
```
### Example 
```cobol
PERFORM READ-NEXT
   UNTIL WS-EOF = 'Y'
```
📌 Condition is checked before execution by default.
## 5. TEST BEFORE vs TEST AFTER

### TEST BEFORE (Default)

- Condition is checked first
- Paragraph may not execute at all

```cobol
PERFORM PARA-1
   UNTIL condition
```
## TEST AFTER
- Paragraph executes at least once
```cobol
PERFORM PARA-1
   WITH TEST AFTER
   UNTIL condition
```
📌 Equivalent to DO-WHILE vs DO-UNTIL.

## 6. PERFORM VARYING (Counter Loop)

### Purpose

- Implements counted loops (FOR-loop equivalent)

---

### Syntax

```cobol
PERFORM paragraph-name
   VARYING index
   FROM start-value
   BY increment
   UNTIL condition
```
### Example 
```cobol
PERFORM DISPLAY-ITEM
   VARYING WS-I FROM 1 BY 1
   UNTIL WS-I > 5
```
## 7. Nested PERFORM VARYING

### Purpose

- Used for processing tables or multi-dimensional arrays

---

### Example

```cobol
PERFORM PARA-1
   VARYING I FROM 1 BY 1 UNTIL I > 10
   AFTER J FROM 1 BY 1 UNTIL J > 5
```
📌 Common in table processing logic.

## 8. PERFORM THRU (Legacy – Use Carefully)
### Purpose

- Executes a range of paragraphs.

### Syntax
```cobol
PERFORM PARA-1 THRU PARA-5
```

⚠️ Risky if paragraphs are reordered.
📌 Allowed but discouraged in modern structured code.


## 9. EXIT Statement

### Purpose

- Marks the logical end of a paragraph

---

### Example

```cobol
PROCESS-DATA.
   IF WS-ERROR = 'Y'
      EXIT
   END-IF
   ADD 1 TO WS-COUNT.
```
📌 EXIT performs no operation — it improves readability only.

## 10. PERFORM vs GO TO (Interview Favorite)

| Aspect | PERFORM | GO TO |
|------|---------|-------|
| Control flow | Structured | Unstructured |
| Readability | High | Poor |
| Maintenance | Easy | Difficult |
| Recommendation | ✅ Always use | ❌ Avoid |

---

## 11. Common Interview Traps

- ❌ Forgetting loop termination
- ❌ Infinite `PERFORM UNTIL` loops
- ❌ Using `PERFORM THRU` blindly
- ❌ Modifying loop variables incorrectly
- ❌ Mixing `GO TO` with `PERFORM`

---

## 12. Best Practices

- Prefer `PERFORM` over `GO TO`
- Use `END-PERFORM` for inline logic
- Keep loops simple and readable
- Always ensure loop termination
- Use `PERFORM VARYING` for counters

---

## 13. Key Points to Remember

- `PERFORM` enables structured programming
- Supports reuse, looping, and flow control
- `PERFORM VARYING` replaces FOR-loops
- Avoid `GO TO` in modern COBOL
- Mastery of `PERFORM` = **clean, maintainable code**
