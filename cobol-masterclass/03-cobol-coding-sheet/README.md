# COBOL Coding Sheet (Source Program Format)

---

## 1. Introduction to the Coding Sheet

A **COBOL source program** is written using a fixed-format layout known as the **coding sheet**.

Each line of a COBOL program consists of **80 character positions (columns)**.  
Each column range has a **specific meaning**.

This fixed format is followed to:
- Maintain consistency
- Enable correct compilation
- Support readability and debugging

---

## 2. Column Layout Overview

The COBOL coding sheet is divided into the following column ranges:

| Columns | Name | Purpose |
|-------|------|---------|
| 1–6 | Page / Line Numbers | Optional sequence numbers |
| 7 | Indicator Column | Special line indicators |
| 8–11 | Area A | Division, Section, Paragraph names |
| 12–72 | Area B | COBOL statements |
| 73–80 | Identification Area | Programmer information |

---

## 3. Columns 1–6 — Page / Line Numbers

- Columns **1 to 6** are reserved for **page or line numbers**
- These numbers are **optional**
- Compilers usually assign line numbers automatically
- Traditionally used for:
  - Program listings
  - Sorting source code decks

📌 These columns are **ignored by the compiler**.

---

## 4. Column 7 — Indicator Column

Column **7** is known as the **Indicator Column**.

It is used to specify special meanings for a line.

### Indicator characters and their meanings

| Character | Meaning |
|--------|--------|
| `*` | Comment line |
| `-` | Continuation of previous line |
| `/` | Start a new page in listing |
| `D` | Debugging line |
| (Blank) | Normal source line |

---

### 4.1 Comment Lines (`*`)

- If `*` appears in column 7, the entire line is treated as a **comment**
- Comment lines are ignored by the compiler
- Used for:
  - Program documentation
  - Explanatory notes

Example:
```cobol
000100* THIS IS A COMMENT LINE
```
## 4.2 Continuation Lines (`-`)

A hyphen (`-`) in **column 7** indicates that the current line is a **continuation of the previous line**.

### Usage

- Used when a statement is too long to fit on one line
- The continued line must have `-` in column 7

### Example

```cobol
000200     DISPLAY 'THIS IS A VERY LONG MESSAGE THAT NEEDS TO BE
000201-    CONTINUED ON THE NEXT LINE'
```
## 4.3 New Page Indicator (`/`)

A slash (`/`) in **column 7** causes a **page break in the compiler listing**.

### Characteristics

- Affects only the compiler listing
- Does **not** affect program execution

### Example

```cobol
000300/    START OF A NEW PAGE IN LISTING
```

## 4.4 Debugging Lines (`D`)

The character `D` in **column 7** marks a line as a **debugging line**.

### Debugging line behavior

- Compiled **only** when `WITH DEBUGGING MODE` is specified
- Ignored by the compiler otherwise

### Example

```cobol
000400D    DISPLAY 'DEBUG MESSAGE'
```

### ✅ **Section 5**

## 5. Columns 8–11 — Area A

Columns **8 to 11** are known as **Area A**.

### Entries that must begin in Area A

- Division names
- Section names
- Paragraph names
- Level `01` and `77` data descriptions

### Example

```cobol
       IDENTIFICATION DIVISION.
       DATA DIVISION.
       WORKING-STORAGE SECTION.
       01  WS-NAME PIC X(10).
```

### ✅ **Section 6**

## 6. Columns 12–72 — Area B

Columns **12 to 72** are known as **Area B**.

### Area B is used for

- Executable statements
- Data description entries (other than `01` and `77`)
- Clauses and conditions

### Example

```cobol
           MOVE 'ABC' TO WS-NAME
           DISPLAY WS-NAME
```

### ✅ **Section 7**

## 7. Columns 73–80 — Identification Area

Columns **73 to 80** are called the **Identification Area**.

### Characteristics

- Ignored by the compiler
- Used only for documentation purposes

### Common uses

- Programmer initials
- Date
- Version information

### Example

```cobol
           DISPLAY WS-NAME              BSINGH
```

### ✅ **Section 8**

## 8. Importance of Coding Sheet Rules

Following coding sheet rules is important because:

- Misplaced entries may cause compilation errors
- Incorrect column usage can change program meaning
- Debugging becomes easier with proper formatting

## 9. Key Points to Remember

- COBOL uses a **fixed-format source layout**
- Each column range has a defined purpose
- Column 7 controls comments, continuation, and debugging
- Division and section names must begin in **Area A**
- Most executable statements are written in **Area B**

