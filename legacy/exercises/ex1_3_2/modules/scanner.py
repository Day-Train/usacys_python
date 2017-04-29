import sys
import os
import socket
import pyping

from objects.hosts import Host


def scan_port(ip, port):
    host = Host(ip)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host.ip, int(port)))
    if result == 0:
        host.add_port(port)
    sock.close()
    return host

def scan_ports(ip, min_port, max_port):
    host = Host(ip)
    for port in xrange(min_port, max_port):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((host.ip, int(port)))
        if result == 0:
            host.add_port(port)
        sock.close()
    return host