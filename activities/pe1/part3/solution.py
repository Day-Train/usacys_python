#!/usr/bin/env python3

def steg_encode(msg,cover):
    coverindex = 0
    for char in msg:
        charbin = format(ord(char),'0>8b')
        for index in range(0,8):
            coverbinl = list(format(int(cover[coverindex]),'0>8b'))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = str(int(''.join(coverbinl),2))
            coverindex += 1

def steg_decode(stego):
    msgbits = []
    msg = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
        if len(msgbits) == 8:
            msg.append(chr(int(''.join(msgbits),2)))
            msgbits = []
    return ''.join(msg)

if __name__ == '__main__':
    pass
