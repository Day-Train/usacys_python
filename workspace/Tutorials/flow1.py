#!/usr/bin/env python3

def main():

    #Create a list and print each item using a for loop
    mylist = [1,2,3,4,5]
    for item in mylist:
            print(item)
    
    #Create an iterator and iterate through it
    myiter = iter(["apple","banana","cherry"])
    x = next(myiter)
    print('{}'.format(x))
    x = next(myiter)
    print('{}'.format(x))
    x = next(myiter)
    print('{}'.format(x))

def cards():

    deck = []
    suits = ['\u2660','\u2665','\u2666','\u2663']
    ranks = ['A',2,3,4,5,6,7,8,9,10,'J','Q','K']

    for suit in suits:
        for rank in ranks:
            print('{}{}'.format(suit,rank))
 
def myrange():

    for x in range(10):
        print(x)

def myslice():
    
    mylist = [1,2,3,4,5,6]
    
    #Note that the slice function is inclusive start, exclusive end: [)
    print(mylist[1:4])

    #You can also print in steps: print items indexed between 1 and 4 every two steps
    print(mylist[1:6:2])

def words():

    name = '1a2b3c'
    mylist = name.list()

    for char in mylist:
        if mylist.isdigit():
            print(char)

#cards()
#main()
#myrange()
#myslice()
words()
