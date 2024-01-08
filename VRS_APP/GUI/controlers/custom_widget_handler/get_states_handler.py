from .handler import Handler
from ...comunication import AppMessage
from ..confirmation_box import ConfirmationBoxButton


class GetStatesHandler(Handler):
    def __init__(self, settings=None):
        self.settings = settings["message_codes"]

    def handle_button(self, request):
        if ConfirmationBoxButton().question(request):
            return AppMessage(task_code=None,
                              message_code=self.settings["get_states"],
                              value=None)

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        pass

    def handle_message(self, request):
        pass
