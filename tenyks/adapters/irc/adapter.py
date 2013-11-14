import os
import socket
import ssl

from tenyks.adapters.base import BaseAdapter


def get_certs_bundle():
    return os.path.join(os.path.dirname(__file__), 'cacert.pem')


class IrcAdapter(BaseAdapter):

    def __init__(self, name, **config):
        self.name = name
        self.config = config
        super(IrcAdapter, self).__init__()

    def connect(self):
        pass

    def run(self):
        while True:
            pass

    @property
    def using_ssl(self):
        return ('ssl' in self.config and self.config['ssl'])

    def get_socket(self):
        if self.using_ssl:
            if 'ssl_version' in self.config and self.config['ssl_version']:
                if self.config['ssl_version'] == 2:
                    ssl_version = ssl.PROTOCOL_SSLv2
                elif self.config['ssl_version'] == 3:
                    ssl_version = ssl.PROTOCOL_SSLv3
                else:
                    ssl_version = ssl.PROTOCOL_SSLv23
            else:
                # SSLv23 is the default for python ssl and gevent ssl
                ssl_version = ssl.PROTOCOL_SSLv23
            return ssl.wrap_socket(
                socket.socket(),
                cert_reqs=ssl.CERT_REQUIRED,
                ca_certs=get_certs_bundle(),
                ssl_version=ssl_version)
        else:
            return socket.socket()
