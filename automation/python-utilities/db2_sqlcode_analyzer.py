"""
DB2 SQLCODE Analyzer
-------------------
Analyzes DB2 SQLCODEs and provides explanation and fix suggestions.

Author: Bhim Singh
"""

import sys

SQLCODE_MAP = {
    "-911": {
        "meaning": "Deadlock or timeout occurred.",
        "causes": [
            "Long-running transactions",
            "Lock contention",
            "Missing COMMITs"
        ],
        "fix": [
            "Add COMMIT checkpoints",
            "Reduce transaction scope",
            "Reschedule conflicting jobs"
        ]
    },
    "-913": {
        "meaning": "Deadlock or timeout (rolled back).",
        "causes": [
            "High lock contention",
            "Utility running on object"
        ],
        "fix": [
            "Retry transaction",
            "Check running utilities",
            "Coordinate batch schedules"
        ]
    },
    "-805": {
        "meaning": "DBRM or package not found.",
        "causes": [
            "Program not rebound",
            "Wrong PLAN or PACKAGE",
            "Incorrect collection ID"
        ],
        "fix": [
            "Rebind DBRM/package",
            "Verify PLAN/PACKAGE name",
            "Check environment mismatch"
        ]
    },
    "-904": {
        "meaning": "Resource unavailable.",
        "causes": [
            "Tablespace in STOP state",
            "Dataset unavailable",
            "Utility running"
        ],
        "fix": [
            "Start tablespace",
            "Check dataset availability",
            "Wait for utility completion"
        ]
    },
    "-818": {
        "meaning": "Timestamp mismatch between load module and DBRM.",
        "causes": [
            "Program recompiled without rebind",
            "Old load module deployed"
        ],
        "fix": [
            "Recompile and rebind",
            "Ensure correct load library"
        ]
    },
    "+100": {
        "meaning": "No rows found.",
        "causes": [
            "SELECT returned no rows",
            "End of cursor reached"
        ],
        "fix": [
            "Check application logic",
            "Handle NOT FOUND condition properly"
        ]
    }
}

def analyze_sqlcode(sqlcode):
    print("\n=== DB2 SQLCODE ANALYSIS ===\n")

    info = SQLCODE_MAP.get(sqlcode)

    if not info:
        print(f"SQLCODE {sqlcode} is not defined in this analyzer.")
        return

    print(f"SQLCODE : {sqlcode}")
    print(f"Meaning : {info['meaning']}\n")

    print("Possible causes:")
    for cause in info["causes"]:
        print(f" - {cause}")

    print("\nSuggested fixes:")
    for fix in info["fix"]:
        print(f" - {fix}")

    print("\n=== ANALYSIS COMPLETE ===\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python db2_sqlcode_analyzer.py <SQLCODE>")
        sys.exit(1)

    analyze_sqlcode(sys.argv[1])
