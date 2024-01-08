# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QLabel, QVBoxLayout

from ..py_toggle import PyToggle


# PY INPUTS
# ///////////////////////////////////////////////////////////////
class PyCheckBox(QWidget):
    def __init__(self,
                 parent,
                 object_name,
                 text
                 ):
        super().__init__()
        # SET OBJECT NAME
        self.setObjectName(object_name)
        self.setParent(parent)
        self.text = text

        #  SET WIDGETS
        self.label_name = QLabel(text)
        self.label_name.setStyleSheet(f"color: #8a95aa ;border: 0px transparent;")
        self.checkbox = PyToggle(parent=self, object_name="py_toggle")

        # CREATE LAYOUT
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # ADD WIDGETS

        layout.addWidget(self.label_name)
        layout.addWidget(self.checkbox)

        self.setLayout(layout)


