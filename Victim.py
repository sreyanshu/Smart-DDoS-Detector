from http.server import HTTPServer, BaseHTTPRequestHandler
from datetime import datetime
import logging

LOG_FILE = 'requests.log'

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        ip = self.client_address[0]
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        log_entry = f"{ip},{now}\n"

        with open(LOG_FILE, 'a') as f:
            f.write(log_entry)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'OK')

def run_server():
    server = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
    print("Victim Server running on port 8080...")
    server.serve_forever()

run_server()
