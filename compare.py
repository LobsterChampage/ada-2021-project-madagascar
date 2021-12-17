import pandas as pd
from financials import ticker_of_company
from popularity import trending_history
import datetime 
import yfinance as yf
import statsmodels.formula.api as smf

#Data is our data frame with all the companies with first column 1 or 0 if Elon Musk talks about it.
# after,Name of the company and the other four covariates 

#Call this function for all our functions and a set of company that will represent the controled one.

def compare(working_quote, companies, shares, hist): 
    # Returns a df with the following columns:
    output = pd.DataFrame(columns = ['company',
                                'date',
                                'close',
                                'volume',
                                'money_volume',
                                'marketcap',
                                'popularity',
                                'Elon',
                                'compare',
                                'sentiment',
                                'numOccurrences'])
    date = working_quote['date']
    
    df_trend = trending_history(companies, date)
    pop_list = df_trend.values.tolist()[0]
    
    #if a quote is before the stock was listed
    if hist[0].index[0].date() > datetime.date.fromisoformat(date):
        return output
    
    for i in range(len(companies)):
        if hist[i].index[0].date() <= datetime.date.fromisoformat(date):
            #in case of error
            market_data = pd.concat((pd.DataFrame([0], columns=['Close']),(pd.DataFrame([0], columns=['Volume']))),axis=1)
            
            for j in range(len(hist[i])):
                if hist[i].iloc[j].name.date() > datetime.date.fromisoformat(date):
                    market_data = hist[i].iloc[j]
                    break

            close = market_data['Close']
            volume = market_data['Volume']
            money_volume = close * volume
            marketcap = close * (shares[i] or 0)
            
            if i == 0:
                Elon = 1
                compare = None
                sentiment = working_quote['sentiment']
                numOccurrences = working_quote['numOccurrences']
            else:
                Elon = 0
                compare = companies[0]
                sentiment = 0
                numOccurrences = 0
            
            row = [companies[i],
                date,
                close,
                volume,
                money_volume,
                marketcap,
                pop_list[i],
                Elon,
                compare,
                sentiment,
                numOccurrences]
            output.loc[len(output)] = row
    
    return output

def create_data(companies_list, data, counting=False):
    c_list = companies_list
    company = c_list[0]
    company_quotes = data[data['ORG'] == company]
    company_quotes = company_quotes.sort_values('date', axis = 0)
    company_quotes = company_quotes[['ORG', 'date', 'sentiment', 'numOccurrences']]
    grouped = company_quotes.groupby('date').agg({'sentiment': 'mean', 'numOccurrences': 'sum'})
    dates = pd.DataFrame(grouped.index)
    grouped.index = [*range(len(grouped))]
    comp = pd.DataFrame(['Apple'], columns=['company'])
    comp = pd.concat([comp]*len(grouped))
    comp.index = [*range(len(comp))]
    working_quotes = pd.concat((comp,dates,grouped[['sentiment', 'numOccurrences']]),axis=1)
    #contains (company(always same), dates, sentiment(aggregated), 'numOccurences(aggregated)')
    
    first_date = working_quotes.iloc[0]['date']
    
    ticker = [ticker_of_company(c_list[0]),
             ticker_of_company(c_list[1]),
             ticker_of_company(c_list[2]),
             ticker_of_company(c_list[3]),
             ticker_of_company(c_list[4])]
    
    shares = [yf.Ticker(ticker[0]).info['sharesOutstanding'],
            yf.Ticker(ticker[1]).info['sharesOutstanding'],
            yf.Ticker(ticker[2]).info['sharesOutstanding'],
            yf.Ticker(ticker[3]).info['sharesOutstanding'],
            yf.Ticker(ticker[4]).info['sharesOutstanding']]
    
    hist = [yf.Ticker(ticker[0]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[1]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[2]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[3]).history(start=first_date)[['Close', 'Volume']],
           yf.Ticker(ticker[4]).history(start=first_date)[['Close', 'Volume']]]
    
    output = pd.DataFrame(columns = ['company',
                                    'date',
                                    'close',
                                    'volume',
                                    'money_volume',
                                    'marketcap',
                                    'popularity',
                                    'Elon',
                                    'compare',
                                    'sentiment',
                                    'numOccurrences'])
    
    for i in range (len(working_quotes)):
        if counting:
            print('{}/{}'.format((i+1),len(working_quotes)))
        company = compare(working_quotes.iloc[i], companies_list, shares, hist)
        output = pd.concat([output, company], axis=0)
    return output

def get_features(data, timing=False):
    """data should be org_dataset with sentiment scores and iso date format yyyy-mm-dd"""

    #Apple
    data_Apple = create_data(['Apple','Microsoft','IBM','Samsung','Lenovo'], data, counting=timing)
    #Twitter 
    data_Twitter = create_data(['Twitter','Google','Facebook','Snapchat','Pinterest'], data, counting=timing)
    #Ford
    data_Ford = create_data(['Ford','Toyota','BMW','General Motors','Stellantis'], data, counting=timing)
    #PayPal
    data_Paypal = create_data(['PayPal','Western Union','EuroNet','MoneyGram','Visa'], data, counting=timing)
    #Tesla
    data_Tesla = create_data(['Tesla','Daimler','Lucid','VolksWagen','General Motors'], data, counting=timing)
    frame = [data_Apple, data_Twitter, data_Ford, data_Paypal, data_Tesla]
    data = pd.concat(frame)
    return data

def add_propensityscore (data):#so that if we want to change only the first line don't have to do it
    #Normalise the features 
    data['close']= (data['close']-data['close'].mean())/data['close'].std()
    data['volume']= (data['volume']-data['volume'].mean())/data['volume'].std()
    data['money_volume']= (data['money_volume']-data['money_volume'].mean())/data['money_volume'].std()
    data['marketcap']= (data['marketcap']-data['marketcap'].mean())/data['marketcap'].std()
    data['popularity']= (data['popularity']-data['popularity'].mean())/data['popularity'].std()
    #Create the model
    mod = smf.logit(formula='Elon ~ money_volume + marketcap + popularity', data=data)
    res = mod.fit()
    print(res.summary())
    data['propensity_score'] = res.predict()