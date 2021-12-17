#!pip install CurrencyConverter
from datetime import date
from currency_converter import CurrencyConverter
import pandas as pd
import yfinance as yf
from financials import *

#Had to do this manually. Took to much time when using yfinance
def curForCompany(name):
    if name in ['BMW', 'Daimler', 'Volkswagen']:
        return 'EUR'
    elif name == 'Samsung':
        return 'KRW'
    elif name == 'Lenovo':
        return 'HKD'
    return 'USD'

def correctDateFormat(dateTxt):
    a = dateTxt.split('-')
    yyyy = int(a[0])
    mm = int(a[1])
    dd = int(a[2])
    return date(yyyy, mm, dd)

def convertCurrency(amount, from_currency, to_currency, date=False):
    c = CurrencyConverter(fallback_on_missing_rate=True)
    if not date:
        return c.convert(amount, from_currency, to_currency)
    return c.convert(amount, from_currency, to_currency, correctDateFormat(date))

#Datafram has to be in a given format in order for this function to work
#index, company, date, close, volume, money_volume, marketcap, popularity, Elon, compare, sentiment, numOccurrences
def convertToUSD_special_df(data = pd.read_csv('Data/FinalFeatures2.csv.bz2')):
    df = data
    for index, row in df.iterrows():
        currency = curForCompany(row['company'])#yf.Ticker(ticker_of_company(row['company'])).info['currency']
        date = row['date']
        
        df.at[index,'close'] = convertCurrency(row['close'], currency, 'USD', date)
        df.at[index,'money_volume'] = convertCurrency(row['money_volume'], currency, 'USD', date)
        df.at[index,'marketcap'] = convertCurrency(row['marketcap'], currency, 'USD', date)
        
    return df
        