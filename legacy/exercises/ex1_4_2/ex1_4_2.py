import tornado.ioloop
import tornado.web

import argparse
import sys

from modules.scanner import *
from hashlib import sha1


class MainHandler(tornado.web.RequestHandler):
    def initialize(self, result):
        self.result = result

    def get(self):
        key = sha1('ex1_4_2').hexdigest()
        self.render('index.html', title='Netmap Results', result=self.result, key=key)


def make_app(result):
    return tornado.web.Application([
        (r"/", MainHandler, {'result': result}),
    ])


def main(host, ports):
    if '-' in ports:
        ps = ports.split('-')
        result = scan_ports(host, int(ps[0]), int(ps[1]))
    else:
        result = scan_port(host, ports)

    app = make_app(result)
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Port scanner')
    parser.add_argument('host', type=str, help='IP of host to scan')
    parser.add_argument('ports', type=str, help='Ports to scan, ex. 445, 20-25')
    args = parser.parse_args()
    main(args.host, args.ports)

