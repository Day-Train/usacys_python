#!/usr/bin/env python3

def my_func(filename, rainbow, bignum, x):
        ret = 0
        if filename == '':
            ret |= 0x1
        if rainbow:
            ret |= 0x10
        if bignum > 1000000:
            ret |= 0x20
        if x != 0 and x != 1:
            ret |= 0x2
        return ret
