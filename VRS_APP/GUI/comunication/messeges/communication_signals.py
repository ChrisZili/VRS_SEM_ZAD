from PySide6.QtCore import QObject, Signal


class CommunicationSignals(QObject):
    receive = Signal(object)
    send = Signal(object)