from urllib.parse import urlparse, parse_qs
import argparse
import socketserver
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler
import collections
import os
import sys
import json
import ArReader

mod_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, mod_path)


"""
Very simple HTTP server in python (Updated for Python 3.7)
"""


class Server(BaseHTTPRequestHandler):

    def _set_headers(self, type):
        self.send_response(200)
        self.send_header("Content-type", type)
        self.end_headers()

    def _html(self, message):
        content = f"<html><body><h1>{message}</h1></body></html>"
        return content.encode("utf8")  # NOTE: must return a bytes object!

    def do_GET(self):

        parsed_url = urlparse(self.path)
        data_query = parse_qs(parsed_url.query)

        if "file" in data_query:
            ArReader.ArReader().instance.open(data_query['file'][0])
            resp = json.dumps(
                ArReader.ArReader().instance.getElements()).encode('utf-8')
            self._set_headers('application/json')
        else:
            resp = open('html/index.html', 'rb').read()
            self._set_headers('text/html')

        self.wfile.write(resp)

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        # Doesn't do anything with posted data
        self._set_headers()
        self.wfile.write(self._html("POST!"))


def run(server_class=HTTPServer, handler_class=Server, addr="localhost", port=8000):
    server_address = (addr, port)
    httpd = server_class(server_address, handler_class)

    print(f"Starting httpd server on {addr}:{port}")
    httpd.serve_forever()


# Entry point
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Run a simple HTTP server")
    parser.add_argument(
        "-l",
        "--listen",
        default="localhost",
        help="Specify the IP address on which the server listens",
    )
    parser.add_argument(
        "-p",
        "--port",
        type=int,
        default=8000,
        help="Specify the port on which the server listens",
    )
    args = parser.parse_args()
    run(addr=args.listen, port=args.port)
