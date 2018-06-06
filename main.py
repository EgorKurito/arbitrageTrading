# Beta: 1.0.0
import logging
import json
import time
import ssl

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
            self.url
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
