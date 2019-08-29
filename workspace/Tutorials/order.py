#!/usr/bin/env python3

def order(sentence):
    # code here
    #split into list
    mylist = sentence.split()
    newlist = ['','','','','','','','','']
                
    #for each item in list find number
    for word in mylist:
        for char in word:
            if char.isdigit():
                newlist[int(char)-1] = word
                                                            
    #place item in list based on number
    output = ' '.join(newlist)
    print(output.strip())

order("is2 Thi1s T4est 3a")
