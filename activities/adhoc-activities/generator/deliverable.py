#!/usr/bin/env python3

def fib():
    '''
    Generator that yields the Fibonacci series forever.
    Each number is the sum of the two preceding numbers,
    starting from 0 and 1
    '''
    a,b = 0,1
    while True:
        yield a
        a,b = b, a+b




if __name__ == '__main__':
    fibgen = fib()
    for i in range(17):
        print(next(fibgen))



