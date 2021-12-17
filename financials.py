import yfinance as yf
from googlesearch import search
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
import dateutil.parser as dparser
import datetime
from pytrends.request import TrendReq


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
    result = result.split('/')
    #for special cases...
    if result[-2] == 'finance.yahoo.com':
        return result[-1].split('=')[-1]
    return result[-2]


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




def get_time_from_df (df):
    cols = df['quoteID']
    n_rows = cols.shape[0] 
    date_col = []
    for ii in range(0,n_rows):
        current_date_string = cols.iloc[ii]
        segmented_date = current_date_string.split('-',3)
        reassemble_date = segmented_date[0] + '-' + segmented_date[1] + '-' + segmented_date[2]
        formated_date = dparser.parse(reassemble_date,fuzzy=True,yearfirst =True)
        current_date = formated_date.strftime('%Y-%m-%d') 
        date_col.append(current_date)
    return date_col




def percentage_change_part1(company_name, start_date, end_date,cond_end_date,add_to_end=2,subtract_to_start=2):
    """
    Returns the percentage change for a given day compared to the first day
    """
    if (cond_end_date == 0):
        df = stock_history(company_name, start_date, end_date)
        x1 = df.iloc[0,0]
        x2 = df.iloc[-1,0]
        perc_change = round(( (x2-x1)/(x1) ) * 100 ,2)
    elif (cond_end_date == 1):
        
        current_date = start_date
        current_date_temp = datetime.datetime.strptime(current_date, '%Y-%m-%d')
        new_end_date = current_date_temp + datetime.timedelta(days=add_to_end)
        new_end_date  = new_end_date.date()                                               
        new_start_date =  current_date_temp - datetime.timedelta(days=subtract_to_start)
        new_start_date = new_start_date.date()
        df = stock_history(company_name, new_start_date, new_end_date)
        x1 = df.iloc[0,0]
        x2 = df.iloc[-1,0]
        perc_change = round(( (x2-x1)/(x1) ) * 100 ,2)
        
    return perc_change

def get_perc_change_array(df):
    dates_me = get_time_from_df(df)
    n_points = df.shape[0]
    all_perc = []
    for ii in range(0,n_points):
        company_name = df['ORG'].iloc[ii]
        start_date = dates_me[ii]
        end_date = dates_me[ii]
        current_perc = percentage_change_part1(company_name, start_date, end_date,1,2,2)
        all_perc.append(current_perc)
    return all_perc


def googleTrends_perc_change(company_name, quote_date):
    """
    This functions calculate the stock popularity change for a given company between a given date
    """
    pytrends = TrendReq(hl='en-US', tz=360) 
    kw_list = []
    kw_list.append(company_name)
    quote_date_temp = datetime.datetime.strptime(quote_date, '%Y-%m-%d')
    end_date = quote_date_temp + datetime.timedelta(days=2)
    end_date  = end_date.date()                                               
    start_date =  quote_date_temp - datetime.timedelta(days=2)
    start_date = start_date.date()
    start_date = str(start_date)
    end_date = str(end_date)
    pytrends.build_payload(kw_list, cat=0, timeframe=start_date + ' ' + end_date) 
    data = pytrends.interest_over_time() 
    data = data.reset_index() 
    x1 = data.iloc[0,1]
    x2 = data.iloc[-1,1]
    perc_change = round(( (x2-x1)/(x1) ) * 100 ,2)
    return perc_change


def google_perc_change_array(df):
    """
    This functions calculate the stock popularity change for a given company between multiple given dates
    """
    dates_me = get_time_from_df(df)
    n_points = df.shape[0]
    all_perc = []
    for ii in range(0,n_points):
        company_name = df['ORG'].iloc[ii]
        quote_date = dates_me[ii]
        current_perc = googleTrends_perc_change(company_name, quote_date)
        all_perc.append(current_perc)
    return all_perc