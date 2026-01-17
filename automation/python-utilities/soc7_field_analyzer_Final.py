#!/usr/bin/env python3
"""
SOC7 Field Analyzer (Phase 4)
============================

Inputs:
1. Job log (SOC7 + OFFSET)
2. COBOL source (PIC + USAGE)
3. Compile listing (OFFSET + LENGTH)

Output:
- Exact SOC7-causing field with reason and recommendation
"""

import sys
import re
import os


# -------------------------
# Phase 1: Job log analysis
# -------------------------
def analyze_job_log(log_file):
    print("\n=== SOC7 JOB LOG ANALYSIS ===\n")

    if not os.path.exists(log_file):
        print(f"[ERROR] Job log not found: {log_file}")
        sys.exit(1)

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
        sys.exit(0)

    print("SOC7 (Data Exception) detected.")

    offset_match = re.search(
        r"OFFSET\s*(?:[:=]?\s*)X'([0-9A-F]+)'",
        content,
        re.IGNORECASE
    )

    if not offset_match:
        print("Offset not found in job log.")
        sys.exit(1)

    offset_hex = offset_match.group(1)
    offset_dec = int(offset_hex, 16)

    print(f"Offset detected : X'{offset_hex}' ({offset_dec})")

    return offset_dec, offset_hex


# --------------------------------
# Phase 2: COBOL source field parse
# --------------------------------
def parse_cobol_fields(cobol_file):
    print("\n=== COBOL FIELD MAP ===\n")

    if not os.path.exists(cobol_file):
        print(f"[ERROR] COBOL source not found: {cobol_file}")
        sys.exit(1)

    field_pattern = re.compile(
        r"^\s*(\d+)\s+([\w-]+)\s+PIC\s+([^.\s]+)(.*)\.",
        re.IGNORECASE
    )

    fields = {}

    with open(cobol_file, "r", errors="ignore") as f:
        for line in f:
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

                fields[name.upper()] = {
                    "level": level,
                    "pic": pic,
                    "usage": usage
                }

                print(
                    f"Level {level} | Field {name} | "
                    f"PIC {pic} | USAGE {usage}"
                )

    return fields


# ------------------------------------
# Phase 3: Compile listing offset parse
# ------------------------------------
def parse_compile_listing(listing_file):
    print("\n=== COMPILE LISTING OFFSET MAP ===\n")

    if not os.path.exists(listing_file):
        print(f"[ERROR] Compile listing not found: {listing_file}")
        sys.exit(1)

    entry_pattern = re.compile(
    r"^\s*(?:\d+\s+)?([\w-]+).*OFFSET\s+(\d+)\s+LENGTH\s+(\d+)",
    re.IGNORECASE
    )

    offset_map = []

    with open(listing_file, "r", errors="ignore") as f:
        for line in f:
            match = entry_pattern.search(line)
            if match:
                field = match.group(1)
                offset = int(match.group(2))
                length = int(match.group(3))
                start = offset
                end = offset + length - 1

                offset_map.append({
                    "field": field,
                    "start": start,
                    "end": end
                })

                print(
                    f"{field:10} OFFSET {start:04} "
                    f"LENGTH {length} RANGE {start:04}-{end:04}"
                )

    return offset_map


# -----------------------------------------
# Phase 4: Exact SOC7 root cause resolution
# -----------------------------------------
def find_exact_soc7_field(offset, offset_map, cobol_fields):
    print("\n=== EXACT SOC7 ROOT CAUSE ===\n")

    for entry in offset_map:
        if entry["start"] <= offset <= entry["end"]:
            field_name = entry["field"]
            cobol_info = cobol_fields.get(field_name.upper(), {})

            print(f"SOC7 OFFSET      : {offset}")
            print(f"FIELD NAME       : {field_name}")
            print(f"OFFSET RANGE     : {entry['start']:04}-{entry['end']:04}")

            if cobol_info:
                print(f"PIC              : {cobol_info['pic']}")
                print(f"USAGE            : {cobol_info['usage']}")

                if cobol_info["usage"] == "DISPLAY" and re.search(r"9", cobol_info["pic"]):
                    print("\nROOT CAUSE:")
                    print("Invalid numeric data in DISPLAY field.")

                    print("\nRECOMMENDED FIX:")
                    print("Validate input data before MOVE or arithmetic operation.")
                else:
                    print("\nNOTE:")
                    print("Field is COMP/COMP-3; check upstream MOVE or data corruption.")
            else:
                print("\nNOTE:")
                print("Field not found in COBOL source (check copybooks).")

            return

    print("No matching field found for SOC7 offset.")


# -----------------
# Main entry point
# -----------------
def main():
    if len(sys.argv) != 4:
        print(
            "Usage:\n"
            "  python soc7_field_analyzer_Final.py <job_log> <cobol_src> <compile_listing>\n\n"
            "Example:\n"
            "  python soc7_field_analyzer_Final.py "
            "sample_soc7_job_log.txt sample_cobol_program.cbl sample_compile_listing.txt"
        )
        sys.exit(1)

    job_log = sys.argv[1]
    cobol_src = sys.argv[2]
    listing = sys.argv[3]

    offset_dec, _ = analyze_job_log(job_log)
    cobol_fields = parse_cobol_fields(cobol_src)
    offset_map = parse_compile_listing(listing)
    record_offset = offset_dec if offset_dec < 4096 else offset_dec % 256
    find_exact_soc7_field(record_offset, offset_map, cobol_fields)

if __name__ == "__main__":
    main()
