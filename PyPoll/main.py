# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 18:12:48 2019

@author: User
"""

import csv
import os
#My Functions
def RowCount(mylist):
    return sum(1 for row in mylist)-1

def ColumnTotal(mylist,MyCol):
    return [sum(int(r[MyCol]) for r in mylist)][0]

def ResetCSVStartPOS(myList,Myreader):
    myList.seek(0)
    next(Myreader)


def Convert(tup, di): 
    for a, b,c in tup: 
        di.setdefault(c, []).append(a) 
    return di 
def WriteOutput(mylist):
    with open('Output.txt','w+') as f:
        for li in mylist:
            print(li)
            print(li,file=f)
def MinMax(test,ThisList,mycol):
    tmp_value=0
    tmp_li=[]
    if test== 'Max' or test =='max':
        for li in ThisList:
            if li[mycol]>tmp_value:
                tmp_value=li[mycol]
                tmp_li=li
    elif test == 'Min' or test =='min':
        for li in ThisList:
            if li[mycol]<tmp_value:
                tmp_value=li[mycol]
                tmp_li=li
    return tmp_li
def ReadFile(FileName):
   with open(filename,newline="") as CSVfile:
    CSVReader = csv.reader(CSVfile,delimiter=",")
    next(CSVReader)
    return list(CSVReader)    
#set file path
#filename = 'C:\\Users\\User\\Desktop\\python testing with spyder\\budget_data.csv'

filename = os.path.join('Resources','election_data.csv')
Mylist =ReadFile(filename)

d={}
CName=[]
SumTotes=[]
Ptotes=[]
FinalList=[]
temp_List=[]
x=Convert(Mylist, d)
RCount=RowCount(Mylist)

for key, value in x.items() :
    CName.append(key)
    SumTotes.append(len([item for item in value if item]))
    Ptotes.append(len([item for item in value if item])/RCount)
    
FinalList=list(zip(CName,SumTotes,Ptotes))



temp_List.append('Election Results')
temp_List.append('-------------------------')
temp_List.append(f'Total Votes: {RCount} ')
temp_List.append('-------------------------')  
for Rows in FinalList:
    temp_List.append(f'{Rows[0]} : {Rows[2]:.3%} ({Rows[1]})')
temp_List.append('-------------------------')   

Winner=MinMax("Max",FinalList,1)
temp_List.append(f'Winner: {Winner[0]}')
WriteOutput(temp_List)

