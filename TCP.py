from socketserver import BaseRequestHandler, TCPServer
from socket import socket, AF_INET, SOCK_STREAM


class TestTCPHandler(BaseRequestHandler):

    def handle(self):
        print("handle activated", self.client_address)
        self.data = self.request.recv(1024).strip()
        print(self.data)
        self.request.send(b'privet')


if __name__ == "__main__":
    server = TCPServer(('localhost', 15555), TestTCPHandler)
    server.serve_forever()

s = socket(AF_INET, SOCK_STREAM)
s.connect(('localhost', 15555))
s.send(b'Hello')
print(s.recv(1024).strip())
