# -*- coding: utf-8 -*-
"""
Read tfm transactions file and put the text into a dataframe for the BEM team

@author: FY776EW
"""

#
#from docx import Document
#
#    # read the docx file
#rootdir = 'C:\\Users\\fy776ew\\Documents\\_DS\_rawsourcedata\\'
##doc = docx.Document(os.path.join(rootdir, "oracle-corporation_annual_report_1994.docx"))
#document = Document('oracle-corporation_annual_report_1994.docx')
import os
import os.path
from os.path import basename, splitext
import configparser
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy import Text, Column, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
import docx2txt
import docx #docx library
from docx import Document
import string
import pandas as pd
import csv
import re, sys, os
import numpy as np
# extract text
rootdir = "C:\\Users\\fy776ew\\Documents\\_DS\_rawsourcedata\\"

file=os.path.join(rootdir, "sec3_transactions_2019.docx")
textfile=os.path.join(rootdir, "sec3_transactions_2019.txt")

def maingrp():
    with open(textfile, 'r', encoding='utf-8') as f:
            lines=f.readlines()
    for line in lines:
        pattern0=re.compile(r'\w\d\d\d\s[-]\s\w\d\d\d')
#        re_newline = re.compile(r'\n')
        if re.match(pattern0, line):
            #re.match() will give you the word and words after that word in each line
            #re.search() will give you the entire line
            #when you search use '|' to add more parameters            
            #print(line)
            pass
        if "Credit" in line or "Debit" in line :
            print(line)

maingrp()

#print the grouping matches
def Indgrp():
    with open(textfile, 'r', encoding='utf-8') as f:
        lines=f.readlines()
#    for line in lines:
#        #pattern=re.compile(r'\w\d\d\d\s\s\s\s')
#        pattern=re.compile(r'^\b[A-Z]{1}\d{3}[a-zA-Z]?\b')
#        if re.match(pattern, line):
        m=re.search(r'^\b[A-Z]{1}\d{3}[a-zA-Z]?\b', lines)
        m.groups()
#           print(line.split()[2])
       
Indgrp()

#individual Group's text using df
def grphdrTxt():
    #pat=re.compile(r'\w\d\d\d\s\s\s\s')
    with open(textfile, 'r', encoding='utf-8') as f:
        lines=f.readlines()
        for element in lines:
            match=re.match(r'\w\d\d\d\s\s\s\s', element)            
            if match:           
                print(match.group())
                print(element)
            else:
                pass
grphdrTxt()

def textsearch():
    file=open(textfile).read().splitlines()
    for index, line in enumerate(file):
        if "Budgetary Entry" in line:
            print(file[index+1: index+4])
        elif "Proprietary Entry" in line: 
            print("P: ", file[index+1:index+4])
        else:
            print("none")
textsearch()

###data frame
df=pd.read_csv(textfile, error_bad_lines=False)
df.columns=['text']
#df['text'].str.len() #number of characters
#df['text'].str.contains(r'\w\d\d\d\s\s\s')
df['text']=df['text'].str.strip()
#df1=df['text'].str.lstrip().str.rstrip() #removing white spaces from the left and right
#df1=df1.apply(lambda x:pd.Series(x))
#df1.columns=['text']

#Group 0
df['grp']=df['text'].str.split("    ").str.get(0).str.strip()
#Group Description
df['grp_descr']=df['text'].str.split("    ").str.get(1).str.strip()
#df['grp_descr'].fillna('', inplace=True)
#Budgetary or Proprietary
df.loc[df['grp'].str.contains('Budgetary'), 'BP']='Budgetary Entry'
df.loc[df['grp'].str.contains('Proprietary'), 'BP']='Proprietary Entry'
#df['BP'].fillna('', inplace=True)
#Debit and Credit 
df.loc[df['grp'].str.contains('Debit'), 'C/D']='Debit'
df.loc[df['grp'].str.contains('Credit'), 'C/D']='Credit'
df['C/D'].fillna('', inplace=True)
#Credit Indicator No
df['cred_no']=df['text'].str.split("Debit").str.get(0).str.strip().str.split("          ").str.get(1).str.strip()
df['cred_no'].fillna('', inplace=True)
#Debit Indicator No
df['deb_no']=df['text'].str.split("Credit").str.get(0).str.strip().str.split("          ").str.get(1).str.strip()
df['deb_no'].fillna('', inplace=True)
#Debit and Credit Nos
df['AcctNo'] = df[['cred_no', 'deb_no']].astype(str).sum(axis=1).str.strip()


#main group name extraction
#index = df[df["grp"].str.contains(r"^\w\d+\s")].index.values # find the value with regex pattern
#grp_Series = df.loc[index]["grp"] # use the index to find the value of the cell in the "grp" column

df1=df[['grp_descr', 'BP', 'C/D','AcctNo']].copy()
df1[df1.BP.notnull()]



#re.search(r'^\b[A-Z]{1}\d{3}[a-zA-Z]?\b', lines)
