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
    time.sleep(5)

# Subscribe to some channels
wss.subscribe_to_ticker('OMGUSD')


t = time.time()
while time.time() - t < 5:
    pass

ticker_1 = wss.tickers('OMGUSD')


while True:
    ticker_11 = ticker_1.get()
    ticker_1_Ask = ticker_11[0][0][6]
    ticker_1_Bid = ticker_11[0][0][0]






