import yfinance as yf
from googlesearch import search
import datetime as dt
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def get_dates(start_date, weeks, days):
    """
    Takes in the start date as a string on the format from Quotebank and returns the start end end dates formatted for yFinance
    """
    start_date = dt.datetime.strptime(start_date, '%Y-%m-%d %H:%M:%S')
    end_date = start_date + dt.timedelta(weeks=weeks, days=days)
    return start_date.strftime('%Y-%m-%d'), end_date.strftime('%Y-%m-%d')

def ticker_of_company(company_name):
    """
    Return the ticker of a company by using google search api
    """
    result = search("Yahoo Finance " + company_name)
    result = result[0].lower()
    return result.split('/')[-2]

def stock_history(company_name, start_date, end_date, plot=False):
    """
    Returns yFinance dataframe of stock info for the company between given dates
    """
    ticker = ticker_of_company(company_name)
    company = yf.Ticker(ticker)
    
    df = company.history(start=start_date, end=end_date)[['Close']]

    if plot:
        a = df[['Close']]
        a.plot.line(title=f'{company_name} {start_date} - {end_date}')
        plt.show()
    
    return df