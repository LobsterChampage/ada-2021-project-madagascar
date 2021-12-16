import pandas as pd
from financials import stock_info_date
from popularity import trending_history
import datetime 

def compareCompanies(companies, tickers, date, shares, hist):
    # Returns a df with the following columns: ['Date', 'Close', 'Volume', 'MarketCap', 'Popularity']
    df = pd.DataFrame(companies, columns=['Name'])
    df['Date'] = date
    
    marketData = []

    for i in range(len(tickers)):
        marketData.append(obs_info(tickers[i], date, shares[i], hist[i]).values.tolist())
    
    df['Close'] = [i[0] for i in marketData]
    df['Volume'] = [i[1] for i in marketData]
    df['MarketCap'] = [i[2] for i in marketData]
    
    df_trend = trending_history(companies, date)
    df_trend_list = df_trend.values.tolist()[0]
    df['Popularity'] = df_trend_list
    
    return df

def obs_info(ticker, date, sharesOutstanding, comp_hist):
    for i in range(len(comp_hist)):
        if comp_hist.iloc[i].name.date() > datetime.date.fromisoformat(date):
            df = comp_hist.iloc[i]
            break
    df['MarketCap'] = int (sharesOutstanding or 0)*df['Close']
    
    return df
def compare(company_quote, date, companies, tickers, shares, hist): 

    company = compareCompanies(companies, tickers, date, shares, hist)

    company ['Elon']= 0
    company ['compare'] = company_quote
    company.at[4,'Elon'] = 1
    company.at[4,'compare'] = 'None'
    return company
    