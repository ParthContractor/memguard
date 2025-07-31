# Main
import argparse
from cli.scan import scan

def main():
    parser = argparse.ArgumentParser(description="memguard CLI - Scan Swift files for memory risk patterns")
    subparsers = parser.add_subparsers(dest='command')

    # Scan command
    scan_parser = subparsers.add_parser('scan', help='Scan Swift files in the current directory')
    
    args = parser.parse_args()

    if args.command == 'scan':
        scan()

if __name__ == '__main__':
    main()
