"""

"""
import argparse

from modules.scanner import scan_ip


def main(host, port):
    result = scan_ip(host, port)
    for op in result.openports:
        print(op)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('host', type=str, help='IP of host to scan')
    parser.add_argument('port', type=str, help='Port to scan')
    args = parser.parse_args()
    main(args.host, args.port)