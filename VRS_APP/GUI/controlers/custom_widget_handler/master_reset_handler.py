from .handler import Handler
from json_settings import Settings
from ...comunication import AppMessage
from ..confirmation_box import ConfirmationBoxButton


class MasterResetHandler(Handler):


    def __init__(self,
                 master_reset=None,
                 task_table=None):
        self.settings = Settings().items["message_codes"]
        self.master_reset = master_reset
        self.task_table = task_table

    def handle_button(self, request):
        if ConfirmationBoxButton().question(request):
            self.task_table.reset_tasks()
            return AppMessage(task_code=None,
                              message_code=self.settings["master_reset"],
                              value=None)

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        pass

    def handle_message(self, request):
        self.task_table.reset_tasks()