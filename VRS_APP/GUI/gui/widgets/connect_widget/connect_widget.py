from ..py_empty_card import EmptyCard

from ..regular_button import RegularButton
from ..indication_button import IndicationButton


from PySide6.QtWidgets import QGridLayout, QVBoxLayout, QHBoxLayout
class ConnectWidget(EmptyCard):
    def __init__(self, parent, connection):
        super().__init__(parent)
        self.connected = False

        self.layout = QHBoxLayout()
        self.main_layout.addLayout(self.layout, 1, 0)
        self.setMaximumHeight(100)

        self.connect_button = RegularButton(
            text="Connect",
            parent=self,
            object_name="connect_button",
            connection=connection
        )

        self.indication_button = IndicationButton(
            parent=self,
            object_name="indication_button",
            connection=connection
        )


        self.layout.addWidget(self.connect_button)
        self.layout.addWidget(self.indication_button)
