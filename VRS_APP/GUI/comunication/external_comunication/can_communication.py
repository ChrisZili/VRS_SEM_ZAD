from .external_comunication import ExternalCommunication
import can
from ..messeges import AppMessage
from can import Message


class CanCommunication(ExternalCommunication):
    def __init__(self,
                 channel=None,
                 bus_type=None,
                 bitrate=None,
                 handler=None):
        super().__init__()
        self.channel = channel
        self.bus_type = bus_type
        self.bitrate = bitrate
        self.can = can.interface.Bus(channel=self.channel, interface=self.bus_type, bitrate=self.bitrate)
        self.notifier = None

    def send(self, request: AppMessage):

        self.can.send(self.to_external_msg(request))
        print(f"CanCommunication send : {request}")

    def receive(self, request):

        message = self.to_app_msg(request)
        print(f"CanCommunication receive : {message}")
        return message

    def to_external_msg(self, request):

        value = request.value if request.value is not None else 0
        message_code = request.message_code if request.message_code is not None else 0
        task_code = request.task_code if request.task_code is not None else 0
        return Message(arbitration_id=message_code, data=[task_code, value])

    def to_app_msg(self, request):
        return AppMessage(message_code=request.arbitration_id,
                          task_code=request.data[0],
                          value=request.data[1])

    def set_handler(self, handler):
        self.notifier = can.Notifier(self.can, [handler])
