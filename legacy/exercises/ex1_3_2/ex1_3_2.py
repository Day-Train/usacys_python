"""

"""
import argparse
import sys

from modules import *


def main(host, ports):
    if '-' in ports:
        ps = ports.split('-')
        result = scan_ports(host, int(ps[0]), int(ps[1]))
    else:
        result = scan_port(host, ports)
    for op in result.openports:
        print(op)


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('host', type=str, help='IP of host to scan')
    parser.add_argument('ports', type=str, help='Ports to scan, ex. 445, 20-25')
    args = parser.parse_args()
    main(args.host, args.ports)