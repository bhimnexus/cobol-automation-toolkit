"""
JCL Error Analyzer
-----------------
Analyzes mainframe job logs / SYSOUT files and provides
root cause analysis with suggested fixes.

Author: Bhim Singh
"""

import re
import sys

ABEND_MAP = {
    "S0C7": {
        "cause": "Data exception – invalid numeric data.",
        "fix": "Check PIC definitions, COMP fields, and input data."
    },
    "S0C4": {
        "cause": "Protection exception – invalid memory reference.",
        "fix": "Check subscript usage, pointer logic, and table bounds."
    },
    "S322": {
        "cause": "Time limit exceeded.",
        "fix": "Optimize logic or increase TIME parameter in JCL."
    }
}

MESSAGE_MAP = {
    "IEC": {
        "cause": "Dataset allocation or access error.",
        "fix": "Verify dataset name, DISP, volume, and catalog entry."
    },
    "IEFC": {
        "cause": "JCL syntax or parameter error.",
        "fix": "Review JOB/EXEC/DD statements carefully."
    },
    "IKJ": {
        "cause": "TSO or command execution error.",
        "fix": "Check command syntax and user permissions."
    }
}

def analyze_log(file_path):
    print("\n=== JCL JOB FAILURE ANALYSIS ===\n")

    try:
        with open(file_path, "r", errors="ignore") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return

    issues_found = False

    for line in lines:
        # Detect ABENDs
        for abend in ABEND_MAP:
            if abend in line:
                issues_found = True
                print(f"🔴 ABEND DETECTED: {abend}")
                print(f"   Cause : {ABEND_MAP[abend]['cause']}")
                print(f"   Fix   : {ABEND_MAP[abend]['fix']}\n")

        # Detect system messages
        for msg in MESSAGE_MAP:
            if msg in line:
                issues_found = True
                print(f"🔴 MESSAGE DETECTED: {msg}")
                print(f"   Cause : {MESSAGE_MAP[msg]['cause']}")
                print(f"   Fix   : {MESSAGE_MAP[msg]['fix']}\n")

    if not issues_found:
        print("✅ No known ABENDs or JCL errors detected.")
        print("ℹ️ Job may have completed successfully or needs manual review.")

    print("\n=== ANALYSIS COMPLETE ===\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python jcl_error_analyzer.py <job_log_file>")
        sys.exit(1)

    analyze_log(sys.argv[1])
