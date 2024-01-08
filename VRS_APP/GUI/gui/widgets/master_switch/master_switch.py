from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout

from ..py_checkbox import PyCheckBox


class MasterSwitchToggle(QWidget):
    def __init__(self, parent,
                 object_name,
                 text,
                 toggle_connection,
                 ):
        super().__init__()
        self.active = False
        self.text = text
        self.setParent(parent)
        self.setObjectName(object_name)
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)

        self.sound_label = QLabel(text)
        self.sound_label.setStyleSheet(
            "color: #8a95aa; font-size: 30px; font-weight: bold;margin-top:15px")

        self.checkbox = PyCheckBox(parent=parent, object_name=object_name, text="")
        if toggle_connection:
            self.checkbox.checkbox.clicked.connect(toggle_connection)

        self.layout.addWidget(self.sound_label, Qt.AlignCenter, Qt.AlignRight)
        self.layout.addWidget(self.checkbox, Qt.AlignCenter, Qt.AlignLeft)

    def on(self):
        self.checkbox.checkbox.setChecked(True)
        self.active = True

    def off(self):
        self.checkbox.checkbox.setChecked(False)
        self.active = False
