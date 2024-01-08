# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QGridLayout

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////


# IMPORT STYLES
# ///////////////////////////////////////////////////////////////
# from . styles import Styles
from ..py_push_button import PyPushButton
from ..task_window import TaskWindow


class TaskWindowAdditionalButton(TaskWindow):
    def __init__(
            self,
            parent=None,
            object_name="task_window",
            text="",
            button_connection=None,):
        super().__init__(parent=parent, object_name=object_name,text=text,button_connection=button_connection)

        self.activation_button = PyPushButton(
            text="Aktivuj rakvu",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"],
            margin=5,
            parent=self,
            object_name="activation_button"

        )
        self.activation_button.setMinimumHeight(40)
        if button_connection is not None:
            self.activation_button.clicked.connect(button_connection)
        self.lower_layout.addWidget(self.activation_button,1,0,1,2)
