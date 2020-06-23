#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 11:02:35 2019

@author: lucianovboas
"""
#First: Calling Libraries:
import pandas as pd
from selenium import webdriver


#Second: Using Chromedriver to download the dataset straight into a csv file.
chromedriver = '/Users/lucianovboas/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/'
driver = webdriver.Chrome('/Users/lucianovboas/anaconda3/lib/python3.7/site-packages/selenium/webdriver/chrome/chromedriver')
driver.implicitly_wait(30)
driver.get('https://quickstats.nass.usda.gov/data/spreadsheet/C32C16BF-F56C-3A73-B05D-E144ACBEF726.csv')
    
