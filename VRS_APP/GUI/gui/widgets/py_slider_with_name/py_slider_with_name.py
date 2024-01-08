# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QWidget, QGridLayout
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ..py_slider import PySlider
from ...core import Themes


# PY INPUTS
# ///////////////////////////////////////////////////////////////
class PySliderWithName(QWidget):
    def __init__(self,
                 parent,
                 object_name="slider_with_name",
                 text="",
                 value=50,
                 message_code=None
                 ):
        super().__init__()

        themes = Themes()
        self.themes = themes.items
        self.setParent(parent)

        # SET OBJECT NAME
        self.setObjectName(object_name)
        self.message_code = message_code

        #  SET WIDGETS
        self.label_name = QLabel(text)
        self.label_name.setStyleSheet(f"color:#8a95aa;border: 0px transparent;")
        self.value = QLabel(f"{str(value)}%")
        self.value.setStyleSheet(f"color:#8a95aa;border: 0px transparent;")

        self.slider = PySlider(
            margin=8,
            bg_size=10,
            bg_radius=5,
            handle_margin=-3,
            handle_size=16,
            handle_radius=8,
            bg_color=self.themes["app_color"]["dark_three"],
            bg_color_hover=self.themes["app_color"]["dark_four"],
            handle_color=self.themes["app_color"]["context_color"],
            handle_color_hover=self.themes["app_color"]["context_hover"],
            handle_color_pressed=self.themes["app_color"]["context_pressed"],
            parent=parent,
            object_name=object_name
        )
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setMinimumWidth(200)
        self.slider.setValue(value)
        self.slider.last_value = value

        # CREATE LAYOUT
        self.layout = QGridLayout()
        self.layout.setColumnStretch(0, 1)
        # layout.setAlignment(Qt.AlignCenter)
        self.setLayout(self.layout)

        # ADD WIDGETS

        self.layout.addWidget(self.label_name, 0, 0)
        self.layout.addWidget(self.value, 0, 1)
        self.layout.addWidget(self.slider, 1, 0, 1, 2)

    def set_value(self, value):
        self.slider.setValue(value)
        self.slider.last_value = value
        self.value.setText(str(value))

    def set_text(self, value):
        self.value.setText(f"{str(value)}%")
