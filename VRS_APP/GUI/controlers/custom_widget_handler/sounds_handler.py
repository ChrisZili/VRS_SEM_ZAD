from .handler import Handler
from ..confirmation_box import ConfrimationBoxSlider, ConfrimationBoxToggle
from ...comunication import AppMessage
from json_settings import Settings
import os
from playsound import playsound






class SoundsHandler(Handler):

    def __init__(self,
                 settings,
                 sounds=None,
                 master_sound_task=False):
        super().__init__()
        self.sounds = sounds
        self.setting = settings["message_codes"]
        self.current_dir = os.getcwd()
        self.music_folder = settings["music_folder"]
        self.master_sound_task = master_sound_task


    def handle_button(self, request):
        pass

    def handle_toggle(self, request):
        text = f"zvuk pre {request.parent().parent().text}"
        if ConfrimationBoxToggle().question(request, text):
            if request.parent().objectName() == "sounds_master_switch":
                request.parent().parent().parent().master_active = request.isChecked()

            else:
                request.parent().parent().active = request.isChecked()
            return None
        else:
            if request.parent().objectName() == "sounds_master_switch":
                request.parent().parent().parent().master_active = request.isChecked()

            else:
                request.parent().parent().active = request.isChecked()

            return None

    def handle_slider(self, request):
        text = f"zvuk pre {request.parent().parent().text}"

        if request.parent().parent().parent.master_active and not request.parent().parent().parent.master_sounds.active:
            request.last_value = request.value()
            request.parent().set_text(request.value())
            if request.parent().parent().task is not None:
                return AppMessage(task_code=request.parent().parent().task["task_code"],
                                  message_code=self.setting["task_sound"]["volume"],
                                  value=request.value())


        else:
            request.clearFocus()
            request.setValue(request.last_value)

            return

    def handle_message(self, request):
        if request.message_code == self.setting["task_sound"]["volume"]:
            self.handle_volume(request)
        else:
            print(f"Sounds handler : Playing sound >> {request}")
            self.handle_play(request)

    def handle_volume(self, request):
        task = self.sounds.get_task_from_sound(request.task_code)
        task.volume_slider.set_value(request.value)
        task.volume_slider.slider.clearFocus()

    def handle_play(self, request):
        try:
            file = os.path.join(self.current_dir, self.music_folder, f"task{request.task_code}",
                                f"sound{request.value}.mp3")

            playsound(file, False)
        except:
            file = os.path.join(self.current_dir, self.music_folder, f"task{request.task_code}",
                                f"sound{request.value}.wav")

            playsound(file, False)
