from PySide6.QtWidgets import QWidget, QGridLayout

from ..task_window import TaskWindow


class TaskTable(QWidget):
    def __init__(self,
                 object_name="",
                 tasks=None,
                 parent=None,
                 button_connection=None,
                 ):
        super().__init__(parent=parent)
        self.tasks: list[TaskWindow] = []
        self.setObjectName(object_name)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.set_tasks(tasks=tasks, button_connection=button_connection)

    def set_tasks(self, tasks: list, button_connection=None):
        row = 0
        column = 0
        for task in tasks:
            self.tasks.append(TaskWindow(parent=self,
                                         object_name=task['name'],
                                         text=task["text"],
                                         button_connection=button_connection,
                                         task=task))
            self.grid_layout.addWidget(self.tasks[-1], row, column)
            if column == 1:
                column = 0
                row += 1
            else:
                column += 1

    def reset_tasks(self):
        for task in self.tasks:
            task.reset_tasks()

    def get_task(self, task_code):
        for task in self.tasks:
            if task.task["task_code"] == task_code:
                return task
        return None
