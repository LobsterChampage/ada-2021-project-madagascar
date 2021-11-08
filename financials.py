# pip install yfinance
# pip install pytrends
# python3 -m pip install googlesearch-python

import yfinance as yf
from googlesearch import search
import datetime as dt
import matplotlib.pyplot as plt
plt.style.use('seaborn')

# Takes in the start date as a string on the format from Quotebank and returns the start end end dates formatted for yFinance
def get_dates(start_date, weeks, days):
    start_date = dt.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_date = start_date + dt.timedelta(weeks=weeks, days=days)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')

# Return the ticker of a company by using google search api
def ticker_of_company(company_name):
    result = search("Yahoo Finance " + company_name)
    result = result[0].lower()
    return result.split('/')[-2]

# Returns yFinance dataframe of stock info for the company between given dates
def stock_history(company_name, start_date, end_date, plot=False):
    ticker = ticker_of_company(company_name)
    company = yf.Ticker(ticker)
    
    df = company.history(start=start_date, end=end_date)[['Close']]

    if plot:
        a = df[['Close']]
        a.plot.line(title=f'{company_name} {start_date} - {end_date}')
        plt.show()
    
    return df