# pip install yfinance
# pip install pytrends
# python3 -m pip install googlesearch-python

import numpy as np
import pandas as pd
import os
import re

import yfinance as yf
from googlesearch import search
import datetime
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def endDate(startDate, weeks, days):
    endDate = start + datetime.timedelta(weeks=weeks, days=days)
    return startDate.strftime('%Y-%m-%d'), endDate.strftime('%Y-%m-%d')

# Return the ticker of a company by using google search api
def tickerOfCompany(companyName):
    result = search("Yahoo Finance " + companyName)
    result = result[0].lower()
    return result.split('/')[-2]

def stockHistory(companyName, startDate, endDate):
    ticker = tickerOfCompany(companyName)
    company = yf.Ticker(ticker)
    
    df = company.history(start=startDate, end=endDate)
    
    return df

def stockPrices(companyName, startDate, endDate):
    ticker = tickerOfCompany(companyName)
    company = yf.Ticker(ticker)
    
    df = company.history(start=startDate, end=endDate)
    
    start = df['Close'].iloc[0]
    end = df['Close'].iloc[-1]
    
    return start, end