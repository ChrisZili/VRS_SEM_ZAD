import os
import sys
from sys import platform

from PySide6.QtCore import Qt
# from PyQt6.QtGui import Font, FontDatabase
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QStyleFactory
from GUI import MainWindow

# os.environ["QT_FONT_DPI"] = "96"

if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    print(platform)

    if platform == "darwin":
        os.environ["QT_FONT_DPI"] = "2"
    if platform == "win32" or platform == "cygwin":
        os.environ["QT_FONT_DPI"] = "96"

    style = QStyleFactory.create("Fusion")
    app = QApplication(sys.argv)
    # app.QFontDatabase.addApplicationFont("Segoe UI.ttf")
    app.setStyle(style)
    app.setWindowIcon(QIcon("GUI/escape.ico"))
    app.setAttribute(Qt.ApplicationAttribute.AA_DontUseNativeDialogs, True)
    window = MainWindow()




    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    os._exit(app.exec())
    # sys.exit()
