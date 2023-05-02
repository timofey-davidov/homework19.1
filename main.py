import json
from http.server import BaseHTTPRequestHandler, HTTPServer

hostname = "localhost"
serverPort = 8080

class MyServer(BaseHTTPRequestHandler):
    def __get_json_data(self):
        with open("list.json", "r") as json_file:
            return json.load(json_file)

    def __save_json_data(self, json_data):
        with open("list.json", "w") as json_file:
            json.dump(json_data, json_file)

    def do_POST(self):
        c_len = int(self.headers.get("Content-Length"))
        client_data = self.rfile.read(c_len)
        client_data = client_data.decode()
        #ответ от сервера к клиенту
        self.send_response(201)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes(client_data, "utf-8"))

    def do_GET(self):
        json_data = self.__get_json_data()
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(bytes("Hello, World wide web!", "utf-8"))

if __name__ == '__main__':
    webServer = HTTPServer((hostname, serverPort), MyServer)
    print("Server started at http://%s:%s" % (hostname, serverPort))
    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped")