import requests
import json
import ssl
import time
import logging

from websocket import create_connection

from threading import Thread

# Settings
# Url API
url = 'wss://api.bitfinex.com/ws/2'
# Logging
logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',
                    )
# Tickets
tickets = ['EOSBTC', 'EOSETH', 'ETHBTC']
# Pair
pair_1 = {'pair': None, 'Ask_Price': None, 'Bid_Price': None}
pair_2 = {'pair': None, 'Ask_Price': None, 'Bid_Price': None}
pair_3 = {'pair': None, 'Ask_Price': None, 'Bid_Price': None}
all_pair = [pair_1, pair_2, pair_3]

# Main
class BTXBot(Thread):
    def __init__(self, ticket):
        Thread.__init__(self)
        self.ticket = ticket


    def run(self):
        ws = create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE})
        time.sleep(3)
        ticker = dict(event="subscribe", channel="ticker", symbol="t{}".format(self.ticket))
        ws.send(json.dumps(ticker))

        while True:

            result = json.loads(ws.recv())
            if (len(result) == 2) and (str(result)[-4:-2] != 'hb'):
                # t_A - Ticker_Ask; t_B - Ticker_Bid
                t_A = result[1][0]
                t_B = result[1][2]
                dif = ((t_A - t_B) / (t_A + t_B) / 2) * 100

                t_ticket = [self.ticket, t_A, t_B, dif]

                if t_ticket[0] == tickets[0]:
                    all_pair[0]['pair'] = tickets[0]
                    all_pair[0]['Ask_Price'] = t_ticket[1]
                    all_pair[0]['Bid_Price'] = t_ticket[2]
                elif t_ticket[0] == tickets[1]:
                    all_pair[1]['pair'] = tickets[1]
                    all_pair[1]['Ask_Price'] = t_ticket[1]
                    all_pair[1]['Bid_Price'] = t_ticket[2]
                else:
                    all_pair[2]['pair'] = tickets[2]
                    all_pair[2]['Ask_Price'] = t_ticket[1]
                    all_pair[2]['Bid_Price'] = t_ticket[2]
                print(all_pair)





def main(tickets):
    for ticket in tickets:
        thread = BTXBot(ticket)
        thread.start()

if __name__ == "__main__":
    main(tickets)


