# Scan
import os
import glob
from engine.matcher import load_patterns, scan_file

def scan(directory="."):
    patterns = load_patterns()
    swift_files = glob.glob(os.path.join(directory, "**/*.swift"), recursive=True)

    print(f"🔍 Scanning directory: {os.path.abspath(directory)}")
    print(f"📦 Swift files found: {len(swift_files)}")

    if not swift_files:
        print("⚠️  No Swift files found. Please check the path.")
        return

    for filepath in swift_files:
        matches = scan_file(filepath, patterns)
        if matches:
            print(f"\n📄 File: {filepath}")
            for match in matches:
                print(f"  🔹 Line {match['line']}: {match['code']}")
                print(f"     💡 {match['description']}")
                print()  # blank line for readability
