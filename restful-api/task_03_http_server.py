#!/usr/bin/python3

"""Module to create my first simple web server """


import http.server
import socketserver
import json

PORT = 8000


class RequestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        """Class to define the Get method"""

        match self.path:

            case "/":
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Hello, this is a simple API!")

            case "/data":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                data = {
                    "name": "John",
                    "age": 30,
                    "city": "New York"
                }
                self.wfile.write(json.dumps(data).encode())

            case "/info":
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                version = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
                self.wfile.write(json.dumps(version).encode())

            case "/status":
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"OK")

            case _:
                self.send_response(404)
                self.send_header("Content-type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Endpoint not found")


with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("serving at port", PORT)
    httpd.serve_forever()
