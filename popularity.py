from pytrends.request import TrendReq
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn')

#Returns panda dataframe with how kw_list has been trending over a timeframe
def trending_history(kw_list, start_date, end_date, plot=False):
    pytrends = TrendReq(hl='en-US', tz=360)
    pytrends.build_payload(kw_list, cat=0, timeframe=f'{start_date} {end_date}', geo='', gprop='')
    df = pytrends.interest_over_time()
    
    if plot:
        df.plot.line(title=f'{kw_list} {start_date} - {end_date}')
        plt.show()
    
    return df