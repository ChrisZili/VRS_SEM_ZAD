from .handler import Handler
from ..confirmation_box import ConfrimationBoxSlider, ConfrimationBoxToggle
from json_settings import Settings
from ...comunication import AppMessage


class LightsHandler(Handler):

    def __init__(self,
                 settings,
                 lights_master_switch=None,
                 lights=None):
        super().__init__()
        self.lights_master_switch = lights_master_switch
        self.lights = lights
        self.settings = settings["message_codes"]

    def handle_button(self, request):
        pass

    def handle_toggle(self, request):
        text = request.parent().parent().text

        if ConfrimationBoxToggle().question(request, text):
            # print(request)
            request.parent().parent().active = request.isChecked()

        else:
            request.parent().parent().active = request.isChecked()

        return None

    def handle_slider(self, request):
        text = request.parent().parent().text
        # if ConfrimationBoxSlider().question(request, text):
        if self.lights_master_switch.checkbox.checkbox.isChecked():
            request.last_value = request.value()
            request.parent().set_text(request.value())

            return AppMessage(task_code=0,
                              message_code=self.settings["light"]["volume"],
                              value=request.value())

        else:
            request.clearFocus()
            request.setValue(request.last_value)

            return

    def handle_message(self, request):
        self.lights.volume_slider.set_value(request.value)
        self.lights.volume_slider.slider.clearFocus()
