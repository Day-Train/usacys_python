#!/usr/bin/env python3

import socket

#Server Code
def tcp_echo():
    s = socket.socet() #AF_INET and SOCK_STREAM by default
    s.bind(('0.0.0.0',12345))
    s.listen()
    while True:
        conn, address = s.accept()
        print('connection accepted from {}'.format(address))
        conn.sendall(conn.recv(4096))
        conn.close()

def udp_echo():
    s = socket.socket(type = socket.SOCK_DGRM)
    s.bind(('0.0.0.0',12345))
    while True:
        data, address = s.recvfrom(4096)
        print(data,'received from {}'.format(address))
        s.sendto(data,address)

#Client Code
def client():
    s = socket.socket()
    s.connect((address,port))
    s.sendall(b'jason')
    msg = bytearray()
    data = s.recv(1)
    while data:
        msg.extend(data)
        data = s.recv(1)
    return msg

if __name__ == '__main__':
    tcp_echo()
