#!/user/bin/env python3

import os

def myfunc():
    with open("mysource.txt") as source, open("mycopy.txt", 'w') as destination:
        destination.write(source.read())

myfunc()
