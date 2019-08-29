#!/usr/bin/env python3

a = int(input('Please enter a positive number: '))

if((a % 3) == 0 and (a % 5) == 0):
    print('fizzbuzz')
elif(a % 5 == 0):
    print('buzz')
elif(a % 3 == 0):
    print('fizz')
else:
    print(a)

