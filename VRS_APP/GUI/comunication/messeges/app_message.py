from GUI.comunication.messeges.abcmessage import ABCMessage
from can import Message


class AppMessage(ABCMessage):

    def __init__(self,
                 task_code=None,
                 message_code=None,
                 value=None):
        super().__init__(task_code, message_code, value)

    # def to_can_msg(self):
    #     task_code : int = 0
    #     value: int = 0
    #     if self.task_code is not None :
    #         task_code = int(self.task_code)
    #     if self.value is not None :
    #         value = int(self.value)
    #     return AppMessage(arbitration_id=int(self.message_code), data=[task_code, value])
    #