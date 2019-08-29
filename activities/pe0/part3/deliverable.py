#!/usr/bin/env python3

def guess_number(number):

    n = number
    val = int(input('Please enter a number between 0 and 100: '))
    
    def checker(k):
        if(k < 0 or k > 100):
            val = int(input('Out of bounds, please enter a number between 0 and 100: '))
    
    checker(val)

    while(True):
        checker(val)
        if(val == n):
            checker(val)
            print('WIN')
            break
        elif(val < n):
            checker(val)
            print('Too low')
            val = int(input('Please enter a number between 0 and 100: '))
        elif(val > n):
            checker(val)
            print('Too high')
            val = int(input('Please enter a number between 0 and 100: '))

guess_number(23)
