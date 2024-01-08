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
from ..py_empty_card import EmptyCard
from ..regular_button import RegularButton
from ..indication_button import IndicationButton
from ....comunication import AppMessage


class TaskWindow(EmptyCard):
    def  __init__(
            self,
            parent=None,
            object_name="task_window",
            text="",
            button_connection=None,
            task: dict = None,

    ):
        super().__init__(parent=parent, object_name=object_name, text=text, task=task)
        self.buttons = {}
        self.lower_layout = QGridLayout()
        self.main_layout.addLayout(self.lower_layout, 1, 0)

        # INDICATION BUTTON
        # //////////////////////////////////////////////////////////////
        self.buttons["indication_button"] = IndicationButton(
            parent=self,
            object_name="indication_button",
            connection=button_connection
        )

        # WIDGETS OF LOWER LAYOUT
        # //////////////////////////////////////////////////////////////
        # TASK FINISHED BUTTON
        # //////////////////////////////////////////////////////////////
        self.buttons["finish_button"] = RegularButton(
            text="Uloha Splnena",
            parent=self,
            object_name="finish_button",
            connection=button_connection
        )
        self.buttons["finish_button"].setMinimumHeight(50)

        self.buttons["reset_button"] = RegularButton(
            text="Resetovat Ulohu",
            parent=self,
            object_name="reset_button",
            connection=button_connection
        )
        self.buttons["reset_button"].setMinimumHeight(50)


        # ADD TO UPPER LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.upper_layout.addWidget(self.buttons["indication_button"], alignment=Qt.AlignRight | Qt.AlignTop)

        # ADD TO LOWER LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.lower_layout.addWidget(self.buttons["finish_button"], 0, 0)
        self.lower_layout.addWidget(self.buttons["reset_button"], 0, 1)
        self.set_additional_buttons(buttons=task["buttons"]["additional_buttons"], button_connection=button_connection)

    def finish_task(self, message_code):
        self.buttons["indication_button"].set_green()
        return AppMessage(task_code=self.task["task_code"],
                          message_code=message_code,
                          value=None)

    def reset_task(self, message_code):
        self.buttons["indication_button"].set_red()
        return AppMessage(task_code=self.task["task_code"],
                          message_code=message_code,
                          value=None)

    def activate_action(self, message_code):

        return AppMessage(task_code=self.task["task_code"],
                          message_code=message_code,
                          value=None)

    def reset_tasks(self):
        self.buttons["indication_button"].set_red()

    def set_additional_buttons(self, buttons: list, button_connection=None):
        button_pos = 3
        row = 1
        col = 0
        if len(buttons) % 2 == 0:
            for _button in buttons:
                button = RegularButton(
                    text=_button["text"],
                    parent=self,
                    object_name=_button["name"],
                    connection=button_connection
                )
                button.setMinimumHeight(50)
                self.lower_layout.addWidget(button, row, col)
                self.buttons[_button["name"]] = button
                # self.buttons.append(button)
                col += 1
                if col == 2:
                    col = 0
                    row += 1
        else:
            for _button in range(len(buttons) - 1):
                button = RegularButton(
                    text=_button["text"],
                    parent=self,
                    object_name=_button["name"],
                    connection=button_connection
                )
                button.setMinimumHeight(50)
                button.setMinimumWidth(180)
                self.lower_layout.addWidget(button, row, col)
                self.buttons[_button["name"]] = button
                # self.buttons.append(button)
                col += 1
                if col == 2:
                    col = 0
                    row += 1
            button = RegularButton(
                text=buttons[-1]["text"],
                parent=self,
                object_name=buttons[-1]["name"],
                connection=button_connection
            )
            button.setMinimumHeight(50)
            self.lower_layout.addWidget(button, row, col,1,2)
