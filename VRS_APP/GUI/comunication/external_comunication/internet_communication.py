import socket
import threading
from time import sleep
from .external_comunication import ExternalCommunication
from PySide6.QtCore import Signal


class InternetCommunication(ExternalCommunication):
    def to_app_msg(self, request):
        pass

    def to_external_msg(self, request):
        pass

    def __init__(self, server_ip, server_port, handler=None):

        super().__init__(handler)
        self.HEADER = 16
        self.PORT = server_port
        self.FORMAT = 'utf-8'
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.SERVER = server_ip
        self.connected = False
        self.last_received_msg = None
        self.client = None
        self.handler = handler

    def run(self):
        self.connect()
        self.receive()

    def connect(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.connect((self.SERVER, self.PORT))
        self.connected = True
        sleep(0.2)

    def disconnect(self):
        self.send(self.DISCONNECT_MESSAGE)
        self.connected = False
        self.client.close()
        self.client = None
        print(f"[DISCONNECTED] {self.SERVER} disconnected.")

    def send(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        if self.client is not None:
            self.client.send(send_length)
            self.client.send(message)

    def receive(self):
        while True:
            if self.connected and self.client is not None:
                try:
                    msg_length = self.client.recv(self.HEADER).decode(self.FORMAT)
                    if msg_length:
                        msg_length = int(msg_length)
                        msg = self.client.recv(msg_length).decode(self.FORMAT)
                        self.last_received_msg = msg
                        self.handler(msg)
                except OSError:
                    pass

    def set_handler(self, handler):
        self.handler = handler
