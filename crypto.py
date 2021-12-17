#from crypto import *

from request import Request, Session
import json
import pprint

#First one is for current price
#url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/historical'

#The API key
headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'91127bb4-8767-4df6-8aa9-eae87fc765b8'
}


# Important: Need these numbers in order to access data
# Bitcoin is 1
# Dogecoin is 74
# Ethereum is 1027

def numberFromName(name):
    if name == 'bitcon':
        return 1
    elif name == 'dogecoin':
        return 74
    elif name == 'ethereum':
        return 1027
    else:
        return 0
    

def cryptoData(name, start, end):
    number = numberFromName(name.lower())
    
    parameters = {
        'id':number,
        'interval':'24h',
        #'time_start':start,
        #'time_end':end,
        'convert':'USD'
    }

    session = Session()
    session.headers.update(headers)

    response = session.get(url, params = parameters)
    #pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
    pprint.pprint(json.loads(response.text))    
