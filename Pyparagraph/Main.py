# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 17:10:41 2019

@author: User
"""

import os
import csv
import string

def left(s, amount):
    return s[:amount]
def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

#My Functions
def RowCount(mylist):
    return sum(1 for row in mylist)-1


def WriteOutput(mylist):
    with open('Output.txt','w+') as f:
        for li in mylist:
            print(li)
            print(li,file=f)


def ReadFile(FileName):
   with open(filename,newline="") as CSVfile:
    CSVReader = csv.reader(CSVfile,delimiter=",")
    next(CSVReader)
    return list(CSVReader) 
def ReadTxt(fileName):   
    with open(filename,'r') as myfile:
        if myfile.mode=='r':
            return myfile.read()
def WordCount(test_string):
    return sum([i.strip(string.punctuation).isalpha() for i in test_string.split()])          
def SentCount(test_string):
    count=0
    for i in test_string: 
        if i == '.': 
            count = count + 1
    return count
    

filename = os.path.join('Resources','TestText.txt')
Mylist=ReadTxt(filename)
WCnt=0
PCnt=0
ALCnt = 0
ASCnt = 0

WCnt=WordCount(Mylist)
PCnt = SentCount(Mylist)


