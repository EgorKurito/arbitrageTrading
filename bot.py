import requests
import logging
import time
import sys

from btfxwss import BtfxWss

# Make a 'list' of all pairs of crypto currency from the 'str' object
tickets = requests.get('https://api.bitfinex.com/v1/symbols').text.upper().replace('"','')[1:-1].split(',')

# Setting the BtfxWss Library
log = logging.getLogger(__name__)

fh = logging.FileHandler('test.log')
fh.setLevel(logging.DEBUG)
sh = logging.StreamHandler(sys.stdout)
sh.setLevel(logging.DEBUG)

log.addHandler(sh)
log.addHandler(fh)
logging.basicConfig(level=logging.DEBUG, handlers=[fh, sh])

wss = BtfxWss()
wss.start()

while not wss.conn.connected.is_set():
    time.sleep(1)

for ticket in tickets:
    wss.subscribe_to_ticker(ticket)

    t = time.time()
    while time.time() - t < 0.5:
        pass

    try:
        ticker = wss.tickers(ticket).get()
    except KeyError:
        continue
    # t_A - Ticker_Ask; t_B - Ticker_Bid
    t_A = ticker[0][0][6]
    t_B = ticker[0][0][0]

    dif = ((t_A-t_B)/(t_A+t_B)/2)*100
    print(dif)