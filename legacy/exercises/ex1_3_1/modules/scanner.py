import sys
import os
import socket

sys.path.append(os.path.join("C:\\portscanner\\objects"))

from hosts import Host

def scan_ip(ip, port):
    host = Host(ip)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((host.ip, int(port)))
    if result == 0:
        host.add_port(port)
    sock.close()
    return host