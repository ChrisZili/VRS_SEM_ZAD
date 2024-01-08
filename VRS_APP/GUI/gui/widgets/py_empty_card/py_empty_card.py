# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QFrame, QGridLayout, QHBoxLayout, QLabel, QGraphicsDropShadowEffect

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from json_settings import Settings

# IMPORT STYLES
# ///////////////////////////////////////////////////////////////
from .styles import Styles
from ....gui.core.json_themes import Themes


class EmptyCard(QFrame):

    def __init__(
            self,
            parent,
            object_name="task_window",
            text="",
            layout=Qt.Horizontal,
            margin=5,
            spacing=2,
            bg_color="#2c313c",
            text_color="#8a95aa",
            text_font="9pt 'Segoe UI'",
            border_radius=45,
            border_size=4.5,
            border_color="#343b48",
            enable_shadow=False,
            task: dict = None

    ):
        super().__init__()
        self.task = task
        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # PROPERTIES
        # ///////////////////////////////////////////////////////////////
        self.parent = parent
        self.text = text
        self.setParent(parent)
        self.setObjectName(object_name)
        self.layout = layout
        self.margin = margin
        self.bg_color = bg_color
        self.text_color = text_color
        self.text_font = text_font
        self.border_radius = border_radius
        self.border_size = border_size
        self.border_color = border_color
        self.enable_shadow = enable_shadow
        themes = Themes()
        self.themes = themes.items

        # LAYOUT
        # ///////////////////////////////////////////////////////////////
        self.main_layout = QGridLayout()
        # self.upper_layout = QHBoxLayout()
        # self.upper_layout.setStretch(1, 2)
        # self.upper_layout.setSpacing(0)

        self.main_layout.setContentsMargins(15, 15, 15, 15)
        self.main_layout.setSpacing(0)
        # self.main_layout.addLayout(self.upper_layout, 0, 0)

        # self.setLayout(self.main_layout)

        # WIDGETS OF UPPER LAYOUT
        # //////////////////////////////////////////////////////////////
        # TASK LABEL
        # //////////////////////////////////////////////////////////////
        if text != "":
            self.upper_layout = QHBoxLayout()
            self.upper_layout.setStretch(1, 2)
            self.upper_layout.setSpacing(0)
            self.main_layout.addLayout(self.upper_layout, 0, 0)
            self.task_name = QLabel(text)
            self.task_name.setAlignment(Qt.AlignLeft | Qt.AlignTop)
            self.task_name.setStyleSheet(f"color: #8a95aa ;border: 1px transparent;")
            self.upper_layout.addWidget(self.task_name)

        self.setLayout(self.main_layout)
        # SHADOW
        # ///////////////////////////////////////////////////////////////
        if self.enable_shadow:
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 60))
            self.setGraphicsEffect(self.shadow)

        # APPLY STYLESHEET
        # ///////////////////////////////////////////////////////////////
        self.set_stylesheet()

        # ADD WIDGETS
        # ///////////////////////////////////////////////////////////////

        # APPLY AND UPDATE STYLESHEET
        # ///////////////////////////////////////////////////////////////

    def set_stylesheet(
            self,
            bg_color=None,
            border_radius=None,
            border_size=None,
            border_color=None,
            text_color=None,
            text_font=None
    ):
        # CHECK BG COLOR
        if bg_color != None:
            internal_bg_color = bg_color
        else:
            internal_bg_color = self.bg_color

        # CHECK BORDER RADIUS
        if border_radius != None:
            internal_border_radius = self.border_radius
        else:
            internal_border_radius = self.border_radius

        # CHECK BORDER SIZE
        if border_size != None:
            internal_border_size = border_size
        else:
            internal_border_size = self.border_size

        # CHECK BORDER COLOR
        if text_color != None:
            internal_text_color = text_color
        else:
            internal_text_color = self.text_color

        # CHECK TEXT COLOR
        if border_color != None:
            internal_border_color = border_color
        else:
            internal_border_color = self.border_color

        # CHECK TEXT COLOR
        if text_font != None:
            internal_text_font = text_font
        else:
            internal_text_font = self.text_font

        self.setStyleSheet(Styles.bg_style.format(
            _bg_color=internal_bg_color,
            _border_radius=internal_border_radius,
            _border_size=internal_border_size,
            _border_color=internal_border_color,
            _text_color=internal_text_color,
            _text_font=internal_text_font
        ))
