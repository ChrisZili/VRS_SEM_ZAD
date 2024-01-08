from PySide6.QtWidgets import QGridLayout, QHBoxLayout, QWidget, QLabel

from ..py_empty_card import EmptyCard
from ..slider_card import SliderCard
from ..master_switch import MasterSwitchToggle
from ..master_sounds import MasterSounds


class SoundTable(QWidget):
    def __init__(self, parent, object_name: str, text: str, toggle_connection: callable, slider_connection: callable,
                 tasks: list):
        # super().__init__()
        super().__init__(parent)
        self.tasks: list[SliderCard] = []
        self.setObjectName(object_name)
        self.setParent(parent)

        self.grid_layout = QGridLayout()
        self.setLayout(self.grid_layout)
        self.sounds_master_switch = MasterSwitchToggle(parent=self,
                                                       object_name="sounds_master_switch",
                                                       text=text,
                                                       toggle_connection=toggle_connection)
        self.master_active = self.sounds_master_switch.checkbox.checkbox.isChecked()
        print(f"Sounds master switch active: {self.master_active}")
        self.grid_layout.addWidget(self.sounds_master_switch, 0, 0, 1, 2)
        self.master_sounds = MasterSounds(parent=self,slider_connection=slider_connection)
        self.grid_layout.addWidget(self.master_sounds, 1, 0, 1, 2)
        self.setup_table(tasks=tasks,
                         toggle_connection=toggle_connection,
                         slider_connection=slider_connection)

    def setup_table(self, tasks: list[dict], toggle_connection, slider_connection: callable):
        row = 2
        column = 0
        for task in tasks:
            if task["sounds"]["active"]:
                self.tasks.append(SliderCard(parent=self,
                                             object_name=f"sound_{task['task_code']}",
                                             text=task["text"],
                                             checkbox_text="Vypnuty/Zapnuty",
                                             slider_text="Hlasitost",
                                             toggle_connection=toggle_connection,
                                             slider_connection=slider_connection,
                                             task=task,
                                             slider_value=task["sounds"]["value"]))

                self.grid_layout.addWidget(self.tasks[-1], row, column)
                if column == 1:
                    column = 0
                    row += 1
                else:
                    column += 1

    def get_task_from_sound(self, task_code=None):
        if task_code is not None:
            for task in self.tasks:
                if task.task["task_code"] == task_code:
                    return task
        else:
            return None
