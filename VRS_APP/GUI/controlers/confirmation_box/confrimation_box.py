from PySide6.QtWidgets import QMessageBox


class ConfirmationBox:

    @staticmethod
    def question(request):
        try:
            button_reply = QMessageBox.Warning.question(request, "",
                                                f"Naozaj chete stlacit {request.parent().text} {request.text}",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        except:
            button_reply = QMessageBox.Warning.question(request, "", f"Naozaj chete stlacit {request.text}",
                                                QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if button_reply == QMessageBox.No:
            return False
        else:
            return True
