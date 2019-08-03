# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 13:16:08 2019

@author: User
"""
import os
import csv
import locale
locale.setlocale(locale.LC_ALL, '' )


def left(s, amount):
    return s[:amount]
def right(s, amount):
    return s[-amount:]

def mid(s, offset, amount):
    return s[offset:offset+amount]

#My Functions
def RowCount(mylist):
    return sum(1 for row in mylist)-1

def ColumnTotal(mylist,MyCol):
    return [sum(float(r[MyCol]) for r in mylist)][0]

def ResetCSVStartPOS(myList,Myreader):
    myList.seek(0)
    next(Myreader)

def WriteOutput(mylist):
    filepath=os.path.join('Output','Output.txt')
    with open(filepath,'w+') as f:
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
filename = os.path.join('Resources','budget_data.csv')
#Open the file
Mylist=ReadFile(filename)
    
MyText=[]
RowDiff=[]
  

last_value = list(map(lambda x:x[-1],Mylist))
for LI in range(len(last_value)):
    if LI ==0 :
        RowDiff.append(0)
    else:   
        RowDiff.append(float(last_value[LI])-float(last_value[LI-1]))
 
for LI in range(len(Mylist)):
    Mylist[LI].append(int(RowDiff[LI]))


   
MAX=MinMax("Max",Mylist,2)
MIN=MinMax("Min",Mylist,2)
MyText.append('Financial Analysis')
MyText.append('----------------------------')
MyText.append(f'Total Months: {RowCount(Mylist)}')
MyText.append(f'Total: {locale.currency(ColumnTotal(Mylist,1), grouping=True)}')
MyText.append(f'Average  Change: {locale.currency(ColumnTotal(Mylist,2)/ RowCount(Mylist), grouping = True)}') 
MyText.append(f'Greatest Increase in Profits: {MAX[0]} Amount : {locale.currency(MAX[2] , grouping = True)}')
MyText.append(f'Greatest Decrease in Profits:{MIN[0]} Amount : {locale.currency(MIN[2] , grouping = True)}')    
WriteOutput(MyText)
