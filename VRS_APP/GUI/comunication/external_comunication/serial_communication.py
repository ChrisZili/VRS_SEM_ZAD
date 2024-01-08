from time import sleep
from PySide6.QtWidgets import QMessageBox

from .external_comunication import ExternalCommunication
from ..messeges import AppMessage
import serial.tools.list_ports


class SerialCommunication(ExternalCommunication):
    def __init__(self, handler=None, bitrate=None):
        super().__init__(handler)
        self.bitrate = bitrate
        self.serial_port = self.find_serial_port()
        self.serial = None
        self.set_serial_com()
        sleep(0.5)

    def send(self, request):

        data = f"{request.message_code},{request.task_code},{request.value}"
        data_to_send = f"${data}#"
        print(f"SerialCommunication send : {data_to_send}")
        while True:
            try:
                if self.serial.in_waiting <= 0:
                    self.serial.flush()
                    self.serial.write(self.to_external_msg(request))
                    break
            except Exception as e:
                print(f"{e} from send")
                # reply = QMessageBox(
                #     text=f"Prosím pripojte zariadenie do USB a slačte OK")
                # reply.setIcon(QMessageBox.Icon.Critical)
                # reply.setStandardButtons(QMessageBox.Ok)
                #
                # reply.setStyleSheet(f"background-color:#1b1e23;")
                # res = reply.exec_()
                self.set_serial_com()
                sleep(0.5)
                continue

        # self.serial.flush()
        # self.serial.reset_input_buffer()

    def receive(self, request=None):
        message = ""
        while True:
            try:
                if self.serial.in_waiting > 0:
                    incoming_byte = self.serial.readline().decode('utf-8').strip()
                    # incoming_byte = incoming_byte.strip()
                    if incoming_byte[0] == '$' and incoming_byte[-1] == '#':
                        print(f"SerialCommunication receive : {incoming_byte[1:-1]}")
                        self.handler(incoming_byte[1:-1])


            except Exception as e:
                print(f"{e} from recieve")
                # reply = QMessageBox(
                #     text=f"Prosím pripojte zariadenie do USB a slačte OK")
                # reply.setIcon(QMessageBox.Icon.Error)
                # reply.setStandardButtons(QMessageBox.Critical)
                #
                # reply.setStyleSheet(f"background-color:#1b1e23;")
                # res = reply.exec_()


                self.set_serial_com()
                sleep(0.5)
                continue

    def set_handler(self, handler):
        self.handler = handler

    def to_app_msg(self, request):
        data = request.split(',')
        return AppMessage(message_code=int(data[0]),
                          task_code=int(data[1]),
                          value=int(data[2]))

    def to_external_msg(self, request):
        value = request.value if request.value is not None else 0
        message_code = request.message_code if request.message_code is not None else 0
        task_code = request.task_code if request.task_code is not None else 0
        data = f"{message_code},{task_code},{value}"
        data_to_send = f"${data}#"
        return data_to_send.encode('utf-8')

    def find_serial_port(self):
        while True:
            available_ports = serial.tools.list_ports.comports()
            if not available_ports:
                print("No serial ports found")
            else:
                # print("Available serial ports:")
                for port in available_ports:
                    if "usbserial" in port.device or "COM" in port.device:
                        return port.device

    def set_serial_com(self):
        self.serial_port = self.find_serial_port()
        self.serial = serial.Serial(self.serial_port, self.bitrate)
        self.serial.close()
        self.serial.open()
        self.serial.flush()
        print(f"SerialCommunication set_serial_com : {self.serial_port}")
        sleep(0.5)
