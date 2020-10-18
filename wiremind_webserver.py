from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        path = self.path
        if "firstname" not in path or "lastname" not in path:
            message = "Greetings stranger !\n"
        else:
            firstname = path.split("&")[0].split("=")[1]
            lastname = path.split("&")[1].split("=")[1]
            message = "Greetings " + firstname + " " + lastname + "!\n"
        self.send_response(200)
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))


httpd = HTTPServer(('0.0.0.0', 8001), SimpleHTTPRequestHandler)
httpd.serve_forever()
