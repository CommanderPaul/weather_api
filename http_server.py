"""
Heavily borrowed from https://gist.github.com/Integralist/ce5ebb37390ab0ae56c9e6e80128fdc2
"""

import time
import json
from http.server import BaseHTTPRequestHandler, HTTPServer
from call_weatherman import CallWeatherman
from sqlite_dao import SqLiteDao

HOST_NAME = 'localhost'
PORT_NUMBER = 8080


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
        self.send_header('Content-type', 'application/json')
        self.end_headers()

        json_response = ""
        if status_code == 200:
            if path == "/temperature":
                timestamp = time.time()
                db = SqLiteDao()
                check = db.check_for_expiry(timestamp)
                db.close_connection()

                if check:
                    print("Use record, it isn't that old")
                    query_time, temperature = check
                else:
                    query_time, temperature = self.call_the_weatherman(timestamp)

                response_dict = {'query_time': query_time, 'temperature': temperature}
                json_response = json.dumps(response_dict)

        return bytes(json_response, 'UTF-8')

    def respond(self, opts):
        response = self.handle_http(opts['status'], self.path)
        self.wfile.write(response)

    @staticmethod
    def call_the_weatherman(timestamp):
        print("Call the weatherman")

        weatherman = CallWeatherman()
        weatherman.execute()

        db = SqLiteDao()
        db.insert_temperature(timestamp, weatherman.temperature)
        db.close_connection()

        return timestamp, weatherman.temperature


if __name__ == '__main__':

    httpd = HTTPServer((HOST_NAME, PORT_NUMBER), MySimpleRequestHandler)

    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
