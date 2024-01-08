# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
                            QMetaObject, QObject, QPoint, QRect,
                            QSize, QTime, QUrl, Qt, Signal)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QScrollArea, QSizePolicy,
    QStackedWidget, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    clicked = Signal(object)
    released = Signal(object)
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.verticalLayout_2 = QVBoxLayout(MainPages)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(3)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setStyleSheet(u"background: transparent;")
        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.tasks = QWidget()
        self.tasks.setObjectName(u"tasks")
        self.tasks.setGeometry(QRect(0, 0, 838, 578))
        self.tasks.setStyleSheet(u"background: transparent;")
        self.task_layout = QVBoxLayout(self.tasks)
        self.task_layout.setObjectName(u"task_layout")
        self.task_layout.setContentsMargins(5, 5, 5, 5)
        self.task_layout_row1 = QHBoxLayout()
        self.task_layout_row1.setObjectName(u"task_layout_row1")
        self.task_layout_row2 = QVBoxLayout()
        self.task_layout_row2.setContentsMargins(0, 20, 0, 0)
        self.task_layout_row2.setObjectName(u"task_layout_row2")
        self.task_layout.addLayout(self.task_layout_row1)
        self.task_layout.addLayout(self.task_layout_row2)

        self.task_grid_layout = QGridLayout()
        self.task_grid_layout.setObjectName(u"task_grid_layout")

        self.task_layout.addLayout(self.task_grid_layout)

        self.scrollArea.setWidget(self.tasks)

        self.page_1_layout.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.title_label)

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QVBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)


        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.scrollArea_2 = QScrollArea(self.page_3)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setStyleSheet(u"background: transparent;")
        self.scrollArea_2.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_2.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.scrollArea_2.setWidgetResizable(True)
        self.controls = QWidget()
        self.controls.setObjectName(u"controls")
        self.controls.setGeometry(QRect(0, 0, 824, 564))
        self.verticalLayout_4 = QVBoxLayout(self.controls)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.row1 = QHBoxLayout()
        self.row1.setObjectName(u"row1")

        self.verticalLayout_4.addLayout(self.row1)

        self.row2 = QVBoxLayout()
        self.row2.setObjectName(u"row2")

        self.verticalLayout_4.addLayout(self.row2)

        self.row3 = QVBoxLayout()
        self.row3.setObjectName(u"row3")

        self.verticalLayout_4.addLayout(self.row3)

        self.scrollArea_2.setWidget(self.controls)

        self.page_3_layout.addWidget(self.scrollArea_2)

        self.pages.addWidget(self.page_3)

        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"font-size: 14pt")
        self.page_4_layout = QVBoxLayout(self.page_4)
        self.page_4_layout.setSpacing(5)
        self.page_4_layout.setObjectName(u"page_4_layout")
        self.page_4_layout.setContentsMargins(5, 5, 5, 5)
        self.scrollArea_4 = QScrollArea(self.page_4)
        self.scrollArea_4.setObjectName(u"scrollArea_4")
        self.scrollArea_4.setAutoFillBackground(False)
        self.scrollArea_4.setStyleSheet(u"background: transparent;")
        self.scrollArea_4.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea_4.setWidgetResizable(True)
        self.tasks4 = QWidget()
        self.tasks4.setObjectName(u"tasks")
        self.tasks4.setGeometry(QRect(0, 0, 838, 578))
        self.tasks4.setStyleSheet(u"background: transparent;")
        self.task4_layout = QHBoxLayout()
        self.task4_layout.setObjectName(u"task_layout")
        self.task4_layout.setContentsMargins(5, 5, 5, 5)
        self.task4_layout_row1 = QHBoxLayout()
        self.task4_layout_row1.setObjectName(u"task4_layout_row1")

        self.page_4_layout.addLayout(self.task4_layout_row1)

        self.task4_layout_row2 = QHBoxLayout()
        self.task4_layout_row2.setObjectName(u"task4_layout_row2")

        self.page_4_layout.addLayout(self.task4_layout_row2)

        self.task4_layout_row3 = QVBoxLayout()
        self.task4_layout_row3.setObjectName(u"task4_layout_row3")

        self.page_4_layout.addLayout(self.task4_layout_row3)

        self.scrollArea_4.setWidget(self.tasks4)

        self.page_4_layout.addWidget(self.scrollArea_4)

        self.pages.addWidget(self.page_4)


        self.verticalLayout_2.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"Custom Widgets Page", None))
        self.description_label.setText(QCoreApplication.translate("MainPages", u"Here will be all the custom widgets, they will be added over time on this page.\n"
"I will try to always record a new tutorial when adding a new Widget and updating the project on Patreon before launching on GitHub and GitHub after the public release.", None))
    # retranslateUi

