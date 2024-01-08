from PySide6.QtCore import Qt

from ..py_push_button import PyPushButton
from ...core.json_themes import Themes

themes = Themes().items


class IndicationButton(PyPushButton):
    def __init__(self,
                 text="",
                 radius=10,
                 color=themes["app_color"]["red"],
                 bg_color=themes["app_color"]["red"],
                 bg_color_hover=themes["app_color"]["red"],
                 bg_color_pressed=themes["app_color"]["red"],
                 margin=0,
                 parent=None,
                 object_name="",
                 connection=None,
                 alignment=Qt.AlignCenter | Qt.AlignVCenter
                 ):
        super().__init__(text=text,
                         radius=radius,
                         color=color,
                         bg_color=bg_color,
                         bg_color_hover=bg_color_hover,
                         bg_color_pressed=bg_color_pressed,
                         margin=margin,
                         parent=parent,
                         object_name=object_name
                         )
        self.setFixedSize(20, 20)
        if connection is not None:
            self.clicked.connect(connection)
