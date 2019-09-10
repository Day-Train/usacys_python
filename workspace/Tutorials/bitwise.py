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

#mask - If 'mask' does not have bit 0x100 set to 1, set the bit 0x80 in the return value
#
#bVal - If 'bVal' is not 0 or 1, set bet 0x1000 in the return value
def my_mask_func(mask,bVal):
    ret = 0
    
    if (mask&0x100) == 0:
        ret |= 0x80

    if bVal != 0 and bVal != 1:
        ret |= 0x1000

    return ret

#Given a string as an argument (strng), return the argument reversed and
#with all spaces replaced with the underscore '_' character.
def my_strng_func(strng):
    return '_'.join(strng[::-1].split(' '))

    #alternative
    #return strng[::-1].replace(' ','_')

