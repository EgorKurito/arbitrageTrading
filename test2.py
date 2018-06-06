# Beta: 1.0.0
import logging
import json
import time
import ssl

try:
    import thread
except ImportError:
    import _thread as thread

import websocket

log = logging.getLogger(__name__)

class Connect():
    """Dock String"""
    def __init__(self, url=None, timeout=None, sslopt=None, log_level=None):

        self.socket = None
        self.url = 'wss://api.bitfinex.com/ws/2'
        self.sslopt = sslopt if sslopt else {"cert_reqs": ssl.CERT_NONE}

        self.log = logging.getLogger(self.__module__)
        if log_level == logging.DEBUG:
            websocket.enableTrace(True)
        self.log.setLevel(level=log_level if log_level else logging.INFO)

    def connect(self):
        """
        Websocket connection
        :return:
        """
        self.log.debug("_connect(): Initializing connection >>>")
        self.socket = websocket.WebSocketApp(
            self.url,
            on_open=self._on_open,
            on_message=self._on_message,
            on_error=self._on_error,
            on_close=self._on_close
        )

        self.log.debug("_connect(): Starting connection >>>")
        self.socket.run_forever(sslopt=self.sslopt)

    def run(self):
        """
        Main method
        :return:
        """
        self.log.debug("run(): Starting >>>")
        self.connect()

    def _on_message(self, ws, message):
        print(message)

    def _on_error(self, ws, error):
        print(error)

    def _on_close(self, ws):
        print("close")

    def _on_open(self, ws):
        def run(*args):
            ws.send(json.dumps({
                "event": "subscribe",
                "channel": "book",
                "pair": "BTCUSD",
                "prec": "P0"
            }))
            time.sleep(1)
            ws.close()
            print("thread terminating...")

        thread.start_new_thread(run, ())

x = Connect()
x.run()
