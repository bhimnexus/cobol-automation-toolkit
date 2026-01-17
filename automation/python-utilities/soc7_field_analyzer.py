#!/usr/bin/env python3
"""
SOC7 Field Analyzer
-------------------
Phase 1:
- Detects SOC7 abend from mainframe job logs
- Extracts offset information if available

Phase 2:
- Parses COBOL program to list field definitions
- Identifies PIC clauses and USAGE (DISPLAY / COMP / COMP-3)
"""

import sys
import re
import os


def analyze_job_log(log_file):
    print("\n=== SOC7 JOB LOG ANALYSIS ===\n")

    if not os.path.exists(log_file):
        print(f"[ERROR] File not found: {log_file}")
        return None

    with open(log_file, "r", errors="ignore") as f:
        content = f.read()

    # Detect SOC7
    if "SOC7" not in content:
        print("No SOC7 abend detected.")
        return None

    print("SOC7 (Data Exception) detected.")

    # Try to find offset like X'01A4'
    offset_match = re.search(r"OFFSET\s*[:=]\s*X'([0-9A-F]+)'", content, re.IGNORECASE)

    if offset_match:
        offset = offset_match.group(1)
        print(f"Offset detected : X'{offset}'")
        return offset
    else:
        print("Offset not found in job log.")
        return None


def parse_cobol_fields(cobol_file):
    print("\n=== COBOL FIELD MAP ===\n")

    if not os.path.exists(cobol_file):
        print(f"[ERROR] COBOL file not found: {cobol_file}")
        return []

    with open(cobol_file, "r", errors="ignore") as f:
        lines = f.readlines()

    field_pattern = re.compile(
        r"^\s*(\d+)\s+([\w-]+)\s+PIC\s+([^.\s]+)(.*)\.",
        re.IGNORECASE
    )

    fields = []

    for line in lines:
        match = field_pattern.match(line)
        if match:
            level = match.group(1)
            name = match.group(2)
            pic = match.group(3)
            rest = match.group(4).upper()

            usage = "DISPLAY"
            if "COMP-3" in rest:
                usage = "COMP-3"
            elif "COMP" in rest:
                usage = "COMP"

            fields.append({
                "level": level,
                "name": name,
                "pic": pic,
                "usage": usage
            })

    if not fields:
        print("No COBOL fields detected.")
        return []

    for f in fields:
        print(
            f"Level {f['level']} | "
            f"Field {f['name']} | "
            f"PIC {f['pic']} | "
            f"USAGE {f['usage']}"
        )

    return fields


def main():
    if len(sys.argv) != 3:
        print(
            "Usage:\n"
            "  python soc7_field_analyzer.py <job_log_file> <cobol_program>\n\n"
            "Example:\n"
            "  python soc7_field_analyzer.py sample_soc7_job_log.txt sample_cobol_program.cbl"
        )
        sys.exit(1)

    job_log = sys.argv[1]
    cobol_file = sys.argv[2]

    analyze_job_log(job_log)
    parse_cobol_fields(cobol_file)


if __name__ == "__main__":
    main()
