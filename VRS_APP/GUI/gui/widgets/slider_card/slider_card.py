# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QHBoxLayout
# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////

# IMPORT STYLES
# ///////////////////////////////////////////////////////////////
# from . styles import Styles
from ..py_empty_card import EmptyCard
from ..py_checkbox import PyCheckBox
from ..py_slider_with_name import PySliderWithName


class SliderCard(EmptyCard):
    def __init__(
            self,
            parent,
            object_name,
            text,
            checkbox_name ="toggle",
            checkbox_text = "",
            slider_name="slider",
            slider_value=50,
            slider_text="",
            toggle_connection=None,
            slider_connection=None,
            task: dict = None,
            active=False):
        super().__init__(parent=parent, object_name=object_name, text=text)
        self.setParent(parent)
        self.active = active
        self.task = task
        self.lower_layout = QHBoxLayout()
        self.main_layout.addLayout(self.lower_layout, 1, 0)

        # ON/OFF BUTTON
        # //////////////////////////////////////////////////////////////
        # self.on_off_button = PyCheckBox(parent=parent,
        #                                 object_name=f"{object_name}_toggle",
        #                                 text=checkbox_text,
        #                                 )
        # self.active = self.on_off_button.checkbox.isChecked()
        # if toggle_connection is not None:
        #     self.on_off_button.checkbox.clicked.connect(toggle_connection)
        # VOLUME SLIDER
        # //////////////////////////////////////////////////////////////
        self.volume_slider = PySliderWithName(
            parent=self,
            object_name=f"{object_name}_slider",
            text=slider_text,
            value=slider_value,
        )
        if slider_connection is not None:
            self.volume_slider.slider.valueChanged.connect(slider_connection)
            # self.volume_slider.slider.sliderChange.connect(slider_connection)

        # WIDGETS OF LOWER LAYOUT
        # //////////////////////////////////////////////////////////////
        # self.lower_layout.addWidget(self.on_off_button, alignment=Qt.AlignCenter)
        self.lower_layout.addWidget(self.volume_slider, alignment=Qt.AlignCenter)
