from .handler import Handler
from ...comunication import AppMessage
from ..confirmation_box import ConfirmationBoxButton


class JumpScareHandler(Handler):

    def __init__(self, settings=None):
        super().__init__()
        self.settings = settings

    def handle_button(self, request):
        if "demons" in request.parent().objectName():
            message_code,task_code = self.get_buttons(from_widget="demons", button_name=request.objectName())

        elif "screams" in request.parent().objectName():
            message_code,task_code = self.get_buttons(from_widget="screams", button_name=request.objectName())

        elif "hallway" in request.parent().objectName():
            message_code,task_code = self.get_buttons(from_widget="hallway", button_name=request.objectName())

        elif "kitchen" in request.parent().objectName():
            message_code,task_code = self.get_buttons(from_widget="kitchen", button_name=request.objectName())

        elif "bedroom" in request.parent().objectName():
            message_code,task_code = self.get_buttons(from_widget="bedroom", button_name=request.objectName())

        if message_code is not None and task_code is not None and ConfirmationBoxButton().question(request):
            return AppMessage(task_code=task_code,
                              message_code=message_code,
                              value=None)
        else :
            return None

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        pass

    def handle_message(self, request):
        pass

    def get_buttons(self, from_widget, button_name):
        for button in self.settings["jump_scares"][f"{from_widget}"]["buttons"]:
            if button["name"] == button_name:
                return button["message_code"],button["task_code"]
