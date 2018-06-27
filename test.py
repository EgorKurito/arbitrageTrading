import requests
import json
import ssl
import time

from websocket import create_connection

from threading import Thread

# Settings
url = 'wss://api.bitfinex.com/ws/2'

# Make a 'list' of all pairs of crypto currency from the 'str' object
# tickets = requests.get('https://api.bitfinex.com/v1/symbols').text.upper().replace('"','')[1:-1].split(',')
tickets = ['EOSBTC', 'EOSETH', 'ETHBTC']
# Good tickets
good_tickets = []
# Connection
ws = create_connection(url, sslopt={"cert_reqs": ssl.CERT_NONE} )



class BTXBot(Thread):
    def __init__(self, ticket, name):
         Thread.__init__(self)
         self.ticket = ticket

    def run(self):
        ticker = dict(event="subscribe", channel="ticker", symbol="t{}".format(self.ticket))
        ws.send(json.dumps(ticker))

        while True:
            result = json.loads(ws.recv())
            if (len(result) == 2) and (str(result)[-4:-2] != 'hb'):
                print(result)

def main(tickets):
    for item, ticket in enumerate(tickets):
        name = "Поток %s" % (item+1)
        thread = BTXBot(ticket, name)
        thread.start()

if __name__ == "__main__":
    tickets = ['EOSBTC', 'EOSETH', 'ETHBTC']
    main(tickets)

'''
for ticket in tickets:

    ticker = dict(event="subscribe", channel="ticker", symbol="t{}".format(ticket))
    ws.send(json.dumps(ticker))

    while True:
        result = json.loads(ws.recv())


        #if (len(result) == 2) and (str(result)[-4:-2] != 'hb'):

        
            #t_A - Ticker_Ask; t_B - Ticker_Bid
            t_A = result[1][0]
            t_B = result[1][2]
            dif = ((t_A - t_B) / (t_A + t_B) / 2) * 100
            
            if dif > -0.01:
                #t_ticket = [ticket, t_A, t_B]
                #good_tickets.append(t_ticket)
                print(ticket)
                print(dif)
            break
        

print(good_tickets)
'''
