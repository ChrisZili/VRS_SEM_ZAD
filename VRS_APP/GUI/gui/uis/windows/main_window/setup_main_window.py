# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////


# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from PySide6.QtGui import QIcon

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////


# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////


# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from PySide6.QtWidgets import QLabel, QHeaderView, QAbstractItemView, QTableWidgetItem

from ....widgets.jump_scare_widget import JumpScareWidget
from .....gui.widgets.task_table import TaskTable
from .....gui.widgets import PyGrips, PyPushButton, PyCircularProgress, PySlider, PyIconButton, PyLineEdit, PyToggle, \
    PyTableWidget
from .....gui.widgets.slider_card import SliderCard
from .....gui.widgets.sound_table import SoundTable
from .....gui.widgets.timer import Timer
from .....gui.widgets.task_window.task_window import TaskWindow
from .....gui.widgets import TaskWindowAdditionalButton, MasterSwitchToggle, MasterSounds, JumpScareFrame, \
    ConnectWidget, SenzorWidget, CameraWidget, BackingSensorWidget

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////


# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # ///////////////////////////////////////////////////////////////
        # ///////////////////   GET SETTINGS ///////////////////////////
        # ///////////////////////////////////////////////////////////////

        settings = Settings()
        self.settings = settings.items

        # ///////////////////////////////////////////////////////////////
        # ///////////////////   SETUP MAIN WINDOW //////////////////////
        # ///////////////////////////////////////////////////////////////

        self.ui = UiMainWindow()
        self.ui.setup_ui(self)

        # //////////////////////////////////////////////////////////////

    # ///////////////////////////////////////////////////////////////
    # ///////////////////   ADD LEFT MENUS //////////////////////
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": " ",
            "btn_tooltip": " ",
            "show_top": True,
            "is_active": True
        },
        # {
        #     "btn_icon": "icon_widgets.svg",
        #     "btn_id": "btn_add_user",
        #     "btn_text": "Ovladanie",
        #     "btn_tooltip": "Ovladanie",
        #     "show_top": True,
        #     "is_active": False
        # },
        # {
        #     "btn_icon": "icon_ghost.png",
        #     "btn_id": "btn_jump_scares",
        #     "btn_text": "Strasidelne efekty",
        #     "btn_tooltip": "Strasidelne efekty",
        #     "show_top": True,
        #     "is_active": False
        # }
        # {
        #     "btn_icon": "icon_settings.svg",
        #     "btn_id": "btn_settings",
        #     "btn_text": "Settings",
        #     "btn_tooltip": "Open settings",
        #     "show_top": False,
        #     "is_active": False
        # }
    ]

    # ///////////////////////////////////////////////////////////////
    # ///////////////////   ADD TITLE BAR MENUS /////////////////////
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        # {
        #     "btn_icon" : "icon_search.svg",
        #     "btn_id" : "btn_search",
        #     "btn_tooltip" : "Search",
        #     "is_active" : False
        # },
        # {
        #     "btn_icon" : "icon_settings.svg",
        #     "btn_id" : "btn_top_settings",
        #     "btn_tooltip" : "Top settings",
        #     "is_active" : False
        # }
    ]

    # ///////////////////////////////////////////////////////////////
    # ///////////////////   SETUP BTNS SENDERS /////////////////////
    # Get sender() function when btn is clickeD
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() is not None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() is not None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() is not None:
            return self.ui.left_column.sender()
        elif self.ui.load_pages.pages.sender() is not None:
            return self.ui.load_pages.pages.sender()

    # ////////////////////////////////////////////////////////////////
    # ///////// SETUP MAIN WINDOW WITH CUSTOM WIDGETS ///////////////
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # /////////////////////////////////////////////////////////////
        # ///////////////   APP TITLE   ///////////////////////////////
        # /////////////////////////////////////////////////////////////

        self.setWindowTitle(self.settings.items["app_name"])

        # //////////////////////////////////////////////////////////////
        # /////////////  CUSTOM TITLE BAR    ///////////////////////////
        # //////////////////////////////////////////////////////////////

        if self.settings.items["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)
        # ///////////////////////////////////////////////////////////////
        # //////////////  ADD GRIPS   //////////////////////////////////
        # ///////////////////////////////////////////////////////////////

        if self.settings.items["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # ///////////////////////////////////////////////////////////////
        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # /////////////////     # ADD MENUS     ///////////////////////
        # ////////////////////////////////////////////////////////////

        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # ///////////////////////////////////////////////////////////////
        # ///////////////////   SET SIGNALS //////////////////////////
        # ////////////////////////////////////////////////////////////

        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ///////////////////   ADD MENUS //////////////////////////////
        # ////////////////////f//////////////////////////////////////////

        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # ///////////////////////////////////////////////////////////////
        # ///////////////////   SET SIGNALS /////////////////////////////
        # ///////////////////////////////////////////////////////////////

        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # //////////////////////////////////////////////////////////////
        # ///////////////////   ADD TITLE /////////////////////////////
        # ////////////////////////////////////////////////////////////

        if self.settings.items["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings.items["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to Escape Room")

        # ///////////////////////////////////////////////////////////////
        # /////////////////   LEFT COLUMS SET SIGNALS ///////////////////
        # ///////////////////////////////////////////////////////////////

        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # ///////////////////////////////////////////////////////////////
        # ///    SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS  ////
        # ///////////////////////////////////////////////////////////////

        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # /////////////     LOAD THEME COLOR        ////////////////
        # ///////////////////////////////////////////////////////////////

        themes = Themes()
        self.themes = themes.items
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # /////////////////    PAGES       /////////////////////////////
        # ///////////////////////////////////////////////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # /////////////////    PAGE 1       ////////////////////////////
        # ///////////////////////////////////////////////////////////////
        self.connect_widget = ConnectWidget(self, self.connect_button_clicked)
        self.range_sensor = SenzorWidget(self, self.connect_button_clicked, "Range sensor", "cm")
        self.tempeture_sensor = SenzorWidget(self, self.connect_button_clicked, "Tempeture sensor", "°C")
        self.humidity_sensor = SenzorWidget(self, self.connect_button_clicked, "Humidity sensor", "%")
        self.camera_widget = CameraWidget()
        self.backing_sensor = BackingSensorWidget(self)

        # ///////////////////////////////////////////////////////////////
        # ///////////////// ADD LOGO TO MAIN PAGE      /////////////////
        # ///////////////////////////////////////////////////////////////

        # self.logo_svg = QSvgWidget(Functions.set_svg_image("escape.svg"))
        # self.ui.load_pages.logo_layout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # ///////////////   FIRST ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        self.ui.load_pages.task_layout_row1.addWidget(self.connect_widget)
        self.ui.load_pages.task_layout_row1.addWidget(self.range_sensor)
        self.ui.load_pages.task_layout_row1.addWidget(self.tempeture_sensor)
        self.ui.load_pages.task_layout_row1.addWidget(self.humidity_sensor)
        self.ui.load_pages.task_layout_row2.addWidget(self.camera_widget, Qt.AlignCenter, Qt.AlignCenter)
        self.ui.load_pages.task_layout_row2.addWidget(self.backing_sensor, Qt.AlignCenter, Qt.AlignCenter)

        # ///////////////////////////////////////////////////////////////
        # ///////////////   SECOND ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # /////////////////    PAGE 2       ////////////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # ///////////////   FIRST ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # ///////////////   SECOND ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # ///////////////   THIRD ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # /////////////////    PAGE 3       ////////////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # ///////////////   FIRST ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # ///////////////  SECOND ROW LAYOUT      ///////////////////////
        # ///////////////////////////////////////////////////////////////

        # ///////////////////////////////////////////////////////////////
        # # ////////////////  RIGHT COLUMN  ////////////////////////////
        # ///////////////////////////////////////////////////////////////

        # BTN 1
        self.right_btn_1 = PyPushButton(
            text="Show Menu 2",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_right = QIcon(set_svg_icon("no_icon.svg"))
        self.right_btn_1.setIcon(self.icon_right)
        self.right_btn_1.setMaximumHeight(40)
        self.right_btn_1.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_2
        ))
        self.ui.right_column.btn_1_layout.addWidget(self.right_btn_1)

        # BTN 2
        self.right_btn_2 = PyPushButton(
            text="Show Menu 1",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon_left = QIcon(set_svg_icon("no_icon.svg"))
        self.right_btn_2.setIcon(self.icon_left)
        self.right_btn_2.setMaximumHeight(40)
        self.right_btn_2.clicked.connect(lambda: MainFunctions.set_right_column_menu(
            self,
            self.ui.right_column.menu_1
        ))
        self.ui.right_column.btn_2_layout.addWidget(self.right_btn_2)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

    # ///////////////////////////////////////////////////////////////
    # # /////////// RESIZE GRIPS AND CHANGE POSITION  ///////////////
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings.items["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)

    # //////////////////////////////////////////////////////////////
    # /////////// GET CUSTOM WIDGETS TO APPLICATION ////////////////
    # //////////////////////////////////////////////////////////////

    # def get_tasks_table(self):
    #     return self.tasks_table
    #
    # def get_master_reset_button(self):
    #     return self.master_reset_button
    #
    # def get_maintenance_button(self):
    #     return self.maintenance_button
    #
    # def get_new_game_button(self):
    #     return self.new_game_button
    #
    # def get_lights_master_switch(self):
    #     return self.lights_master_switch
    #
    # def get_lights_table(self):
    #     return self.lights_table
    #
    # def get_sounds_table(self):
    #     return self.sounds_table
    #
    # def get_timer(self):
    #     return self.timer

    def get_connect_widget(self):
        return self.connect_widget

    def get_camera_widget(self):
        return self.camera_widget

    def get_range_sensor(self):
        return self.range_sensor

    def get_temperature_sensor(self):
        return self.tempeture_sensor

    def get_humidity_sensor(self):
        return self.humidity_sensor

    def get_backing_sensor(self):
        return self.backing_sensor
