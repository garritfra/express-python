#!/usr/bin/env python3
from http.server import HTTPServer, SimpleHTTPRequestHandler, HTTPStatus


class Handler(SimpleHTTPRequestHandler):

    def do_GET(self):
        self.send_response(HTTPStatus.OK)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'Hello, World!')
        return


def run(port, server_class=HTTPServer, handler_class=Handler):
    print("Server running at " + str(port))
    httpd = HTTPServer(("localhost", port), Handler)
    httpd.serve_forever()


run(8080)
