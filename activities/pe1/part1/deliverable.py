#!/usr/bin/env python3

def invert(l):
    """Inverts the given list
    Args:
        l (list): list of strings representing integers in the range [0-255]
    Returns:
        None
    """
    
    k = 0

    for word in l:
        l[k] = str(255 - int(word))
        k += 1

    pass

def inverted(l):
    """Returns a new list that is the given list inverted
    Args:
        l (list): list of strings representing integers in the range [0-255]
    Returns:
        list: new list that is the given list inverted
    """

    newlist = l.copy()
    m = 0

    for word in newlist:
        newlist[m] = str(255 - int(word))
        m += 1

    #Alternatively
    #newl = []
    #for item in l:
    #   newl.apprent(str(255 - int(item)))
    #return newl
    return newlist

    pass

if __name__ == '__main__':
    pass
