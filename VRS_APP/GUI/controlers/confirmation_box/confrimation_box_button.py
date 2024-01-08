from PySide6.QtWidgets import QMessageBox


class ConfirmationBoxButton:

    @staticmethod
    def question(request):
        try:
            reply = QMessageBox(
                text=f"Naozaj chete stlacit {request.parent().text} - {request.text}")
            reply.setIcon(QMessageBox.Icon.Question)
            reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            reply.setStyleSheet(f"background-color:#1b1e23;color:#8a95aa;")
            res = reply.exec_()

        except:
            reply = QMessageBox(
                text=f"Naozaj chete stlacit - {request.text}")
            reply.setIcon(QMessageBox.Icon.Question)
            reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            reply.setStyleSheet(f"background-color:#1b1e23;color:#8a95aa;")
            res = reply.exec_()
        finally:
            return res == QMessageBox.Yes
