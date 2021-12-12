import yfinance as yf
from googlesearch import search
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
plt.style.use('seaborn')

def get_dates(start_date, weeks, days):
    """
    This functions takes in the start date as a string from Quotebank and returns the start and end dates formatted for 
    yFinance. 
    
    INPUTS: 
    start_date: date extracted from Quotebank as a string (in our case the date is extracted from the data file we created).
    weeks: The number of weeks to add to the start date to obtain the end date.
    days: The number of days to add to the start date to obtain the end date. 
    end_date = startdate + weeks + days 
    
    OUTPUT: 
    start_date: returns start date formatted for yFinance. 
    end_date: returns end date formatted for yFinance. 
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


def stock_info_date(company_name, date):
    """
    Returns close price, volume, and marketcap
    """
    ticker = ticker_of_company(company_name)
    company = yf.Ticker(ticker)
    
    df = company.history(start=date)[['Close', 'Volume']]
    numberOfShares = company.info['sharesOutstanding']
    df['MarketCap'] = numberOfShares*df['Close']
    
    return df.iloc[1]



#Should rewrite this to use stock_info_date
def stock_history(company_name, start_date, end_date, plot=False):
    """
    Returns yFinance dataframe of stock info for the company between given dates
    Returns close price, volume, and marketcap
    """
    ticker = ticker_of_company(company_name)
    company = yf.Ticker(ticker)
    
    df = company.history(start=start_date, end=end_date)[['Close', 'Volume']]
    numberOfShares = company.info['sharesOutstanding']
    
    df['MarketCap'] = numberOfShares*df['Close']

    if plot:
        a = df[['Close']]
        a.plot.line(title=f'{company_name} {start_date} - {end_date}')
        plt.show()
    
    return df


# The functions below are used to analyze the change in stock prices over a given time period

def dailyChange(company_name, start_date, end_date):
    """
    Returns the change in the stock price compared to the previous day
    In other word the function returns the daily change of a stock price
    """
    df = stock_history(company_name, start_date, end_date)
    result = [0]
    for i in range(len(df)-1):
        changeFromPreviousDay = (df.iloc[i+1])/df.iloc[i]
        result.append(float(changeFromPreviousDay))
    return result
    
# We use the word index as a term for the collection/list of stocks

def dailyChangeIndex(companies, start_date, end_date):
    """
    Returns a datafram for dailyChange for multiple companies
    """
    df = pd.DataFrame()
    for i in range(0, len(companies)):
        df[companies[i]] = dailyChange(companies[i], start_date, end_date)
    return df

def indexStockPrice(companies, start_date, end_date):
    """
    Returns all stock prices for the companies in the index 
    """
    df = pd.DataFrame()  
    for i in range(0, len(companies)):
        df[companies[i]] = stock_history(ticker_of_company(companies[i]), start_date, end_date)
    return df

def changeInPriceFromStart(company_name, start_date, end_date):
    """
    Returns the percentage change for a given day compared to the first day
    """
    df = stock_history(company_name, start_date, end_date)
    result = [1]
    for i in range(len(df)-1):
        changeFromStart = (df.iloc[i+1])/df.iloc[0]
        result.append(float(changeFromStart))
    return result



def changeIndex(companies, start_date, end_date):
    """
    As dailyChangeIndex but for changeInPriceFromStart instead
    """
    df = pd.DataFrame()
    for i in range(0, len(companies)):
        df[companies[i]] = changeInPriceFromStart(companies[i], start_date, end_date)
    return df

def createIndex(companies, start_date, end_date):
    """
    Returns the proper (as in financial markets, but a simplification) index of a list of companies
    Each stock is valued the same, that is they affect the index equally
    """

    
    df = changeIndex(companies, start_date, end_date)
    df['Index'] = df.iloc[:].mean(axis=1)
    
    return df['Index']*100