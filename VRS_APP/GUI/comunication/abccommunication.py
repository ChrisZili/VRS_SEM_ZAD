from abc import ABC, abstractmethod
from .external_comunication import ExternalCommunication
from GUI.comunication.messeges.abcmessage import ABCMessage


class ABCCommunication(ABC):
    def __init__(self,
                 handler=None,
                 external_communication: ExternalCommunication = None):
        self.handler = handler
        self.external_communication = external_communication

    @abstractmethod
    def send_to_external(self, request: ABCMessage):
        ...

    @abstractmethod
    def receive_from_external(self, request: ABCMessage):
        ...

    @abstractmethod
    def send_to_app(self, request: ABCMessage):
        ...

    @abstractmethod
    def receive_from_app(self, request: ABCMessage):
        ...
