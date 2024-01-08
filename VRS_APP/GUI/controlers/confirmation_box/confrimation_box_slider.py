from PySide6.QtWidgets import QMessageBox


class ConfrimationBoxSlider:

    @staticmethod
    def question(request,text):
        reply = QMessageBox(
            text=f"Naozaj chete stlacit {request.parent().text} - {request.text}")
        reply.setIcon(QMessageBox.Icon.Question)
        reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply.setStyleSheet(f"background-color:#1b1e23;")
        res = reply.exec_()

        if res == QMessageBox.No:
            request.clearFocus()
            request.setValue(request.last_value)
            print(f"Value changed back to {request.last_value}")
            return False
        else:
            return True
