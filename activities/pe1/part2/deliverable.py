#!/usr/bin/env python3

#a = 'a'
#l = [250,251,252,251,250,249,248,249]

def steg_encode_char(char, cover):
    '''LSB encodes a character
    Args:
        char (str): a single character string
        cover (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        None
    '''

    #Read cover into list

    #Convert char to binary
    msgbin = format(ord(char),'0>8b')

    for i in range(0,8):
        coverbin1 = list(format(int(cover[i]),'0>8b'))
        coverbin1[-1] = msgbin[i]
        cover[i] = str(int(''.join(coverbin1),2))

    print(cover)
    pass

def steg_decode_char(stego):
    '''LSB decodes a character
    Args:
        stego (list): list of 8 strings representing integers in the range [0-255]
    Returns:
        str: character that was decoded
    '''

    msgbits = []

    for word in stego:
        msgbits.append(bin(int(word))[-1])
    
    output = chr(int(''.join(msgbits),2))

    print(output)

    return output

    pass

if __name__ == '__main__':
    pass

#steg_encode_char(a,l)
#steg_decode_char(['250','251','253','250','250','248','248','249'])

#msgbits = ['0','1','1','0','0','0','0','1'] 
#print(chr(int(''.join(msgbits),2)))
