#!/usr/bin/python3

# Mostly copied from https://picamera.readthedocs.io/en/release-1.13/recipes2.html
# Run this script, then point a web browser at http:<this-ip-address>:8000
# Note: needs simplejpeg to be installed (pip3 install simplejpeg).

import io
import logging
import socketserver
import socket 
from http import server
from threading import Condition
import threading
from time import sleep

from picamera2 import Picamera2
from picamera2.encoders import JpegEncoder
from picamera2.outputs import FileOutput

PAGE = """\
<html>
<head>
<title>picamera2 MJPEG streaming demo</title>
</head>
<body>
<h1>Picamera2 MJPEG Streaming Demo</h1>
<img src="stream.mjpg" width="640" height="480" />
</body>
</html>
"""

from time import sleep

import serial.tools.list_ports






class SerialCommunication():
    def __init__(self, handler=None, bitrate=115200):
        super().__init__()
        self.bitrate = bitrate
        # /dev/ttyACM0 /dev/serial0/dev/serial0
        self.serial_port = "/dev/serial0"
        self.serial = None
        self.set_serial_com()
        self.handler = handler
        sleep(0.5)

    def send(self, request):

        data_to_send = f"{request}\n\r"
        print(f"SerialCommunication send : {data_to_send.encode()}")
        print(f"SerialCommunication send data length : {len(data_to_send.encode())}")
        while True:
            try:
                
                # if self.serial.in_waiting <= 0:
                self.serial.flush()
                self.serial.write(data_to_send.encode())
                break
                # else:
                #     print(f"SerialCommunication send : {self.serial.in_waiting}")
            except Exception as e:
                print(f"{e} from send")
                sleep(0.5)
                continue

    def receive(self):
        message = ""
        print("[INFO] SerialCommunication receive thread started")
        while True:

            try:
                if self.serial.in_waiting > 0:
                    incoming_byte = self.serial.readline()
                    incoming_byte = incoming_byte.decode('utf-8').rstrip()
                    sleep(0.1)
                    print(f"SerialCommunication receive : {incoming_byte}")
                    self.handler(incoming_byte)
                    

            except Exception as e:
                sleep(0.5)
                continue

    def set_handler(self, handler):
        self.handler = handler

    def to_app_msg(self, request):
        # data = request.split(',')
        # return AppMessage(message_code=int(data[0]),
        #                   task_code=int(data[1]),
        #                   value=int(data[2]))
        return request

    def to_external_msg(self, request):
        value = request.value if request.value is not None else 0
        message_code = request.message_code if request.message_code is not None else 0
        task_code = request.task_code if request.task_code is not None else 0
        data = f"{message_code},{task_code},{value}"
        data_to_send = f"${request}#"
        return data_to_send.encode('utf-8')

    def find_serial_port(self):
        while True:
            available_ports = serial.tools.list_ports.comports()
            print(available_ports)
            sleep(10)
            if not available_ports:
                print("No serial ports found")
            else:
                for port in available_ports:
                    if "serial" in port.device or "COM" in port.device:
                        print(f"SerialCommunication find_serial_port : {port.device}")
                        return port.device

    def set_serial_com(self):
        # self.serial_port = self.find_serial_port()
        self.serial = serial.Serial(self.serial_port, self.bitrate, timeout=1)
        self.serial = serial.Serial(self.serial_port, baudrate=self.bitrate, bytesize=8, parity='N', stopbits=1, timeout=None, xonxoff=False, rtscts=True)
        self.serial.close()
        self.serial.open()
        self.serial.flush()
        print(f"SerialCommunication set_serial_com : {self.serial_port}")
        sleep(0.5)


class Server:
    def __init__(self,message_handler=None):
        self.HEADER = 16
        self.FORMAT = 'utf-8'
        self.PORT = 5050
        self.SERVER = "25.59.215.144"
        self.ADDR = (self.SERVER, self.PORT)
        self.DISCONNECT_MESSAGE = "!DISCONNECT"
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind(self.ADDR)
        self.message_handler = message_handler
    
    def handle_client(self, conn, addr):
        print(f"[NEW CONNECTION] {addr} connected.")
        connected = True
        while connected:
            try:
                msg_length = conn.recv(self.HEADER).decode(self.FORMAT)
            except Exception as e:
                print(f"{e} from handle_client")
                continue
            try:  
                if msg_length is not None:
                    msg_length = int(msg_length)
                
                    msg = conn.recv(msg_length).decode(self.FORMAT)
                    print(f"[{addr}] {msg}")
                    if msg == self.DISCONNECT_MESSAGE:
                        connected = False
                    print(f"[{addr}] {msg}")
                    self.message_handler(msg)
            except Exception as e:
                print(f"{e} from handle_client")
                continue
            
        conn.close()

    def start(self):
        self.server.listen()
        print(f"[LISTENING] Server is listening on {self.SERVER}")
        while True:
            self.conn, self.addr = self.server.accept()

            thread = threading.Thread(target=self.handle_client, args=(self.conn, self.addr))
            thread.start()
            print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")

    def send_to_client(self, msg):
        message = msg.encode(self.FORMAT)
        msg_length = len(message)
        send_length = str(msg_length).encode(self.FORMAT)
        send_length += b' ' * (self.HEADER - len(send_length))
        self.conn.send(send_length)
        self.conn.send(msg.encode(self.FORMAT))

class StreamingOutput(io.BufferedIOBase):
    def __init__(self):
        self.frame = None
        self.condition = Condition()

    def write(self, buf):
        with self.condition:
            self.frame = buf
            self.condition.notify_all()


class StreamingHandler(server.BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(301)
            self.send_header('Location', '/index.html')
            self.end_headers()
        elif self.path == '/index.html':
            content = PAGE.encode('utf-8')
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.send_header('Content-Length', len(content))
            self.end_headers()
            self.wfile.write(content)
        elif self.path == '/stream.mjpg':
            self.send_response(200)
            self.send_header('Age', 0)
            self.send_header('Cache-Control', 'no-cache, private')
            self.send_header('Pragma', 'no-cache')
            self.send_header('Content-Type', 'multipart/x-mixed-replace; boundary=FRAME')
            self.end_headers()
            try:
                while True:
                    with output.condition:
                        output.condition.wait()
                        frame = output.frame
                    self.wfile.write(b'--FRAME\r\n')
                    self.send_header('Content-Type', 'image/jpeg')
                    self.send_header('Content-Length', len(frame))
                    self.end_headers()
                    self.wfile.write(frame)
                    self.wfile.write(b'\r\n')
            except Exception as e:
                logging.warning(
                    'Removed streaming client %s: %s',
                    self.client_address, str(e))
        else:
            self.send_error(404)
            self.end_headers()


class StreamingServer(socketserver.ThreadingMixIn, server.HTTPServer):
    allow_reuse_address = True
    daemon_threads = True

def video_stream_thread():
    try:
        address = ('', 8000)
        server = StreamingServer(address, StreamingHandler)
        server.serve_forever()
    finally:
        picam2.stop_recording()


picam2 = Picamera2()
picam2.configure(picam2.create_video_configuration(main={"size": (640, 480)}))
output = StreamingOutput()
picam2.start_recording(JpegEncoder(), FileOutput(output))



def internet_handler(request):
    print(f"SerialCommunication internet_handler : {request}")
    # if len(request) == 10:
    serial_com.send(request)

class mainloop():
    def __init__(self):
        self.video_thread = threading.Thread(target=video_stream_thread)
        self.video_thread.deamon = True
        self.video_thread.start()

        self.server = Server(self.internet_handler)
        self.server_thread = threading.Thread(target=self.server.start)
        self.server_thread.deamon = True
        self.server_thread.start()

        self.serial_com = SerialCommunication(handler=self.serial_handler)
        self.serial_recieve_thread = threading.Thread(target=self.serial_com.receive)
        self.serial_recieve_thread.deamon = True
        self.serial_recieve_thread.start()
    
    def serial_handler(self, request):
        print(f"SerialCommunication serial_handler : {request}")
        self.server.send_to_client(request)
    
    def internet_handler(self, request):
        print(f"SerialCommunication internet_handler : {request}")
        # if len(request) == 10:
        self.serial_com.send(request)

main = mainloop()

while True:
    sleep(30)
    print("main thread") 


# video_thread = threading.Thread(target = video_stream_thread)
# video_thread.deamon = True
# video_thread.start()
