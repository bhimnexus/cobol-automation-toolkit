# Chapter 14 — Tables, OCCURS, INDEX & SEARCH
IBM Enterprise COBOL (z/OS)

---

## 1. Introduction to Tables in COBOL

### Purpose

Tables (arrays) are used to store **multiple occurrences of similar data** in contiguous memory locations.

They are commonly used for:
- Master data lookups
- Code-to-description mapping
- Salary slabs, rates, limits
- In-memory processing for performance

📌 In COBOL, tables are defined using the `OCCURS` clause.

---

## 2. OCCURS Clause — Basics

### Purpose

The `OCCURS` clause defines **repeating data items**.

---

### Syntax

```cobol
level-number data-name
```
### Example
```cobol
01 WS-SCORES.
   05 WS-SCORE PIC 9(03) OCCURS 5 TIMES.
```
📌 This creates 5 contiguous memory locations for WS-SCORE.
## 3. Accessing Table Elements (Subscripts)

### Purpose

A **subscript** is used to access a specific occurrence of a table element.

It represents the **occurrence number** (1, 2, 3, …) of the table entry.

---

### Key Characteristics of Subscripts

- Must be a **numeric data item**
- Can be a literal or a variable
- Can be used in **arithmetic operations**
- Can be **displayed**
- Slower than indexes (calculated at runtime)

---

### Syntax

```cobol
table-name(subscript)
```
### Example
```cobol
01 WS-SCORES.
   05 WS-SCORE PIC 9(03) OCCURS 5 TIMES.

01 WS-I PIC 9 VALUE 1.

MOVE 100 TO WS-SCORE(WS-I).
```
📌 This moves 100 into the first occurrence of WS-SCORE.
### Accessing Multiple Elements
```cobol
MOVE 85 TO WS-SCORE(1)
MOVE 90 TO WS-SCORE(2)
MOVE 75 TO WS-SCORE(3)
```
### Looping with Subscripts
```cobol
PERFORM VARYING WS-I FROM 1 BY 1
   UNTIL WS-I > 5
   DISPLAY WS-SCORE(WS-I)
END-PERFORM
```
📌 Subscripts work naturally with PERFORM VARYING.
Common Mistakes (Interview + Production)

- ❌ Using subscript value starting from 0
- ❌ Exceeding OCCURS limit
- ❌ Using subscripts for very large tables
- ❌ Forgetting to initialize the subscript

When to Use Subscripts

- ✅ Small tables
- ✅ Simple loops
- ✅ When arithmetic on position is required
- ❌ Large tables
- ❌ Performance-critical lookups
  
📌 For large or frequently searched tables, use INDEX instead.

## 4. OCCURS with Group Items
**Purpose:** Tables can be defined at the group level to store structured records.

### Example
```cobol
01 EMP-TABLE.
   05 EMP-REC OCCURS 10 TIMES.
      10 EMP-ID   PIC 9(05).
      10 EMP-NAME PIC X(20).
```
## 5. OCCURS DEPENDING ON (Dynamic Tables)
### Purpose: 
Defines tables whose size is decided at runtime, which is essential for memory management.

### Syntax
```COBOL

OCCURS max TIMES
DEPENDING ON identifier.
### Example
```COBOL

01 WS-COUNT PIC 9(02).
01 WS-TABLE.
   05 WS-VALUE PIC 9(03)
      OCCURS 1 TO 50 TIMES
      DEPENDING ON WS-COUNT.
```
⚠️ Critical: The WS-COUNT variable must be populated with a valid value before the program attempts to access the table elements.

## 6. INDEXED BY Clause (Indexes)

### Purpose

Indexes provide **faster access** to table elements.

They store **displacement (address offset)**, not the occurrence number.

---

### Example

```cobol
01 WS-TABLE.
   05 WS-VALUE PIC 9(03)
      OCCURS 10 TIMES
      INDEXED BY IDX.
```
## Index Characteristics
- Cannot be displayed
- Cannot be used in arithmetic operations
- Modified only using:
   -   SET
   -   SEARCH
   -   PERFORM

📌 Indexes are more efficient than subscripts and are preferred for
large or frequently accessed tables.

## 7. Subscript vs Index (Interview Favorite)

### Purpose

Both **subscripts** and **indexes** are used to access table elements,
but they work very differently internally.

Understanding this difference is **frequently tested in interviews**
and is critical for performance-sensitive applications.

---

### Comparison Table

| Aspect | Subscript | Index |
|------|----------|-------|
| Type | Numeric data item | Internal pointer |
| Stores | Occurrence number | Displacement (address offset) |
| Arithmetic allowed | ✅ Yes | ❌ No |
| Display allowed | ✅ Yes | ❌ No |
| Speed | Slower (runtime calculation) | Faster (direct access) |
| How modified | Arithmetic statements

## 8. SEARCH Statement (Sequential Search)

### Purpose

The `SEARCH` statement is used to **search table entries sequentially**  
from the **first occurrence to the last**.

It is typically used when:
- Table size is small
- Data is not sorted
- Search logic is simple

📌 `SEARCH` performs a **linear search**.

---

### Prerequisites

- Table must be defined with `OCCURS`
- Table must be defined with `INDEXED BY`
- Index must be **initialized before SEARCH**

---

### Syntax

```cobol
SET index-name TO 1

SEARCH table-name
   AT END
      imperative-statement-1
   WHEN condition
      imperative-statement-2
END-SEARCH
```
### Example
```cobol
01 WS-TABLE.
   05 WS-VALUE PIC 9(03)
      OCCURS 10 TIMES
      INDEXED BY IDX.

SET IDX TO 1

SEARCH WS-VALUE
   AT END
      DISPLAY 'VALUE NOT FOUND'
   WHEN WS-VALUE(IDX) = 100
      DISPLAY 'VALUE FOUND'
END-SEARCH
```
📌 The table is searched one element at a time until a match is found
or the table ends.

### How SEARCH Works (Internally)

- COBOL checks the element at the current index
- If the condition is **TRUE** → executes the `WHEN` block
- If the condition is **FALSE** → index is incremented automatically
- The process repeats until:
  - A match is found, or
  - End of table is reached

---

### Important Rules (Interview Critical)

- `SET index-name TO 1` **must be done explicitly**
- Table **does not need to be sorted**
- Multiple `WHEN` conditions are allowed
- Index is advanced automatically by COBOL

---

### Common Mistakes

- ❌ Forgetting to initialize the index
- ❌ Using `SEARCH` without `INDEXED BY`
- ❌ Assuming `SEARCH` performs binary search
- ❌ Missing `AT END` handling

---

### When to Use SEARCH

✅ Small tables  
✅ Unsorted data  
✅ Simple lookups  

❌ Large tables  
❌ Performance-critical searches  

📌 For large sorted tables, use **`SEARCH ALL`**.

## 9. SEARCH ALL (Binary Search)

### Purpose

`SEARCH ALL` is used to perform a **binary search** on a table.

It is designed for:
- Large tables
- High-performance lookups
- Frequently searched reference data

📌 `SEARCH ALL` is **much faster than SEARCH**, but has **strict rules**.

---

### Mandatory Rules (Very Important)

For `SEARCH ALL` to work correctly:

- Table **must be sorted**
- Table must be defined with:
  - `ASCENDING KEY` or `DESCENDING KEY`
- Table must be defined with `INDEXED BY`
- Only **one WHEN condition** is allowed
- Only `=` comparison is permitted
- Logical operator allowed: `AND` only

⚠️ Violation of these rules results in **unpredictable behavior**.

---

### Table Definition Example

```cobol
01 EMP-TABLE.
   05 EMP-REC OCCURS 10 TIMES
      ASCENDING KEY EMP-ID
      INDEXED BY IDX.
      10 EMP-ID   PIC 9(04).
      10 EMP-NAME PIC X(20).
```
---
### SEARCH ALL Syntax
```cobol
SEARCH ALL table-name
   AT END
      imperative-statement-1
   WHEN condition
      imperative-statement-2
END-SEARCH
```
### Example
```cobol
SEARCH ALL EMP-REC
   AT END
      DISPLAY 'EMPLOYEE NOT FOUND'
   WHEN EMP-ID(IDX) = 2005
      DISPLAY 'EMPLOYEE FOUND'
END-SEARCH
```
📌 COBOL automatically performs a binary search using the index.

### How SEARCH ALL Works (Internally)

- COBOL checks the **middle element** of the table
- Compares the key with the search value
- Narrows the search to:
  - Left half, or
  - Right half
- Repeats until:
  - A match is found, or
  - The search range is exhausted

📌 Time complexity: **O(log n)**

---

### SEARCH vs SEARCH ALL (Interview Favorite)

| Aspect | SEARCH | SEARCH ALL |
|------|--------|-----------|
| Search type | Sequential | Binary |
| Table sorted | Not required | **Mandatory** |
| Performance | Slower | Faster |
| Table size | Small | Large |
| Multiple `WHEN` | Allowed | ❌ Not allowed |
| Logical operators | Any | Only `AND` |

---

### Common Interview & Production Mistakes

- ❌ Using `SEARCH ALL` on an unsorted table
- ❌ Forgetting `ASCENDING` / `DESCENDING KEY`
- ❌ Using multiple `WHEN` conditions
- ❌ Using `OR` in `SEARCH ALL`
- ❌ Assuming `SEARCH ALL` sets index value manually

---

### When to Use SEARCH ALL

✅ Large tables  
✅ Sorted reference data  
✅ Performance-critical lookups  

❌ Small tables  
❌ Unsorted data  
❌ Complex conditions  

---

### Key Points to Remember

- `SEARCH ALL` = Binary search
- Table **must be sorted**
- Faster than `SEARCH`
- Strict syntax and rules
- Frequently asked in interviews



 
