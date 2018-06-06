import logging
import time
import sys

from btfxwss import BtfxWss


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

# Subscribe to some channels
wss.subscribe_to_ticker('YYWETH')
wss.subscribe_to_ticker('EOSETH')
wss.subscribe_to_ticker('EOSUSD')

t = time.time()
while time.time() - t < 0.5:
    pass

ticker_1 = wss.tickers('YYWETH')
ticker_2 = wss.tickers('EOSETH')
ticker_3 = wss.tickers('EOSUSD')
'''
while True:
    ticker_11 = ticker_1.get()
    ticker_1_Ask = ticker_11[0][0][6]
    ticker_1_Bid = ticker_11[0][0][0]

    ticker_22 = ticker_2.get()
    ticker_2_Ask = ticker_22[0][0][6]
    ticker_2_Bid = ticker_22[0][0][0]

    ticker_33 = ticker_3.get()
    ticker_3_Ask = ticker_33[0][0][6]
    ticker_3_Bid = ticker_33[0][0][0]

    x = 216.01542311
    xxx = x * ticker_1_Ask / ticker_2_Ask * ticker_3_Bid
    print(xxx)

    time.sleep(7)
'''



# noinspection PyUnreachableCode
class Bitfinex:
    """
    Algorithm of trade
    """
    def __init__(self, ticket1=None, ticket2=None, ticket3=None, ):
        self.ticket1 = ticket1
        self.ticket2 = ticket2
        self.ticket3 = ticket3



x


