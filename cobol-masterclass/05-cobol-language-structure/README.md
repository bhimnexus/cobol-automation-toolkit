# COBOL Language Structure

---

## 1. Introduction

COBOL is a **structured, English-like programming language**.  
Its language structure is designed to make programs:

- Easy to read
- Easy to maintain
- Suitable for business users and programmers

A COBOL program is built using **well-defined building blocks**, arranged in a clear hierarchy.

Understanding these building blocks is essential before writing or reading COBOL programs.

---

## 2. Character Set

The **character set** defines the valid characters that can be used in a COBOL program.

### COBOL Character Set Includes

#### Digits
- `0 1 2 3 4 5 6 7 8 9`

#### Alphabets
- Uppercase letters: `A` to `Z`
- COBOL is **not case-sensitive**

#### Space
- Space (` `) is a valid character

#### Special Characters
- `+  -  *  /  (  )  =`
- `$  ,  .  ;  :`
- `'  "  <  >`

📌 These characters are used to form **words, literals, and symbols** in COBOL.

---

## 3. Word

A **word** is a sequence of one or more characters.

### Types of Words in COBOL

#### 3.1 Reserved Words
- Words predefined by COBOL
- Have special meaning
- Cannot be used as variable names

Examples:
- `MOVE`
- `ADD`
- `IF`
- `PERFORM`
- `READ`

---

#### 3.2 User-Defined Words
- Created by the programmer
- Used as:
  - Data names
  - Paragraph names
  - Section names

Rules:
- 1 to 30 characters long
- Must contain at least one alphabet
- Hyphen (`-`) is allowed
- Cannot begin or end with a hyphen

Example:
```cobol
01  WS-TOTAL-AMOUNT PIC 9(05).
```

## 4. Literal

A **literal** is a constant value written directly in the COBOL program.

Literals do not change during program execution.

---

### 4.1 Numeric Literals

- Contain only digits
- May include an optional sign (`+` or `-`)
- No quotation marks are used

#### Examples

```cobol
MOVE 100 TO WS-COUNT
MOVE -25 TO WS-BALANCE
```
#### 4.2 Non-Numeric Literals

Enclosed within single or double quotation marks

Can contain alphabets, digits, spaces, and special characters

#### Examples
```cobo
MOVE 'SUCCESS' TO WS-STATUS
MOVE 'HELLO WORLD' TO WS-MESSAGE
```

---

## ✅ **Section 5 — Clause**

## 5. Clause

A **clause** is a group of words that specifies an attribute of a data item or statement.

Clauses provide additional information such as:
- Data type
- Size
- Initial value
- Storage format

### Common Clauses

- `PIC`
- `VALUE`
- `USAGE`
- `SIGN`

### Example

```cobol
01  WS-COUNT PIC 9(03) VALUE 100.
```

---

## ✅ **Section 6 — Statement**

## 6. Statement

A **statement** is a complete instruction that tells the program to perform a specific action.

Statements are written in the **Procedure Division**.

### Examples

```cobol
MOVE A TO B
ADD A TO B
DISPLAY WS-NAME
```

---

## ✅ **Section 7 — Sentence**

## 7. Sentence

A **sentence** is one or more COBOL statements terminated by a **period (`.`)**.

The period acts as an **implicit scope terminator**.

### Example

```cobol
MOVE A TO B
ADD B TO C.
```
All statements before the period belong to the same sentence.


---

## ✅ **Section 8 — Paragraph**

## 8. Paragraph

A **paragraph** is a named block of code consisting of one or more sentences.

### Characteristics

- Paragraph names must be unique within a section
- Used to logically organize program code

### Example

```cobol
CALCULATE-TOTAL.
    ADD PRICE TO TOTAL.
```

---

## ✅ **Section 9 — Section**

## 9. Section

A **section** is a collection of related paragraphs.

Sections improve program structure and readability.

### Characteristics

- Section names must be unique within a program
- Commonly used in the Procedure Division

### Example

```cobol
PROCESS-RECORDS SECTION.
    READ-FILE.
    UPDATE-TOTAL.
```

---

## ✅ **Section 10 — Division**

## 10. Division

A **division** is a major structural unit of a COBOL program.

COBOL programs consist of **four divisions**:

1. Identification Division
2. Environment Division
3. Data Division
4. Procedure Division

Each division has a specific purpose and responsibility.

## ✅ Section 11 — Program

## 11. Program

A **COBOL program** is a complete set of instructions made up of:

- Divisions
- Sections
- Paragraphs
- Sentences
- Statements

### Program Start Example

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. SAMPLE1.
```
### Program End Example
```cobol
STOP RUN.
```


## ✅ **Section 12 — Hierarchy Summary**

The structural hierarchy of COBOL is as follows:
```
Character
↓
Word
↓
Clause
↓
Statement
↓
Sentence
↓
Paragraph
↓
Section
↓
Division
↓
Program
```
## 13. Key Points to Remember

- COBOL is a **structured and hierarchical language**
- Each level builds upon the previous one
- Clear structure improves readability and maintenance
- Understanding language structure is essential before writing programs



