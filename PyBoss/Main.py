# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 21:11:32 2019

@author: User
"""
import os
import csv
import datetime

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




Mylist=[]
WID=[]
FName=[]
LName=[]
DOB=[]
F_SSN=[]
ST=[]
Final_List=[]   
Tmp_List=[]
filename = os.path.join('Resources','employee_data.csv')
Mylist=ReadFile(filename)

us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
 
for Rows in Mylist:
    WID.append(Rows[0])
    tmp_String=str(Rows[1])
    FName.append(mid(tmp_String,0,tmp_String.find(' ')))
    LName.append(mid(tmp_String,tmp_String.find(' ')+1,len(tmp_String)-len(mid(tmp_String,0,tmp_String.find(' ')))))
    DOB.append(datetime.datetime.strptime(Rows[2],'%Y-%m-%d').strftime('%m/%d/%y'))
    tmp_String = str(Rows[3])
    F_SSN.append('###-##-' + tmp_String[-4:])
    ST.append(us_state_abbrev[str(Rows[4])])

Final_List=list(zip(WID,FName,LName,DOB,F_SSN,ST))


Tmp_List.append('Emp ID|First Name|Last Name|DOB|SSN|State')
for rows in Final_List:
    Tmp_List.append(f'{rows[0]}|{rows[1]}|{rows[2]}|{rows[3]}|{rows[4]}|{rows[5]}')
    
WriteOutput(Tmp_List)
   