from ..py_push_button import PyPushButton
from ...core.json_themes import Themes

themes = Themes().items


class RegularButton(PyPushButton):
    def __init__(self,
                 text="",
                 radius=8,
                 color=themes["app_color"]["text_foreground"],
                 bg_color=themes["app_color"]["dark_one"],
                 bg_color_hover=themes["app_color"]["dark_three"],
                 bg_color_pressed=themes["app_color"]["dark_four"],
                 margin=0,
                 parent=None,
                 object_name="",
                 connection=None
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
        self.setMinimumHeight(40)
        if connection is not None:
            self.clicked.connect(connection)
