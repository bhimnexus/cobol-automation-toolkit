# COBOL Automation Toolkit

A curated set of COBOL, JCL, DB2, and automation utilities created from real production support and development experience.

## Includes
- COBOL code templates  
- JCL utility samples  
- DB2 best practices  
- Python + REXX automation scripts  
- AI-assisted modernization utilities  

## Purpose
To help teams accelerate delivery, reduce RCA time, and adopt modernization gradually while leveraging Agentic AI for automation.

## Usage

### 🔧 JCL Job Failure Analyzer (Python)

This utility analyzes mainframe job output logs (JES/SYSOUT) and provides
automated root cause analysis (RCA) with fix suggestions.

**Location:**  
automation/python-utilities/jcl_error_analyzer.py

**How to run:**
```bash
python jcl_error_analyzer.py <job_log_file>
```

**Example**

python jcl_error_analyzer.py sample_job_log.txt

### 🔧 Dataset Checker Utility (REXX)

A REXX utility to verify dataset existence and basic accessibility on the mainframe.

**Location:**  
automation/rexx-scripts/dataset-checker.rexx

**How to run (TSO):**

EX 'HLQ.REXXLIB(DATASETCK)'

**Use cases:**
- Validate input/output datasets before job execution
- Prevent JCL failures due to missing datasets
- Lightweight pre-check utility for batch jobs

### 🔧 DB2 SQLCODE Analyzer (Python)

A Python utility that analyzes DB2 SQLCODEs and provides
production-focused explanations, possible causes, and fix suggestions.

**Location:**  
automation/python-utilities/db2_sqlcode_analyzer.py

**How to run:**
```bash
python db2_sqlcode_analyzer.py <SQLCODE>
```
****Example:****
python db2_sqlcode_analyzer.py -805


---

### 🔧 SOC7 Field Analyzer (Python – Production RCA Module)

A production-grade SOC7 (Data Exception) Root Cause Analysis utility that
pinpoints the exact COBOL field causing the abend using:

- Job log offset (JES/SYSOUT)
- COBOL source definitions (PIC, USAGE)
- Compile listing offsets (OFFSET, LENGTH)

#### Inputs
1. SOC7 job log (JES/SYSOUT with OFFSET X'hhhh')
2. COBOL source program
3. Compile listing

#### Location
automation/python-utilities/soc7_field_analyzer_Final.py

#### How to run
```bash
python soc7_field_analyzer_Final.py \
  <job_log> \
  <cobol_source> \
  <compile_listing>
```

**Example**
```bash
python soc7_field_analyzer_Final.py \
  sample_soc7_job_log.txt \
  sample_cobol_program.cbl \
  sample_compile_listing.txt
```

Output:
- Exact SOC7-causing field name
- Offset range from compile listing
- PIC and USAGE clause
- Root cause explanation
- Production-ready fix recommendation


Typical Production Use Cases:
- SOC7 / Data Exception abends
- Invalid numeric DISPLAY data
- MOVE or arithmetic failures
- Batch job production RCA

This tool demonstrates how mainframe production RCA can be automated using deterministic logic — without relying on runtime debuggers.





