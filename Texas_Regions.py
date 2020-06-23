#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 17:46:32 2019

@author: lucianovboas
"""

#First: Calling Libraries:
import io
import pandas as pd
import requests as r
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

#Second: Acessising url, defining path and priting (it has to run all these following lines together):
url = 'https://www.dfps.state.tx.us/contact_us/counties.asp?r=all'
path = 'desktop/texas_regions.csv'
dfs = pd.read_html('https://www.dfps.state.tx.us/contact_us/counties.asp?r=all')
for df in dfs:
    print(df)

#Third: Checking the Data:
df.head(62)
df.describe
df.columns
df.count()
df.dtypes

#Forth: Changing "DeWitt" to "De Witt":
df.loc[61, "County"] = "De Witt"
df.loc[61]


#Fifth: Exporting to CSV:
df.to_csv('desktop/texas_regions.csv', index=False, encoding='utf8')

