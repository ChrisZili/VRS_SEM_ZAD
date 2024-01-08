from GUI.comunication.messeges.communication_signals import CommunicationSignals
from .external_comunication import ExternalCommunication
from .abccommunication import ABCCommunication
from GUI.comunication.messeges.app_message import AppMessage


class Communication(ABCCommunication):
    def __init__(self,
                 external_communication: ExternalCommunication = None,
                 ):
        super().__init__()
        self.signals = CommunicationSignals()
        self.external_communication = external_communication
        self.external_communication.set_handler(self.receive_from_external)

    def send_to_external(self, request):
        # self.external_communication.send(request.to_can_msg())
        # print("Communication sent signal")
        self.external_communication.send(request)

    def receive_from_external(self, request):
        # message = self.external_communication.to_app_msg(request)
        self.send_to_app(request)

    def send_to_app(self, request):
        self.signals.send.emit(request)

    def receive_from_app(self, request: AppMessage):
        self.send_to_external(request)

    # def __init__(self):
    #     super().__init__()
    #     self.signals = CommunicationSignals()
    #
    # def run(self):
    #     while True:
    #         print("Communication sent signal")
    #         self.signals.receive.emit("Communication sent signal")
    #         time.sleep(15)
    #
    # def recieve(self, data):
    #     print(f"Communication recieved data{data}")
