from .handler import Handler
from ..confirmation_box import ConfirmationBoxButton
from ...comunication import AppMessage
import os
from playsound import playsound


class NewGameHandler(Handler):


    def __init__(self,
                 settings,
                 timer=None,
                 task_table=None):
        self.settings = settings["message_codes"]
        self.music_folder = settings["music_folder"]
        self.timer = timer
        self.task_table = task_table
        self.current_dir = os.getcwd()
        super().__init__()

    def handle_button(self, request):
        if request.objectName() == "new_game_button":
            if ConfirmationBoxButton().question(request):
                self.task_table.reset_tasks()
                self.timer.reset()
                self.timer.start()
                # try:
                #     file = os.path.join(self.current_dir, self.music_folder, f"new_game",
                #                         f"sound.mp3")
                #
                #     playsound(file, False)
                # except:
                #     file = os.path.join(self.current_dir, self.music_folder, f"new_game",
                #                         f"sound.wav")
                #
                #     playsound(file, False)
                #
                return AppMessage(task_code=None,
                                  message_code=self.settings["new_game"],
                                  value=None)

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        pass

    def reset_task(self):
        self.task_table.reset_task()

    def handle_message(self, request):
        self.task_table.reset_tasks()
        self.timer.reset()
        self.timer.start()