# Chapter 12 — IF Statement, Conditions & EVALUATE
IBM Enterprise COBOL (z/OS)

---

## 1. IF Statement — Introduction

### Purpose

The `IF` statement is used to **control program flow** based on conditions.

It allows the program to:
- Make decisions
- Choose different execution paths
- Implement business rules

📌 `IF` is the **most frequently used control statement** in COBOL.

---

## 2. Basic IF Syntax

```cobol
IF condition
   imperative-statement
END-IF
```
### Example
```cobol
IF WS-COUNT > 0
   DISPLAY 'COUNT IS POSITIVE'
END-IF
```
📌 END-IF is the explicit scope terminator and is strongly recommended.

## 3. IF–ELSE Syntax
```cobol
IF condition
   statement-block-1
ELSE
   statement-block-2
END-IF
```
### Example
```cobol
IF WS-AMOUNT >= 1000
   DISPLAY 'HIGH VALUE'
ELSE
   DISPLAY 'LOW VALUE'
END-IF
```
## 4. Nested IF Statements
### Purpose
Used when decisions depend on multiple conditions.

### Example
```cobol
IF WS-A > 0
   IF WS-B > 0
      DISPLAY 'BOTH POSITIVE'
   ELSE
      DISPLAY 'A POSITIVE, B NOT'
   END-IF
END-IF
```
📌 Avoid deep nesting — it reduces readability.

## 5. Relational Conditions
### Supported Operators
```
Operator	Meaning
=	Equal
>	Greater than
<	Less than
>=	Greater than or equal
<=	Less than or equal
<>	Not equal
```

### Example
```cobol
IF WS-SALARY <> 0
   DISPLAY 'SALARY PRESENT'
END-IF
```
## 6. Logical Conditions (AND / OR)
####Rules
AND is evaluated before OR
```
Parentheses override precedence
```
### Example
```cobol
IF WS-A > 0 AND WS-B > 0
   DISPLAY 'BOTH POSITIVE'
END-IF
```
### With Parentheses
```cobol
IF (WS-A > 0 OR WS-B > 0) AND WS-C = 'Y'
   DISPLAY 'CONDITION MET'
END-IF
```
## 7. Negated Conditions (NOT)
### Purpose
Reverses the result of a condition.

### Example
```cobol
IF NOT WS-EOF
   PERFORM READ-NEXT
END-IF
```
📌 NOT NEGATIVE is not the same as POSITIVE (ZERO is neither).

## 8. Sign Test
### Purpose
Checks the sign of numeric data.

### Syntax
```cobol
IF identifier IS POSITIVE
IF identifier IS NEGATIVE
IF identifier IS ZERO
```
### Example
```cobol
IF WS-BALANCE IS NEGATIVE
   DISPLAY 'OVERDRAFT'
END-IF
```
## 9. Class Test
### Purpose
Validates data content.

#### Built-in Classes
```cobol
NUMERIC
ALPHABETIC
ALPHABETIC-UPPER
ALPHABETIC-LOWER
```
### Example
```cobol
IF WS-INPUT IS NUMERIC
   MOVE WS-INPUT TO WS-AMOUNT
ELSE
   DISPLAY 'INVALID NUMBER'
END-IF
```
## 10. Condition Names (88 Level Usage)
### Purpose
### Improves readability of conditions.

### Example
```cobol
01 WS-STATUS PIC X.
   88 SUCCESS VALUE 'S'.
   88 FAILURE VALUE 'F'.

IF SUCCESS
   DISPLAY 'PROCESS SUCCESSFUL'
END-IF
```
📌 Highly recommended for business rules.

## 11. NEXT SENTENCE vs CONTINUE (Important)

### CONTINUE
No operation

Control passes to next statement

``` cobol
IF WS-FLAG = 'Y'
   CONTINUE
END-IF
```
NEXT SENTENCE ❌ (Avoid)
Jumps to next period (.)

Breaks structured flow

📌 Do not use NEXT SENTENCE in modern COBOL.

## 12. EVALUATE Statement (CASE Structure)
### Purpose
Replaces complex nested IF statements.

### Basic Syntax
```cobol
EVALUATE subject
   WHEN condition-1
      statement-1
   WHEN condition-2
      statement-2
   WHEN OTHER
      statement-n
END-EVALUATE
```
## 13. EVALUATE TRUE
### Purpose
Allows complex conditions in WHEN.

### Example
```cobol
EVALUATE TRUE
   WHEN WS-A > 0 AND WS-B > 0
      DISPLAY 'BOTH POSITIVE'
   WHEN WS-A > 0
      DISPLAY 'A POSITIVE'
   WHEN OTHER
      DISPLAY 'NONE POSITIVE'
END-EVALUATE
```
## 14. Multiple Subjects in EVALUATE
### Syntax
```cobol
EVALUATE subject-1 ALSO subject-2
   WHEN value-1 ALSO value-2
      statement
END-EVALUATE
```
### Example
```cobol
EVALUATE WS-STATUS ALSO WS-TYPE
   WHEN 'A' ALSO '1'
      DISPLAY 'TYPE A1'
   WHEN 'B' ALSO '2'
      DISPLAY 'TYPE B2'
   WHEN OTHER
      DISPLAY 'UNKNOWN'
END-EVALUATE
```
📌 Number of subjects must match number of objects.

## 15. IF vs EVALUATE (Interview Favorite)

| Aspect | IF | EVALUATE |
|------|----|----------|
| Readability | Lower when nested | High |
| Multiple conditions | Complex | Clean |
| Default path | ELSE | WHEN OTHER |
| Recommendation | Limited use | Preferred |

## 16. Common Interview Traps

- ❌ Forgetting `AND` / `OR` precedence
- ❌ Missing `WHEN OTHER` in `EVALUATE`
- ❌ Using `NEXT SENTENCE`
- ❌ Deep nested `IF`s
- ❌ Not using `88`-level conditions

## 17. Best Practices

- Use `END-IF` always
- Prefer `EVALUATE` over nested `IF`s
- Always code `WHEN OTHER`
- Use condition names (`88` level)
- Keep conditions simple and readable

---

## 18. Key Points to Remember

- `IF` controls program flow
- Conditions drive business logic
- `EVALUATE` is COBOL’s CASE statement
- Structured logic improves maintainability
- Mastery of conditions = **core COBOL skill**
- Structured logic improves maintainability
- Mastery of conditions = core COBOL skill
