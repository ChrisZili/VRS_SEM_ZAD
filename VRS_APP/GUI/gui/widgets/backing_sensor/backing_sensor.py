import sys
from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton
from PySide6.QtGui import QPainter, QColor, QBrush
from PySide6.QtCore import Qt


class BackingSensorWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__()
        self.setMinimumSize(700, 400)
        self.setWindowTitle("Backing Sensor")
        self.orange = QColor(255, 165, 0)
        self.grey = QColor(128, 128, 128)
        self.parent = parent

        # Rectangles with different widths
        self.rectangles = [
            {"width": 480, "color": self.grey},
            {"width": 520, "color": self.grey},
            {"width": 560, "color": self.grey},
            {"width": 600, "color": self.grey},
            {"width": 640, "color": self.grey}
        ]


        layout = QVBoxLayout()
        self.setLayout(layout)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Drawing rectangles with different widths and colors
        for i, rect_data in enumerate(self.rectangles):
            painter.setBrush(QBrush(rect_data["color"]))
            painter.drawRect(
                self.width() / 2 - rect_data["width"] / 2,
                20 + i * 20,  # Spacing between rectangles
                rect_data["width"],
                15
            )

    def change_colors(self):
        # Change colors of rectangles
        new_colors = [Qt.blue, Qt.magenta, Qt.cyan, Qt.darkGreen, Qt.darkRed]
        for i, color in enumerate(new_colors):
            self.rectangles[i]["color"] = color
        self.update()  # Update the widget to reflect the new colors

    def change_last_rectangle_color(self):
        self.rectangles[-1]["color"] = Qt.green
        self.update()

    def change_4th_rectangle_color(self, color):
        self.rectangles[3]["color"] = Qt.darkGreen
        self.update()

    def change_3rd_rectangle_color(self, color):
        self.rectangles[2]["color"] = self.orange
        self.update()

    def change_2nd_rectangle_color(self, color):
        self.rectangles[1]["color"] = Qt.red
        self.update()

    def change_1st_rectangle_color(self, color):
        self.rectangles[0]["color"] = Qt.red
        self.update()
