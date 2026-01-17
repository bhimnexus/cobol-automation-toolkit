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



