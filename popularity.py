from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

#Returns panda dataframe with how kw_list has been trending over a timeframe
def trending_history(kw_list, start_date, end_date=False, plot=False):
    if not end_date:
        end_date = start_date
        
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat=0, timeframe=f'{start_date} {end_date}', geo='', gprop='')
    df = pytrends.interest_over_time()
    del df['isPartial']
    
    if plot:
        df.plot.line(title=f'{kw_list} {start_date} - {end_date}')
        plt.show()
    
    return df

def mostTrending(kw_list, start_date, end_date=False):
    if not end_date:
        end_date = start_date
    
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat=0, timeframe=f'{start_date} {end_date}', geo='', gprop='')
    df = pytrends.interest_over_time()
    del df['isPartial']
    
        
    #dividing list into sequences of five 
