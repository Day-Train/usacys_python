#!/usr/bin/env python3

def steg_encode(msg, cover):
    '''LSB encodes a message
    Args:
        msg (str): a string message to encode
        cover (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''

    #Convert msg to char list
    msglist = list(msg)

    #Conver char list to bin list
    msglistbin = []
    for char in msglist:
        msglistbin.append(format(ord(char),'0>8b'))
    print(msglistbin)


    pass

def steg_decode(stego):
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    pass

if __name__ == '__main__':
	pass

steg_encode('hello',['250']*16)
