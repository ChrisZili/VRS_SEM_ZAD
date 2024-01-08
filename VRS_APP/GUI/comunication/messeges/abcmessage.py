from abc import ABC


class ABCMessage(ABC):
    def __init__(self,
                 task_code=None,
                 message_code=None,
                 value=None):
        self.task_code = task_code
        self.message_code = message_code
        self.value = value

    def get_task_code(self):
        return self.task_code

    def get_message_code(self):
        return self.message_code

    def get_value(self):
        return self.value

    def __str__(self):
        return f"task_code: {self.task_code}, message_code: {self.message_code}, value: {self.value}"

    def __repr__(self):
        return f"task_code: {self.task_code}, message_code: {self.message_code}, value: {self.value}"

    def __eq__(self, other):
        return self.task_code == other.task_code and self.message_code == other.message_code and self.value == other.value

    def __ne__(self, other):
        return not self.__eq__(other)
