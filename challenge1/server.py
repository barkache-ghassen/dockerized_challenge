from http.server import BaseHTTPRequestHandler, HTTPServer

class OnlyContractHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Always return contract.html no matter what the user requests
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        with open("contract.html", "rb") as file:
            self.wfile.write(file.read())

# Run server on port 8000
HTTPServer(("", 8000), OnlyContractHandler).serve_forever()
