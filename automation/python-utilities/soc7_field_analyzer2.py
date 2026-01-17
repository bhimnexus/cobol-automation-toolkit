#!/usr/bin/env python3
"""
SOC7 Field Analyzer
==================
Phase 1:
- Detect SOC7 / S0C7 abend
- Extract offset from job log

Phase 2:
- Parse COBOL field definitions (PIC, USAGE)

Phase 3:
- Identify high-risk fields likely causing SOC7
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

    soc7_patterns = [
        r"S0C7",
        r"SOC7",
        r"DATA\s+EXCEPTION",
        r"COMPLETION\s+CODE\s*=\s*0C7"
    ]

    if not any(re.search(p, content, re.IGNORECASE) for p in soc7_patterns):
        print("No SOC7 abend detected.")
        return None

    print("SOC7 (Data Exception) detected.")

    offset_match = re.search(
        r"OFFSET\s*(?:[:=]?\s*)X'([0-9A-F]+)'",
        content,
        re.IGNORECASE
    )

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

    for f in fields:
        print(
            f"Level {f['level']} | "
            f"Field {f['name']} | "
            f"PIC {f['pic']} | "
            f"USAGE {f['usage']}"
        )

    return fields


def analyze_soc7_risk(fields):
    print("\n=== SOC7 FIELD RISK ANALYSIS ===\n")

    high_risk = []
    low_risk = []

    for f in fields:
        pic = f["pic"].upper()
        usage = f["usage"]

        # Numeric DISPLAY fields are the most common SOC7 cause
        if re.match(r"S?9", pic) and usage == "DISPLAY":
            high_risk.append(f)
        else:
            low_risk.append(f)

    if high_risk:
        print("HIGH RISK FIELDS (Most likely SOC7 cause):\n")
        for f in high_risk:
            print(
                f"- {f['name']} (PIC {f['pic']}, {f['usage']})\n"
                f"  Reason: Numeric DISPLAY field — invalid input causes SOC7\n"
            )
    else:
        print("No high-risk DISPLAY numeric fields found.\n")

    print("LOW RISK FIELDS:\n")
    for f in low_risk:
        print(f"- {f['name']} (PIC {f['pic']}, {f['usage']})")

    if high_risk:
        print(
            "\nRecommendation:\n"
            f"Check input data for field '{high_risk[0]['name']}' "
            "in the input file feeding this program."
        )


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
    fields = parse_cobol_fields(cobol_file)
    analyze_soc7_risk(fields)


if __name__ == "__main__":
    main()

