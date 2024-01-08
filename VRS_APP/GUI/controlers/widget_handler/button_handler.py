from ..custom_widget_handler.handler import Handler
from ..custom_widget_handler.handler_factory import HandlerFactory
from ...gui import PyPushButton
from json_settings import Settings


class ButtonHandler:

    def __init__(self):

        super().__init__()
        self.settings = Settings().items["message_codes"]

    def handle(self, request: PyPushButton, handler_factory):
        # print(f"Button {request.objectName()} pressed")
        # print(f"Button handler: {request.parent().objectName()}")
        handler: Handler = handler_factory.get_widget_handler(request)
        return handler.handle_button(request)
