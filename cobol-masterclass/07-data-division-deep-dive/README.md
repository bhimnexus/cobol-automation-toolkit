# Chapter 7 — Data Division Deep Dive

---

## 1. Introduction to the Data Division

The **Data Division** defines **all data items** used by a COBOL program.

It tells the compiler:
- What data exists
- How much storage is required
- How the data is structured
- How the data is represented internally

📌 A COBOL program **cannot process data unless it is defined** in the Data Division.

---

## 2. Purpose of the Data Division

The Data Division is used to define:

- File records
- Working storage variables
- Constants and flags
- Tables (arrays)
- Data passed between programs

📌 The Data Division is **optional only if the program does not use any data**.

---

## 3. Sections of the Data Division

The Data Division contains the following sections:

1. File Section  
2. Working-Storage Section  
3. Linkage Section  

Each section has a **specific role**.

---

## 4. File Section

### Purpose

The **File Section** defines the **record layout** of files used by the program.

- Describes how a record looks in memory
- Works together with the `FILE-CONTROL` paragraph

📌 Files defined here are accessed in the **Procedure Division**.

---

### Example

```cobol
FILE SECTION.
FD EMP-FILE.
01 EMP-RECORD.
   05 EMP-ID        PIC 9(05).
   05 EMP-NAME      PIC X(20).
   05 EMP-SALARY    PIC 9(07)V99.
```
## 5. Working-Storage Section

### Purpose

The **Working-Storage Section** is used to define:

- Variables
- Counters
- Flags
- Intermediate results
- Constants

📌 Data in Working-Storage **retains its value throughout program execution**.

### Example

```cobol
WORKING-STORAGE SECTION.
01 WS-TOTAL-SALARY PIC 9(09) VALUE ZERO.
01 WS-EOF-FLAG     PIC X     VALUE 'N'.
```

---

## 6. Linkage Section

### Purpose

The **Linkage Section** is used to define:

- Data passed from calling programs
- Parameters received from JCL `PARM`
- Shared data in subprograms

📌 Data in the Linkage Section **does not belong to the program**.

### Example

```cobol
LINKAGE SECTION.
01 LK-PARAM-DATA.
   05 LK-LENGTH PIC S9(04) COMP.
   05 LK-VALUE  PIC X(20).
```

---

## 7. Data Description Entry (General Format)

A data item is defined using a **Data Description Entry**.

### General Syntax
```
level-number data-name
[PICTURE clause]
[VALUE clause]
[USAGE clause].
```

## 8. Level Numbers

Level numbers define the **hierarchy of data items**.

### Common Level Numbers

| Level | Meaning |
|------|--------|
| 01 | Record / Group item |
| 02–49 | Subordinate items |
| 66 | RENAMES clause |
| 77 | Independent data item |
| 88 | Condition name |

### Example

```cobol
01 EMPLOYEE.
   05 EMP-ID     PIC 9(05).
   05 EMP-NAME   PIC X(20).
```

---

## 9. Group Item vs Elementary Item

### Group Item

- Has **no PICTURE clause**
- Represents a **collection of fields**

### Elementary Item

- Has a **PICTURE clause**
- Represents a **single data value**

### Example

```cobol
01 EMP-RECORD.
   05 EMP-ID     PIC 9(05).
   05 EMP-NAME   PIC X(20).

EMP-RECORD → Group item
EMP-ID, EMP-NAME → Elementary items
```

---

## 10. Data Names and FILLER

### Data Name Rules

- 1 to 30 characters
- Must contain at least one alphabet
- Hyphen (`-`) allowed (not at start or end)

### FILLER

- Used when a field is **not referenced**
- Cannot be used in Procedure Division

### Example

```cobol
05 FILLER PIC X(10).
```

---

## 11. PICTURE Clause (PIC)

### Purpose

The `PICTURE` clause defines:

- Data type
- Length
- Format

### Common Picture Symbols

#### Numeric
- `9` → Digit
- `V` → Implied decimal
- `S` → Sign

#### Alphanumeric
- `X` → Any character
- `A` → Alphabetic

### Example

```cobol
05 WS-AMOUNT PIC S9(07)V99.
05 WS-NAME   PIC X(20).
```

---

## 12. VALUE Clause

### Purpose

The `VALUE` clause initializes data items.

📌 Used only in **Working-Storage**.

### Example

```cobol
01 WS-COUNT  PIC 9(03) VALUE 100.
01 WS-STATUS PIC X     VALUE 'Y'.
```

---

## 13. USAGE Clause

### Purpose

Defines the **internal storage format**.

### Common USAGE Types

- `DISPLAY` (default)
- `COMP` (Binary)
- `COMP-3` (Packed Decimal)
- `INDEX`

### Example

```cobol
05 WS-BALANCE PIC S9(07) COMP-3.
```


---

## 14. REDEFINES Clause

### Purpose

Allows multiple views of the **same memory area**.

### Example

```cobol
01 WS-DATE        PIC 9(08).
01 WS-DATE-REDEF REDEFINES WS-DATE.
   05 WS-YEAR     PIC 9(04).
   05 WS-MONTH    PIC 9(02).
   05 WS-DAY      PIC 9(02).
```

---

## 15. RENAMES Clause (66 Level)

### Purpose

Groups existing fields under a **new name**.

### Example

```cobol
01 WS-RECORD.
   05 WS-PART1 PIC X(05).
   05 WS-PART2 PIC X(05).
66 WS-COMBINE RENAMES WS-PART1 THRU WS-PART2.
```

---

## 16. Condition Names (88 Level)

### Purpose

Provides **meaningful names** for conditions.

### Example

```cobol
01 WS-STATUS PIC X.
   88 SUCCESS VALUE 'S'.
   88 FAILURE VALUE 'F'.
```
```
IF SUCCESS
   DISPLAY 'PROCESS OK'
END-IF
```

---

## **17. OCCURS Clause (Tables)**

### Purpose

Defines **arrays / tables**.

### Example

```cobol
01 WS-SCORES.
   05 WS-SCORE PIC 9(03) OCCURS 5 TIMES.
```


---

## 18. Data Division Best Practices

- Use meaningful data names
- Avoid excessive `77` levels
- Prefer `88` for conditions
- Use `COMP-3` for financial data
- Group related data logically

## 19. Key Points to Remember

- Data Division defines **what data exists**
- Structure is **hierarchical**
- Storage format matters for **performance**
- Clear data design simplifies logic
- Mastery of Data Division is critical for **COBOL expertise**

