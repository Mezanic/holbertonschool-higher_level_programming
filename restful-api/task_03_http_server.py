#!/usr/bin/python3
"""Module For create a simple HTTP server"""


import http.server
import json

PORT = 8000


class RequestHandler(http.server.BaseHTTPRequestHandler):
    """Class for handle request in http"""

    def do_GET(self):
        """ Define for handle get request"""

        match self.path:

            case '/':
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Hello, this is a simple API!")

            case "/data":
                data = {"name": "John", "age": 30, "city": "New York"}
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(data).encode())

            case "/info":
                info = {
                    "version": "1.0",
                    "description": "A simple API built with http.server"
                }
                self.send_response(200)
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(info).encode())

            case "/status":
                self.send_response(200)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"OK")

            case _:
                self.send_response(404)
                self.send_header("Content-Type", "text/plain")
                self.end_headers()
                self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    with http.server.HTTPServer(("", PORT), RequestHandler) as httpd:
        print(f"Serving on port {PORT}...")
        httpd.serve_forever()
