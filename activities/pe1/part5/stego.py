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

    coverlistbin = []
    msglistbin = []
    
    #Convert integer values to binary
    for item in cover:
        coverlistbin.append(format(int(item), '0>8b'))

    #Convert char list to binary
    for char in msglist:
        msglistbin.append(format(ord(char),'0>8b'))

    #For char at index i, position j in msglistbin
    #Take string at index i in coverlistbin and replace element [-1] with char
    #char       cover
    # i,j       i,-1
    # i,j+1     i+1,-1
    #...
    # i,j+7     i+7,-1
    # i+1,j     i+8,-1
    #...
    # i+1,j+7   i+15,-1
    #...
    #...
    # i+n,j+7   i+8*n-1,-1

    #This list will store the modified cover in binary
    output = []

    i = 0
    for i in range(len(msglistbin)):
        k = 0
        while k < 8:
            word = coverlistbin[i][0:7] + msglistbin[i][k]
            output.append(word)
            k += 1
        i += 1

    #This list will store the modified cover as integers
    final = []

    for byte in output:
        final.append(int(byte,2))

    return final
    pass

def steg_decode(stego):
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    stegolistbin = []

    for value in stego:
        stegolistbin.append(format(int(value),'0>8b'))

    msgbin = ''

    i = 0
    for i in range(len(stego)):
        msgbin += stegolistbin[i][-1]
        i += 1

    msglistbin = [msgbin[k:k+8] for k in range(0, len(stego), 8)]

    charnum = []
    for item in msglistbin:
        charnum.append(chr(int(item,2)))

    output = ''.join(charnum)

    return output
    pass

if __name__ == '__main__':
	pass

stego = steg_encode('hello',['250']*40)
steg_decode(stego)
