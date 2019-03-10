"""
Heavily borrowed from https://gist.github.com/Integralist/ce5ebb37390ab0ae56c9e6e80128fdc2
"""

import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from call_weatherman import CallWeatherman

HOST_NAME = 'localhost'
PORT_NUMBER = 8080          # can't be a protected port without some hassle


class MySimpleRequestHandler(BaseHTTPRequestHandler):






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

                weatherman = CallWeatherman()
                temperature = weatherman.execute()



                response_dict = {'query_time': timestamp, 'temperature': weatherman.temperature}
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

