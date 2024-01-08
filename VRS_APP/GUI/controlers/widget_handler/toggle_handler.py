from ..custom_widget_handler.handler import Handler
from ..custom_widget_handler.handler_factory import HandlerFactory


class ToggleHandler:
    def handle(self, request,handler_factory):
        handler: Handler = handler_factory.get_widget_handler(request)
        return handler.handle_toggle(request)


