from abc import ABC, abstractmethod


class Handler(ABC):

    @abstractmethod
    def handle_button(self, request):
        ...

    @abstractmethod
    def handle_toggle(self, request):
        ...

    @abstractmethod
    def handle_slider(self, request):
        ...

    @abstractmethod
    def handle_message(self, request):
        ...

