import pandas as pd
from financials import stock_info_date
from popularity import trending_history

def compareCompanies(companies, date):
    # Returns a df with the following columns: ['Date', 'Close', 'Volume', 'MarketCap', 'Popularity']
    df = pd.DataFrame(companies, columns=['Name'])
    df['Date'] = date
    
    marketData = []
    for company in companies:
        marketData.append(stock_info_date(company, date).values.tolist())
    
    df['Close'] = [i[0] for i in marketData]
    df['Volume'] = [i[1] for i in marketData]
    df['MarketCap'] = [i[2] for i in marketData]
    
    
    df_trend = trending_history(companies, date)
    df_trend_list = df_trend.values.tolist()[0]
    df['Popularity'] = df_trend_list
    
    return df