#!/usr/bin/env python3

def steg_encode(msg, cover):
    '''LSB encodes a message
    Args:
        msg (str): a string message to encode
        cover (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    '''
    #for sentinel bit uncomment following line of code
    #msg = msg + chr(128)
    coverindex = 0
    for char in msg:
        charbin = format(ord(char), '0>8b')
        for index in range(0,8):
            coverbinl = list(format(int(cover[coverindex]), '0>8b'))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = str(int(''.join(coverbinl),2))
            coverindex += 1


    pass

def steg_decode(stego):
    '''LSB decodes a message
    Args:
        stego (list): list of strings representing integers in the range [0-255]
    Returns:
        str: message that was decoded
    '''
    #Break out of decoding when sentinel bit found
    #e.g. if ord(b) == 128: break
    msgbits = []
    msg = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
        if len(msgbits) == 8:
            msg.append(chr(int(''.join(msgbits),2)))
            msgbits.clear()
    
    return ''.join(msg)
    pass

if __name__ == '__main__':
    pass

