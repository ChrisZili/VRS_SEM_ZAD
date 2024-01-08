from ..custom_widget_handler.handler import Handler
from ..custom_widget_handler.handler_factory import HandlerFactory


class SliderHandler():
    def handle(self, request,handler_factory):
        # print(f"Slider handler: name = {request.objectName()} parent = {request.parent().objectName()}")
        handler: Handler = handler_factory.get_widget_handler(request)
        return handler.handle_slider(request)

        # button_reply = QMessageBox.question(request, "", f"Naozaj chete stlacit slider", QMessageBox.Yes | QMessageBox.No,
        #                                     QMessageBox.No)
        #
        # if button_reply == QMessageBox.No:
        #     # sender.setValue(current_value)
        #     request.clearFocus()
        #     request.setValue(request.last_value)
        #     print(f"Value changed back to {request.last_value}")
        #     return
        # else:
        #     print(request.parent().parent().active)
        #     if request.parent().parent().parent.master_active and request.parent().parent().active:
        #         request.last_value = request.value()
        #         if request.parent().parent().task is not None:
        #             return{
        #                 "button_code": request.parent().parent().task["sounds"],
        #                 "message_code": request.parent().parent().task["message_code"],
        #                 "value": request.value()
        #             }
        #
        #     else:
        #         request.clearFocus()
        #         request.setValue(request.last_value)
        #         print(f"Value changed back to {request.last_value}")
        #
        #         return
