from json_settings import Settings
from ..py_empty_card import EmptyCard
from PySide6.QtWidgets import QHBoxLayout
from PySide6.QtCore import Qt

from ..py_slider_with_name import PySliderWithName

settings = Settings()


class MasterSounds(EmptyCard):

    def __init__(self,
                 parent=None,
                 object_name="master_sounds",
                 text="Master Sounds",
                 slider_connection=None):
        super().__init__(parent=parent, object_name="master_sounds", text="")
        self.slider_connection = slider_connection
        self.sliders = {}
        self.active = False
        self.lower_layout = QHBoxLayout()
        self.main_layout.addLayout(self.lower_layout, 1, 0)
        self.setup_master_sounds()

        # self.volume_slider = PySliderWithName(
        #     parent=self,
        #     object_name=f"{object_name}_slider",
        #     text="",
        #     value=50,
        # )
        # if slider_connection is not None:
        #     self.volume_slider.slider.valueChanged.connect(slider_connection)
        #     # self.volume_slider.slider.sliderChange.connect(slider_connection)
        #
        # # WIDGETS OF LOWER LAYOUT
        # # //////////////////////////////////////////////////////////////
        # # self.lower_layout.addWidget(self.on_off_button, alignment=Qt.AlignCenter)
        # self.lower_layout.addWidget(self.volume_slider, alignment=Qt.AlignCenter)

    def setup_master_sounds(self):
        for slider in settings.items["message_codes"]["master_sounds"]:
            new_slider = PySliderWithName(
                parent=self,
                object_name=f"{slider['name']}",
                text=slider["text"],
                value=slider["value"],
                message_code=slider["volume"]
            )
            self.sliders[slider["name"]] = new_slider
            if self.slider_connection is not None:
                new_slider.slider.valueChanged.connect(self.slider_connection)
            self.lower_layout.addWidget(self.sliders[slider["name"]], alignment=Qt.AlignCenter)

    def get_slider(self, slider_name):
        for slider in self.sliders:
            if slider == slider_name:
                return self.sliders[slider]
