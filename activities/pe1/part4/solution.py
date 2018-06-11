#!/usr/bin/env python3

def read_pgm(filename):
    with open(filename,'r') as fp:
        content = fp.read()
    content = content.split()
    return (content[0:4],content[4:])

def write_pgm(filename,content):
    fp = open(filename,'w')
    for p in content[0]+content[1]:
        fp.write('{}\n'.format(p))
    fp.close()

def invert(content):
    for pixelindex in range(len(content[1])):
        content[1][pixelindex] = str(255 - int(content[1][pixelindex]))

if __name__ == '__main__':
    pass
