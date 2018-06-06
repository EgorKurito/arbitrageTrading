import websocket
from websocket import create_connection

import ssl
import json
import time
import logging


# Setting
url = "wss://api.bitfinex.com/ws/2"
sslopt = {"cert_reqs": ssl.CERT_NONE}

ws = create_connection(url, sslopt=sslopt)
ws.send(json.dumps({
    "event": "subscribe",
    "channel": "ticker",
    "symbol": "tBTCUSD"
}))

while True:
    result = ws.recv()
    result = json.loads(result)
    print ("Received '%s'" % result)

ws.close()
