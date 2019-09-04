#!/usr/bin/env python3

def read_pgm(filename):
    '''Reads a PGM file
    Args:
        filename (str): the file name of a PGM file on disk to read from
    Returns:
        tuple:
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    '''

    headervalues = []
    pixelvalues = []

    with open(filename) as fp:
        data = fp.read()
        raw = data.split()

        i = 0
        while i < 4:
            headervalues.append(raw[i])
            i += 1

        for j in range(i,len(raw)):
            pixelvalues.append(raw[j])
            j += 1
    
    readtuple = (headervalues, pixelvalues)
    return readtuple

    #print(readtuple)

    pass

def write_pgm(filename,content):
    '''Writes a PGM file
    Args:
        filename (str): the file name to be used for the written file
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''
    with open(filename, 'w') as fp:
        i = 0
        while i < 4:
            fp.write(content[0][i] + '\n')
            i += 1

        j = 0
        while j < len(content[1]):
            fp.write(content[1][j] + '\n')
            j += 1

    pass

def invert(content):
    '''Modifies the pixel intensities of the given content to be inverted
    Args:
        content (tuple):
            1st element is a list of PGM header values as strings
            2nd element is a list of pixel intensities as strings
    Returns:
        None
    '''

    inverted = []

    for pixel in content[1]:
        inverted.append(str(255 - int(pixel)))

    invertedtuple = (content[0],inverted)

    #return invertedtuple
    pass

if __name__ == '__main__':
    contents = read_pgm('plain.pgm')
    invert(contents)
    write_pgm('inverted.pgm',contents)
    
    pass


