from ..custom_widget_handler import Handler


class MessageHandler:
    def __init__(self,
                 handler_factory=None):
        self.handler_factory = handler_factory

    def handle(self, request):
        handler: Handler = self.handler_factory.get_message_handler(request)
        return handler.handle_message(request)

