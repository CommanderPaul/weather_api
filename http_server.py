"""
Heavily borrowed from https://gist.github.com/Integralist/ce5ebb37390ab0ae56c9e6e80128fdc2
"""

import time
from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import json

HOST_NAME = 'localhost'
PORT_NUMBER = 8080          # can't be a protected port without some hassle


class MySimpleRequestHandler(BaseHTTPRequestHandler):

    def __init__(self):

        

        pass

    # Override do_GET
    def do_GET(self):
        paths = {
            '/temperature': {'status': 200}
        }

        if self.path in paths:
            self.respond(paths[self.path])
        else:
            self.respond({'status': 404})

    def handle_http(self, status_code, path):
        self.send_response(status_code)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        json_response = ""
        if status_code == 200:

            if path == "/temperature":

                timestamp = time.time()

                response_dict = {'query_time': timestamp, 'temperature': 100}
                json_response = json.dumps(response_dict)

            # TODO add city search here

        return bytes(json_response, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)


if __name__ == '__main__':

    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MySimpleRequestHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

