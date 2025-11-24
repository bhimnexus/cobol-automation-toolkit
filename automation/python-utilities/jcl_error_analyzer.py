import re

# -------------------------------------------------------------
#  PYTHON UTILITY: JCL ERROR ANALYZER
#  AUTHOR: BHIM SINGH (bhimnexus)
#  DESCRIPTION:
#     - Reads a JCL sysout/log file
#     - Detects common ABENDs, JCL errors, missing datasets
#     - Prints suggestions for RCA
# -------------------------------------------------------------

ERROR_PATTERNS = {
    "S0C7": "Data exception – invalid numeric data.",
    "S0C4": "Protection exception – bad memory reference.",
    "S322": "Time out – job exceeded allocated CPU time.",
    "JCL ERROR": "General JCL error – check syntax.",
    "DATA SET NOT FOUND": "Dataset missing – check DD statements.",
    "IKJ56500A": "Command error – check TSO/ISPF command.",
    "IEC070I": "DD statement issue – missing dataset.",
    "IEC130I": "Invalid volume or UNIT parameter."
}

def analyze_jcl_output(file_path):
    print("\n=== JCL ERROR ANALYZER ===\n")
    
    try:
        with open(file_path, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print(f"[ERROR] File not found: {file_path}")
        return

    found_any = False

    for code, meaning in ERROR_PATTERNS.items():
        if re.search(code, content):
            print(f"[FOUND] {code} → {meaning}")
            found_any = True

    if not found_any:
        print("No known JCL or ABEND errors detected.")

    print("\nAnalysis complete.\n")

if __name__ == "__main__":
    file_path = input("Enter JCL output file path: ")
    analyze_jcl_output(file_path)
