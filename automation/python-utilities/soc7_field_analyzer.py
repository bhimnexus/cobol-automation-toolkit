"""
SOC7 Field Analyzer – Phase 1
-----------------------------
Parses mainframe job logs to detect SOC7 abends
and extracts useful diagnostic hints.

Author: Bhim Singh
"""

import sys
import re

def analyze_job_log(log_file):
    print("\n=== SOC7 JOB LOG ANALYSIS ===\n")

    try:
        with open(log_file, "r", errors="ignore") as f:
            lines = f.readlines()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {log_file}")
        return

    soc7_found = False
    program_name = None
    offset = None

    for line in lines:
        # Detect SOC7 / Data Exception
        if "SOC7" in line or "S0C7" in line:
            soc7_found = True
            print("🔴 SOC7 (Data Exception) detected")

        # Detect program name
        if "PROGRAM" in line.upper():
            program_name = line.strip()

        # Detect offset information (common compiler messages)
        match = re.search(r"OFFSET\s+X'([0-9A-F]+)'", line.upper())
        if match:
            offset = match.group(1)

    if not soc7_found:
        print("✅ No SOC7 detected in job log.")
        return

    print("\n--- Extracted Hints ---")

    if program_name:
        print(f"Program Info : {program_name}")
    else:
        print("Program Info : Not found in log")

    if offset:
        print(f"Offset       : X'{offset}'")
    else:
        print("Offset       : Not found")

    print("\nNext steps:")
    print("- Review arithmetic statements around the offset")
    print("- Check numeric/COMP/COMP-3 fields")
    print("- Validate input file data")

    print("\n=== ANALYSIS COMPLETE ===\n")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python soc7_field_analyzer.py <job_log_file>")
        sys.exit(1)

    analyze_job_log(sys.argv[1])
