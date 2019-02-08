#!/usr/bin/env python3
import socket
import marshal
import multiprocessing
import time
import base64

PAYLOAD = b'aW1wb3J0IHdlYmJyb3dzZXIKd2ViYnJvd3Nlci5vcGVuKCdodHRwczovL3d3dy55b3V0dWJlLmNv\nbS93YXRjaD92PW9IZzVTSllSSEEwJyxuZXc9MSk=\n'


def connection_handler(connection):
    '''Handles connections to the server and sends PAYLOAD
    Args:
        connection (socket.socket): socket used to communicate with the connected client
    Returns:
        None
    '''
    raise NotImplementedError # This line should be removed
    
    # Student implemention goes here ##########################################



    ###########################################################################

    # Server initiates the close resulting in TIME_WAIT.
    # Client can then detect end-of-data by receiving 0 bytes.
    connection.shutdown(socket.SHUT_RDWR)
    connection.close()


def server(bindto='',port=12345):
    '''Accepts connections and spawns processes to handle them
    Args
        bindto (str): IPv4 address in dotted decimal notation to which clients can connect
        port (int): port number to which clients can connect
    Returns:
        None
    '''
    raise NotImplementedError # This line should be removed

    # Student implementation goes here ########################################



    ###########################################################################

def client(connectto='127.0.0.1',port=12345):
    '''Connects to a server and attempts to execute the received code
    Args:
        connectto (str): IPv4 address in dotted decimal notation of the server to connect to
        port (int): port number that the server is listening on
    Returns:
        None
    '''
    raise NotImplementedError # This line should be removed

    message = bytearray() # extend this bytearray with data received until 0 bytes received

    # Student implementation goes here ########################################


    
    ###########################################################################

    # Attempt to decode and execute whatever came from the server
    codebytes = base64.decodebytes(message)
    codeobj = compile(codebytes,'<string>','exec')
    exec(codeobj)


if __name__ == '__main__':
    pass
