import requests
url = 'https://api.bitfinex.com/v1/symbols'
tickers = requests.get(url).text.upper()