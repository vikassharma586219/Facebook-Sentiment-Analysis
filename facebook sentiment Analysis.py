# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 12:33:33 2020

@author: Admin
"""

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
nltk.downloader.download('vader_lexicon')
file=r"C:\Users\Admin\Desktop\fb analysis.xlsx"
xl=pd.ExcelFile(file)#Read from Excel
dfs=xl.parse(xl.sheet_names[0])#parsing excel sheet to data frame
dfs=list(dfs['your posts'])#remove blank spaces
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="21:06"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])