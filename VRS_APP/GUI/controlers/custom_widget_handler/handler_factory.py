from .get_states_handler import GetStatesHandler
from .lights_handler import LightsHandler
from .maintenence_handler import MaintenenceHandler
from .master_reset_handler import MasterResetHandler
from .master_sounds_handler import MasterSoundsHandler
from .new_game_handler import NewGameHandler
from .sounds_handler import SoundsHandler
from .task_window_handler import TaskWindowHandler
from .jump_scare_handler import JumpScareHandler


class HandlerFactory:
    def __init__(self,
                 settings,
                 task_table=None,
                 master_reset=None,
                 maintenenace=None,
                 new_game=None,
                 timer=None,
                 lights_master_switch=None,
                 lights=None,
                 sounds=None):
        self.settings = settings
        self.task_table = task_table
        self.master_reset = master_reset
        self.maintenenace = maintenenace
        self.new_game = new_game
        self.timer = timer
        self.lights_master_switch = lights_master_switch
        self.lights = lights
        self.sounds = sounds
        self.handler_types = ["task_window", "task_table", "lights", "task"]

    def get_widget_handler(self, widget):
        parent = widget.parent()
        if widget.objectName() == "new_game_button":
            return NewGameHandler(settings=self.settings,
                                  timer=self.timer,
                                  task_table=self.task_table)

        if widget.objectName() == "maintenance_button":
            return MaintenenceHandler(timer=self.timer, settings=self.settings)

        elif "jump_scares" in parent.objectName():
            return JumpScareHandler(settings=self.settings)

        elif "light_master_switch" in parent.objectName() or "lights" in parent.objectName():
            return LightsHandler(settings=self.settings,
                                 lights_master_switch=self.lights_master_switch)

        elif parent.objectName() == "task_window" or \
                parent.objectName() == "task_table" or "task" in parent.objectName():
            return TaskWindowHandler(settings=self.settings)

        elif "master_sounds" == widget.parent().parent().objectName().strip():
            # print("Master sounds")
            return MasterSoundsHandler(settings=self.settings, sounds=self.sounds, master_sound_task=True)

        elif "sound" in parent.objectName():
            return SoundsHandler(settings=self.settings, sounds=self.sounds)

        elif widget.objectName() == "master_reset":
            return MasterResetHandler(task_table=self.task_table)

        elif widget.objectName() == "get_states":
            return GetStatesHandler(settings=self.settings)

    def get_message_handler(self, message):
        if message.message_code == self.settings["message_codes"]["finish"] or message.message_code == \
                self.settings["message_codes"]["reset"]:

            return TaskWindowHandler(settings=self.settings,
                                     task_table=self.task_table)

        elif message.message_code == self.settings["message_codes"]["master_reset"]:
            return MasterResetHandler(task_table=self.task_table)

        elif message.message_code == self.settings["message_codes"]["maintenance"]:
            return MaintenenceHandler(timer=self.timer, settings=self.settings)

        elif message.message_code == self.settings["message_codes"]["new_game"]:
            return NewGameHandler(settings=self.settings,
                                  timer=self.timer,
                                  task_table=self.task_table)

        elif message.message_code == self.settings["message_codes"]["light"]["volume"]:
            return LightsHandler(settings=self.settings,
                                 lights_master_switch=self.lights_master_switch,
                                 lights=self.lights)

        elif message.message_code == self.settings["message_codes"]["task_sound"]["volume"] or message.message_code == self.settings["message_codes"]["play_sound"]:
            return SoundsHandler(settings=self.settings, sounds=self.sounds)
