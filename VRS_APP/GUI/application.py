from time import sleep

# ////////////////////////////////////////////////////////////////
# ///////////////////    GUI IMPORTS  ///////////////////////////
# ///////////////////////////////////////////////////////////////
import PySide6.QtCore as QtCore
from PySide6.QtCore import QThreadPool, Signal, QObject, Slot
from PySide6.QtWidgets import QMessageBox, QMainWindow
from PySide6.QtWidgets import QMainWindow
from PySide6.QtGui import QImage, QPixmap
from .gui import UiMainWindow, SetupMainWindow, MainFunctions, set_svg_icon
import sys
import os
import threading
import re

# ////////////////////////////////////////////////////////////////
# ///////////////    COMMUNICATION IMPORTS  //////////////////////
# ///////////////////////////////////////////////////////////////

import can
from .comunication import Communication, CommunicationSignals, CanCommunication, AppMessage
import can.interfaces.virtual
from .comunication.external_comunication.serial_communication import SerialCommunication
from .comunication.external_comunication.internet_communication import InternetCommunication

# ////////////////////////////////////////////////////////////////
# ////////////////    CONTROLLERS IMPORTS  //////////////////////
# ///////////////////////////////////////////////////////////////

from .controlers import ButtonHandler, SliderHandler, ToggleHandler
from .controlers.message_handler.message_handler import MessageHandler
from .controlers import HandlerFactory

from .gui.widgets import XboxController
# ////////////////////////////////////////////////////////////////
# ///////////////    SETTINGS IMPORTS  //////////////////////////
# ///////////////////////////////////////////////////////////////

from json_settings import Settings

# ////////////////////////////////////////////////////////////////
# //////////////////    MAIN WINDOW  ////////////////////////////
# ///////////////////////////////////////////////////////////////

IP = "25.59.215.144"


class internet_signal(QObject):
    signal = Signal(str)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # ////////////////////////////////////////////////////////////////
        # //////////////////    LOAD SETTINGS  //////////////////////////
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = Settings()

        # ////////////////////////////////////////////////////////////////
        # ///////////////    SETUP MAIN WINDOW  //////////////////////////
        # ///////////////////////////////////////////////////////////////

        self.ui = UiMainWindow(close_connection=self.on_close)
        self.ui.setup_ui(self)
        self.hide_grips = True  # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # ////////////////////////////////////////////////////////////////
        # ////////////////    GET CUSTOM WIDGETS  ////////////////////////
        # ////////////////////////////////////////////////////////////////

        # self.task_table = SetupMainWindow.get_tasks_table(self)
        # self.master_reset_button = SetupMainWindow.get_master_reset_button(self)
        # self.maintenance_button = SetupMainWindow.get_maintenance_button(self)
        # self.new_game_button = SetupMainWindow.get_new_game_button(self)
        # self.timer = SetupMainWindow.get_timer(self)
        # self.lights_master_switch = SetupMainWindow.get_lights_master_switch(self)
        # self.lights_table = SetupMainWindow.get_lights_table(self)
        # self.sound_table = SetupMainWindow.get_sounds_table(self)
        pic = QPixmap("black.jpg")
        self.camera_widget = SetupMainWindow.get_camera_widget(self)
        self.connect_widget = SetupMainWindow.get_connect_widget(self)
        self.xbox_controller = XboxController(left_joystick_connection=self.left_joystick_connection,
                                              right_joystick_connection=self.right_joystick_connection)
        self.range_sensor = SetupMainWindow.get_range_sensor(self)
        self.temperature_sensor = SetupMainWindow.get_temperature_sensor(self)
        self.humidity_sensor = SetupMainWindow.get_humidity_sensor(self)
        self.backing_sensor = SetupMainWindow.get_backing_sensor(self)
        # ////////////////////////////////////////////////////////////////
        # //////////////////    GET HANDLERS  ////////////////////////////
        # ///////////////////////////////////////////////////////////////

        # ////////////////////////////////////////////////////////////////
        # ////////////////    SHOW MAIN WINDOW  //////////////////////////
        # ////////////////////////////////////////////////////////////////

        self.show()
        sleep(1)

        # ////////////////////////////////////////////////////////////////
        # //////////////////    COMMUNICATION  //////////////////////////
        # ///////////////////////////////////////////////////////////////

        # self.external_communication = CanCommunication(channel='test',
        #                                                bitrate=500000,
        #                                                bus_type='virtual')

        self.external_communication = InternetCommunication(server_ip=IP, server_port=5050)
        # self.external_communication.connect()
        self.communication = Communication(external_communication=self.external_communication)
        # self.communication.send_to_external("Hello from main window")
        self.communication.signals.send.connect(self.on_external_msg_recieved)
        self.communication.signals.receive.connect(self.handle_message_from_server)

        # ////////////////////////////////////////////////////////////////
        # //////////////////    APP THREADS    //////////////////////////
        # ///////////////////////////////////////////////////////////////
        self.client_recieve_thread = threading.Thread(target=self.external_communication.receive)
        self.client_recieve_thread.daemon = True
        self.client_recieve_thread.start()

        self.camera_cleaner_thread = threading.Thread(target=self.camera_widget.cam_cleaner.run,
                                                      args=([self.camera_widget.camera]))
        self.camera_cleaner_thread.daemon = True
        self.camera_cleaner_thread.start()
        self.last_camera_value = None

        self.camera_thread = threading.Thread(target=self.camera_widget.camera_thread.run)
        self.camera_thread.daemon = True
        self.camera_thread.start()

        # self.camera_status_thread = threading.Thread(target=self.camera_status)
        # self.camera_status_thread.daemon = True
        # self.camera_status_thread.start()

        # self.xbox_controller_thread = threading.Thread(target=self.xbox_controller.run)
        # # self.xbox_controller_thread.daemon = True
        # self.xbox_controller_thread.start()

        self.connect_controller()

    # ////////////////////////////////////////////////////////////////
    # //////////////    LEFT MENU BTN IS CLICKED  ////////////////////
    # ///////////////////////////////////////////////////////////////

    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active
        # top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        # top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////

        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # WIDGETS BTN
        if btn.objectName() == "btn_widgets":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # JUMP SCARES BTN
        if btn.objectName() == "btn_jump_scares":
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_4)
        # LOAD USER PAGE
        if btn.objectName() == "btn_add_user":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3 
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        # BOTTOM INFORMATION
        if btn.objectName() == "btn_info":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                self.ui.left_menu.select_only_one_tab(btn.objectName())

                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)

                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_2,
                    title="Info tab",
                    icon_path=set_svg_icon("icon_info.svg")
                )

        # SETTINGS LEFT
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            # CHECK IF LEFT COLUMN IS VISIBLE
            if not MainFunctions.left_column_is_visible(self):
                # Show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column":
                    self.ui.left_menu.deselect_all_tab()
                    # Show / Hide
                    MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            # Change Left Column Menu
            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu=self.ui.left_column.menus.menu_1,
                    title="Settings Left Column",
                    icon_path=set_svg_icon("icon_settings.svg")
                )

        # ////////////////////////////////////////////////////////////////
        # //////////////////    TITLE BAR MENU  //////////////////////////
        # ///////////////////////////////////////////////////////////////
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)

            # DEBUG
        # print(f"Button {btn.objectName()}, clicked!")

    # ////////////////////////////////////////////////////////////////
    # //////////////    LEFT MENU BTN RELEASE  //////////////////////
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        # print(f"Button {btn.objectName()}, released!")

    # ////////////////////////////////////////////////////////////////
    # //////////////    APP BUTTONS CLICKED  /////////////////////////
    # ///////////////////////////////////////////////////////////////
    def btns_tasks_clicked(self):
        message = self.buttons_handler.handle(self.sender(), self.handler_factory)
        if message:
            self.communication.send_to_external(message)

    # ////////////////////////////////////////////////////////////////
    # //////////////    APP TOGGLES CONNECTION //////////////////////
    # ///////////////////////////////////////////////////////////////
    def toggle_clicked(self) -> None:
        message = self.toggle_handler.handle(self.sender(), self.handler_factory)
        if message:
            self.communication.send_to_external(message)

    # ////////////////////////////////////////////////////////////////
    # /////////////////    SLIDER CONNECTIONS  //////////////////////
    # ///////////////////////////////////////////////////////////////
    def slider_clicked(self):

        message = self.slider_handler.handle(self.sender(), self.handler_factory)
        if message:
            self.communication.send_to_external(message)

    # ////////////////////////////////////////////////////////////////
    # ///////////////////    TIMER CONNECTIION  /////////////////////
    # ///////////////////////////////////////////////////////////////
    def action_10_minutes(self):
        self.communication.send_to_external(AppMessage(task_code=0,
                                                       message_code=
                                                       self.settings.items["message_codes"]["10_min_action"]["sound"],
                                                       value=None))
        self.communication.send_to_external(AppMessage(task_code=0,
                                                       message_code=
                                                       self.settings.items["message_codes"]["10_min_action"]["light"],
                                                       value=None))

    # ///////////////////////////////////////////////////////////////
    # /////////////////////    RESIZE EVENT  ////////////////////////
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        # print(f"Button {btn.objectName()}, released!")

    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # ///////////////////////////////////////////////////////////////
    # ////////////////    MOUSE CLICKED EVENT  //////////////////////
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()

    # ///////////////////////////////////////////////////////////////
    # ////////////    COMMUNICATION CONNECTIONS  ////////////////////


    def on_external_msg_recieved(self, data):
        print(f"MainWindow recieved {data}")
        self.communication.signals.receive.emit(data)

    def extract_number(self,input_string):
        # Use regular expressions to find the first sequence of digits in the string
        match = re.search(r'\d+', input_string)
        if match:
            return int(match.group())  # Extract the found number as an integer
        else:
            return None  # Return None if no number is founds
    @QtCore.Slot(str)
    def handle_message_from_server(self, message):
        if message[0] == "L":
            number = self.extract_number(message)
            if number is not None:
                self.range_sensor.update_value(number)
        if message[0] == "T":
            number = self.extract_number(message)
            if number is not None:
                self.temperature_sensor.update_value(number)
        if message[0] == "H":
            number = self.extract_number(message)
            if number is not None:
                self.humidity_sensor.update_value(number)
        if message[0] == "R":
            number = self.extract_number(message)
            if number is not None:
                self.backing_sensor.updare_backing_sensor(number)



    def communication_data_send(self, data):
        self.communication.send_to_external(data)

    # ///////////////////////////////////////////////////////////////

    # ///////////////////////////////////////////////////////////////
    # ////////////////////    ON APP CLOSE  /////////////////////////
    # ///////////////////////////////////////////////////////////////
    def on_close(self):
        reply = QMessageBox(
            text=f"Naozaj chete ukončiť aplikáciu?")
        reply.setIcon(QMessageBox.Icon.Question)
        reply.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        reply.setStyleSheet(f"background-color:#1b1e23;color:#8a95aa;")
        res = reply.exec_()

        if res == QMessageBox.Yes:
            self.close()
            # os._exit(0)

    def connect_button_clicked(self):
        if self.external_communication.connected:
            self.connect_widget.indication_button.set_red()
            self.connect_widget.connect_button.setText("Connect")
            self.external_communication.disconnect()
            self.camera_widget.disconnect_camera()


        else:
            self.external_communication.connected = True
            self.connect_widget.indication_button.set_green()
            self.connect_widget.connect_button.setText("Disconnect")
            print("Connecting")

            self.external_communication.connect()

            self.camera_widget.connect_camera()
            print(self.camera_widget.camera)

    def connect_controller(self):
        self.xbox_controller.run()

    def left_joystick_connection(self, value):
        if self.external_communication.connected:
            if value is not None:
                if len(str(value)) == 10:
                    self.communication.send_to_external(f"1{str(value)}")

    def right_joystick_connection(self, value):
        self.last_camera_value = value
        if self.external_communication.connected:
            if value is not None:
                if len(str(value)) == 10:
                    self.communication.send_to_external(f"2{str(value)}")
        # self.camera_widget.camera_thread.updateCrossPosition(value[0], value[1])

    def camera_status(self):
        sleep(5)
        while True:
            if self.external_communication.connected:
                self.communication.send_to_external("4xxxxxxxxxx")
                sleep(1)
