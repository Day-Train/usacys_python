#!/usr/bin/env python3

import nlp
import sys
import collections
import string

def caesar_encrypt(plaintext,key):
    trans = collections.deque(string.ascii_lowercase)
    trans.rotate(key)
    cipher = str.maketrans(string.ascii_lowercase,''.join(trans))
    return plaintext.lower().translate(cipher)

def caesar_decrypt(ciphertext,key):
    trans = collections.deque(string.ascii_lowercase)
    trans.rotate(key)
    cipher = str.maketrans(''.join(trans),string.ascii_lowercase)
    return ciphertext.lower().translate(cipher)

def caesar_brute(ciphertext,trainingtext):
    trained = nlp.vsm(trainingtext)
    possible = []
    for key in range(0,26):
        pt = caesar_decrypt(ciphertext,key)
        metric = nlp.similarity(trained,nlp.vsm(pt))
        possible.append((metric,key,pt))
    return possible

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
            if ord(character) >= 128:
            #if not character.isalnum():
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
    stego = input('Enter the filename for the image')
    filename = input('Enter the filename for training text')
    with open(filename) as fp:
        trainingtext = fp.read()
    ciphertext = decode_pgm(stego)

    print(max(caesar_brute(ciphertext,trainingtext)))
