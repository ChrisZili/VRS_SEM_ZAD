from .handler import Handler
from ..confirmation_box import ConfirmationBoxButton
from json_settings import Settings
from ...comunication import AppMessage
import os
from playsound import playsound


class TaskWindowHandler(Handler):

    def __init__(self,
                 settings,
                 task_table=None):
        super().__init__()
        self.settings = settings["message_codes"]
        self.music_folder = settings["music_folder"]
        self.current_dir = os.getcwd()
        self.task_table = task_table

    def handle_button(self, request):
        if request.objectName() != "indication_button" and ConfirmationBoxButton().question(request):

            if request.objectName() == "reset_button":
                return request.parent().reset_task(message_code=self.settings["reset"])

            elif request.objectName() == "finish_button":
                # print(os.path.join(self.current_dir, self.music_folder, request.parent().objectName(),
                #                    f"{request.parent().objectName()}.mp3"))
                task_code = request.parent().task["task_code"]
                # try:
                #     print("Playing mp3")
                #     file = os.path.join(self.current_dir, self.music_folder, request.parent().objectName(),
                #                         f"sound1.mp3")
                #     playsound(file, False)
                # except OSError:
                #     print("Playing wav")
                #     file = os.path.join(self.current_dir, self.music_folder, request.parent().objectName(),
                #                         f"sound1.wav")
                #     playsound(file, False)

                return request.parent().finish_task(message_code=self.settings["finish"])

            elif request.objectName() == "activation_button":

                return request.parent().activate_action(message_code=self.settings["activation"])
            elif request.objectName() == "commentator_button":
                return AppMessage(task_code=request.parent().task["task_code"],
                                  message_code=self.settings["commentator_sound"],
                                  value=None)

            else:

                return AppMessage(task_code=None,
                                  message_code=None,
                                  value=None)

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        pass

    def handle_message(self, request):
        # print(request.message_code)
        if request.message_code == self.settings["reset"]:
            self.task_table.get_task(request.task_code).reset_task(message_code=request.message_code)
        elif request.message_code == self.settings["finish"]:
            self.task_table.get_task(request.task_code).finish_task(message_code=request.message_code)
        elif request.message_code == self.settings["activation"]:
            self.task_table.get_task(request.task_code).activate_action(message_code=request.message_code)

