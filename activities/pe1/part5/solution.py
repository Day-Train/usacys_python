#!/usr/bin/env python3

def steg_encode(msg,cover):
    coverindex = 0
    for char in msg+chr(128):
        charbin = format(ord(char),'0>8b')
        for index in range(0,8):
            coverbinl = list(format(int(cover[coverindex]),'0>8b'))
            coverbinl[-1] = charbin[index]
            cover[coverindex] = int(''.join(coverbinl),2)
            coverindex += 1

def steg_decode(stego):
    msgbits = []
    msg = []
    for b in stego:
        msgbits.append(bin(int(b))[-1])
        if len(msgbits) == 8:
            character = chr(int(''.join(msgbits),2))
            #if ord(character) >= 128:
            if not character.isalnum():
                break
            msg.append(chr(int(''.join(msgbits),2)))
            msgbits = []
    return ''.join(msg)

def read_pgm(filename):
    with open(filename) as fp:
        content = fp.read()
    content = content.split()
    return (content[:4],content[4:])

def write_pgm(filename,content):
    with open(filename,'w') as fp:
        for p in content[0]+content[1]:
            fp.write('{}\n'.format(p))

def encode_pgm(msg,coverfilename,outputfilename):
    content = read_pgm(coverfilename)
    steg_encode(msg,content[1])
    write_pgm(outputfilename,content)

def decode_pgm(stegfilename):
    content = read_pgm(stegfilename)
    return steg_decode(content[1])
    
if __name__ == '__main__':
    encode_pgm('hello world','plain.pgm','steg.pgm')
    #print(decode_pgm('steg.pgm'))

