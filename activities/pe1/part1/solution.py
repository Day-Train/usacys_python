#!/usr/bin/env python3

def invert(l):
    for n in range(0,len(l)):
        l[n] = str(255 - int(l[n]))

def inverted(l):
    #newl = []
    #for n in l:
    #    newl.append(str(255-int(n)))
    return [str(255-int(n)) for n in l]

if __name__ == '__main__':
    pass
