from PySide6.QtWidgets import QMessageBox


class ConfrimationBoxToggle:

    @staticmethod
    def question(request,text):
        checked = request.isChecked()
        if checked == True:
            on = "Zapnúť"
        else:
            on = "Vypnúť"
        print(f"checked = {request.isChecked()}")
        try:
            reply = QMessageBox(
                text=f"Naozaj chete {on} {text}")
            reply.setIcon(QMessageBox.Icon.Question)
            reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            reply.setStyleSheet(f"background-color:#1b1e23;color:#8a95aa;")
            res = reply.exec_()

        except:
            reply = QMessageBox(
                text=f"Naozaj chete stlacit {request.text}")
            reply.setIcon(QMessageBox.Icon.Question)
            reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

            reply.setStyleSheet(f"background-color:#1b1e23;color:#8a95aa;")
            res = reply.exec_()
        finally:
            if res == QMessageBox.No:
                request.setChecked(not checked)
                request.setup_animation(not checked)
                return False
            else:
                return True
