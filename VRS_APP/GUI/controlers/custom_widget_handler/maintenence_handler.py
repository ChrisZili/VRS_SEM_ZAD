from .handler import Handler
from ...comunication import AppMessage
from ..confirmation_box import ConfirmationBoxButton


class MaintenenceHandler(Handler):

    def __init__(self,
                 timer=None,
                    settings=None
                 ):
        super().__init__()
        self.timer = timer
        self.settings = settings["message_codes"]


    def handle_button(self, request):
        if request.objectName() == "maintenance_button":
            if ConfirmationBoxButton().question(request):
                self.timer.stop()
                return AppMessage(task_code=None,
                                  message_code=self.settings["maintenance"],
                                  value=None)

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        pass

    def handle_message(self, request):
        self.timer.stop()
