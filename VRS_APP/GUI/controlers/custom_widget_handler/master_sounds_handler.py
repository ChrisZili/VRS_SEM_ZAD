from time import sleep

from .handler import Handler
from ...comunication import AppMessage
from subprocess import call

class MasterSoundsHandler(Handler):
    def __init__(self,
                 settings=None,
                 master_sound_task=None,
                 sounds=None):
        super().__init__()
        self.settings = settings["message_codes"]
        self.master_sound_task = master_sound_task
        self.sounds = sounds
        self.volume = call(["amixer", "-D", "pulse", "sset", "Master", "0%"])


    def handle_button(self, request):
        pass

    def handle_toggle(self, request):
        pass

    def handle_slider(self, request):
        if request.parent().parent().parent.master_active:

            slider = request.parent().parent().get_slider(request.parent().objectName())
            slider.set_value(request.value())
            slider.set_text(request.value())


            if slider.objectName() == "case_sound":
                slider.parent().active = True
                for sound in self.sounds.tasks:
                    sound.volume_slider.set_value(request.value())
                    sound.volume_slider.set_text(request.value())
            slider.parent().active = False

            return AppMessage(task_code=None,
                              message_code=slider.message_code,
                              value=request.value())
        else:
            request.clearFocus()
            request.setValue(request.last_value)

            return

    def handle_message(self, request):
        pass
