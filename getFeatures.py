import pandas as pd
from financials import *
from popularity import trending_history
from compare import *
import time
import warnings
from pandas.core.common import SettingWithCopyWarning
warnings.simplefilter(action="ignore", category= SettingWithCopyWarning)
def create_data(companies_list,elon_org_df):
    Company = companies_list
    company_quotes = Company [-1]
    quotes = elon_org_df[elon_org_df['ORG'] == company_quotes]
    quotes = quotes.sort_values('date', axis = 0)
    quotes = quotes['date']
    q = []
    for i in range(len(quotes)):
        q.append(quotes.iloc[i][0:10])
    quotes = pd.Series(q).unique()
    first_date = quotes[0]
    ticker =[ticker_of_company(Company[0]),
             ticker_of_company(Company[1]),
             ticker_of_company(Company[2]),
             ticker_of_company(Company[3]),
             ticker_of_company(Company[4])]
    shares=[yf.Ticker(ticker[0]).info['sharesOutstanding'],
            yf.Ticker(ticker[1]).info['sharesOutstanding'],
            yf.Ticker(ticker[2]).info['sharesOutstanding'],
            yf.Ticker(ticker[3]).info['sharesOutstanding'],
            yf.Ticker(ticker[4]).info['sharesOutstanding']]
    hist =[yf.Ticker(ticker[0]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[1]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[2]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[3]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[4]).history(start=first_date)[['Close', 'Volume']]]
    data = pd.DataFrame(columns = ['Name','Date','Close','Volume','MarketCap','Popularity','Elon','compare'])
    for i in range (len(quotes)):
        date = quotes [i] 
        company = compare(company_quotes, date, Company, ticker, shares, hist)
        frame = [data, company]
        data = pd.concat(frame)
    data['Money Volume'] = data['Volume']*data['Close']
    return data
def getFeatures(elon_org_df):
    #Apple: 
    data_Apple = create_data(['Microsoft','IBM','Samsung','Dell','Apple'],elon_org_df )
    #Twitter 
    data_Twitter = create_data(['Google','Facebook','Snapchat','Pinterest','Twitter'],elon_org_df)
    #Ford
    data_Ford = create_data(['Toyota','BMW','General Motors','Stellantis','Ford'],elon_org_df)
    #PayPal : 
    data_PayPal = create_data(['Western Union','EuroNet','MoneyGram','Payoneer','PayPal'],elon_org_df)
    frame = [data_Apple,data_Twitter,data_Ford,data_PayPal]
    data = pd.concat(frame)
    return data
                             
def getFeaturesTesla(elon_org_df):
    quotes = elon_org_df[elon_org_df['ORG']== 'Tesla']
    quotes = quotes.sort_values('date', axis = 0)
    quotes = quotes['date']
    q = []
    for i in range(len(quotes)):
        q.append(quotes.iloc[i][0:10])
    quotes = pd.Series(q).unique()
    Company = ['Rivian','Lucid','VolksWagen','General Motors','Tesla']
    first_date = quotes[0]
    ticker =[ticker_of_company(Company[0]),
             ticker_of_company(Company[1]),
             ticker_of_company(Company[2]),
             ticker_of_company(Company[3]),
             ticker_of_company(Company[4])] 
    shares=[yf.Ticker(ticker[0]).info['sharesOutstanding'],
            yf.Ticker(ticker[1]).info['sharesOutstanding'],
            yf.Ticker(ticker[2]).info['sharesOutstanding'],
            yf.Ticker(ticker[3]).info['sharesOutstanding'],
            yf.Ticker(ticker[4]).info['sharesOutstanding']]
    hist =[yf.Ticker(ticker[0]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[1]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[2]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[3]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[4]).history(start=first_date)[['Close', 'Volume']]]
    data = pd.DataFrame(columns = ['Name','Date','Close','Volume','MarketCap','Popularity','Elon','compare'])
    for i in range (100):
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (100,200): 
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (200,300):
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (300,400):
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (400,500):
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (500,600):
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (600,700):
            date = quotes [i] 
            company = compare('Tesla', date, Company, ticker, shares, hist)
            frame = [data, company]
            data = pd.concat(frame)
    for i in range (700, len(quotes)):
            date = quotes[i]
            company = compare('Tesla', date,Company, ticker, shares, hist)
            frame = [data,company]
            data = pd.concat(frame)
    data['Money Volume'] = data['Volume']*data['Close']
    return data

                             