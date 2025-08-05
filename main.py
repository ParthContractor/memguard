# Main
import argparse
from cli.scan import scan

def main():
    parser = argparse.ArgumentParser(description="memguard - Swift memory leak scanner")
    subparsers = parser.add_subparsers(dest="command")

    scan_parser = subparsers.add_parser("scan", help="Scan Swift files for leak-prone patterns")
    scan_parser.add_argument("--dir", default=".", help="Directory to scan (default: current)")

    args = parser.parse_args()

    if args.command == "scan":
        scan(args.dir)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
