#!/usr/bin/env python3

def read_pgm(filename):
    '''Reads a PGM file
    Args:
        filename (str): the file name of a PGM file on disk to read from
    Returns:
        tuple:
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings'''
    with open(filename) as internal:
        data = internal.read()
    
    pixels = list(data.split())
    header = pixels[0:4:]
    pixel_int = pixels[4::]
    final = (header,pixel_int)
    return(final)
    pass

def write_pgm(filename,content):
    '''Writes a PGM file
    Args:
        filename (str): the file name to be used for the written file
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None'''
    
        
        
    with open(filename,'w') as internal:
        for field in content[0] + content[1]:
            internal.write(field+'\n')    
    pass

def invert(content):
    '''Modifies the pixel intensities of the given content to be inverted
    Args:
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None'''
    for idx in range(len(content[1])):
        content[1][idx] = str(255 - int(content[1][idx]))
        
    pass

if __name__ == '__main__':
    pass
    content = read_pgm('plain.pgm')
    invert(content)
    write_pgm('inverted.pgm', content)
