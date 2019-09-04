#!/usr/bin/env python3

import stego
import files

def sentinel():
    return chr(128)

def encode_pgm(msg,coverfilename,outputfilename):
    '''Encodes a message in a PGM file
    Args:
        msg (str): the message to encode
        coverfilename (str): the name of the PGM file on disk to use as the cover
        outputfilename (str): the name of the new PGM file to write
    Returns:
        None
    '''
    
    #Read file from coverfilename
    cover = files.read_pgm(coverfilename)

    #Encode message
    encodedcover = stego.steg_encode(msg,cover[1])

    #Wrote to file
    files.write_pgm(outputfilename,encodedcover)
    pass

def decode_pgm(filename):
    '''Decodes a message hidden in a PGM file
    Args:
        filename (str): the name of the PGM file that contains a hidden message
    Returns:
        str: the message that was encoded in the PGM file
    '''
    pass

if __name__ == '__main__':
    pass
encode_pgm('hello','plain.pgm','output.pgm')
