# Chapter 15 — File Handling (QSAM, VSAM, READ / WRITE)
IBM Enterprise COBOL (z/OS)

---

## 1. Introduction to File Handling

### Purpose

File handling in COBOL is used to:

- Read data from files
- Write data to files
- Update existing records
- Delete records
- Process large volumes of business data

📌 Most enterprise COBOL programs are **file-driven**.

---

### What Is a File in COBOL?

A file is a **collection of related records**, and each record is a
collection of **fields**.

Example:
- Employee file
- Account master file
- Transaction file

---

### Types of Files in COBOL (High Level)

COBOL supports two major categories of files:

- **QSAM files** (Sequential files)
- **VSAM files** (Advanced indexed files)

📌 The file type determines:
- Access method
- Performance
- Update capability

---

### Typical File Processing Flow

1. Allocate file (JCL)
2. Define file in COBOL
3. Open file
4. Read / Write / Update records
5. Close file

📌 Missing or incorrect steps lead to **runtime errors**.

---

### Why File Handling Is Interview-Critical

- Core of batch processing
- Heavy use in banking systems
- Strong testing area in interviews
- Many production abends are file-related

---

### Key Points to Remember

- File handling is fundamental to COBOL
- COBOL programs usually revolve around files
- Understanding file types is critical
- Proper file handling prevents production failures

## 2. File Organization Types in COBOL

### Purpose

The **file organization** defines **how records are stored and accessed**
on disk.

Choosing the correct file organization impacts:
- Performance
- Access method
- Update capability
- Program complexity

📌 File organization is a **very common interview topic**.

---

## 2.1 Sequential Files (QSAM)

### Definition

Sequential files store records **one after another** in sequence.

Records are processed **in the order they are stored**.

---

### Characteristics

- Records accessed sequentially only
- No random access
- Simple and fast for batch processing
- Widely used in legacy batch jobs

---

### Access Methods

- Sequential READ only

---

### Common Use Cases

- Daily transaction processing
- Reports
- Data extracts
- Interface files

---

### Example

```cobol
SELECT EMP-FILE ASSIGN TO EMPDD
   ORGANIZATION IS SEQUENTIAL.
```
📌 Sequential files are also known as QSAM files.


---
