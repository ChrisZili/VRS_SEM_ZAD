# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////


# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton

# STYLE
# ///////////////////////////////////////////////////////////////
style = '''
QPushButton {{

    margin: {_margin};
    padding-left: {_padding};
    padding-right:{_padding};
    
    color: {_color};
	border-radius: {_radius};	
	background-color: {_bg_color};
}}
QPushButton:hover {{
	background-color: {_bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {_bg_color_pressed};
}}
'''


# PY PUSH BUTTON
# ///////////////////////////////////////////////////////////////
class PyPushButton(QPushButton):
    def __init__(
            self,
            text,
            radius,
            color,
            bg_color,
            bg_color_hover,
            bg_color_pressed,
            padding=None,
            margin=None,
            parent=None,
            object_name="py_push_button"

    ):
        super().__init__(parent=parent,text=text)
        self.margin = margin
        self.padding = padding
        self.radius = radius
        self.text = text
        self.setObjectName(object_name)
        # SET PARAMETERS

        if parent is not None:
            self.setParent(parent)
        self.setCursor(Qt.PointingHandCursor)

        # SET STYLESHEET
        custom_style = style.format(
            _margin=margin,
            _color=color,
            _radius=radius,
            _bg_color=bg_color,
            _bg_color_hover=bg_color_hover,
            _padding=padding,
            _bg_color_pressed=bg_color_pressed

        )
        self.setStyleSheet(custom_style)

        if margin is not None:
            self.setContentsMargins(margin, -margin, margin, -margin)

    def set_red(self):
        self.setStyleSheet(style.format(
            _margin=self.margin,
            _color="#ff5555",
            _radius=self.radius,
            _bg_color="#ff5555",
            _bg_color_hover="#ff5555",
            _padding=self.padding,
            _bg_color_pressed="#ff5555"
        ))

    def set_green(self):
        self.setStyleSheet(style.format(
            _margin=self.margin,
            _color="#00ff7f",
            _radius=self.radius,
            _bg_color="#00ff7f",
            _bg_color_hover="#00ff7f",
            _padding=self.padding,
            _bg_color_pressed="#00ff7f"
        ))

