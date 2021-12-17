from request import Request, Session
import json
import pprint

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

parameters = {
    'slug':'bitcoin,ethereum',
    'convert':'USD'
}

#The API key
headers = {
    'Accepts':'application/json',
    'X-CMC_PRO_API_KEY':'91127bb4-8767-4df6-8aa9-eae87fc765b8'
}

session = Session()
session.headers.update(headers)

response = session.get(url, params = parameters)
pprint.pprint(json.loads(response.text)['data']['1']['quote']['USD']['price'])
