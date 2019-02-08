#!/usr/bin/env python3
import unittest
import unittest.mock
import importlib
import sys
import pathlib
import random
import io
import binascii
import string
import utility
import socket
import multiprocessing

import solution as student

class TestPart2(unittest.TestCase):

    def server(self,q):
        server_socket = socket.socket()
        server_socket((bindto='',port=self.port))
        server_socket.listen()
        
        connection,address = server_socket.listen()
        
        message = bytearray()
        bytes_received = server_socket.recv(self.recv_buffer_size)
        while len(bytes_received):
            message.extend(bytes_received)
            bytes_received = server_socket.recv(self.recv_buffer_size)

        

    def setUp(self):
        self.payload = b'aW1wb3J0IHdlYmJyb3dzZXIKd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL3d3dy55b3V0dWJlLmNv\nbS93YXRjaD92PW9IZzVTSllSSEEwJyxuZXc9MSk=\n'
        self.port = random.randint(1025,65530)
        self.recv_buffer_size = 64
    
    def test_connection_handler(self):
        with unittest.mock.patch('socket.socket') as mock_socket:
            mock_socket.return_value.send.return_value = self.payload

    def test_client(self):
        pass

    def test_server(self):
        pass



if __name__ == '__main__':
    unittest.main()
