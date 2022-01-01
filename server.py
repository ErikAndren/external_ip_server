from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import os

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes("%s" % self.client_address[0], "utf-8"))

if __name__ == "__main__":
    hostName = os.environ.get('HOST_NAME', '')
    serverPort = int(os.environ.get('SERVER_PORT', 8081))

    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("External ip echo server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")
