from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello Wiremind!\n')


httpd = HTTPServer(('0.0.0.0', 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()