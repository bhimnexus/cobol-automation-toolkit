# DB2 SQLCODE Helper

A practical reference for common DB2 SQLCODEs encountered in
COBOL-DB2 batch and online applications.

This guide focuses on **real production scenarios** and **what to do next**.

---

## 🔴 SQLCODE -911 / -913
**Meaning:** Deadlock or timeout occurred.

**Common causes:**
- Long-running transactions
- Table or row lock contention
- Missing COMMITs

**What to check:**
- Program COMMIT frequency
- Lock escalation
- Concurrent batch jobs

**Suggested fix:**
- Add COMMIT checkpoints
- Reduce transaction scope
- Coordinate batch schedules

---

## 🔴 SQLCODE -805
**Meaning:** DBRM or package not found.

**Common causes:**
- Program not rebound after change
- Wrong PLAN or PACKAGE version
- Incorrect collection ID

**What to check:**
- BIND status
- Correct PLAN/PACKAGE in JCL
- Environment mismatch (DEV/QA/PROD)

---

## 🔴 SQLCODE -904
**Meaning:** Resource unavailable.

**Common causes:**
- Tablespace in STOP or RESTRICT state
- Dataset unavailable
- Utility running on object

**What to check:**
- Tablespace status
- Active DB2 utilities
- System messages

---

## 🔴 SQLCODE -818
**Meaning:** Timestamp mismatch between load module and DBRM.

**Common causes:**
- Program recompiled but not rebound
- Old load module deployed

**What to check:**
- Compile + BIND sequence
- Load library version
- Promotion process

---

## 🔴 SQLCODE +100
**Meaning:** No rows found.

**Common causes:**
- SELECT returned zero rows
- Cursor FETCH at end

**What to check:**
- Application logic
- Cursor handling
- Expected business data

---

## 📌 Notes
- Always capture SQLCODE, SQLSTATE, and table name
- Check DB2 subsystem logs for context
- Avoid hard-coding retry logic
