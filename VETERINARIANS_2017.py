#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 17 20:35:52 2019

@author: lucianovboas
"""

#First: Call Libraries:
import io
import pandas as pd
import requests as r
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Second: Accessing url, defining path and printing data on console:
url = 'https://www.dshs.texas.gov/chs/hprc/tables/2017/VET17.aspx'
path = 'desktop/veterinarians_2017.csv'
dfs = pd.read_html('https://www.dshs.texas.gov/chs/hprc/tables/2017/VET17.aspx')
for df in dfs:
    print(df)

#Third: Checking the quality of the data:
df.head(20)
df.describe
df.columns
df.count()
df.dtypes

#Forth: Enumerating the "-" values in the two columns we have it:
df['Ratio of 2017 Population to Veterinarian'].value_counts()
   #I found 34 "-" 
df['Rank'].value_counts()
   #I found 35 "-"

#Fith: Replacing the "-" for zeros:
df['Ratio of 2017 Population to Veterinarian'] = df['Ratio of 2017 Population to Veterinarian'].replace("-", "0")
df['Rank'] = df['Rank'].replace("-", "0")


#Sixth: Exporting to CSV:
df.to_csv('desktop/veterinarians_2017.csv', index=False, encoding='utf8')




