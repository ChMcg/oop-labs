import socket, time, json
# from typing import List, Tuple
from typing import *

class UnknownData(Exception):
    pass

class ConnectionManager():
    def __init__(self, HOST: str = None, PORT: int = None):
        self.sock = socket.socket()
        self.clients : List[socket.socket] = []
        if not HOST is None and not PORT is None: 
            self.HOST = HOST
            self.PORT = PORT
            # self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.sock.bind((HOST, PORT))
            self.sock.listen(1)

    def recv(self) -> str:
        data = self.sock.recv(1024)
        return data.decode()

    def recvfrom(self, num: int) -> str:
        data : bytes = self.clients[num].recv(1024)
        return data.decode()
    
    def send_to_clients(self, data: str):
        assert len(data.encode()) < 1024
        for socket in self.clients:
            socket.send(data.encode())
            # self.sock.sendto(data.encode(), addr)
    # def send_to(self, data: str, addr: Tuple[str, int]):
    #     assert len(data.encode()) < 1024
    #     # self.sock.sendto(data.encode(), addr)

    def send(self, data: str):
        assert len(data.encode()) < 1024
        self.sock.send(data.encode())

    def connect(self, HOST, PORT):
        self.sock.connect((HOST, PORT))
        # data = {
        #     'type': 'reg'
        # }
        # data = json.dumps(data, ensure_ascii=False).encode()
        # self.sock.sendto(data, (HOST, PORT))
        # pass

    def wait_connect(self):
        conn, addr = self.sock.accept()
        self.clients.append(conn)
        # data, addr = self.sock.recvfrom(1024)
        # data : Dict = json.loads(data.decode())
        # if 'type' not in data.keys():
        #     raise UnknownData(json.dumps(data, ensure_ascii=False, indent=2))
        # if data['type'] == 'reg':
        #     self.clients.append(addr)
        #     print('new client:', addr)
        