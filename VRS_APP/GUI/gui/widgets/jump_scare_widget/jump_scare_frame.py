from ..py_empty_card import EmptyCard
from ..regular_button import RegularButton


class JumpScareFrame(EmptyCard):

    def __init__(self, parent=None, object_name="jump_scare_frame", text="", buttons=None, btn_connection=None):
        super().__init__(parent=parent, object_name=object_name, text=text, border_radius=45)
        self.buttons = {}
        self.set_buttons(buttons=buttons, button_connection=btn_connection)

    def set_buttons(self, buttons: list, button_connection=None):

        button_pos = 3
        row = 1
        col = 0
        if len(buttons) % 2 == 0:
            for _button in buttons:

                button = RegularButton(
                    text=_button['text'],
                    parent=self,
                    object_name=_button["name"],
                    connection=button_connection
                )
                button.setMinimumHeight(50)
                self.main_layout.addWidget(button, row, col)
                self.buttons[_button["name"]] = button
                # self.buttons.append(button)
                col += 1
                if col == 2:
                    col = 0
                    row += 1
        else:
            for _button in buttons[:-1]:

                button = RegularButton(
                    text=_button["text"],
                    parent=self,
                    object_name=_button["name"],
                    connection=button_connection
                )
                button.setMinimumHeight(50)
                self.main_layout.addWidget(button, row, col)
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
            self.main_layout.addWidget(button, row, col, 1, 2)
