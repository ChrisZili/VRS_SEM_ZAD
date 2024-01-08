from .jump_scare_frame import JumpScareFrame
from ..py_empty_card import EmptyCard
from PySide6.QtWidgets import QGridLayout, QLabel, QPushButton, QWidget,QVBoxLayout
from PySide6.QtCore import Qt


class JumpScareWidget(QWidget):

    def __init__(self,
                 parent=None,
                 object_name="",
                 text="",
                 headline="",
                 buttons=None,
                 btn_connection=None):
        super().__init__(parent=parent)
        self.setObjectName(object_name)
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)
        self.headline = QLabel(headline)
        self.headline.setStyleSheet(
            "color: #8a95aa; font-size: 30px; font-weight: bold")
        self.main_layout.addWidget(self.headline, Qt.AlignCenter, Qt.AlignCenter)

        self.frame = JumpScareFrame(parent=self, object_name=object_name, text=text, buttons=buttons,
                                    btn_connection=btn_connection)
        self.main_layout.addWidget(self.frame)
        self.main_layout.setAlignment(Qt.AlignCenter)
