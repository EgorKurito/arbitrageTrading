import requests
import json
import ssl
import time

from websocket import create_connection

import threading
import logging

# Settings
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
# Url API
url = 'wss://api.bitfinex.com/ws/2'


# Make a 'list' of all pairs of crypto currency from the 'str' object
# tickets = requests.get('https://api.bitfinex.com/v1/symbols').text.upper().replace('"','')[1:-1].split(',')
tickets = ['EOSBTC', 'EOSETH', 'ETHBTC']

def subscribe(ticket):
    ws = create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
    time.sleep(3)
    ticker = dict(event="subscribe", channel="ticker", symbol="t{}".format(ticket))
    ws.send(json.dumps(ticker))

    while True:

        result = json.loads(ws.recv())
        if (len(result) == 2) and (str(result)[-4:-2] != 'hb'):
            # t_A - Ticker_Ask; t_B - Ticker_Bid
            t_A = result[1][0]
            t_B = result[1][2]
            dif = ((t_A - t_B) / (t_A + t_B) / 2) * 100

            t_ticket = [ticket, t_A, t_B, dif]

            logging.debug(t_ticket)


for ticket in tickets:
    t = threading.Thread(target=subscribe, args=(ticket, ))
    t.start()