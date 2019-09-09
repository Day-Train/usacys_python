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
    msgbits = []
    msg = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
        if len(msgbits) == 8:
            c = chr(int(''.join(msgbits),2))
            if c ==chr(128):
                break

            msg.append(c)
            msgbits.clear()
            
    
    return ''.join(msg)
    pass

if __name__ == '__main__':
    pass

