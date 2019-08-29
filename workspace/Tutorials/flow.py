#!/usr/bin/env python3

val = input('Please enter an integer here: ')

def myfunc(a):
    if(a > 10):
        print('{} is greater than 10'.format(a))
    elif(a < 10):
        print('{} is less than 10'.format(a))
    elif(a == 10):
        print('{} equals 10'.format(a))
#    else:
#        print('{} is not an integer'.format(a))

myfunc(val)
