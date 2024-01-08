from abc import ABC, abstractmethod


class ExternalCommunication(ABC):
    def __init__(self,
                 handler=None):
        self.handler = handler

    @abstractmethod
    def send(self, request):
        ...

    @abstractmethod
    def receive(self, request):
        ...

    @abstractmethod
    def set_handler(self, handler):
        ...

    @abstractmethod
    def to_app_msg(self, request):
        ...

    @abstractmethod
    def to_external_msg(self, request):
        ...