import requests
import json
import ssl
import time

from websocket import create_connection

# Settings
url = 'wss://api.bitfinex.com/ws/2'

# Make a 'list' of all pairs of crypto currency from the 'str' object
tickets = requests.get('https://api.bitfinex.com/v1/symbols').text.upper().replace('"','')[1:-1].split(',')
# Connection
ws = create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE} )

for ticket in tickets:

    ticker = dict(event="subscribe", channel="ticker", symbol="t{}".format(ticket))
    ws.send(json.dumps(ticker))

    while True:
        result = json.loads(ws.recv())
        if len(result) == 2:
            # t_A - Ticker_Ask; t_B - Ticker_Bid
            t_A = result[1][0]
            t_B = result[1][2]
            dif = ((t_A - t_B) / (t_A + t_B) / 2) * 100
            if dif > -0.01:
                print(ticket)
                print(dif)
            break

