#!/user/bin/env python3

import os

def myfunc():
    with open("mysource.txt") as source, open("mycopy.txt", 'w') as destination:
        destination.write(source.read())

myfunc()

#Reads 5 bytes
with open('test.txt') as fp:
    fp.read(5)

#Reads one line then read all lines
with open('test.txt') as fp:
    fp.readline()
    fp.readlines()

#Read and print each line single spaced
with open('test.txt') as fp:
    for line in fp:
        print(line, end='') #without the end='', outpu will be double spaced

import os
with open('test.txt') as fp:
    fp.tell()
    fp.read(5)
    fp.tell()
    fp.read(5)
    fp.tell()
    fp.seek(0, os.SEEK_SET) #reset to beginning
    fp.tell()

#Read a file and write it to another
with open('test.txt') as source, open('copy.txt', 'w') as destination
    destination.write(source.read())

#Write user supplied data to file
with open("user.txt", 'w') as destination:
    while True:
        data = input("Text for file or EOF? ")
        if data == 'EOF':
            break
        destination.write(data + '\n')

#Find total characters
num = len(open('travel_plans.txt.').read().split())

#Find number of lines
num_lines = len(open('school_prompt.txt').readlines())

#Assign the first 30 characters of school_prompt.txt as a string
beginning_chars = open('school_prompt.txt').read()[:30]

#Using the file school_prompt.text assign third word of every line to a list
three = []
with open('school_prompt') as fp:
    for line in fp:
        three.append(line.split()[2])
