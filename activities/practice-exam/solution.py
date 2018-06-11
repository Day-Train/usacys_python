#!/usr/bin/env python3

def q1(floatstr):
    '''
    Given the floatstr, which is a comma separated string of
    floats, return a list with each of the floats in the 
    argument as elements in the list.
    '''
    '''
    #One method
    newlist = []
    for y in floatstr.split(','):
        newlist.append(float(y))
    return newlist
    '''
    return [float(x) for x in floatstr.split(',')]


def q2(*args):
    '''
    Given the variable length argument list, return the average
    of all the numbers in the list as a float
    '''
    return sum(*args)/len(*args)

def q3(lst,n):
    '''
    Given a list (lst) and a number of items (n), return a new 
    list containing the last n entries in lst.
    '''
    return lst[-n:]
    
def q4(strng):
    '''
    Given an input string, return a list containing the ordinal numbers of 
    each character in the string in the order found in the input string.
    '''
    return [ord(x) for x in list(strng)]

def q5(strng):
    '''
    Given an input string, return a tuple with each element in the tuple
    containing a single word from the input string in order.
    '''
    return tuple(list(strng.split()))

def q6():
    '''
    Given an input string similar to the below, craft a regular expression  
    pattern to match and extract the date, time, and temperature in groups  
    and return this pattern. Samples given below.
    Date: 12/31/1999 Time: 11:59 p.m. Temperature: 44 F
    Date: 01/01/2000 Time: 12:01 a.m. Temperature: 5.2 C
    '''
    #pat = r"Date:\s+([0-9]+/[0-9]+/[0-9]+)\s+Time:\s+([0-9]+:[0-9]+\s[a|p]\.m\.)\s+Temperature:\s+([0-9.]+\s[KkFfCc])"
    pat = r"Date: (\d+/\d+/\d+) Time: (\d+:\d+ .\.m\.) Temperature: ([\d\.]+ [FfCc])"
    return pat

def q7(filename):
    '''
    Given a filename, open the file and return the length of the first line 
    in the file excluding the line terminator.
    '''
    with open(filename) as fp:
        return len(fp.readline()) - 1 #Line terminator

def q8(filename,lst):
    '''
    Given a filename and a list, write each entry from the list to the file
    on separate lines until a case-insensitive entry of "stop" is found in 
    the list. If "stop" is not found in the list, write the entire list to 
    the file on separate lines.
    '''
    #'''
    with open(filename, 'w') as fp:
        for item in lst:
            if item.lower() == 'stop':
                break
            fp.write('{}\n'.format(item))
    #'''

def q9(miltime):
    '''
    Given the military time in the argument miltime, return a string 
    containing the greeting of the day.
    0300-1159 "Good Morning"
    1200-1559 "Good Afternoon"
    1600-2059 "Good Evening"
    2100-0259 "Good Night"
    '''
    if miltime >= 301 and miltime < 1200:
        return "Good Morning"
    elif miltime >= 1200 and miltime < 1600:
        return "Good Afternoon"
    elif miltime >= 1600 and miltime < 2100:
        return "Good Evening"
    elif miltime >= 2100 or miltime < 300:
        return "Good Night"
    
def q10(numlist):
    '''
    Given the argument numlist as a list of numbers, return True if all 
    numbers in the list are NOT negative. If any numbers in the list are
    negative, return False.
    '''
    for i in numlist:
        if i < 0:
            return False
    return True

