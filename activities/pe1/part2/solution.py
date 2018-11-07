#!/usr/bin/env python3

def steg_encode_char(char, cover):
    '''LSB encodes a character
    Args:
        char (str): a single character string
        cover (list): list of integers in the range [0-255]
    Returns:
        None
    '''
    charbin = format(ord(char),'0>8b')
    for index in range(0,8):
        coverbinl = list(format(int(cover[index]),'0>8b'))
        coverbinl[-1] = charbin[index]
        cover[index] = str(int(''.join(coverbinl),2))

def steg_decode_char(stego):
    '''LSB decodes a character
    Args:
        stego (list): list of integers in the range [0-255]
    Returns:
        str: character that was decoded
    '''
    #msgbits = []
    #for b in stego:
    #    msgbits.append(bin(int(b))[-1])
    #return chr(int(''.join(msgbits),2))

    return chr(int(''.join([bin(int(b))[-1] for b in stego]),2))

if __name__ == '__main__':
    pass
