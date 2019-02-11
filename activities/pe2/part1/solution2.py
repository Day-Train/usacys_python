#!/usr/bin/env python3

import random
import string
import time
from utility import *
from functools import lru_cache

def profile(func):
    def profile_inner(*args,**kwargs):
        begin = time.perf_counter()
        func(*args,**kwargs)
        print('{} took {}s'.format(func.__name__,time.perf_counter()-begin))
    return profile_inner

@lru_cache(maxsize=256)
def bits(byte):
    masks = [2**i for i in range(7,-1,-1)]
    return [1 if byte&mask else 0 for mask in masks]

@profile
def encode_lsb(msg,pgm,ri):
    for byte in msg:
        for bit in bits(byte):
            pgm[ri] ^= (-bit ^ pgm[ri]) & 1
            ri += 1

@profile
def encode_lsb2(msg,pgm,ri):
    for byte in msg:
        for bit in bits(byte):
            if bit and not (pgm[ri] & 1):
                pgm[ri] |= 1
            elif not bit and (pgm[ri] & 1):
                pgm[ri] &= ~1
            ri += 1

@profile 
def encode_lsb3(msg,pgm,ri):
    for byte in msg:
        for bit in bits(byte):
            pgm[ri] = (pgm[ri] & ~1) | (-bit & 1)
            ri += 1

def encode_pgm(msg, infile, outfile):
    '''LSB encodes a message
    Args:
        msg (bytes): bytes object to encode
        infile (str): name of the raw PGM file on disk to use as the cover
        outfile (str): name of the new PGM file to write
    Returns:
        None
    '''
    with open(infile,'rb') as fp:
        pgm = bytearray(fp.read())
    rindex = raster_index(pgm)

    msg = bytearray(msg)
    msg.append(0x80)
    encode_lsb(msg,pgm,rindex)

    with open(outfile,'wb') as fp:
        fp.write(pgm)

def decode_pgm(infile):
    '''LSB decodes a message
    Args:
        infile (str): name of the PGM file to read/decode
    Returns:
        bytes: message that was decoded from the PGM file
    '''
    msg = bytearray()

    with open(infile,'rb') as fp:
        data = fp.read()

    ri = raster_index(data)

    lsb = data[ri] & 0x1
    while True:
        msgbyte = 0
        for shift in range(7,-1,-1):
            msgbyte |= (data[ri] & 0x1) << shift
            ri += 1
        if msgbyte == 0x80:
            break
        msg.append(msgbyte)
    return bytes(msg)

if __name__ == '__main__':
    msg = bytes([ord(random.choice(string.ascii_lowercase)) for _ in range(1500)])
    #msg = b'hello world'
    encode_pgm(msg,'plain.pgm','out.pgm')
    #print(decode_pgm('out.pgm'))
    print(bits.cache_info())
