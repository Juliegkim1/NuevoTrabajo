# -*- coding: utf-8 -*-
"""
Created on Fri Sep 28 18:49:58 2018

@author: JK
"""

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
from itertools import permutations 
# extract text
rootdir = "C:\\Users\\fy776ew\\Documents\\Github\\glextracter\\"

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
            pass
        if "Letter of credit" in line: 
            pass
            
        if "Budgetary Entry" in line or "Proprietary Entry" in line :
            BudProp= line.split()
            print(BudProp)
            #'BP': BudProp[0:1], 

        if  "Credit" in line or "Debit" in line :
            parts = line.split()
#            descrip = " ".join(parts[2:])
            df=pd.DataFrame(parts[:2])
            print(df)
#            writer = pd.ExcelWriter('output.xlsx')
#            df.to_excel(writer,'Sheet1')
#            writer.save()         

#            d={'BP': BudProp[:1], 'CandD': parts[:1], 'GL': parts[:2], 'Des': " ".join(parts[2:])}
#            df=pd.DataFrame(d)
#            df=df.append(df)
#            print(df)
#            writer = pd.ExcelWriter('output.xlsx')
#            tabledata.to_excel(writer,'Sheet1')
#            writer.save()
            #print(tabledata)
            #print(tabledata['CandD'].head(10))
        else: 
                pass          
    
maingrp()

#Get rid of let of credit