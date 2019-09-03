#!/usr/bin/env python3

import os

def main()
    with open("file", 'rb') as binfle:
        header = binfile.read(4)
            if header == bytes([0xff, 0xd8, 0xff, 0xe0]):
                print('JPEG')
            elif:
                #Include statements for other file types
            else:
                print('Unknown file type {} {} {} {}'.format(hex(header[0]), hex(header[1]), hex(header[2]), hex(header[3]))
