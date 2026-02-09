# 📘 PART 6 — COBOL Program Divisions

---

## 1. Introduction

A COBOL program is organized into **divisions**.  
Each division has a **specific responsibility** and follows a **fixed order**.

Divisions provide:
- Clear separation of concerns
- Better readability
- Easier maintenance

A COBOL program can contain **up to four divisions**.

---

## 2. List of COBOL Divisions

The four divisions of a COBOL program are:

1. Identification Division  
2. Environment Division  
3. Data Division  
4. Procedure Division  

📌 **Important:**  
- Divisions must appear in this **exact order**
- Missing or misplaced divisions cause compilation errors

---

## 3. Identification Division

### Purpose

The **Identification Division** identifies the program to the compiler and to users.

It contains:
- Program name
- Documentation-related information

This division is **mandatory**.

---

### Structure

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. program-name.
```

## PROGRAM-ID Paragraph

- `PROGRAM-ID` is **mandatory**
- Defines the **name of the program**

### Program name rules (IBM COBOL)

- Maximum **8 characters**
- Must begin with an **alphabet**
- Alphanumeric characters are allowed

### Example

```cobol
IDENTIFICATION DIVISION.
PROGRAM-ID. PAYROLL1.
```

## Optional Documentation Paragraphs

The following paragraphs are **optional** and used only for documentation:

- `AUTHOR`
- `INSTALLATION`
- `DATE-WRITTEN`
- `DATE-COMPILED`
- `SECURITY`

### Example

```cobol
AUTHOR. BHIM SINGH.
DATE-WRITTEN. 10-FEB-2026.
SECURITY. CONFIDENTIAL.
```

---

## ✅ **4. Environment Division**

## 4. Environment Division

### Purpose

The **Environment Division** describes the **hardware and system environment** used by the program.

- It is the **only machine-dependent division** in COBOL
- When a program is moved to another system, changes—if any—are usually limited to this division

---

### Sections in Environment Division

The Environment Division contains two sections:

1. Configuration Section
2. Input-Output Section

## 5. Configuration Section

### Purpose

Provides information about:

- The system where the program is **compiled**
- The system where the program is **executed**
- Special hardware-related definitions

📌 This section is **optional in COBOL 85 and later**.

### SOURCE-COMPUTER Paragraph

Specifies the computer used for compilation.

### Example

```cobol
SOURCE-COMPUTER. IBM-4381 WITH DEBUGGING MODE.
```
WITH DEBUGGING MODE enables lines marked with D in column 7


---

### OBJECT-COMPUTER Paragraph

Specifies the computer on which the program will run.

### Example

```cobol
OBJECT-COMPUTER. IBM-4381.
```

Usually the same as SOURCE-COMPUTER.


---

### SPECIAL-NAMES Paragraph

Used to define special conventions.

### Common uses

- Currency symbol substitution
- Decimal point definition
- Custom character classes

### Example

```cobol
SPECIAL-NAMES.
    CURRENCY SIGN IS '$'
    DECIMAL-POINT IS COMMA
    CLASS DIGIT IS '0' THRU '9'.
```

---

## 6. Input-Output Section

### Purpose

Defines **files** used by the program and how they are controlled.

📌 This section is **mandatory if files are used**.

### FILE-CONTROL Paragraph

Used to:

- Associate program file names with JCL DD names
- Define file organization and access mode

### Example

```cobol
FILE-CONTROL.
    SELECT EMP-FILE ASSIGN TO EMPDD
    ORGANIZATION IS SEQUENTIAL
    FILE STATUS IS WS-EMP-STATUS.
```

---

### I-O CONTROL Paragraph

Used for advanced file handling such as:

- Checkpointing
- Shared storage areas

📌 This paragraph is **rarely used** in modern applications.

## 7. Data Division

### Purpose

The **Data Division** defines all data items used by the program.

This includes:

- File records
- Working variables
- Data passed between programs

📌 The Data Division is **optional only if the program does not use data**.

### Sections in Data Division

1. File Section
2. Working-Storage Section
3. Linkage Section

### File Section

Defines the **record layout** of files.

### Example

```cobol
FILE SECTION.
FD EMP-FILE.
01 EMP-RECORD.
   05 EMP-ID     PIC 9(05).
   05 EMP-NAME   PIC X(20).
```


---

### Working-Storage Section

Used to define:

- Variables
- Counters
- Flags
- Intermediate values

### Example

```cobol
WORKING-STORAGE SECTION.
01 WS-TOTAL-SALARY PIC 9(07) VALUE ZERO.
```


---

### Linkage Section

Used to define:

- Data received from calling programs
- Parameters passed through JCL `PARM`

### Example

```cobol
LINKAGE SECTION.
01 LK-DATA.
   05 LK-LENGTH PIC S9(04) COMP.
   05 LK-VALUE  PIC X(20).
```

---

## 8. Procedure Division

### Purpose

The **Procedure Division** contains the **business logic** of the program.

This is where:

- Calculations are performed
- Files are processed
- Decisions are made

### Structure

```cobol
PROCEDURE DIVISION.
```

---

## 9. Program Termination

A COBOL program must end with **one of the following**:

- `STOP RUN` → Main program
- `EXIT PROGRAM` → Subprogram
- `GOBACK` → Main or subprogram

### Example

```cobol
STOP RUN.
```

---

## 10. Division Summary Table

| Division | Mandatory | Purpose |
|--------|----------|--------|
| Identification | Yes | Program identification |
| Environment | No | System and file environment |
| Data | Optional | Data definitions |
| Procedure | Yes | Business logic |

## 11. Key Points to Remember

- Divisions must appear in the **correct order**
- Identification and Procedure Divisions are **mandatory**
- Environment Division handles **machine dependency**
- Data Division defines **all data**
- Procedure Division contains **executable logic**

