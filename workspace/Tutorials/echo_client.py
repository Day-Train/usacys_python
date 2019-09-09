#!/usr/bin/env python3

import socket

#Implement exception handling by wrapping s.connect() in a try block
 
ip_addr = '192.168.241.207'     
port_num = 12345

def tcp_echo():
    s = socket.socket()
    try:
        s.connect((ip_addr,port_num))
    except:
        print('Unable to connect to {}:{}'.format(ip_addr,port_num))
    s.sendall(b'hello world')
    echodata = s.recv(4096)
    print(echodata)

def udp_echo():
    s = socket.socket(type = socket.SOCK_DGRAM)
    try:
        s.sendto(b'Wie geht\'s es Ihnen?',(ip_addr,port_num))
    except:
        print('An exception occurred')
    echodata,address = s.recvfrom(4096)
    print(echodata)

if __name__ == '__main__':
    udp_echo()
