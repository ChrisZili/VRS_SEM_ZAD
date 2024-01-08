from ..py_empty_card import EmptyCard
from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout, QLabel
from PySide6.QtCore import Qt
class SenzorWidget(EmptyCard):
    def __init__(self, parent, connection, object_name="senzor_widget",unit=""):
        super().__init__(parent, object_name=object_name)
        self.main_layout.setContentsMargins(10,10,10,10)
        self.connected = False
        self.unit = unit
        self.setMaximumHeight(100)
        self.connection = connection
        self.layout = QHBoxLayout()
        self.main_layout.addLayout(self.layout, 1, 0)
        self.name = QLabel(object_name)
        self.name.setStyleSheet(
            "color: #8a95aa; font-size: 10px; font-weight: bold")

        self.value = QLabel(f"senzor_value{self.unit}")
        self.value.setStyleSheet(
            "color: #8a95aa; font-size: 10px; font-weight: bold")

        self.layout.addWidget(self.name)
        self.layout.addWidget(self.value)

    def update_value(self, value):
        self.value.setText(f"{value} {self.unit}")
        self.update()
