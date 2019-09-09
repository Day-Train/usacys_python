#!/usr/bin/env python3

import part3    #encoding/decoding methods
import part4    #file i/o

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
    content = part4.read_pgm(coverfilename)

    #Encode message + sentinel
    part3.steg_encode(msg+sentinel(),content[1])

    #Write to file
    part4.write_pgm(outputfilename,content)
    pass

def decode_pgm(filename):
    '''Decodes a message hidden in a PGM file
    Args:
        filename (str): the name of the PGM file that contains a hidden message
    Returns:
        str: the message that was encoded in the PGM file
    '''

    content = part4.read_pgm(filename)

    return part3.steg_decode(content[1])

    pass

if __name__ == '__main__':
    encode_pgm('super secret message','plain.pgm','steg.pgm')
    print(decode_pgm('steg.pgm'))
    
    pass
