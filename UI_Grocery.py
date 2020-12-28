# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'TathaStu_UI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
import pandas
from PIL import Image, ImageDraw, ImageFont
import textwrap
import json
from pathlib import Path

configFile = open('config.json')
pathData = json.load(configFile)

for details in pathData['params']:
    fsnFolder = details['fsnPath']
    logoFolder = details['logoPath']

# import tathastu_logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 800)
        MainWindow.setMaximumSize(QSize(800, 800))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        # Frame_1 Starts
        self.Frame_1 = QFrame(self.centralwidget)
        self.Frame_1.setObjectName(u"Frame_1")
        self.Frame_1.setGeometry(QRect(210, 110, 541, 591))
        self.Frame_1.setMaximumSize(QSize(600, 800))
        self.Frame_1.setStyleSheet(u"QFrame{\n"
"background-color: rgb(255, 255, 255);\n"
"border: 0;\n"
"border-radius:32px;\n"
"}")
        self.Frame_1.setFrameShape(QFrame.StyledPanel)
        self.Frame_1.setFrameShadow(QFrame.Plain)

        # Frame_2 Starts
        self.Frame_2 = QFrame(self.centralwidget)
        self.Frame_2.setObjectName(u"Frame_2")
        self.Frame_2.setGeometry(QRect(210, 110, 541, 591))
        self.Frame_2.setMaximumSize(QSize(600, 800))
        self.Frame_2.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border: 0;\n"
                                   "border-radius:32px;\n"
                                   "}")
        self.Frame_2.setFrameShape(QFrame.StyledPanel)
        self.Frame_2.setFrameShadow(QFrame.Plain)
        self.Frame_2.setVisible(False)

        # Frame_3 Starts
        self.Frame_3 = QFrame(self.centralwidget)
        self.Frame_3.setObjectName(u"Frame_3")
        self.Frame_3.setGeometry(QRect(210, 110, 541, 591))
        self.Frame_3.setMaximumSize(QSize(600, 800))
        self.Frame_3.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border: 0;\n"
                                   "border-radius:32px;\n"
                                   "}")
        self.Frame_3.setFrameShape(QFrame.StyledPanel)
        self.Frame_3.setFrameShadow(QFrame.Plain)
        self.Frame_3.setVisible(False)

        # Frame_4 Starts
        self.Frame_4 = QFrame(self.centralwidget)
        self.Frame_4.setObjectName(u"Frame_4")
        self.Frame_4.setGeometry(QRect(210, 110, 541, 591))
        self.Frame_4.setMaximumSize(QSize(600, 800))
        self.Frame_4.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border: 0;\n"
                                   "border-radius:32px;\n"
                                   "}")
        self.Frame_4.setFrameShape(QFrame.StyledPanel)
        self.Frame_4.setFrameShadow(QFrame.Plain)
        self.Frame_4.setVisible(False)

        # Frame_5 Starts
        self.Frame_5 = QFrame(self.centralwidget)
        self.Frame_5.setObjectName(u"Frame_5")
        self.Frame_5.setGeometry(QRect(210, 110, 541, 591))
        self.Frame_5.setMaximumSize(QSize(600, 800))
        self.Frame_5.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border: 0;\n"
                                   "border-radius:32px;\n"
                                   "}")
        self.Frame_5.setFrameShape(QFrame.StyledPanel)
        self.Frame_5.setFrameShadow(QFrame.Plain)
        self.Frame_5.setVisible(False)

        # Frame_6 Starts
        self.Frame_6 = QFrame(self.centralwidget)
        self.Frame_6.setObjectName(u"Frame_6")
        self.Frame_6.setGeometry(QRect(210, 110, 541, 591))
        self.Frame_6.setMaximumSize(QSize(600, 800))
        self.Frame_6.setStyleSheet(u"QFrame{\n"
                                   "background-color: rgb(255, 255, 255);\n"
                                   "border: 0;\n"
                                   "border-radius:32px;\n"
                                   "}")
        self.Frame_6.setFrameShape(QFrame.StyledPanel)
        self.Frame_6.setFrameShadow(QFrame.Plain)
        self.Frame_6.setVisible(False)

        # # Frame_7 Starts
        # self.Frame_7 = QFrame(self.centralwidget)
        # self.Frame_7.setObjectName(u"Frame_7")
        # self.Frame_7.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_7.setMaximumSize(QSize(600, 800))
        # self.Frame_7.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_7.setFrameShape(QFrame.StyledPanel)
        # self.Frame_7.setFrameShadow(QFrame.Plain)
        # self.Frame_7.setVisible(False)
        #
        # # Frame_8 Starts
        # self.Frame_8 = QFrame(self.centralwidget)
        # self.Frame_8.setObjectName(u"Frame_8")
        # self.Frame_8.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_8.setMaximumSize(QSize(600, 800))
        # self.Frame_8.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_8.setFrameShape(QFrame.StyledPanel)
        # self.Frame_8.setFrameShadow(QFrame.Plain)
        # self.Frame_8.setVisible(False)
        #
        # # Frame_9 Starts
        # self.Frame_9 = QFrame(self.centralwidget)
        # self.Frame_9.setObjectName(u"Frame_9")
        # self.Frame_9.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_9.setMaximumSize(QSize(600, 800))
        # self.Frame_9.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_9.setFrameShape(QFrame.StyledPanel)
        # self.Frame_9.setFrameShadow(QFrame.Plain)
        # self.Frame_9.setVisible(False)
        #
        # # Frame_10 Starts
        # self.Frame_10 = QFrame(self.centralwidget)
        # self.Frame_10.setObjectName(u"Frame_10")
        # self.Frame_10.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_10.setMaximumSize(QSize(600, 800))
        # self.Frame_10.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_10.setFrameShape(QFrame.StyledPanel)
        # self.Frame_10.setFrameShadow(QFrame.Plain)
        # self.Frame_10.setVisible(False)
        #
        # # Frame_11 Starts
        # self.Frame_11 = QFrame(self.centralwidget)
        # self.Frame_11.setObjectName(u"Frame_11")
        # self.Frame_11.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_11.setMaximumSize(QSize(600, 800))
        # self.Frame_11.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_11.setFrameShape(QFrame.StyledPanel)
        # self.Frame_11.setFrameShadow(QFrame.Plain)
        # self.Frame_11.setVisible(False)
        #
        # # Frame_12 Starts
        # self.Frame_12 = QFrame(self.centralwidget)
        # self.Frame_12.setObjectName(u"Frame_12")
        # self.Frame_12.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_12.setMaximumSize(QSize(600, 800))
        # self.Frame_12.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_12.setFrameShape(QFrame.StyledPanel)
        # self.Frame_12.setFrameShadow(QFrame.Plain)
        # self.Frame_12.setVisible(False)
        #
        # # Frame_13 Starts
        # self.Frame_13 = QFrame(self.centralwidget)
        # self.Frame_13.setObjectName(u"Frame_13")
        # self.Frame_13.setGeometry(QRect(210, 110, 541, 591))
        # self.Frame_13.setMaximumSize(QSize(600, 800))
        # self.Frame_13.setStyleSheet(u"QFrame{\n"
        #                            "background-color: rgb(255, 255, 255);\n"
        #                            "border: 0;\n"
        #                            "border-radius:32px;\n"
        #                            "}")
        # self.Frame_13.setFrameShape(QFrame.StyledPanel)
        # self.Frame_13.setFrameShadow(QFrame.Plain)
        # self.Frame_13.setVisible(False)

        # Select Background Button_1
        self.Select_BG_1 = QPushButton(self.Frame_1)
        self.Select_BG_1.setObjectName(u"Select_BG_1")
        self.Select_BG_1.setGeometry(QRect(70, 220, 201, 41))
        self.Select_BG_1.clicked.connect(self.FunctionBG1)
        self.Select_BG_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(21,200,232);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select Background Button_2
        self.Select_BG_2 = QPushButton(self.Frame_2)
        self.Select_BG_2.setObjectName(u"Select_BG_2")
        self.Select_BG_2.setGeometry(QRect(70, 220, 201, 41))
        self.Select_BG_2.clicked.connect(self.FunctionBG1)
        self.Select_BG_2.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "	border:2px solid rgb(21,200,232);\n"
                                       "	border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select Background Button_3
        self.Select_BG_3 = QPushButton(self.Frame_3)
        self.Select_BG_3.setObjectName(u"Select_BG_3")
        self.Select_BG_3.setGeometry(QRect(70, 220, 201, 41))
        self.Select_BG_3.clicked.connect(self.FunctionBG1)
        self.Select_BG_3.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "	border:2px solid rgb(21,200,232);\n"
                                       "	border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select Background Button_4
        self.Select_BG_4 = QPushButton(self.Frame_4)
        self.Select_BG_4.setObjectName(u"Select_BG_4")
        self.Select_BG_4.setGeometry(QRect(70, 220, 201, 41))
        self.Select_BG_4.clicked.connect(self.FunctionBG1)
        self.Select_BG_4.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "	border:2px solid rgb(21,200,232);\n"
                                       "	border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select Background Button_5
        self.Select_BG_5 = QPushButton(self.Frame_5)
        self.Select_BG_5.setObjectName(u"Select_BG_5")
        self.Select_BG_5.setGeometry(QRect(70, 220, 201, 41))
        self.Select_BG_5.clicked.connect(self.FunctionBG1)
        self.Select_BG_5.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "	border:2px solid rgb(21,200,232);\n"
                                       "	border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select Background Button_6
        self.Select_BG_6 = QPushButton(self.Frame_6)
        self.Select_BG_6.setObjectName(u"Select_BG_6")
        self.Select_BG_6.setGeometry(QRect(70, 220, 201, 41))
        self.Select_BG_6.clicked.connect(self.FunctionBG1)
        self.Select_BG_6.setStyleSheet(u"QPushButton{\n"
                                       "	background-color: rgb(255, 255, 255);\n"
                                       "	border:2px solid rgb(21,200,232);\n"
                                       "	border-radius:10px;\n"
                                       "}\n"
                                       "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # # Select Background Button_7
        # self.Select_BG_7 = QPushButton(self.Frame_7)
        # self.Select_BG_7.setObjectName(u"Select_BG_7")
        # self.Select_BG_7.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_7.clicked.connect(self.FunctionBG1)
        # self.Select_BG_7.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select Background Button_8
        # self.Select_BG_8 = QPushButton(self.Frame_8)
        # self.Select_BG_8.setObjectName(u"Select_BG_8")
        # self.Select_BG_8.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_8.clicked.connect(self.FunctionBG1)
        # self.Select_BG_8.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select Background Button_9
        # self.Select_BG_9 = QPushButton(self.Frame_9)
        # self.Select_BG_9.setObjectName(u"Select_BG_9")
        # self.Select_BG_9.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_9.clicked.connect(self.FunctionBG1)
        # self.Select_BG_9.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select Background Button_10
        # self.Select_BG_10 = QPushButton(self.Frame_10)
        # self.Select_BG_10.setObjectName(u"Select_BG_10")
        # self.Select_BG_10.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_10.clicked.connect(self.FunctionBG1)
        # self.Select_BG_10.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select Background Button_11
        # self.Select_BG_11 = QPushButton(self.Frame_11)
        # self.Select_BG_11.setObjectName(u"Select_BG_11")
        # self.Select_BG_11.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_11.clicked.connect(self.FunctionBG1)
        # self.Select_BG_11.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select Background Button_12
        # self.Select_BG_12 = QPushButton(self.Frame_12)
        # self.Select_BG_12.setObjectName(u"Select_BG_12")
        # self.Select_BG_12.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_12.clicked.connect(self.FunctionBG1)
        # self.Select_BG_12.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select Background Button_13
        # self.Select_BG_13 = QPushButton(self.Frame_13)
        # self.Select_BG_13.setObjectName(u"Select_BG_13")
        # self.Select_BG_13.setGeometry(QRect(70, 220, 201, 41))
        # self.Select_BG_13.clicked.connect(self.FunctionBG1)
        # self.Select_BG_13.setStyleSheet(u"QPushButton{\n"
        #                                "	background-color: rgb(255, 255, 255);\n"
        #                                "	border:2px solid rgb(21,200,232);\n"
        #                                "	border-radius:10px;\n"
        #                                "}\n"
        #                                "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select CSV File Button_1
        self.Select_CSV_1 = QPushButton(self.Frame_1)
        self.Select_CSV_1.setObjectName(u"Select_CSV_1")
        self.Select_CSV_1.setGeometry(QRect(70, 280, 201, 41))
        self.Select_CSV_1.clicked.connect(self.FunctionData1)
        self.Select_CSV_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(21,200,232);\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select CSV File Button_2
        self.Select_CSV_2 = QPushButton(self.Frame_2)
        self.Select_CSV_2.setObjectName(u"Select_CSV_2")
        self.Select_CSV_2.setGeometry(QRect(70, 280, 201, 41))
        self.Select_CSV_2.clicked.connect(self.FunctionData1)
        self.Select_CSV_2.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border:2px solid rgb(21,200,232);\n"
                                        "	border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select CSV File Button_3
        self.Select_CSV_3 = QPushButton(self.Frame_3)
        self.Select_CSV_3.setObjectName(u"Select_CSV_3")
        self.Select_CSV_3.setGeometry(QRect(70, 280, 201, 41))
        self.Select_CSV_3.clicked.connect(self.FunctionData1)
        self.Select_CSV_3.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border:2px solid rgb(21,200,232);\n"
                                        "	border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select CSV File Button_4
        self.Select_CSV_4 = QPushButton(self.Frame_4)
        self.Select_CSV_4.setObjectName(u"Select_CSV_4")
        self.Select_CSV_4.setGeometry(QRect(70, 280, 201, 41))
        self.Select_CSV_4.clicked.connect(self.FunctionData1)
        self.Select_CSV_4.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border:2px solid rgb(21,200,232);\n"
                                        "	border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select CSV File Button_5
        self.Select_CSV_5 = QPushButton(self.Frame_5)
        self.Select_CSV_5.setObjectName(u"Select_CSV_5")
        self.Select_CSV_5.setGeometry(QRect(70, 280, 201, 41))
        self.Select_CSV_5.clicked.connect(self.FunctionData1)
        self.Select_CSV_5.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border:2px solid rgb(21,200,232);\n"
                                        "	border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Select CSV File Button_6
        self.Select_CSV_6 = QPushButton(self.Frame_6)
        self.Select_CSV_6.setObjectName(u"Select_CSV_6")
        self.Select_CSV_6.setGeometry(QRect(70, 280, 201, 41))
        self.Select_CSV_6.clicked.connect(self.FunctionData1)
        self.Select_CSV_6.setStyleSheet(u"QPushButton{\n"
                                        "	background-color: rgb(255, 255, 255);\n"
                                        "	border:2px solid rgb(21,200,232);\n"
                                        "	border-radius:10px;\n"
                                        "}\n"
                                        "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # # Select CSV File Button_7
        # self.Select_CSV_7 = QPushButton(self.Frame_7)
        # self.Select_CSV_7.setObjectName(u"Select_CSV_7")
        # self.Select_CSV_7.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_7.clicked.connect(self.FunctionData1)
        # self.Select_CSV_7.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select CSV File Button_8
        # self.Select_CSV_8 = QPushButton(self.Frame_8)
        # self.Select_CSV_8.setObjectName(u"Select_CSV_8")
        # self.Select_CSV_8.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_8.clicked.connect(self.FunctionData1)
        # self.Select_CSV_8.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select CSV File Button_9
        # self.Select_CSV_9 = QPushButton(self.Frame_9)
        # self.Select_CSV_9.setObjectName(u"Select_CSV_9")
        # self.Select_CSV_9.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_9.clicked.connect(self.FunctionData1)
        # self.Select_CSV_9.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select CSV File Button_10
        # self.Select_CSV_10 = QPushButton(self.Frame_10)
        # self.Select_CSV_10.setObjectName(u"Select_CSV_10")
        # self.Select_CSV_10.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_10.clicked.connect(self.FunctionData1)
        # self.Select_CSV_10.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select CSV File Button_11
        # self.Select_CSV_11 = QPushButton(self.Frame_11)
        # self.Select_CSV_11.setObjectName(u"Select_CSV_11")
        # self.Select_CSV_11.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_11.clicked.connect(self.FunctionData1)
        # self.Select_CSV_11.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select CSV File Button_12
        # self.Select_CSV_12 = QPushButton(self.Frame_12)
        # self.Select_CSV_12.setObjectName(u"Select_CSV_12")
        # self.Select_CSV_12.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_12.clicked.connect(self.FunctionData1)
        # self.Select_CSV_12.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")
        #
        # # Select CSV File Button_13
        # self.Select_CSV_13 = QPushButton(self.Frame_13)
        # self.Select_CSV_13.setObjectName(u"Select_CSV_13")
        # self.Select_CSV_13.setGeometry(QRect(70, 280, 201, 41))
        # self.Select_CSV_13.clicked.connect(self.FunctionData1)
        # self.Select_CSV_13.setStyleSheet(u"QPushButton{\n"
        #                                 "	background-color: rgb(255, 255, 255);\n"
        #                                 "	border:2px solid rgb(21,200,232);\n"
        #                                 "	border-radius:10px;\n"
        #                                 "}\n"
        #                                 "QPushButton:pressed { background-color: rgb(230,250,250) }")

        # Generate Card Button_1
        self.Gen_Card_1 = QPushButton(self.Frame_1)
        self.Gen_Card_1.setObjectName(u"Gen_Card_1")
        self.Gen_Card_1.setGeometry(QRect(70, 340, 411, 51))
        self.Gen_Card_1.clicked.connect(self.FunctionGen1)
        self.Gen_Card_1.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(238, 196, 19);\n"
"border:0;\n"
"border-radius:10px;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(220,180,20) }\n"
"")

        # Generate Card Button_2
        self.Gen_Card_2 = QPushButton(self.Frame_2)
        self.Gen_Card_2.setObjectName(u"Gen_Card_2")
        self.Gen_Card_2.setGeometry(QRect(70, 340, 411, 51))
        self.Gen_Card_2.clicked.connect(self.FunctionGen2)
        self.Gen_Card_2.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(238, 196, 19);\n"
                                      "border:0;\n"
                                      "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
                                      "")

        # Generate Card Button_3
        self.Gen_Card_3 = QPushButton(self.Frame_3)
        self.Gen_Card_3.setObjectName(u"Gen_Card_3")
        self.Gen_Card_3.setGeometry(QRect(70, 340, 411, 51))
        self.Gen_Card_3.clicked.connect(self.FunctionGen3)
        self.Gen_Card_3.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(238, 196, 19);\n"
                                      "border:0;\n"
                                      "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
                                      "")

        # Generate Card Button_4
        self.Gen_Card_4 = QPushButton(self.Frame_4)
        self.Gen_Card_4.setObjectName(u"Gen_Card_4")
        self.Gen_Card_4.setGeometry(QRect(70, 340, 411, 51))
        self.Gen_Card_4.clicked.connect(self.FunctionGen4)
        self.Gen_Card_4.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(238, 196, 19);\n"
                                      "border:0;\n"
                                      "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
                                      "")

        # Generate Card Button_5
        self.Gen_Card_5 = QPushButton(self.Frame_5)
        self.Gen_Card_5.setObjectName(u"Gen_Card_5")
        self.Gen_Card_5.setGeometry(QRect(70, 340, 411, 51))
        self.Gen_Card_5.clicked.connect(self.FunctionGen5)
        self.Gen_Card_5.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(238, 196, 19);\n"
                                      "border:0;\n"
                                      "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
                                      "")

        # Generate Card Button_6
        self.Gen_Card_6 = QPushButton(self.Frame_6)
        self.Gen_Card_6.setObjectName(u"Gen_Card_6")
        self.Gen_Card_6.setGeometry(QRect(70, 340, 411, 51))
        self.Gen_Card_6.clicked.connect(self.FunctionGen6)
        self.Gen_Card_6.setStyleSheet(u"QPushButton{\n"
                                      "background-color: rgb(238, 196, 19);\n"
                                      "border:0;\n"
                                      "border-radius:10px;\n"
                                      "}\n"
                                      "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
                                      "")

        # # Generate Card Button_7
        # self.Gen_Card_7 = QPushButton(self.Frame_7)
        # self.Gen_Card_7.setObjectName(u"Gen_Card_7")
        # self.Gen_Card_7.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_7.clicked.connect(self.FunctionGen7)
        # self.Gen_Card_7.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")
        #
        # # Generate Card Button_8
        # self.Gen_Card_8 = QPushButton(self.Frame_8)
        # self.Gen_Card_8.setObjectName(u"Gen_Card_8")
        # self.Gen_Card_8.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_8.clicked.connect(self.FunctionGen8)
        # self.Gen_Card_8.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")
        #
        # # Generate Card Button_9
        # self.Gen_Card_9 = QPushButton(self.Frame_9)
        # self.Gen_Card_9.setObjectName(u"Gen_Card_9")
        # self.Gen_Card_9.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_9.clicked.connect(self.FunctionGen9)
        # self.Gen_Card_9.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")
        #
        # # Generate Card Button_10
        # self.Gen_Card_10 = QPushButton(self.Frame_10)
        # self.Gen_Card_10.setObjectName(u"Gen_Card_10")
        # self.Gen_Card_10.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_10.clicked.connect(self.FunctionGen10)
        # self.Gen_Card_10.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")
        #
        # # Generate Card Button_11
        # self.Gen_Card_11 = QPushButton(self.Frame_11)
        # self.Gen_Card_11.setObjectName(u"Gen_Card_11")
        # self.Gen_Card_11.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_11.clicked.connect(self.FunctionGen11)
        # self.Gen_Card_11.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")
        #
        # # Generate Card Button_12
        # self.Gen_Card_12 = QPushButton(self.Frame_12)
        # self.Gen_Card_12.setObjectName(u"Gen_Card_12")
        # self.Gen_Card_12.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_12.clicked.connect(self.FunctionGen12)
        # self.Gen_Card_12.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")
        #
        # # Generate Card Button_13
        # self.Gen_Card_13 = QPushButton(self.Frame_13)
        # self.Gen_Card_13.setObjectName(u"Gen_Card_13")
        # self.Gen_Card_13.setGeometry(QRect(70, 340, 411, 51))
        # self.Gen_Card_13.clicked.connect(self.FunctionGen13)
        # self.Gen_Card_13.setStyleSheet(u"QPushButton{\n"
        #                               "background-color: rgb(238, 196, 19);\n"
        #                               "border:0;\n"
        #                               "border-radius:10px;\n"
        #                               "}\n"
        #                               "QPushButton:pressed { background-color: rgb(220,180,20) }\n"
        #                               "")

        # Title and Label_1
        self.Card_Label_1 = QLabel(self.Frame_1)
        self.Card_Label_1.setObjectName(u"Card_Label_1")
        self.Card_Label_1.setGeometry(QRect(100, 50, 341, 41))
        self.Card_Label_1.setLayoutDirection(Qt.RightToLeft)
        self.Card_Label_1.setStyleSheet(u"font: 20pt \"Roboto\";")
        self.Card_Label_1.setFrameShape(QFrame.NoFrame)
        self.Card_Label_1.setAlignment(Qt.AlignCenter)

        # Title and Label_2
        self.Card_Label_2 = QLabel(self.Frame_2)
        self.Card_Label_2.setObjectName(u"Card_Label_2")
        self.Card_Label_2.setGeometry(QRect(100, 50, 341, 41))
        self.Card_Label_2.setLayoutDirection(Qt.RightToLeft)
        self.Card_Label_2.setStyleSheet(u"font: 20pt \"Roboto\";")
        self.Card_Label_2.setFrameShape(QFrame.NoFrame)
        self.Card_Label_2.setAlignment(Qt.AlignCenter)

        # Title and Label_3
        self.Card_Label_3 = QLabel(self.Frame_3)
        self.Card_Label_3.setObjectName(u"Card_Label_3")
        self.Card_Label_3.setGeometry(QRect(100, 50, 341, 41))
        self.Card_Label_3.setLayoutDirection(Qt.RightToLeft)
        self.Card_Label_3.setStyleSheet(u"font: 20pt \"Roboto\";")
        self.Card_Label_3.setFrameShape(QFrame.NoFrame)
        self.Card_Label_3.setAlignment(Qt.AlignCenter)

        # Title and Label_4
        self.Card_Label_4 = QLabel(self.Frame_4)
        self.Card_Label_4.setObjectName(u"Card_Label_4")
        self.Card_Label_4.setGeometry(QRect(100, 50, 341, 41))
        self.Card_Label_4.setLayoutDirection(Qt.RightToLeft)
        self.Card_Label_4.setStyleSheet(u"font: 20pt \"Roboto\";")
        self.Card_Label_4.setFrameShape(QFrame.NoFrame)
        self.Card_Label_4.setAlignment(Qt.AlignCenter)

        # Title and Label_5
        self.Card_Label_5 = QLabel(self.Frame_5)
        self.Card_Label_5.setObjectName(u"Card_Label_5")
        self.Card_Label_5.setGeometry(QRect(100, 50, 341, 41))
        self.Card_Label_5.setLayoutDirection(Qt.RightToLeft)
        self.Card_Label_5.setStyleSheet(u"font: 20pt \"Roboto\";")
        self.Card_Label_5.setFrameShape(QFrame.NoFrame)
        self.Card_Label_5.setAlignment(Qt.AlignCenter)

        # Title and Label_6
        self.Card_Label_6 = QLabel(self.Frame_6)
        self.Card_Label_6.setObjectName(u"Card_Label_6")
        self.Card_Label_6.setGeometry(QRect(100, 50, 341, 41))
        self.Card_Label_6.setLayoutDirection(Qt.RightToLeft)
        self.Card_Label_6.setStyleSheet(u"font: 20pt \"Roboto\";")
        self.Card_Label_6.setFrameShape(QFrame.NoFrame)
        self.Card_Label_6.setAlignment(Qt.AlignCenter)

        # # Title and Label_7
        # self.Card_Label_7 = QLabel(self.Frame_7)
        # self.Card_Label_7.setObjectName(u"Card_Label_7")
        # self.Card_Label_7.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_7.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_7.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_7.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_7.setAlignment(Qt.AlignCenter)
        #
        # # Title and Label_8
        # self.Card_Label_8 = QLabel(self.Frame_8)
        # self.Card_Label_8.setObjectName(u"Card_Label_8")
        # self.Card_Label_8.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_8.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_8.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_8.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_8.setAlignment(Qt.AlignCenter)
        #
        # # Title and Label_9
        # self.Card_Label_9 = QLabel(self.Frame_9)
        # self.Card_Label_9.setObjectName(u"Card_Label_9")
        # self.Card_Label_9.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_9.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_9.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_9.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_9.setAlignment(Qt.AlignCenter)
        #
        # # Title and Label_10
        # self.Card_Label_10 = QLabel(self.Frame_10)
        # self.Card_Label_10.setObjectName(u"Card_Label_10")
        # self.Card_Label_10.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_10.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_10.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_10.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_10.setAlignment(Qt.AlignCenter)
        #
        # # Title and Label_11
        # self.Card_Label_11 = QLabel(self.Frame_11)
        # self.Card_Label_11.setObjectName(u"Card_Label_11")
        # self.Card_Label_11.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_11.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_11.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_11.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_11.setAlignment(Qt.AlignCenter)
        #
        # # Title and Label_12
        # self.Card_Label_12 = QLabel(self.Frame_12)
        # self.Card_Label_12.setObjectName(u"Card_Label_12")
        # self.Card_Label_12.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_12.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_12.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_12.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_12.setAlignment(Qt.AlignCenter)
        #
        # # Title and Label_13
        # self.Card_Label_13 = QLabel(self.Frame_13)
        # self.Card_Label_13.setObjectName(u"Card_Label_13")
        # self.Card_Label_13.setGeometry(QRect(100, 50, 341, 41))
        # self.Card_Label_13.setLayoutDirection(Qt.RightToLeft)
        # self.Card_Label_13.setStyleSheet(u"font: 20pt \"Roboto\";")
        # self.Card_Label_13.setFrameShape(QFrame.NoFrame)
        # self.Card_Label_13.setAlignment(Qt.AlignCenter)

        # Vernac List_1
        self.Select_Vernac_1 = QListWidget(self.Frame_1)
        __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_1)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_1)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_1)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_1)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_1)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Select_Vernac_1.setObjectName(u"Select_Vernac_1")
        self.Select_Vernac_1.setGeometry(QRect(290, 220, 181, 101))
        self.Select_Vernac_1.itemClicked.connect(self.GetVernac1)
        self.Select_Vernac_1.setStyleSheet(u"QListWidget{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border:2px solid rgb(21,200,232);\n"
"	border-radius:10px;\n"
"}")
        # Vernac List_2
        self.Select_Vernac_2 = QListWidget(self.Frame_2)
        __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_2)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_2)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_2)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_2)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_2)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Select_Vernac_2.setObjectName(u"Select_Vernac_2")
        self.Select_Vernac_2.setGeometry(QRect(290, 220, 181, 101))
        self.Select_Vernac_2.itemClicked.connect(self.GetVernac2)
        self.Select_Vernac_2.setStyleSheet(u"QListWidget{\n"
                                           "	background-color: rgb(255, 255, 255);\n"
                                           "	border:2px solid rgb(21,200,232);\n"
                                           "	border-radius:10px;\n"
                                           "}")

        # Vernac List_3
        self.Select_Vernac_3 = QListWidget(self.Frame_3)
        __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_3)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_3)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_3)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_3)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_3)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Select_Vernac_3.setObjectName(u"Select_Vernac_3")
        self.Select_Vernac_3.setGeometry(QRect(290, 220, 181, 101))
        self.Select_Vernac_3.itemClicked.connect(self.GetVernac3)
        self.Select_Vernac_3.setStyleSheet(u"QListWidget{\n"
                                           "	background-color: rgb(255, 255, 255);\n"
                                           "	border:2px solid rgb(21,200,232);\n"
                                           "	border-radius:10px;\n"
                                           "}")

        # Vernac List_4
        self.Select_Vernac_4 = QListWidget(self.Frame_4)
        __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_4)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_4)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_4)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_4)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_4)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Select_Vernac_4.setObjectName(u"Select_Vernac_4")
        self.Select_Vernac_4.setGeometry(QRect(290, 220, 181, 101))
        self.Select_Vernac_4.itemClicked.connect(self.GetVernac4)
        self.Select_Vernac_4.setStyleSheet(u"QListWidget{\n"
                                           "	background-color: rgb(255, 255, 255);\n"
                                           "	border:2px solid rgb(21,200,232);\n"
                                           "	border-radius:10px;\n"
                                           "}")

        # Vernac List_5
        self.Select_Vernac_5 = QListWidget(self.Frame_5)
        __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_5)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_5)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_5)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_5)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_5)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Select_Vernac_5.setObjectName(u"Select_Vernac_5")
        self.Select_Vernac_5.setGeometry(QRect(290, 220, 181, 101))
        self.Select_Vernac_5.itemClicked.connect(self.GetVernac5)
        self.Select_Vernac_5.setStyleSheet(u"QListWidget{\n"
                                           "	background-color: rgb(255, 255, 255);\n"
                                           "	border:2px solid rgb(21,200,232);\n"
                                           "	border-radius:10px;\n"
                                           "}")

        # Vernac List_6
        self.Select_Vernac_6 = QListWidget(self.Frame_6)
        __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_6)
        __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_6)
        __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_6)
        __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_6)
        __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_6)
        __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        self.Select_Vernac_6.setObjectName(u"Select_Vernac_6")
        self.Select_Vernac_6.setGeometry(QRect(290, 220, 181, 101))
        self.Select_Vernac_6.itemClicked.connect(self.GetVernac6)
        self.Select_Vernac_6.setStyleSheet(u"QListWidget{\n"
                                           "	background-color: rgb(255, 255, 255);\n"
                                           "	border:2px solid rgb(21,200,232);\n"
                                           "	border-radius:10px;\n"
                                           "}")

        # # Vernac List_7
        # self.Select_Vernac_7 = QListWidget(self.Frame_7)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_7)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_7)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_7)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_7)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_7)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_7.setObjectName(u"Select_Vernac_7")
        # self.Select_Vernac_7.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_7.itemClicked.connect(self.GetVernac7)
        # self.Select_Vernac_7.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")
        #
        # # Vernac List_8
        # self.Select_Vernac_8 = QListWidget(self.Frame_8)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_8)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_8)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_8)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_8)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_8)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_8.setObjectName(u"Select_Vernac_8")
        # self.Select_Vernac_8.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_8.itemClicked.connect(self.GetVernac8)
        # self.Select_Vernac_8.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")
        #
        # # Vernac List_9
        # self.Select_Vernac_9 = QListWidget(self.Frame_9)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_9)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_9)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_9)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_9)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_9)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_9.setObjectName(u"Select_Vernac_9")
        # self.Select_Vernac_9.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_9.itemClicked.connect(self.GetVernac9)
        # self.Select_Vernac_9.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")
        #
        # # Vernac List_10
        # self.Select_Vernac_10 = QListWidget(self.Frame_10)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_10)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_10)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_10)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_10)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_10)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_10.setObjectName(u"Select_Vernac_10")
        # self.Select_Vernac_10.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_10.itemClicked.connect(self.GetVernac10)
        # self.Select_Vernac_10.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")
        #
        # # Vernac List_11
        # self.Select_Vernac_11 = QListWidget(self.Frame_11)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_11)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_11)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_11)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_11)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_11)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_11.setObjectName(u"Select_Vernac_11")
        # self.Select_Vernac_11.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_11.itemClicked.connect(self.GetVernac11)
        # self.Select_Vernac_11.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")
        #
        # # Vernac List_12
        # self.Select_Vernac_12 = QListWidget(self.Frame_12)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_12)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_12)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_12)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_12)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_12)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_12.setObjectName(u"Select_Vernac_12")
        # self.Select_Vernac_12.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_12.itemClicked.connect(self.GetVernac12)
        # self.Select_Vernac_12.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")
        #
        # # Vernac List_13
        # self.Select_Vernac_13 = QListWidget(self.Frame_13)
        # __qlistwidgetitem = QListWidgetItem(self.Select_Vernac_13)
        # __qlistwidgetitem.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem1 = QListWidgetItem(self.Select_Vernac_13)
        # __qlistwidgetitem1.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem2 = QListWidgetItem(self.Select_Vernac_13)
        # __qlistwidgetitem2.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem3 = QListWidgetItem(self.Select_Vernac_13)
        # __qlistwidgetitem3.setTextAlignment(Qt.AlignCenter);
        # __qlistwidgetitem4 = QListWidgetItem(self.Select_Vernac_13)
        # __qlistwidgetitem4.setTextAlignment(Qt.AlignCenter);
        # self.Select_Vernac_13.setObjectName(u"Select_Vernac_13")
        # self.Select_Vernac_13.setGeometry(QRect(290, 220, 181, 101))
        # self.Select_Vernac_13.itemClicked.connect(self.GetVernac13)
        # self.Select_Vernac_13.setStyleSheet(u"QListWidget{\n"
        #                                    "	background-color: rgb(255, 255, 255);\n"
        #                                    "	border:2px solid rgb(21,200,232);\n"
        #                                    "	border-radius:10px;\n"
        #                                    "}")

        self.Left_Frame = QFrame(self.centralwidget)
        self.Left_Frame.setObjectName(u"Left_Frame")
        self.Left_Frame.setGeometry(QRect(-1, 159, 250, 641))
        self.Left_Frame.setMaximumSize(QSize(250, 800))
        self.Left_Frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(200, 236, 242);\n"
"border:0;\n"
"}")
        self.Left_Frame.setFrameShape(QFrame.StyledPanel)
        self.Left_Frame.setFrameShadow(QFrame.Raised)
        self.Button_1 = QPushButton(self.Left_Frame)
        self.Button_1.setObjectName(u"Button_1")
        self.Button_1.setGeometry(QRect(0, 0, 211, 40))
        self.Button_1.setMaximumSize(QSize(220, 40))
        self.Button_1.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(200, 236, 242);\n"
"	border:0;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(165,225,240) }")
        self.Button_2 = QPushButton(self.Left_Frame)
        self.Button_2.setObjectName(u"Button_2")
        self.Button_2.setGeometry(QRect(-10, 40, 220, 40))
        self.Button_2.setMinimumSize(QSize(220, 40))
        self.Button_2.setMaximumSize(QSize(220, 40))
        self.Button_2.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border:0;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(210,220,220) }")
        self.Button_3 = QPushButton(self.Left_Frame)
        self.Button_3.setObjectName(u"Button_3")
        self.Button_3.setGeometry(QRect(-10, 80, 220, 40))
        self.Button_3.setMinimumSize(QSize(220, 40))
        self.Button_3.setMaximumSize(QSize(220, 40))
        self.Button_3.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(200, 236, 242);\n"
"	border:0;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(165,225,240) }")
        self.Button_4 = QPushButton(self.Left_Frame)
        self.Button_4.setObjectName(u"Button_4")
        self.Button_4.setGeometry(QRect(-10, 120, 220, 40))
        self.Button_4.setMinimumSize(QSize(220, 40))
        self.Button_4.setMaximumSize(QSize(220, 40))
        self.Button_4.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border:0;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(210,220,220) }")
        self.Button_5 = QPushButton(self.Left_Frame)
        self.Button_5.setObjectName(u"Button_5")
        self.Button_5.setGeometry(QRect(-10, 160, 220, 40))
        self.Button_5.setMinimumSize(QSize(220, 40))
        self.Button_5.setMaximumSize(QSize(220, 40))
        self.Button_5.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(200, 236, 242);\n"
"	border:0;\n"
"}\n"
"QPushButton:pressed { background-color: rgb(165,225,240) }")
        self.Button_6 = QPushButton(self.Left_Frame)
        self.Button_6.setObjectName(u"Button_6")
        self.Button_6.setGeometry(QRect(-10, 200, 220, 40))
        self.Button_6.setMinimumSize(QSize(220, 40))
        self.Button_6.setMaximumSize(QSize(220, 40))
        self.Button_6.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(240, 240, 240);\n"
"	border:0;\n"
"}\n"
# "QPushButton:pressed { background-color: rgb(210,220,220) }")
#         self.Button_7 = QPushButton(self.Left_Frame)
#         self.Button_7.setObjectName(u"Button_7")
#         self.Button_7.setGeometry(QRect(-10, 240, 220, 40))
#         self.Button_7.setMinimumSize(QSize(220, 40))
#         self.Button_7.setMaximumSize(QSize(220, 40))
#         self.Button_7.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(200, 236, 242);\n"
# "	border:0;\n"
# "}\n"
# "QPushButton:pressed { background-color: rgb(165,225,240) }")
#         self.Button_8 = QPushButton(self.Left_Frame)
#         self.Button_8.setObjectName(u"Button_8")
#         self.Button_8.setGeometry(QRect(-10, 280, 220, 40))
#         self.Button_8.setMinimumSize(QSize(220, 40))
#         self.Button_8.setMaximumSize(QSize(220, 40))
#         self.Button_8.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(240, 240, 240);\n"
# "	border:0;\n"
# "}\n"
# "QPushButton:pressed { background-color: rgb(210,220,220) }")
#         self.Button_9 = QPushButton(self.Left_Frame)
#         self.Button_9.setObjectName(u"Button_9")
#         self.Button_9.setGeometry(QRect(-10, 320, 220, 40))
#         self.Button_9.setMinimumSize(QSize(220, 40))
#         self.Button_9.setMaximumSize(QSize(220, 40))
#         self.Button_9.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(200, 236, 242);\n"
# "	border:0;\n"
# "}\n"
# "QPushButton:pressed { background-color: rgb(165,225,240) }")
#         self.Button_10 = QPushButton(self.Left_Frame)
#         self.Button_10.setObjectName(u"Button_10")
#         self.Button_10.setGeometry(QRect(-10, 360, 220, 40))
#         self.Button_10.setMinimumSize(QSize(220, 40))
#         self.Button_10.setMaximumSize(QSize(220, 40))
#         self.Button_10.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(240, 240, 240);\n"
# "	border:0;\n"
# "}\n"
# "QPushButton:pressed { background-color: rgb(210,220,220) }")
#         self.Button_11 = QPushButton(self.Left_Frame)
#         self.Button_11.setObjectName(u"Button_11")
#         self.Button_11.setGeometry(QRect(-10, 400, 220, 40))
#         self.Button_11.setMinimumSize(QSize(220, 40))
#         self.Button_11.setMaximumSize(QSize(220, 40))
#         self.Button_11.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(200, 236, 242);\n"
# "	border:0;\n"
# "}\n"
# "QPushButton:pressed { background-color: rgb(165,225,240) }")
#         self.Button_12 = QPushButton(self.Left_Frame)
#         self.Button_12.setObjectName(u"Button_12")
#         self.Button_12.setGeometry(QRect(-10, 440, 220, 40))
#         self.Button_12.setMinimumSize(QSize(220, 40))
#         self.Button_12.setMaximumSize(QSize(220, 40))
#         self.Button_12.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(240, 240, 240);\n"
# "	border:0;\n"
# "}\n"
# "QPushButton:pressed { background-color: rgb(210,220,220) }")
#         self.Button_13 = QPushButton(self.Left_Frame)
#         self.Button_13.setObjectName(u"Button_13")
#         self.Button_13.setGeometry(QRect(-10, 480, 220, 40))
#         self.Button_13.setMinimumSize(QSize(220, 40))
#         self.Button_13.setMaximumSize(QSize(220, 40))
#         self.Button_13.setStyleSheet(u"QPushButton{\n"
# "	background-color: rgb(200, 236, 242);\n"
# "	border:0;\n"
# "}\n"
"QPushButton:pressed { background-color: rgb(165,225,240) }")
        self.BG_Remove = QPushButton(self.centralwidget)
        self.BG_Remove.setObjectName(u"BG_Remove")
        self.BG_Remove.setGeometry(QRect(710, 730, 40, 40))
        self.BG_Remove.setMinimumSize(QSize(40, 40))
        self.BG_Remove.setMaximumSize(QSize(40, 40))
        self.BG_Remove.setStyleSheet(u"QPushButton{\n"
"	font: 18pt \"Roboto\";\n"
"	background-color: rgb(21,200,232);\n"
"	border:0px;\n"
"	border-radius:10px;\n"
"}")
        self.FSN_Button = QPushButton(self.centralwidget)
        self.FSN_Button.setObjectName(u"FSN_Button")
        self.FSN_Button.setGeometry(QRect(650, 730, 40, 40))
        self.FSN_Button.setMinimumSize(QSize(40, 40))
        self.FSN_Button.setMaximumSize(QSize(40, 40))
        self.FSN_Button.setStyleSheet(u"QPushButton{\n"
"	font: 18pt \"Roboto\";\n"
"	background-color: rgb(21,200,232);\n"
"	border:0px;\n"
"	border-radius:10px;\n"
"}t")
        self.Top_Frame = QFrame(self.centralwidget)
        self.Top_Frame.setObjectName(u"Top_Frame")
        self.Top_Frame.setGeometry(QRect(0, 0, 800, 161))
        self.Top_Frame.setMaximumSize(QSize(800, 800))
        self.Top_Frame.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(21, 200, 232);\n"
"	border:0;\n"
"}")
        self.Top_Frame.setFrameShape(QFrame.StyledPanel)
        self.Top_Frame.setFrameShadow(QFrame.Plain)
        self.Logo_Label = QLabel(self.Top_Frame)
        self.Logo_Label.setObjectName(u"Logo_Label")
        self.Logo_Label.setGeometry(QRect(20, 20, 271, 100))
        self.Category_Label = QLabel(self.Top_Frame)
        self.Category_Label.setObjectName(u"Category_Label")
        self.Category_Label.setGeometry(QRect(670, 90, 60, 16))
        self.Category_Label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.Right_Frame = QFrame(self.centralwidget)
        self.Right_Frame.setObjectName(u"Right_Frame")
        self.Right_Frame.setGeometry(QRect(250, 160, 551, 641))
        self.Right_Frame.setMaximumSize(QSize(2000, 2000))
        self.Right_Frame.setStyleSheet(u"QFrame{\n"
"background-color: rgb(240, 240, 240);\n"
"border:0;\n"
"}")
        self.Right_Frame.setFrameShape(QFrame.StyledPanel)
        self.Right_Frame.setFrameShadow(QFrame.Plain)
        MainWindow.setCentralWidget(self.centralwidget)
        self.Right_Frame.raise_()
        self.Top_Frame.raise_()
        self.Left_Frame.raise_()
        self.Frame_1.raise_()
        self.Frame_2.raise_()
        self.Frame_3.raise_()
        self.Frame_4.raise_()
        self.Frame_5.raise_()
        self.Frame_6.raise_()
        # self.Frame_7.raise_()
        # self.Frame_8.raise_()
        # self.Frame_9.raise_()
        # self.Frame_10.raise_()
        # self.Frame_11.raise_()
        # self.Frame_12.raise_()
        # self.Frame_13.raise_()
        self.BG_Remove.raise_()
        self.FSN_Button.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TathaStu v1.01 (Muladhara)", None))
#if QT_CONFIG(tooltip)
        self.Select_BG_1.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - cmd+b", None))
#endif // QT_CONFIG(tooltip)
        self.Select_BG_1.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        self.Select_BG_2.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        self.Select_BG_3.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        self.Select_BG_4.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        self.Select_BG_5.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        self.Select_BG_6.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_7.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_8.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_9.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_10.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_11.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_12.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
        # self.Select_BG_13.setText(QCoreApplication.translate("MainWindow", u"Select Background", None))
#if QT_CONFIG(shortcut)
        self.Select_BG_1.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+B", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Select_CSV_1.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - cmd+d", None))
#endif // QT_CONFIG(tooltip)
        self.Select_CSV_1.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        self.Select_CSV_2.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        self.Select_CSV_3.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        self.Select_CSV_4.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        self.Select_CSV_5.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        self.Select_CSV_6.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_7.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_8.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_9.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_10.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_11.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_12.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
        # self.Select_CSV_13.setText(QCoreApplication.translate("MainWindow", u"Select CSV File", None))
#if QT_CONFIG(shortcut)
        self.Select_CSV_1.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+D", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Gen_Card_1.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - cmd+g", None))
#endif // QT_CONFIG(tooltip)
        self.Gen_Card_1.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 1", None))
        self.Gen_Card_2.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 2", None))
        self.Gen_Card_3.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 3", None))
        self.Gen_Card_4.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 4", None))
        self.Gen_Card_5.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 5", None))
        self.Gen_Card_6.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 6", None))
        # self.Gen_Card_7.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives  7", None))
        # self.Gen_Card_8.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 8", None))
        # self.Gen_Card_9.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 9", None))
        # self.Gen_Card_10.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 10", None))
        # self.Gen_Card_11.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 11", None))
        # self.Gen_Card_12.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 12", None))
        # self.Gen_Card_13.setText(QCoreApplication.translate("MainWindow", u"Generate Creatives 13", None))
#if QT_CONFIG(shortcut)
        self.Gen_Card_1.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+G", None))
#endif // QT_CONFIG(shortcut)
        self.Card_Label_1.setText(QCoreApplication.translate("MainWindow", u"Generate Grab or Gone", None))
        self.Card_Label_2.setText(QCoreApplication.translate("MainWindow", u"Generate Don't Miss Out", None))
        self.Card_Label_3.setText(QCoreApplication.translate("MainWindow", u"Generate Smaller X2 (720x720)", None))
        self.Card_Label_4.setText(QCoreApplication.translate("MainWindow", u"DT-X3", None))
        self.Card_Label_5.setText(QCoreApplication.translate("MainWindow", u"DT Flex", None))
        self.Card_Label_6.setText(QCoreApplication.translate("MainWindow", u"3Grid FoZ", None))
        # self.Card_Label_7.setText(QCoreApplication.translate("MainWindow", u"Generate Flex (1440x560)", None))
        # self.Card_Label_8.setText(QCoreApplication.translate("MainWindow", u"Generate Flex (1440x640)", None))
        # self.Card_Label_9.setText(QCoreApplication.translate("MainWindow", u"Generate L1 App 1Grid", None))
        # self.Card_Label_10.setText(QCoreApplication.translate("MainWindow", u"Generate DT X3", None))
        # self.Card_Label_11.setText(QCoreApplication.translate("MainWindow", u"Generate Intrigue Silver (640x720)", None))
        # self.Card_Label_12.setText(QCoreApplication.translate("MainWindow", u"Generate Intrigue Flash Silver", None))
        # self.Card_Label_13.setText(QCoreApplication.translate("MainWindow", u"Generate Intrigue 2Grid (720x720)", None))

        # Vernac Options_1
        __sortingEnabled = self.Select_Vernac_1.isSortingEnabled()
        self.Select_Vernac_1.setSortingEnabled(False)
        ___qlistwidgetitem = self.Select_Vernac_1.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qlistwidgetitem1 = self.Select_Vernac_1.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        ___qlistwidgetitem2 = self.Select_Vernac_1.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        ___qlistwidgetitem3 = self.Select_Vernac_1.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        ___qlistwidgetitem4 = self.Select_Vernac_1.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        self.Select_Vernac_1.setSortingEnabled(__sortingEnabled)

        # Vernac Options_2
        __sortingEnabled = self.Select_Vernac_2.isSortingEnabled()
        self.Select_Vernac_2.setSortingEnabled(False)
        ___qlistwidgetitem = self.Select_Vernac_2.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qlistwidgetitem1 = self.Select_Vernac_2.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        ___qlistwidgetitem2 = self.Select_Vernac_2.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        ___qlistwidgetitem3 = self.Select_Vernac_2.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        ___qlistwidgetitem4 = self.Select_Vernac_2.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        self.Select_Vernac_2.setSortingEnabled(__sortingEnabled)

        # Vernac Options_3
        __sortingEnabled = self.Select_Vernac_3.isSortingEnabled()
        self.Select_Vernac_3.setSortingEnabled(False)
        ___qlistwidgetitem = self.Select_Vernac_3.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qlistwidgetitem1 = self.Select_Vernac_3.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        ___qlistwidgetitem2 = self.Select_Vernac_3.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        ___qlistwidgetitem3 = self.Select_Vernac_3.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        ___qlistwidgetitem4 = self.Select_Vernac_3.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        self.Select_Vernac_3.setSortingEnabled(__sortingEnabled)

        # Vernac Options_4
        __sortingEnabled = self.Select_Vernac_4.isSortingEnabled()
        self.Select_Vernac_4.setSortingEnabled(False)
        ___qlistwidgetitem = self.Select_Vernac_4.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qlistwidgetitem1 = self.Select_Vernac_4.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        ___qlistwidgetitem2 = self.Select_Vernac_4.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        ___qlistwidgetitem3 = self.Select_Vernac_4.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        ___qlistwidgetitem4 = self.Select_Vernac_4.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        self.Select_Vernac_4.setSortingEnabled(__sortingEnabled)

        # Vernac Options_5
        __sortingEnabled = self.Select_Vernac_5.isSortingEnabled()
        self.Select_Vernac_5.setSortingEnabled(False)
        ___qlistwidgetitem = self.Select_Vernac_5.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qlistwidgetitem1 = self.Select_Vernac_5.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        ___qlistwidgetitem2 = self.Select_Vernac_5.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        ___qlistwidgetitem3 = self.Select_Vernac_5.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        ___qlistwidgetitem4 = self.Select_Vernac_5.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        self.Select_Vernac_5.setSortingEnabled(__sortingEnabled)

        # Vernac Options_6
        __sortingEnabled = self.Select_Vernac_6.isSortingEnabled()
        self.Select_Vernac_6.setSortingEnabled(False)
        ___qlistwidgetitem = self.Select_Vernac_6.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        ___qlistwidgetitem1 = self.Select_Vernac_6.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        ___qlistwidgetitem2 = self.Select_Vernac_6.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        ___qlistwidgetitem3 = self.Select_Vernac_6.item(3)
        ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        ___qlistwidgetitem4 = self.Select_Vernac_6.item(4)
        ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        self.Select_Vernac_6.setSortingEnabled(__sortingEnabled)

        # # Vernac Options_7
        # __sortingEnabled = self.Select_Vernac_7.isSortingEnabled()
        # self.Select_Vernac_7.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_7.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_7.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_7.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_7.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_7.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_7.setSortingEnabled(__sortingEnabled)
        #
        # # Vernac Options_8
        # __sortingEnabled = self.Select_Vernac_8.isSortingEnabled()
        # self.Select_Vernac_8.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_8.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_8.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_8.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_8.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_8.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_8.setSortingEnabled(__sortingEnabled)
        #
        # # Vernac Options_9
        # __sortingEnabled = self.Select_Vernac_9.isSortingEnabled()
        # self.Select_Vernac_9.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_9.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_9.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_9.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_9.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_9.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_9.setSortingEnabled(__sortingEnabled)
        #
        # # Vernac Options_10
        # __sortingEnabled = self.Select_Vernac_10.isSortingEnabled()
        # self.Select_Vernac_10.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_10.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_10.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_10.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_10.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_10.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_10.setSortingEnabled(__sortingEnabled)
        #
        # # Vernac Options_11
        # __sortingEnabled = self.Select_Vernac_11.isSortingEnabled()
        # self.Select_Vernac_11.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_11.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_11.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_11.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_11.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_11.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_11.setSortingEnabled(__sortingEnabled)
        #
        # # Vernac Options_12
        # __sortingEnabled = self.Select_Vernac_12.isSortingEnabled()
        # self.Select_Vernac_12.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_12.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_12.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_12.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_12.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_12.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_12.setSortingEnabled(__sortingEnabled)
        #
        # # Vernac Options_13
        # __sortingEnabled = self.Select_Vernac_13.isSortingEnabled()
        # self.Select_Vernac_13.setSortingEnabled(False)
        # ___qlistwidgetitem = self.Select_Vernac_13.item(0)
        # ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"English", None));
        # ___qlistwidgetitem1 = self.Select_Vernac_13.item(1)
        # ___qlistwidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Hindi", None));
        # ___qlistwidgetitem2 = self.Select_Vernac_13.item(2)
        # ___qlistwidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Kannada", None));
        # ___qlistwidgetitem3 = self.Select_Vernac_13.item(3)
        # ___qlistwidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tamil", None));
        # ___qlistwidgetitem4 = self.Select_Vernac_13.item(4)
        # ___qlistwidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Telugu", None));
        # self.Select_Vernac_13.setSortingEnabled(__sortingEnabled)

#if QT_CONFIG(tooltip)
        self.Button_1.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 1", None))
#endif // QT_CONFIG(tooltip)
        self.Button_1.setText(QCoreApplication.translate("MainWindow", u"Grab or Gone", None))
        self.Button_1.clicked.connect(self.ShowFrame1)
#if QT_CONFIG(shortcut)
        self.Button_1.setShortcut(QCoreApplication.translate("MainWindow", u"1", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Button_2.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 2", None))
#endif // QT_CONFIG(tooltip)
        self.Button_2.setText(QCoreApplication.translate("MainWindow", u"Don't Miss Out", None))
        self.Button_2.clicked.connect(self.ShowFrame2)
#if QT_CONFIG(shortcut)
        self.Button_2.setShortcut(QCoreApplication.translate("MainWindow", u"2", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Button_3.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 3", None))
#endif // QT_CONFIG(tooltip)
        self.Button_3.setText(QCoreApplication.translate("MainWindow", u"Smaller 2Grid (720x720)", None))
        self.Button_3.clicked.connect(self.ShowFrame3)
#if QT_CONFIG(shortcut)
        self.Button_3.setShortcut(QCoreApplication.translate("MainWindow", u"3", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Button_4.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 4", None))
#endif // QT_CONFIG(tooltip)
        self.Button_4.setText(QCoreApplication.translate("MainWindow", u"DT - X3", None))
        self.Button_4.clicked.connect(self.ShowFrame4)
#if QT_CONFIG(shortcut)
        self.Button_4.setShortcut(QCoreApplication.translate("MainWindow", u"4", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Button_5.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 5", None))
#endif // QT_CONFIG(tooltip)
        self.Button_5.setText(QCoreApplication.translate("MainWindow", u"DT Flex", None))
        self.Button_5.clicked.connect(self.ShowFrame5)
#if QT_CONFIG(shortcut)
        self.Button_5.setShortcut(QCoreApplication.translate("MainWindow", u"5", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.Button_6.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 6", None))
#endif // QT_CONFIG(tooltip)
        self.Button_6.setText(QCoreApplication.translate("MainWindow", u"3Grid Offer Zone", None))
        self.Button_6.clicked.connect(self.ShowFrame6)
#if QT_CONFIG(shortcut)
        self.Button_6.setShortcut(QCoreApplication.translate("MainWindow", u"6", None))
#endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_7.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 7", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_7.setText(QCoreApplication.translate("MainWindow", u"Flex (1440x560)", None))
#         self.Button_7.clicked.connect(self.ShowFrame7)
# #if QT_CONFIG(shortcut)
#         self.Button_7.setShortcut(QCoreApplication.translate("MainWindow", u"7", None))
# #endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_8.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 8", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_8.setText(QCoreApplication.translate("MainWindow", u"Flex (1440x640)", None))
#         self.Button_8.clicked.connect(self.ShowFrame8)
# #if QT_CONFIG(shortcut)
#         self.Button_8.setShortcut(QCoreApplication.translate("MainWindow", u"8", None))
# #endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_9.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - 9", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_9.setText(QCoreApplication.translate("MainWindow", u"L1 App 1Grid", None))
#         self.Button_9.clicked.connect(self.ShowFrame9)
# #if QT_CONFIG(shortcut)
#         self.Button_9.setShortcut(QCoreApplication.translate("MainWindow", u"9", None))
# #endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_10.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - a", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_10.setText(QCoreApplication.translate("MainWindow", u"DT X3", None))
#         self.Button_10.clicked.connect(self.ShowFrame10)
# #if QT_CONFIG(shortcut)
#         self.Button_10.setShortcut(QCoreApplication.translate("MainWindow", u"A", None))
# #endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_11.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - b", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_11.setText(QCoreApplication.translate("MainWindow", u"Intrigue Silver (640x720)", None))
#         self.Button_11.clicked.connect(self.ShowFrame11)
# #if QT_CONFIG(shortcut)
#         self.Button_11.setShortcut(QCoreApplication.translate("MainWindow", u"B", None))
# #endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_12.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - c", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_12.setText(QCoreApplication.translate("MainWindow", u"Intrigue Silver Flash", None))
#         self.Button_12.clicked.connect(self.ShowFrame12)
# #if QT_CONFIG(shortcut)
#         self.Button_12.setShortcut(QCoreApplication.translate("MainWindow", u"C", None))
# #endif // QT_CONFIG(shortcut)
# #if QT_CONFIG(tooltip)
#         self.Button_13.setToolTip(QCoreApplication.translate("MainWindow", u"shortcut - d", None))
# #endif // QT_CONFIG(tooltip)
#         self.Button_13.setText(QCoreApplication.translate("MainWindow", u"Intrigue 2Grid (720x720)", None))
#         self.Button_13.clicked.connect(self.ShowFrame13)
# #if QT_CONFIG(shortcut)
#         self.Button_13.setShortcut(QCoreApplication.translate("MainWindow", u"D", None))
#endif // QT_CONFIG(shortcut)
#if QT_CONFIG(tooltip)
        self.BG_Remove.setToolTip(QCoreApplication.translate("MainWindow", u"Upload the sheet and remove the background", None))
#endif // QT_CONFIG(tooltip)
        self.BG_Remove.setText(QCoreApplication.translate("MainWindow", u"\u046a", None))
#if QT_CONFIG(tooltip)
        self.FSN_Button.setToolTip(QCoreApplication.translate("MainWindow", u"Check if FSN is missing in the sheet", None))
#endif // QT_CONFIG(tooltip)
        self.FSN_Button.setText(QCoreApplication.translate("MainWindow", u"\u0468", None))
        self.Logo_Label.setPixmap("Images/Templates/tathastulogo.png") # .setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/tathastulogo/tathastulogo.png\"/></p></body></html>", None))
        self.Category_Label.setText(QCoreApplication.translate("MainWindow", u"Grocery", None))
    # retranslateUi

    def ShowFrame1(self):
        self.Frame_1.setVisible(True)
        self.Frame_2.setVisible(False)
        self.Frame_3.setVisible(False)
        self.Frame_4.setVisible(False)
        self.Frame_5.setVisible(False)
        self.Frame_6.setVisible(False)
        # self.Frame_7.setVisible(False)
        # self.Frame_8.setVisible(False)
        # self.Frame_9.setVisible(False)
        # self.Frame_10.setVisible(False)
        # self.Frame_11.setVisible(False)
        # self.Frame_12.setVisible(False)
        # self.Frame_13.setVisible(False)
    def ShowFrame2(self):
        self.Frame_1.setVisible(False)
        self.Frame_2.setVisible(True)
        self.Frame_3.setVisible(False)
        self.Frame_4.setVisible(False)
        self.Frame_5.setVisible(False)
        self.Frame_6.setVisible(False)
        # self.Frame_7.setVisible(False)
        # self.Frame_8.setVisible(False)
        # self.Frame_9.setVisible(False)
        # self.Frame_10.setVisible(False)
        # self.Frame_11.setVisible(False)
        # self.Frame_12.setVisible(False)
        # self.Frame_13.setVisible(False)
    def ShowFrame3(self):
        self.Frame_1.setVisible(False)
        self.Frame_2.setVisible(False)
        self.Frame_3.setVisible(True)
        self.Frame_4.setVisible(False)
        self.Frame_5.setVisible(False)
        self.Frame_6.setVisible(False)
        # self.Frame_7.setVisible(False)
        # self.Frame_8.setVisible(False)
        # self.Frame_9.setVisible(False)
        # self.Frame_10.setVisible(False)
        # self.Frame_11.setVisible(False)
        # self.Frame_12.setVisible(False)
        # self.Frame_13.setVisible(False)
    def ShowFrame4(self):
        self.Frame_1.setVisible(False)
        self.Frame_2.setVisible(False)
        self.Frame_3.setVisible(False)
        self.Frame_4.setVisible(True)
        self.Frame_5.setVisible(False)
        self.Frame_6.setVisible(False)
        self.Frame_7.setVisible(False)
        # self.Frame_8.setVisible(False)
        # self.Frame_9.setVisible(False)
        # self.Frame_10.setVisible(False)
        # self.Frame_11.setVisible(False)
        # self.Frame_12.setVisible(False)
        # self.Frame_13.setVisible(False)
    def ShowFrame5(self):
        self.Frame_1.setVisible(False)
        self.Frame_2.setVisible(False)
        self.Frame_3.setVisible(False)
        self.Frame_4.setVisible(False)
        self.Frame_5.setVisible(True)
        self.Frame_6.setVisible(False)
        # self.Frame_7.setVisible(False)
        # self.Frame_8.setVisible(False)
        # self.Frame_9.setVisible(False)
        # self.Frame_10.setVisible(False)
        # self.Frame_11.setVisible(False)
        # self.Frame_12.setVisible(False)
        # self.Frame_13.setVisible(False)
    def ShowFrame6(self):
        self.Frame_1.setVisible(False)
        self.Frame_2.setVisible(False)
        self.Frame_3.setVisible(False)
        self.Frame_4.setVisible(False)
        self.Frame_5.setVisible(False)
        self.Frame_6.setVisible(True)
        # self.Frame_7.setVisible(False)
        # self.Frame_8.setVisible(False)
        # self.Frame_9.setVisible(False)
        # self.Frame_10.setVisible(False)
        # self.Frame_11.setVisible(False)
        # self.Frame_12.setVisible(False)
        # self.Frame_13.setVisible(False)
    # def ShowFrame7(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(True)
    #     self.Frame_8.setVisible(False)
    #     self.Frame_9.setVisible(False)
    #     self.Frame_10.setVisible(False)
    #     self.Frame_11.setVisible(False)
    #     self.Frame_12.setVisible(False)
    #     self.Frame_13.setVisible(False)
    # def ShowFrame8(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(False)
    #     self.Frame_8.setVisible(True)
    #     self.Frame_9.setVisible(False)
    #     self.Frame_10.setVisible(False)
    #     self.Frame_11.setVisible(False)
    #     self.Frame_12.setVisible(False)
    #     self.Frame_13.setVisible(False)
    # def ShowFrame9(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(False)
    #     self.Frame_8.setVisible(False)
    #     self.Frame_9.setVisible(True)
    #     self.Frame_10.setVisible(False)
    #     self.Frame_11.setVisible(False)
    #     self.Frame_12.setVisible(False)
    #     self.Frame_13.setVisible(False)
    # def ShowFrame10(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(False)
    #     self.Frame_8.setVisible(False)
    #     self.Frame_9.setVisible(False)
    #     self.Frame_10.setVisible(True)
    #     self.Frame_11.setVisible(False)
    #     self.Frame_12.setVisible(False)
    #     self.Frame_13.setVisible(False)
    # def ShowFrame11(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(False)
    #     self.Frame_8.setVisible(False)
    #     self.Frame_9.setVisible(False)
    #     self.Frame_10.setVisible(False)
    #     self.Frame_11.setVisible(True)
    #     self.Frame_12.setVisible(False)
    #     self.Frame_13.setVisible(False)
    # def ShowFrame12(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(False)
    #     self.Frame_8.setVisible(False)
    #     self.Frame_9.setVisible(False)
    #     self.Frame_10.setVisible(False)
    #     self.Frame_11.setVisible(False)
    #     self.Frame_12.setVisible(True)
    #     self.Frame_13.setVisible(False)
    # def ShowFrame13(self):
    #     self.Frame_1.setVisible(False)
    #     self.Frame_2.setVisible(False)
    #     self.Frame_3.setVisible(False)
    #     self.Frame_4.setVisible(False)
    #     self.Frame_5.setVisible(False)
    #     self.Frame_6.setVisible(False)
    #     self.Frame_7.setVisible(False)
    #     self.Frame_8.setVisible(False)
    #     self.Frame_9.setVisible(False)
    #     self.Frame_10.setVisible(False)
    #     self.Frame_11.setVisible(False)
    #     self.Frame_12.setVisible(False)
    #     self.Frame_13.setVisible(True)

    # Select BG for 2Grid 720x1024 --------
    def FunctionBG1(self):
        global path_bg_1
        filename = QFileDialog.getOpenFileName(self.Select_BG_1, 'Open Image', './', 'Image Files(*.png *.jpg)')
        path_bg_1 = filename[0]
        print(path_bg_1)

    # Select DataSet for 2Grid 720x1024 --------
    def FunctionData1(self):
        global path_data_1
        filename = QFileDialog.getOpenFileName(self.Select_CSV_1, 'Open Dataset', './', 'CSV Files(*.csv)')
        path_data_1 = filename[0]
        print(path_data_1)

    # Select Vernac_1 --------
    def GetVernac1(self):
        global vernac_name_1
        vernac_name_1 = self.Select_Vernac_1.currentItem().text()
        print(vernac_name_1)

    # Select Vernac_2 --------
    def GetVernac2(self):
        global vernac_name_2
        vernac_name_2 = self.Select_Vernac_2.currentItem().text()
        print(vernac_name_2)

    # Select Vernac_3 --------
    def GetVernac3(self):
        global vernac_name_3
        vernac_name_3 = self.Select_Vernac_3.currentItem().text()
        print(vernac_name_3)

    # Select Vernac_4 --------
    def GetVernac4(self):
        global vernac_name_4
        vernac_name_4 = self.Select_Vernac_4.currentItem().text()
        print(vernac_name_4)

    # Select Vernac_5 --------
    def GetVernac5(self):
        global vernac_name_5
        vernac_name_5 = self.Select_Vernac_5.currentItem().text()
        print(vernac_name_5)

    # Select Vernac_6 --------
    def GetVernac6(self):
        global vernac_name_6
        vernac_name_6 = self.Select_Vernac_6.currentItem().text()
        print(vernac_name_6)

    # # Select Vernac_7 --------
    # def GetVernac7(self):
    #     global vernac_name_7
    #     vernac_name_7 = self.Select_Vernac_7.currentItem().text()
    #     print(vernac_name_7)
    #
    # # Select Vernac_8 --------
    # def GetVernac8(self):
    #     global vernac_name_8
    #     vernac_name_8 = self.Select_Vernac_8.currentItem().text()
    #     print(vernac_name_8)
    #
    # # Select Vernac_9 --------
    # def GetVernac9(self):
    #     global vernac_name_9
    #     vernac_name_9 = self.Select_Vernac_9.currentItem().text()
    #     print(vernac_name_9)
    #
    # # Select Vernac_10 --------
    # def GetVernac10(self):
    #     global vernac_name_10
    #     vernac_name_10 = self.Select_Vernac_10.currentItem().text()
    #     print(vernac_name_10)
    #
    # # Select Vernac_11 --------
    # def GetVernac11(self):
    #     global vernac_name_11
    #     vernac_name_11 = self.Select_Vernac_11.currentItem().text()
    #     print(vernac_name_11)
    #
    # # Select Vernac_12 --------
    # def GetVernac12(self):
    #     global vernac_name_12
    #     vernac_name_12 = self.Select_Vernac_12.currentItem().text()
    #     print(vernac_name_12)
    #
    # # Select Vernac_13 --------
    # def GetVernac13(self):
    #     global vernac_name_13
    #     vernac_name_13 = self.Select_Vernac_13.currentItem().text()
    #     print(vernac_name_13)

    # 1. Generate 2Grid 720x1024 --------
    def FunctionGen1(self):
        file_path = QFileDialog.getSaveFileName(self.Gen_Card_1, 'Enter Filename & Save File')
        final_files = file_path[0]
        print(final_files)
        data = pandas.read_csv(path_data_1)

        fsn_names1 = data.POC_FSN.tolist()
        callout1 = data.Eng_C1.tolist()
        callout2 = data.Eng_C2.tolist()
        callout1_hin = data.Hindi_C1.tolist()
        callout2_hin = data.Hindi_C2.tolist()

        maxwidth = 285
        maxheight = 420
        veralign_height = 632

        number1 = 0
        number5 = 0
        number7 = 0

        filename = str(number7)

        while number1 < len(fsn_names1):
            # Popup if image is missing starts here.
            name = fsn_names1[number1]
            name1 = str(fsn_names1[number1]) + ".png"
            myimg = str(name) + ".png"
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                pass
            else:
                QInputDialog.getText(self.centralwidget, "Image is Missing", "Oops! You Have an Image in Society But Not in Folder.", text=name1)
                print(my_file)
            # Popup if image is missing ends here.
            fsn_names1[number1] = fsn_names1[number1] + ".png"
            number1 = number1 + 1

        while number7 < len(fsn_names1):
            background = Image.open(path_bg_1)
            bgwidth, bgheight = background.size

            myimg = fsn_names1[number7]

            # Missing FSN skip starts here
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                filename = str(number7 + 1)
                fsn = Image.open(fp=fsnFolder + myimg)
            else:
                pass
            # Missing FSN skip ends here

            fsn_w, fsn_h = fsn.size

            shadow_img = Image.open("Images/Templates/shadow_gog.png")
            shadow_w, shadow_h = shadow_img.size

            if fsn_w > fsn_h:
                veralign_height = 950
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                print("one")
                background.paste(shadow_img, (0, int((veralign_height)/2+int(hsize/2)-int(shadow_h/2))), shadow_img)
                background.paste(fsn, (44, int((veralign_height-hsize)/2)), fsn)
            elif fsn_h > fsn_w and fsn_w > fsn_h/1.59:
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                if hsize >= 260:
                    veralign_height = 625
                    background.paste(shadow_img, (0, (veralign_height-30)), shadow_img)
                    print("second 1")
                    background.paste(fsn, (44, (veralign_height-hsize)), fsn)
                else:
                    veralign_height = 950
                    background.paste(shadow_img, (0, int((veralign_height) / 2)+30), shadow_img)
                    print("second 2")
                    background.paste(fsn, (44, int((veralign_height - hsize) / 2)), fsn)

            else:
                veralign_height = 632
                wpercent = (maxheight / float(fsn.size[1]))
                wsize = int((float(fsn.size[0]) * float(wpercent)))

                center_hor = int((bgwidth - wsize) / 2)
                center_ver = veralign_height - maxheight

                fsn = fsn.resize((wsize, maxheight))
                background.paste(shadow_img, (int(44 + (maxwidth - shadow_w) / 2), int(veralign_height - shadow_h / 2)), shadow_img)
                background.paste(fsn, (int(44+(maxwidth-wsize)/2), center_ver), fsn)
                print("third")

            if vernac_name_1 == "English":
                callout_1 = callout1[number7]
                callout_2 = callout2[number7]

                max_w = 387

                draw_1 = ImageDraw.Draw(background)
                font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)

                draw_2 = ImageDraw.Draw(background)
                font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 45)

                w, h = draw_1.textsize(callout_1, font=font_family_1)
                if w > max_w:
                    newtext = QInputDialog.getText(self.centralwidget, "Callout1 : Edit Callout", "Callout is exceeding character limit. Please update.", text=callout_1)
                    callout_1 = newtext[0]
                draw_1.text((44, 58), callout_1, "#5f5f5f", font=font_family_1)

                w, h = draw_2.textsize(callout_2, font=font_family_2)
                if w > max_w:
                    newtext = QInputDialog.getText(self.centralwidget, "Callout2 : Edit Callout", "Callout is exceeding character limit. Please update.", text=callout_2)
                    callout_2 = newtext[0]
                draw_2.text((44, 113), callout_2, "#db0552", font=font_family_2)

            elif vernac_name_1 == "Hindi":
                callout_1 = callout1_hin[number7]
                callout_2 = callout2_hin[number7]

                max_w = 387

                draw_1 = ImageDraw.Draw(background)
                font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 31, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)

                draw_2 = ImageDraw.Draw(background)
                font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Bold.ttf", 42, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)

                w, h = draw_1.textsize(callout_1, font=font_family_1)
                if w > max_w:
                    newtext = QInputDialog.getText(self.centralwidget, "Callout1 : Edit Callout", "Callout is exceeding character limit. Please update.", text=callout_1)
                    callout_1 = newtext[0]
                draw_1.text((44, 58), callout_1, "#5f5f5f", font=font_family_1)

                w, h = draw_2.textsize(callout_2, font=font_family_2)
                if w > max_w:
                    newtext = QInputDialog.getText(self.centralwidget, "Callout2 : Edit Callout", "Callout is exceeding character limit. Please update.", text=callout_2)
                    callout_2 = newtext[0]
                draw_2.text((44, 103), callout_2, "#db0552", font=font_family_2)

            background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
            number7 = number7 + 1

    # 2. Generate DMO --------
    def FunctionGen2(self):
        file_path = QFileDialog.getSaveFileName(self.Gen_Card_2, 'Enter Filename & Save File')
        final_files = file_path[0]
        print(final_files)
        data = pandas.read_csv(path_data_1)

        fsn_names1 = data.POC_FSN.tolist()
        callout1 = data.Eng_C1.tolist()
        callout2 = data.Eng_C2.tolist()

        maxwidth = 286
        maxheight = 286
        veralign_height = 478

        number1 = 0
        number7 = 0

        filename = str(number7)

        while number1 < len(fsn_names1):
            # Popup if image is missing starts here.
            name = fsn_names1[number1]
            name1 = str(fsn_names1[number1]) + ".png"
            myimg = str(name) + ".png"
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                pass
            else:
                QInputDialog.getText(self.centralwidget, "Image is Missing", "Oops! You Have an Image in Society But Not in Folder.", text=name1)
            # Popup if image is missing ends here.
            fsn_names1[number1] = fsn_names1[number1] + ".png"
            number1 = number1 + 1

        while number7 < len(fsn_names1):
            background = Image.open(path_bg_1)
            bgwidth, bgheight = background.size

            myimg = fsn_names1[number7]

            # Missing FSN skip starts here
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                filename = str(number7 + 1)
                fsn = Image.open(fp=fsnFolder + myimg)
            else:
                pass
            # Missing FSN skip ends here

            fsn_w, fsn_h = fsn.size

            shadow_img = Image.open("Images/Templates/shadow_gog.png")
            shadow_w, shadow_h = shadow_img.size

            if fsn_w > fsn_h:
                veralign_height = 678
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                print("one")
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int((veralign_height) / 2 + 30)), shadow_img)
                background.paste(fsn, (56, int((veralign_height - hsize) / 2)), fsn)
            else:
                veralign_height = 478
                wpercent = (maxheight / float(fsn.size[1]))
                wsize = int((float(fsn.size[0]) * float(wpercent)))

                center_hor = int((bgwidth - wsize) / 2)
                center_ver = veralign_height - maxheight

                fsn = fsn.resize((wsize, maxheight))
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int(veralign_height - shadow_h / 2)), shadow_img)
                background.paste(fsn, (int(56+(maxwidth-wsize)/2), center_ver), fsn)
                print("third")


            callout_1 = callout1[number7]
            callout_2 = callout2[number7]

            max_w = 395

            draw_1 = ImageDraw.Draw(background)
            font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 31)

            draw_2 = ImageDraw.Draw(background)
            font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 41)

            w, h = draw_1.textsize(callout_1, font=font_family_1)
            draw_1.text((56, 68), callout_1, "#5f5f5f", font=font_family_1)

            w, h = draw_2.textsize(callout_2, font=font_family_2)
            draw_2.text((56, 117), callout_2, "#6615cb", font=font_family_2)

            background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
            number7 = number7 + 1

    def FunctionGen3(self):
        file_path = QFileDialog.getSaveFileName(self.Gen_Card_2, 'Enter Filename & Save File')
        final_files = file_path[0]
        print(final_files)
        data = pandas.read_csv(path_data_1)

        fsn_names1 = data.POC_FSN.tolist()
        callout1 = data.Eng_C1.tolist()
        callout2 = data.Eng_C2.tolist()

        maxwidth = 286
        maxheight = 286
        veralign_height = 478

        number1 = 0
        number7 = 0

        filename = str(number7)

        while number1 < len(fsn_names1):
            # Popup if image is missing starts here.
            name = fsn_names1[number1]
            name1 = str(fsn_names1[number1]) + ".png"
            myimg = str(name) + ".png"
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                pass
            else:
                QInputDialog.getText(self.centralwidget, "Image is Missing", "Oops! You Have an Image in Society But Not in Folder.", text=name1)
            # Popup if image is missing ends here.
            fsn_names1[number1] = fsn_names1[number1] + ".png"
            number1 = number1 + 1

        while number7 < len(fsn_names1):
            background = Image.open(path_bg_1)
            bgwidth, bgheight = background.size

            myimg = fsn_names1[number7]

            # Missing FSN skip starts here
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                filename = str(number7 + 1)
                fsn = Image.open(fp=fsnFolder + myimg)
            else:
                pass
            # Missing FSN skip ends here

            fsn_w, fsn_h = fsn.size

            shadow_img = Image.open("Images/Templates/shadow_gog.png")
            shadow_w, shadow_h = shadow_img.size

            if fsn_w > fsn_h:
                veralign_height = 678
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                print("one")
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int((veralign_height) / 2 + 30)), shadow_img)
                background.paste(fsn, (56, int((veralign_height - hsize) / 2)), fsn)
            else:
                veralign_height = 478
                wpercent = (maxheight / float(fsn.size[1]))
                wsize = int((float(fsn.size[0]) * float(wpercent)))

                center_hor = int((bgwidth - wsize) / 2)
                center_ver = veralign_height - maxheight

                fsn = fsn.resize((wsize, maxheight))
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int(veralign_height - shadow_h / 2)), shadow_img)
                background.paste(fsn, (int(56+(maxwidth-wsize)/2), center_ver), fsn)
                print("third")


            callout_1 = callout1[number7]
            callout_2 = callout2[number7]

            max_w = 395

            draw_1 = ImageDraw.Draw(background)
            font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 31)

            draw_2 = ImageDraw.Draw(background)
            font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 41)

            w, h = draw_1.textsize(callout_1, font=font_family_1)
            draw_1.text((56, 68), callout_1, "#5f5f5f", font=font_family_1)

            w, h = draw_2.textsize(callout_2, font=font_family_2)
            draw_2.text((56, 117), callout_2, "#6615cb", font=font_family_2)

            background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
            number7 = number7 + 1

    def FunctionGen4(self):
        file_path = QFileDialog.getSaveFileName(self.Gen_Card_2, 'Enter Filename & Save File')
        final_files = file_path[0]
        print(final_files)
        data = pandas.read_csv(path_data_1)

        fsn_names1 = data.POC_FSN.tolist()
        callout1 = data.Eng_C1.tolist()
        callout2 = data.Eng_C2.tolist()

        maxwidth = 286
        maxheight = 286
        veralign_height = 478

        number1 = 0
        number7 = 0

        filename = str(number7)

        while number1 < len(fsn_names1):
            # Popup if image is missing starts here.
            name = fsn_names1[number1]
            name1 = str(fsn_names1[number1]) + ".png"
            myimg = str(name) + ".png"
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                pass
            else:
                QInputDialog.getText(self.centralwidget, "Image is Missing", "Oops! You Have an Image in Society But Not in Folder.", text=name1)
            # Popup if image is missing ends here.
            fsn_names1[number1] = fsn_names1[number1] + ".png"
            number1 = number1 + 1

        while number7 < len(fsn_names1):
            background = Image.open(path_bg_1)
            bgwidth, bgheight = background.size

            myimg = fsn_names1[number7]

            # Missing FSN skip starts here
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                filename = str(number7 + 1)
                fsn = Image.open(fp=fsnFolder + myimg)
            else:
                pass
            # Missing FSN skip ends here

            fsn_w, fsn_h = fsn.size

            shadow_img = Image.open("Images/Templates/shadow_gog.png")
            shadow_w, shadow_h = shadow_img.size

            if fsn_w > fsn_h:
                veralign_height = 678
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                print("one")
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int((veralign_height) / 2 + 30)), shadow_img)
                background.paste(fsn, (56, int((veralign_height - hsize) / 2)), fsn)
            else:
                veralign_height = 478
                wpercent = (maxheight / float(fsn.size[1]))
                wsize = int((float(fsn.size[0]) * float(wpercent)))

                center_hor = int((bgwidth - wsize) / 2)
                center_ver = veralign_height - maxheight

                fsn = fsn.resize((wsize, maxheight))
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int(veralign_height - shadow_h / 2)), shadow_img)
                background.paste(fsn, (int(56+(maxwidth-wsize)/2), center_ver), fsn)
                print("third")


            callout_1 = callout1[number7]
            callout_2 = callout2[number7]

            max_w = 395

            draw_1 = ImageDraw.Draw(background)
            font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 31)

            draw_2 = ImageDraw.Draw(background)
            font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 41)

            w, h = draw_1.textsize(callout_1, font=font_family_1)
            draw_1.text((56, 68), callout_1, "#5f5f5f", font=font_family_1)

            w, h = draw_2.textsize(callout_2, font=font_family_2)
            draw_2.text((56, 117), callout_2, "#6615cb", font=font_family_2)

            background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
            number7 = number7 + 1

    def FunctionGen5(self):
        file_path = QFileDialog.getSaveFileName(self.Gen_Card_2, 'Enter Filename & Save File')
        final_files = file_path[0]
        print(final_files)
        data = pandas.read_csv(path_data_1)

        fsn_names1 = data.POC_FSN.tolist()
        callout1 = data.Eng_C1.tolist()
        callout2 = data.Eng_C2.tolist()

        maxwidth = 286
        maxheight = 286
        veralign_height = 478

        number1 = 0
        number7 = 0

        filename = str(number7)

        while number1 < len(fsn_names1):
            # Popup if image is missing starts here.
            name = fsn_names1[number1]
            name1 = str(fsn_names1[number1]) + ".png"
            myimg = str(name) + ".png"
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                pass
            else:
                QInputDialog.getText(self.centralwidget, "Image is Missing", "Oops! You Have an Image in Society But Not in Folder.", text=name1)
            # Popup if image is missing ends here.
            fsn_names1[number1] = fsn_names1[number1] + ".png"
            number1 = number1 + 1

        while number7 < len(fsn_names1):
            background = Image.open(path_bg_1)
            bgwidth, bgheight = background.size

            myimg = fsn_names1[number7]

            # Missing FSN skip starts here
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                filename = str(number7 + 1)
                fsn = Image.open(fp=fsnFolder + myimg)
            else:
                pass
            # Missing FSN skip ends here

            fsn_w, fsn_h = fsn.size

            shadow_img = Image.open("Images/Templates/shadow_gog.png")
            shadow_w, shadow_h = shadow_img.size

            if fsn_w > fsn_h:
                veralign_height = 678
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                print("one")
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int((veralign_height) / 2 + 30)), shadow_img)
                background.paste(fsn, (56, int((veralign_height - hsize) / 2)), fsn)
            else:
                veralign_height = 478
                wpercent = (maxheight / float(fsn.size[1]))
                wsize = int((float(fsn.size[0]) * float(wpercent)))

                center_hor = int((bgwidth - wsize) / 2)
                center_ver = veralign_height - maxheight

                fsn = fsn.resize((wsize, maxheight))
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int(veralign_height - shadow_h / 2)), shadow_img)
                background.paste(fsn, (int(56+(maxwidth-wsize)/2), center_ver), fsn)
                print("third")


            callout_1 = callout1[number7]
            callout_2 = callout2[number7]

            max_w = 395

            draw_1 = ImageDraw.Draw(background)
            font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 31)

            draw_2 = ImageDraw.Draw(background)
            font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 41)

            w, h = draw_1.textsize(callout_1, font=font_family_1)
            draw_1.text((56, 68), callout_1, "#5f5f5f", font=font_family_1)

            w, h = draw_2.textsize(callout_2, font=font_family_2)
            draw_2.text((56, 117), callout_2, "#6615cb", font=font_family_2)

            background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
            number7 = number7 + 1

    def FunctionGen6(self):
        file_path = QFileDialog.getSaveFileName(self.Gen_Card_2, 'Enter Filename & Save File')
        final_files = file_path[0]
        print(final_files)
        data = pandas.read_csv(path_data_1)

        fsn_names1 = data.POC_FSN.tolist()
        callout1 = data.Eng_C1.tolist()
        callout2 = data.Eng_C2.tolist()

        maxwidth = 286
        maxheight = 286
        veralign_height = 478

        number1 = 0
        number7 = 0

        filename = str(number7)

        while number1 < len(fsn_names1):
            # Popup if image is missing starts here.
            name = fsn_names1[number1]
            name1 = str(fsn_names1[number1]) + ".png"
            myimg = str(name) + ".png"
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                pass
            else:
                QInputDialog.getText(self.centralwidget, "Image is Missing", "Oops! You Have an Image in Society But Not in Folder.", text=name1)
            # Popup if image is missing ends here.
            fsn_names1[number1] = fsn_names1[number1] + ".png"
            number1 = number1 + 1

        while number7 < len(fsn_names1):
            background = Image.open(path_bg_1)
            bgwidth, bgheight = background.size

            myimg = fsn_names1[number7]

            # Missing FSN skip starts here
            my_file = Path(fsnFolder + myimg)
            if my_file.is_file():
                filename = str(number7 + 1)
                fsn = Image.open(fp=fsnFolder + myimg)
            else:
                pass
            # Missing FSN skip ends here

            fsn_w, fsn_h = fsn.size

            shadow_img = Image.open("Images/Templates/shadow_gog.png")
            shadow_w, shadow_h = shadow_img.size

            if fsn_w > fsn_h:
                veralign_height = 678
                wpercent = (maxwidth / float(fsn.size[0]))
                hsize = int((float(fsn.size[1]) * float(wpercent)))

                center_hor = int((bgwidth - maxwidth) / 2)
                center_ver = veralign_height - hsize

                fsn = fsn.resize((maxwidth, hsize))
                print("one")
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int((veralign_height) / 2 + 30)), shadow_img)
                background.paste(fsn, (56, int((veralign_height - hsize) / 2)), fsn)
            else:
                veralign_height = 478
                wpercent = (maxheight / float(fsn.size[1]))
                wsize = int((float(fsn.size[0]) * float(wpercent)))

                center_hor = int((bgwidth - wsize) / 2)
                center_ver = veralign_height - maxheight

                fsn = fsn.resize((wsize, maxheight))
                background.paste(shadow_img, (int(56+(maxwidth-shadow_w)/2), int(veralign_height - shadow_h / 2)), shadow_img)
                background.paste(fsn, (int(56+(maxwidth-wsize)/2), center_ver), fsn)
                print("third")


            callout_1 = callout1[number7]
            callout_2 = callout2[number7]

            max_w = 395

            draw_1 = ImageDraw.Draw(background)
            font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 31)

            draw_2 = ImageDraw.Draw(background)
            font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 41)

            w, h = draw_1.textsize(callout_1, font=font_family_1)
            draw_1.text((56, 68), callout_1, "#5f5f5f", font=font_family_1)

            w, h = draw_2.textsize(callout_2, font=font_family_2)
            draw_2.text((56, 117), callout_2, "#6615cb", font=font_family_2)

            background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
            number7 = number7 + 1

    # # 3. Generate 3Grid (480x640) --------
    # def FunctionGen3(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_1, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     slant = data.Eng_Slant_Callout.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     slant_hin = data.Hindi_Slant_Callout.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     slant_kan = data.Kannada_Slant_Callout.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     slant_tam = data.Tamil_Slant_Callout.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     slant_tel = data.Telugu_Slant_Callout.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 360
    #     maxheight = 310
    #     veralign_height = 520
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_3Grid.jpg")
    #
    #             maxheight = 530
    #             maxwidth = 528
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 430, 431))
    #             background.paste(fsn_cropped, (26, 26), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if vernac_name_3 == "English":
    #             if slant[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/BIG_3Grid_480x640_slant.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 30)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 30), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_font = finetext[number7]
    #                 para_finetext = textwrap.wrap(finetext_font, width=100)
    #
    #                 draw_finetext = ImageDraw.Draw(background)
    #                 font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #
    #                 for line in para_finetext:
    #                     w, h = draw_finetext.textsize(line, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 32)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 558), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 580), (448, 580)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=2)
    #
    #             callout_1 = callout1[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 52)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 479), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 539), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_3 == "Hindi":
    #             if slant_hin[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/BIG_3Grid_480x640_slant.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_hin[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 30, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 26), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_hin[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_hin_font = finetext_hin[number7]
    #                 para_finetext_hin = textwrap.wrap(finetext_hin_font, width=100)
    #
    #                 draw_finetext_hin = ImageDraw.Draw(background)
    #                 font_family_finetext_hin = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_hin:
    #                     w, h = draw_finetext_hin.textsize(line, font=font_family_finetext_hin)
    #                     draw_finetext_hin.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_hin)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 32, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 558), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 579), (448, 579)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=2)
    #
    #             callout_1 = callout1_hin[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 42, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 55, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 468), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 522), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_3 == "Kannada":
    #             if slant_kan[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/BIG_3Grid_480x640_slant.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_kan[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 32, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 31), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_kan[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_kan_font = finetext_kan[number7]
    #                 para_finetext_kan = textwrap.wrap(finetext_kan_font, width=100)
    #
    #                 draw_finetext_kan = ImageDraw.Draw(background)
    #                 font_family_finetext_kan = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_kan:
    #                     w, h = draw_finetext_kan.textsize(line, font=font_family_finetext_kan)
    #                     draw_finetext_kan.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext_kan)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 32, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 551), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 579), (448, 579)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=2)
    #
    #             callout_1 = callout1_kan[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 52, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 484), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 544), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_3 == "Tamil":
    #             if slant_tam[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/BIG_3Grid_480x640_slant.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tam[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 28, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 28), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tam[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tam_font = finetext_tam[number7]
    #                 para_finetext_tam = textwrap.wrap(finetext_tam_font, width=100)
    #
    #                 draw_finetext_tam = ImageDraw.Draw(background)
    #                 font_family_finetext_tam = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tam:
    #                     w, h = draw_finetext_tam.textsize(line, font=font_family_finetext_tam)
    #                     draw_finetext_tam.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tam)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 32, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 558), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 579), (448, 579)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=2)
    #
    #             callout_1 = callout1_tam[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 52, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 474), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 531), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_3 == "Telugu":
    #             if slant_tel[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/BIG_3Grid_480x640_slant.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tel[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 27, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 34), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tel[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tel_font = finetext_tel[number7]
    #                 para_finetext_tel = textwrap.wrap(finetext_tel_font, width=100)
    #
    #                 draw_finetext_tel = ImageDraw.Draw(background)
    #                 font_family_finetext_tel = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tel:
    #                     w, h = draw_finetext_tel.textsize(line, font=font_family_finetext_tel)
    #                     draw_finetext_tel.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tel)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 32, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 558), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 579), (448, 579)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=2)
    #
    #             callout_1 = callout1_tel[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 52, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 482), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 541), line, "#26a541", font=font_family_2)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 4. Generate AW3 (480x512) --------
    # def FunctionGen4(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_4, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     callout3 = data.Eng_C3.tolist()
    #     slant = data.Eng_Slant_Callout.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     callout3_hin = data.Hindi_C3.tolist()
    #     slant_hin = data.Hindi_Slant_Callout.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     callout3_kan = data.Kannada_C3.tolist()
    #     slant_kan = data.Kannada_Slant_Callout.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     callout3_tam = data.Tamil_C3.tolist()
    #     slant_tam = data.Tamil_Slant_Callout.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     callout3_tel = data.Telugu_C3.tolist()
    #     slant_tel = data.Telugu_Slant_Callout.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 588
    #     maxheight = 545
    #     veralign_height = 757
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_2Grid.jpg")
    #
    #             maxheight = 665
    #             maxwidth = 668
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 668, 665))
    #             background.paste(fsn_cropped, (26, 26), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if vernac_name_4 == "English":
    #             if slant[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_font = finetext[number7]
    #                 para_finetext = textwrap.wrap(finetext_font, width=100)
    #
    #                 draw_finetext = ImageDraw.Draw(background)
    #                 font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #
    #                 for line in para_finetext:
    #                     w, h = draw_finetext.textsize(line, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 46)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 46)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 60)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_4 == "Hindi":
    #             if slant_hin[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_hin[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_hin[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_hin_font = finetext_hin[number7]
    #                 para_finetext_hin = textwrap.wrap(finetext_hin_font, width=100)
    #
    #                 draw_finetext_hin = ImageDraw.Draw(background)
    #                 font_family_finetext_hin = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_hin:
    #                     w, h = draw_finetext_hin.textsize(line, font=font_family_finetext_hin)
    #                     draw_finetext_hin.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_hin)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_hin[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_hin[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_4 == "Kannada":
    #             if slant_kan[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_kan[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_kan[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_kan_font = finetext_kan[number7]
    #                 para_finetext_kan = textwrap.wrap(finetext_kan_font, width=100)
    #
    #                 draw_finetext_kan = ImageDraw.Draw(background)
    #                 font_family_finetext_kan = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_kan:
    #                     w, h = draw_finetext_kan.textsize(line, font=font_family_finetext_kan)
    #                     draw_finetext_kan.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext_kan)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_kan[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_kan[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #
    #         elif vernac_name_4 == "Tamil":
    #             if slant_tam[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tam[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tam[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tam_font = finetext_tam[number7]
    #                 para_finetext_tam = textwrap.wrap(finetext_tam_font, width=100)
    #
    #                 draw_finetext_tam = ImageDraw.Draw(background)
    #                 font_family_finetext_tam = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tam:
    #                     w, h = draw_finetext_tam.textsize(line, font=font_family_finetext_tam)
    #                     draw_finetext_tam.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tam)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tam[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_tam[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #             # for line in para_3:
    #             #     w, h = draw_3.textsize(line, font=font_family_3)
    #             #     draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_4 == "Telugu":
    #             if slant_tel[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tel[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tel[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tel_font = finetext_tel[number7]
    #                 para_finetext_tel = textwrap.wrap(finetext_tel_font, width=100)
    #
    #                 draw_finetext_tel = ImageDraw.Draw(background)
    #                 font_family_finetext_tel = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tel:
    #                     w, h = draw_finetext_tel.textsize(line, font=font_family_finetext_tel)
    #                     draw_finetext_tel.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tel)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tel[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_tel[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 5. Generate App HPW --------
    # def FunctionGen5(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_5, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Logo_2'] = data['Logo_2'].fillna("--")
    #     data['Logo_1'] = data['Logo_1'].fillna("--")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     logo1 = data.Logo_1.tolist()
    #     logo2 = data.Logo_2.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     cta_eng = data.CTA_Eng.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     cta_hin = data.CTA_Hin.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     cta_kan = data.CTA_Kan.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     cta_tam = data.CTA_Tam.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     cta_tel = data.CTA_Tel.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 424
    #     maxheight = 389
    #     veralign_height = 459
    #     horalign_width = 631
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_App_HPW.jpg")
    #
    #             maxheight = 494
    #             maxwidth = 459
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 494, 459))
    #             background.paste(fsn_cropped, (69, 125), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((horalign_width - maxwidth) / 2)
    #                 center_ver = int(125 + ((veralign_height - hsize) / 2))
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((horalign_width - wsize) / 2)
    #                 center_ver = int(125 + ((veralign_height - maxheight) / 2))
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if logo1[number7] == "--":
    #             pass
    #         else:
    #             first_logo = logo1[number7]
    #             logo1_image = Image.open(fp=logoFolder + first_logo)
    #             logo1_w, logo1_h = logo1_image.size
    #
    #             logo_maxwidth = 323
    #             logo_maxheight = 72
    #
    #             wpercent = (logo_maxheight / float(logo1_image.size[1]))
    #             wsize = int((float(logo1_image.size[0]) * float(wpercent)))
    #
    #             logo1_image = logo1_image.resize((wsize, logo_maxheight))
    #             background.paste(logo1_image, (631, 61))
    #
    #         if logo2[number7] == "--":
    #             pass
    #         else:
    #             if logo1[number7] == "--":
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxwidth = 323
    #                 logo_maxheight = 72
    #
    #                 wpercent = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize = int((float(logo2_image.size[0]) * float(wpercent)))
    #
    #                 logo2_image = logo2_image.resize((wsize, logo_maxheight))
    #                 background.paste(logo2_image, (631, 61))
    #             else:
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxwidth = 323
    #                 logo_maxheight = 72
    #
    #                 wpercent_1 = (logo_maxheight / float(logo1_image.size[1]))
    #                 wsize_1 = int((float(logo1_image.size[0]) * float(wpercent_1)))
    #
    #                 wpercent_2 = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize_2 = int((float(logo2_image.size[0]) * float(wpercent_2)))
    #
    #                 logo2_image = logo2_image.resize((wsize_2, logo_maxheight))
    #                 background.paste(logo2_image, (660 + wsize_1, 61))
    #
    #         if vernac_name_5 == "English":
    #             callout_1 = callout1[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 450), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 306), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     text_height_1 = 183
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 380), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 450), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 307), ((628 + w), 307)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 321), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     text_height_1 = 151
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 399), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 450), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 247), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 181), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 325), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 450), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 248), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 275), ((628 + w), 275)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 291), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 185), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 369), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_5 == "Hindi":
    #             callout_1 = callout1_hin[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-ExtraBold.ttf", 60)
    #                     draw_cta.text((628, 293), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 38)
    #
    #                     text_height_1 = 165
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 71
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 380), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 279), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 316), ((628 + w), 316)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-ExtraBold.ttf", 60)
    #                     draw_cta.text((628, 321), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 38)
    #
    #                     text_height_1 = 148
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 69
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 409), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-ExtraBold.ttf", 60)
    #                     draw_cta.text((628, 243), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 38)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 181), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 332), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 237), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 275), ((628 + w), 275)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-ExtraBold.ttf", 60)
    #                     draw_cta.text((628, 280), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 38)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 180), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 369), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_5 == "Kannada":
    #             callout_1 = callout1_kan[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 318), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 186
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 69
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 384), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 307), ((628 + w), 307)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 337), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 157
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 69
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 403), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 329), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 249), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 276), ((628 + w), 276)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 304), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 196), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 373), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_5 == "Tamil":
    #             callout_1 = callout1_tam[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 50)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 303), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 50)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     text_height_1 = 169
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 70
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 379), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 306), ((628 + w), 306)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 319), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 50)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     text_height_1 = 144
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 70
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 393), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 245), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 50)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 180), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 321), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 249), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 275), ((628 + w), 275)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 289), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 50)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 182), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 365), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_5 == "Telugu":
    #             callout_1 = callout1_tel[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 318), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 170
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 72
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 380), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 306), ((628 + w), 306)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 327), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:60] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 158
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 402), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:30] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 372), line, "#ffffff", font=font_family_2)
    #
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 6. Generate DT HPW --------
    # def FunctionGen6(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_6, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Logo_2'] = data['Logo_2'].fillna("--")
    #     data['Logo_1'] = data['Logo_1'].fillna("--")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     logo1 = data.Logo_1.tolist()
    #     logo2 = data.Logo_2.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     cta_eng = data.CTA_Eng.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #
    #     maxwidth = 435
    #     maxheight = 400
    #     veralign_height = 465
    #     horalign_width = 493
    #
    #     number1 = 0
    #     number5 = 0
    #     number7 = 0
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         # If image if full width
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_App_HPW.jpg")
    #
    #             maxwidth = 493
    #             maxheight = 465
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 494, 459))
    #             background.paste(fsn_cropped, (1094, 55), fsn_alpha)
    #
    #         # If image is not full width
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int(1094 + ((horalign_width - maxwidth) / 2))
    #                 center_ver = int(55 + ((veralign_height - hsize) / 2))
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int(1094 + ((horalign_width - wsize) / 2))
    #                 center_ver = int(55 + ((veralign_height - maxheight) / 2))
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if logo1[number7] == "--":
    #             pass
    #         else:
    #             first_logo = logo1[number7]
    #             logo1_image = Image.open(fp=logoFolder + first_logo)
    #             logo1_w, logo1_h = logo1_image.size
    #
    #             logo_maxheight = 62
    #
    #             wpercent = (logo_maxheight / float(logo1_image.size[1]))
    #             wsize = int((float(logo1_image.size[0]) * float(wpercent)))
    #
    #             logo1_image = logo1_image.resize((wsize, logo_maxheight))
    #             background.paste(logo1_image, (1686, 40))
    #
    #         if logo2[number7] == "--":
    #             pass
    #         else:
    #             if logo1[number7] == "--":
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxheight = 62
    #
    #                 wpercent = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize = int((float(logo2_image.size[0]) * float(wpercent)))
    #
    #                 logo2_image = logo2_image.resize((wsize, logo_maxheight))
    #                 background.paste(logo2_image, (1686, 40))
    #             else:
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxheight = 62
    #
    #                 wpercent_1 = (logo_maxheight / float(logo1_image.size[1]))
    #                 wsize_1 = int((float(logo1_image.size[0]) * float(wpercent_1)))
    #
    #                 wpercent_2 = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize_2 = int((float(logo2_image.size[0]) * float(wpercent_2)))
    #
    #                 logo2_image = logo2_image.resize((wsize_2, logo_maxheight))
    #                 background.paste(logo2_image, (1716 + wsize_1, 40))
    #
    #         callout_1 = callout1[number7]
    #         draw_1 = ImageDraw.Draw(background)
    #         font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #         w, h = draw_1.textsize(callout_1, font=font_family_1)
    #         # (Double Line of Callout_1)
    #         if w > 950:
    #             # If pricecut is not available
    #             if pricecut[number7] == "--":
    #                 if finetext[number7] == "--":
    #                     pass
    #                 else:
    #                     finetext_font = finetext[number7]
    #                     draw_finetext = ImageDraw.Draw(background)
    #                     font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                     w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 715 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                 cta_english = cta_eng[number7]
    #                 draw_cta = ImageDraw.Draw(background)
    #                 font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                 draw_cta.text((1686, 265), cta_english, "#ffea55", font=font_family_cta)
    #
    #                 callout_1 = callout1[number7]
    #                 callout_1 = callout_1[0:60] + "..."
    #                 para = textwrap.wrap(callout_1, width=35)
    #
    #                 callout_2 = callout2[number7]
    #                 para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                 draw_1 = ImageDraw.Draw(background)
    #                 font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                 draw_2 = ImageDraw.Draw(background)
    #                 font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                 text_height_1 = 136
    #                 for line in para:
    #                     w, h = draw_1.textsize(line, font=font_family_1)
    #                     draw_1.text((1686, text_height_1), line, "#ffffff", font=font_family_1)
    #                     text_height_1 += 64
    #
    #                 for line in para_2:
    #                     w, h = draw_2.textsize(line, font=font_family_2)
    #                     draw_2.text((1686, 343), line, "#ffffff", font=font_family_2)
    #             # If pricecut is available
    #             else:
    #                 if finetext[number7] == "--":
    #                     pass
    #                 else:
    #                     finetext_font = finetext[number7]
    #                     draw_finetext = ImageDraw.Draw(background)
    #                     font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                     w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 715 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                 pricecut_font = pricecut[number7]
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                 w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                 draw_pricecut.text((1686, 246), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                 # strikemark
    #                 line_shape = [(1686, 274), ((1686 + w), 274)]
    #                 line_img = ImageDraw.Draw(background)
    #                 line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                 cta_english = cta_eng[number7]
    #                 draw_cta = ImageDraw.Draw(background)
    #                 font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                 draw_cta.text((1686, 288), cta_english, "#ffea55", font=font_family_cta)
    #
    #                 callout_1 = callout1[number7]
    #                 callout_1 = callout_1[0:60] + "..."
    #                 para = textwrap.wrap(callout_1, width=35)
    #
    #                 callout_2 = callout2[number7]
    #                 para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                 draw_1 = ImageDraw.Draw(background)
    #                 font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                 draw_2 = ImageDraw.Draw(background)
    #                 font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                 text_height_1 = 119
    #                 for line in para:
    #                     w, h = draw_1.textsize(line, font=font_family_1)
    #                     draw_1.text((1686, text_height_1), line, "#ffffff", font=font_family_1)
    #                     text_height_1 += 64
    #
    #                 for line in para_2:
    #                     w, h = draw_2.textsize(line, font=font_family_2)
    #                     draw_2.text((1686, 366), line, "#ffffff", font=font_family_2)
    #
    #         # (Single Line of Callout_1)
    #         else:
    #             if pricecut[number7] == "--": # If pricecut is not available
    #                 if finetext[number7] == "--":
    #                     pass
    #                 else:
    #                     finetext_font = finetext[number7]
    #                     draw_finetext = ImageDraw.Draw(background)
    #                     font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                     w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 715 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                 callout_1 = callout1[number7]
    #                 callout_1 = callout_1[0:30] + "..."
    #                 para = textwrap.wrap(callout_1, width=35)
    #
    #                 callout_2 = callout2[number7]
    #                 para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                 cta_english = cta_eng[number7]
    #                 draw_cta = ImageDraw.Draw(background)
    #                 font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                 draw_cta.text((1686, 224), cta_english, "#ffea55", font=font_family_cta)
    #
    #                 draw_1 = ImageDraw.Draw(background)
    #                 font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                 draw_2 = ImageDraw.Draw(background)
    #                 font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                 for line in para:
    #                     w, h = draw_1.textsize(line, font=font_family_1)
    #                     draw_1.text((1686, 159), line, "#ffffff", font=font_family_1)
    #
    #                 for line in para_2:
    #                     w, h = draw_2.textsize(line, font=font_family_2)
    #                     draw_2.text((1686, 302), line, "#ffffff", font=font_family_2)
    #
    #             else: # If Pricecut is available
    #                 if finetext[number7] == "--":
    #                     pass
    #                 else:
    #                     finetext_font = finetext[number7]
    #                     draw_finetext = ImageDraw.Draw(background)
    #                     font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                     w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 715 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                 pricecut_font = pricecut[number7]
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                 w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                 draw_pricecut.text((1686, 216), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                 #strikemark
    #                 line_shape = [(1686, 243), ((1686 + w), 243)]
    #                 line_img = ImageDraw.Draw(background)
    #                 line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                 cta_english = cta_eng[number7]
    #                 draw_cta = ImageDraw.Draw(background)
    #                 font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                 draw_cta.text((1686, 258), cta_english, "#ffea55", font=font_family_cta)
    #
    #                 callout_1 = callout1[number7]
    #                 callout_1 = callout_1[0:30] + "..."
    #                 para = textwrap.wrap(callout_1, width=35)
    #
    #                 callout_2 = callout2[number7]
    #                 para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                 draw_1 = ImageDraw.Draw(background)
    #                 font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                 draw_2 = ImageDraw.Draw(background)
    #                 font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                 for line in para:
    #                     w, h = draw_1.textsize(line, font=font_family_1)
    #                     draw_1.text((1686, 153), line, "#ffffff", font=font_family_1)
    #
    #                 for line in para_2:
    #                     w, h = draw_2.textsize(line, font=font_family_2)
    #                     draw_2.text((1686, 336), line, "#ffffff", font=font_family_2)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 7. Generate Flex (1440x560) --------
    # def FunctionGen7(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_7, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Logo_2'] = data['Logo_2'].fillna("--")
    #     data['Logo_1'] = data['Logo_1'].fillna("--")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     logo1 = data.Logo_1.tolist()
    #     logo2 = data.Logo_2.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     cta_eng = data.CTA_Eng.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     cta_hin = data.CTA_Hin.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     cta_kan = data.CTA_Kan.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     cta_tam = data.CTA_Tam.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     cta_tel = data.CTA_Tel.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 410
    #     maxheight = 390
    #     veralign_height = 420
    #     horalign_width = 440
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_App_HPW.jpg")
    #
    #             maxwidth = 440
    #             maxheight = 420
    #
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 440, 420))
    #             background.paste(fsn_cropped, (83, 70))
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int(83 + ((horalign_width - maxwidth) / 2))
    #                 center_ver = int(70 + ((veralign_height - hsize) / 2))
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int(83 + ((horalign_width - wsize) / 2))
    #                 center_ver = int(70 + ((veralign_height - maxheight) / 2))
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if logo1[number7] == "--":
    #             pass
    #         else:
    #             first_logo = logo1[number7]
    #             logo1_image = Image.open(fp=logoFolder + first_logo)
    #             logo1_w, logo1_h = logo1_image.size
    #
    #             logo_maxwidth = 323
    #             logo_maxheight = 72
    #
    #             wpercent = (logo_maxheight / float(logo1_image.size[1]))
    #             wsize = int((float(logo1_image.size[0]) * float(wpercent)))
    #
    #             logo1_image = logo1_image.resize((wsize, logo_maxheight))
    #             background.paste(logo1_image, (631, 61))
    #
    #         if logo2[number7] == "--":
    #             pass
    #         else:
    #             if logo1[number7] == "--":
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxwidth = 323
    #                 logo_maxheight = 72
    #
    #                 wpercent = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize = int((float(logo2_image.size[0]) * float(wpercent)))
    #
    #                 logo2_image = logo2_image.resize((wsize, logo_maxheight))
    #                 background.paste(logo2_image, (631, 61))
    #             else:
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxwidth = 323
    #                 logo_maxheight = 72
    #
    #                 wpercent_1 = (logo_maxheight / float(logo1_image.size[1]))
    #                 wsize_1 = int((float(logo1_image.size[0]) * float(wpercent_1)))
    #
    #                 wpercent_2 = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize_2 = int((float(logo2_image.size[0]) * float(wpercent_2)))
    #
    #                 logo2_image = logo2_image.resize((wsize_2, logo_maxheight))
    #                 background.paste(logo2_image, (660 + wsize_1, 61))
    #
    #         if vernac_name_7 == "English":
    #             callout_1 = callout1[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 278), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 308), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 260), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 300), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_7 == "Hindi":
    #             callout_1 = callout1_hin[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 278), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 308), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 260), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 300), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_7 == "Kannada":
    #             callout_1 = callout1_kan[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 278), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 308), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_7 == "Tamil":
    #             callout_1 = callout1_tam[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 278), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 308), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_7 == "Telugu":
    #             callout_1 = callout1_tel[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 278), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 308), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 8. Generate Flex (1440x640) --------
    # def FunctionGen8(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_8, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Logo_2'] = data['Logo_2'].fillna("--")
    #     data['Logo_1'] = data['Logo_1'].fillna("--")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     logo1 = data.Logo_1.tolist()
    #     logo2 = data.Logo_2.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     cta_eng = data.CTA_Eng.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     cta_hin = data.CTA_Hin.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     cta_kan = data.CTA_Kan.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     cta_tam = data.CTA_Tam.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     cta_tel = data.CTA_Tel.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 410
    #     maxheight = 390
    #     veralign_height = 437
    #     horalign_width = 461
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_App_HPW.jpg")
    #
    #             maxwidth = 461
    #             maxheight = 437
    #
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 461, 437))
    #             background.paste(fsn_cropped, (84, 101))
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int(84 + ((horalign_width - maxwidth) / 2))
    #                 center_ver = int(101 + ((veralign_height - hsize) / 2))
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int(84 + ((horalign_width - wsize) / 2))
    #                 center_ver = int(101 + ((veralign_height - maxheight) / 2))
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if logo1[number7] == "--":
    #             pass
    #         else:
    #             first_logo = logo1[number7]
    #             logo1_image = Image.open(fp=logoFolder + first_logo)
    #             logo1_w, logo1_h = logo1_image.size
    #
    #             logo_maxwidth = 323
    #             logo_maxheight = 72
    #
    #             wpercent = (logo_maxheight / float(logo1_image.size[1]))
    #             wsize = int((float(logo1_image.size[0]) * float(wpercent)))
    #
    #             logo1_image = logo1_image.resize((wsize, logo_maxheight))
    #             background.paste(logo1_image, (631, 61))
    #
    #         if logo2[number7] == "--":
    #             pass
    #         else:
    #             if logo1[number7] == "--":
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxwidth = 323
    #                 logo_maxheight = 72
    #
    #                 wpercent = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize = int((float(logo2_image.size[0]) * float(wpercent)))
    #
    #                 logo2_image = logo2_image.resize((wsize, logo_maxheight))
    #                 background.paste(logo2_image, (631, 61))
    #             else:
    #                 second_logo = logo2[number7]
    #                 logo2_image = Image.open(fp=logoFolder + second_logo)
    #                 logo2_w, logo2_h = logo2_image.size
    #
    #                 logo_maxwidth = 323
    #                 logo_maxheight = 72
    #
    #                 wpercent_1 = (logo_maxheight / float(logo1_image.size[1]))
    #                 wsize_1 = int((float(logo1_image.size[0]) * float(wpercent_1)))
    #
    #                 wpercent_2 = (logo_maxheight / float(logo2_image.size[1]))
    #                 wsize_2 = int((float(logo2_image.size[0]) * float(wpercent_2)))
    #
    #                 logo2_image = logo2_image.resize((wsize_2, logo_maxheight))
    #                 background.paste(logo2_image, (660 + wsize_1, 61))
    #
    #         if vernac_name_8 == "English":
    #             callout_1 = callout1[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 278), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 308), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 260), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_english = cta_eng[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 60)
    #                     draw_cta.text((628, 300), cta_english, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_8 == "Hindi":
    #             callout_1 = callout1_hin[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 278), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 308), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 260), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_hin[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_hin[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_hindi = cta_hin[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60)
    #                     draw_cta.text((628, 300), cta_hindi, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_hin[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_hin[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Medium.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_8 == "Kannada":
    #             callout_1 = callout1_kan[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 278), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 308), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_kan[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_kan[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_kannada = cta_kan[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_kannada, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_kan[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_kan[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_8 == "Tamil":
    #             callout_1 = callout1_tam[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 278), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 308), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_tam[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tam[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_tamil = cta_tam[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_tamil, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tam[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tam[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=100)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #         if vernac_name_8 == "Telugu":
    #             callout_1 = callout1_tel[number7]
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #             w, h = draw_1.textsize(callout_1, font=font_family_1)
    #             # (Double Line of Callout_1)
    #             if w > 720:
    #                 # If pricecut is not available
    #                 if pricecut[number7] == "--":
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 278), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 357), line, "#ffffff", font=font_family_2)
    #                 # If pricecut is available
    #                 else:
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 280), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     # strikemark
    #                     line_shape = [(628, 300), ((628 + w), 300)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 308), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     text_height_1 = 152
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, text_height_1), line, "#ffffff", font=font_family_1)
    #                         text_height_1 += 64
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 387), line, "#ffffff", font=font_family_2)
    #
    #             # (Single Line of Callout_1)
    #             else:
    #                 if pricecut[number7] == "--": # If pricecut is not available
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 260), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 333), line, "#ffffff", font=font_family_2)
    #
    #                 else: # If Pricecut is available
    #                     if finetext_tel[number7] == "--":
    #                         pass
    #                     else:
    #                         finetext_font = finetext_tel[number7]
    #                         draw_finetext = ImageDraw.Draw(background)
    #                         font_family_finetext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20)
    #                         w, h = draw_finetext.textsize(finetext_font, font=font_family_finetext)
    #                         draw_finetext.text(((bgwidth - 55 - w), 440), finetext_font, "#ffffff", font=font_family_finetext)
    #
    #                     pricecut_font = pricecut[number7]
    #                     draw_pricecut = ImageDraw.Draw(background)
    #                     font_family_pricecut = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40)
    #                     w, h = draw_pricecut.textsize(pricecut_font, font=font_family_pricecut)
    #                     draw_pricecut.text((628, 250), pricecut_font, "#ffea55", font=font_family_pricecut)
    #
    #                     #strikemark
    #                     line_shape = [(628, 270), ((628 + w), 270)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#ffea55", width=3)
    #
    #                     cta_telugu = cta_tel[number7]
    #                     draw_cta = ImageDraw.Draw(background)
    #                     font_family_cta = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60)
    #                     draw_cta.text((628, 300), cta_telugu, "#ffea55", font=font_family_cta)
    #
    #                     callout_1 = callout1_tel[number7]
    #                     callout_1 = callout_1[0:18] + "..."
    #                     para = textwrap.wrap(callout_1, width=35)
    #
    #                     callout_2 = callout2_tel[number7]
    #                     para_2 = textwrap.wrap(callout_2, width=35)
    #
    #                     draw_1 = ImageDraw.Draw(background)
    #                     font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48)
    #
    #                     draw_2 = ImageDraw.Draw(background)
    #                     font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 35)
    #
    #                     for line in para:
    #                         w, h = draw_1.textsize(line, font=font_family_1)
    #                         draw_1.text((628, 192), line, "#ffffff", font=font_family_1)
    #
    #                     for line in para_2:
    #                         w, h = draw_2.textsize(line, font=font_family_2)
    #                         draw_2.text((628, 370), line, "#ffffff", font=font_family_2)
    #
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 9. Generate L1 App 1Grid --------
    # def FunctionGen9(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_9, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     callout3 = data.Eng_C3.tolist()
    #     slant = data.Eng_Slant_Callout.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     callout3_hin = data.Hindi_C3.tolist()
    #     slant_hin = data.Hindi_Slant_Callout.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     callout3_kan = data.Kannada_C3.tolist()
    #     slant_kan = data.Kannada_Slant_Callout.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     callout3_tam = data.Tamil_C3.tolist()
    #     slant_tam = data.Tamil_Slant_Callout.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     callout3_tel = data.Telugu_C3.tolist()
    #     slant_tel = data.Telugu_Slant_Callout.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 588
    #     maxheight = 545
    #     veralign_height = 757
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_2Grid.jpg")
    #
    #             maxheight = 665
    #             maxwidth = 668
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 668, 665))
    #             background.paste(fsn_cropped, (26, 26), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if vernac_name_9 == "English":
    #             if slant[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_font = finetext[number7]
    #                 para_finetext = textwrap.wrap(finetext_font, width=100)
    #
    #                 draw_finetext = ImageDraw.Draw(background)
    #                 font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #
    #                 for line in para_finetext:
    #                     w, h = draw_finetext.textsize(line, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 46)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 46)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 60)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_9 == "Hindi":
    #             if slant_hin[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_hin[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_hin[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_hin_font = finetext_hin[number7]
    #                 para_finetext_hin = textwrap.wrap(finetext_hin_font, width=100)
    #
    #                 draw_finetext_hin = ImageDraw.Draw(background)
    #                 font_family_finetext_hin = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_hin:
    #                     w, h = draw_finetext_hin.textsize(line, font=font_family_finetext_hin)
    #                     draw_finetext_hin.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_hin)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_hin[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_hin[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_9 == "Kannada":
    #             if slant_kan[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_kan[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_kan[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_kan_font = finetext_kan[number7]
    #                 para_finetext_kan = textwrap.wrap(finetext_kan_font, width=100)
    #
    #                 draw_finetext_kan = ImageDraw.Draw(background)
    #                 font_family_finetext_kan = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_kan:
    #                     w, h = draw_finetext_kan.textsize(line, font=font_family_finetext_kan)
    #                     draw_finetext_kan.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext_kan)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_kan[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_kan[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #
    #         elif vernac_name_9 == "Tamil":
    #             if slant_tam[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tam[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tam[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tam_font = finetext_tam[number7]
    #                 para_finetext_tam = textwrap.wrap(finetext_tam_font, width=100)
    #
    #                 draw_finetext_tam = ImageDraw.Draw(background)
    #                 font_family_finetext_tam = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tam:
    #                     w, h = draw_finetext_tam.textsize(line, font=font_family_finetext_tam)
    #                     draw_finetext_tam.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tam)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tam[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_tam[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #             # for line in para_3:
    #             #     w, h = draw_3.textsize(line, font=font_family_3)
    #             #     draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_9 == "Telugu":
    #             if slant_tel[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tel[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tel[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tel_font = finetext_tel[number7]
    #                 para_finetext_tel = textwrap.wrap(finetext_tel_font, width=100)
    #
    #                 draw_finetext_tel = ImageDraw.Draw(background)
    #                 font_family_finetext_tel = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tel:
    #                     w, h = draw_finetext_tel.textsize(line, font=font_family_finetext_tel)
    #                     draw_finetext_tel.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tel)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tel[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_tel[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 10. Generate DT X3 --------
    # def FunctionGen10(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_10, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     callout3 = data.Eng_C3.tolist()
    #     slant = data.Eng_Slant_Callout.tolist()
    #     finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     callout3_hin = data.Hindi_C3.tolist()
    #     slant_hin = data.Hindi_Slant_Callout.tolist()
    #     finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     callout3_kan = data.Kannada_C3.tolist()
    #     slant_kan = data.Kannada_Slant_Callout.tolist()
    #     finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     callout3_tam = data.Tamil_C3.tolist()
    #     slant_tam = data.Tamil_Slant_Callout.tolist()
    #     finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     callout3_tel = data.Telugu_C3.tolist()
    #     slant_tel = data.Telugu_Slant_Callout.tolist()
    #     finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 588
    #     maxheight = 545
    #     veralign_height = 757
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_2Grid.jpg")
    #
    #             maxheight = 665
    #             maxwidth = 668
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 668, 665))
    #             background.paste(fsn_cropped, (26, 26), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if vernac_name_10 == "English":
    #             if slant[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_font = finetext[number7]
    #                 para_finetext = textwrap.wrap(finetext_font, width=100)
    #
    #                 draw_finetext = ImageDraw.Draw(background)
    #                 font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #
    #                 for line in para_finetext:
    #                     w, h = draw_finetext.textsize(line, font=font_family_finetext)
    #                     draw_finetext.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 46)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 46)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/Roboto/Roboto-Medium.ttf", 60)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_10 == "Hindi":
    #             if slant_hin[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_hin[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_hin[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_hin_font = finetext_hin[number7]
    #                 para_finetext_hin = textwrap.wrap(finetext_hin_font, width=100)
    #
    #                 draw_finetext_hin = ImageDraw.Draw(background)
    #                 font_family_finetext_hin = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_hin:
    #                     w, h = draw_finetext_hin.textsize(line, font=font_family_finetext_hin)
    #                     draw_finetext_hin.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_hin)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_hin[number7]
    #
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_hin[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_10 == "Kannada":
    #             if slant_kan[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_kan[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_kan[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_kan_font = finetext_kan[number7]
    #                 para_finetext_kan = textwrap.wrap(finetext_kan_font, width=100)
    #
    #                 draw_finetext_kan = ImageDraw.Draw(background)
    #                 font_family_finetext_kan = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_kan:
    #                     w, h = draw_finetext_kan.textsize(line, font=font_family_finetext_kan)
    #                     draw_finetext_kan.text(((bgwidth - 44 - w), 966), line, "#7e7e7e", font=font_family_finetext_kan)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_kan[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_kan[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #
    #         elif vernac_name_10 == "Tamil":
    #             if slant_tam[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tam[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tam[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tam_font = finetext_tam[number7]
    #                 para_finetext_tam = textwrap.wrap(finetext_tam_font, width=100)
    #
    #                 draw_finetext_tam = ImageDraw.Draw(background)
    #                 font_family_finetext_tam = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tam:
    #                     w, h = draw_finetext_tam.textsize(line, font=font_family_finetext_tam)
    #                     draw_finetext_tam.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tam)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tam[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_tam[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #             # for line in para_3:
    #             #     w, h = draw_3.textsize(line, font=font_family_3)
    #             #     draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         elif vernac_name_10 == "Telugu":
    #             if slant_tel[number7] == "--":
    #                 pass
    #             else:
    #                 bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #                 bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #                 bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #                 background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #
    #                 slanttext_font = slant_tel[number7]
    #                 para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #
    #                 draw_slanttext = ImageDraw.Draw(background)
    #                 font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_slanttext:
    #                     w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #                     draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             if finetext_tel[number7] == "--":
    #                 pass
    #             else:
    #                 finetext_tel_font = finetext_tel[number7]
    #                 para_finetext_tel = textwrap.wrap(finetext_tel_font, width=100)
    #
    #                 draw_finetext_tel = ImageDraw.Draw(background)
    #                 font_family_finetext_tel = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_finetext_tel:
    #                     w, h = draw_finetext_tel.textsize(line, font=font_family_finetext_tel)
    #                     draw_finetext_tel.text(((bgwidth - 44 - w), 966), line, "#7e7e7e",
    #                                            font=font_family_finetext_tel)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 908), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 935), (684, 935)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tel[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             callout_3 = callout3_tel[number7]
    #             para_3 = textwrap.wrap(callout_3, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 48, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_3 = ImageDraw.Draw(background)
    #             font_family_3 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 65, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 733), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 805), line, "#606060", font=font_family_2)
    #
    #             for line in para_3:
    #                 w, h = draw_3.textsize(line, font=font_family_3)
    #                 draw_3.text((45, 889), line, "#26a541", font=font_family_3)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 11. Generate Silver (640x720) --------
    # def FunctionGen11(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_11, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     # data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     # data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     # data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     # data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     # data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     # data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     # data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     # data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     # data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     # data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     # callout3 = data.Eng_C3.tolist()
    #     # slant = data.Eng_Slant_Callout.tolist()
    #     # finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     # callout3_hin = data.Hindi_C3.tolist()
    #     # slant_hin = data.Hindi_Slant_Callout.tolist()
    #     # finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     # callout3_kan = data.Kannada_C3.tolist()
    #     # slant_kan = data.Kannada_Slant_Callout.tolist()
    #     # finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     # callout3_tam = data.Tamil_C3.tolist()
    #     # slant_tam = data.Tamil_Slant_Callout.tolist()
    #     # finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     # callout3_tel = data.Telugu_C3.tolist()
    #     # slant_tel = data.Telugu_Slant_Callout.tolist()
    #     # finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 590
    #     maxheight = 506
    #     veralign_height = 537
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             print("Full image is printing")
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_Silver_640.jpg")
    #
    #             maxwidth = 610
    #             maxheight = 506
    #
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 fsn_cropped = fsn.crop((0, 0, 610, 506))
    #                 background.paste(fsn_cropped, (15, 15), fsn_alpha)
    #             elif fsn_w > fsn_h:
    #                 if fsn_w > fsn_h * 1.2055335:
    #                     wpercent = (maxheight / float(fsn.size[1]))
    #                     wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                     fsn = fsn.resize((wsize, maxheight))
    #                     fsn_cropped = fsn.crop((0, 0, 610, 506))
    #                     background.paste(fsn_cropped, (15, 15), fsn_alpha)
    #                 else:
    #                     wpercent = (maxwidth / float(fsn.size[0]))
    #                     hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                     fsn = fsn.resize((maxwidth, hsize))
    #                     fsn_cropped = fsn.crop((0, 0, 610, 506))
    #                     background.paste(fsn_cropped, (15, 15), fsn_alpha)
    #
    #         elif imagesize[number7] == "BottomAlign": # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w >= fsn_h:
    #                 bottom_touch_height = 521
    #
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int(bottom_touch_height-hsize)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 bottom_touch_height = 521
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int(bottom_touch_height-maxheight)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w >= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if vernac_name_11 == "English":
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 48)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 624), line, "#0e45c9", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 656), (606, 656)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#0e45c9", width=3)
    #
    #             callout_1 = callout1[number7]
    #             # callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 48)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 55)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((35, 552), line, "#333231", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((35, 617), line, "#2c4dd4", font=font_family_2)
    #
    #         elif vernac_name_11 == "Hindi":
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 42, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 627), line, "#0e45c9", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 652), (607, 652)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#0e45c9", width=2)
    #
    #             callout_1 = callout1_hin[number7]
    #             # callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 50, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((39, 548), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((39, 606), line, "#2c4dd4", font=font_family_2)
    #
    #         elif vernac_name_11 == "Kannada":
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 48, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 623), line, "#004ed6", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 652), (606, 652)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#004ed6", width=2)
    #
    #             callout_1 = callout1_kan[number7]
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 50, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((36, 564), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((36, 620), line, "#004ed6", font=font_family_2)
    #
    #         elif vernac_name_11 == "Tamil":
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 631), line, "#004ed6", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 657), (606, 657)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#004ed6", width=2)
    #
    #             callout_1 = callout1_tam[number7]
    #             # callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 50, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((35, 555), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((35, 609), line, "#004ed6", font=font_family_2)
    #
    #         elif vernac_name_11 == "Telugu":
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 48, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 623), line, "#004ed6", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 653), (606, 653)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#004ed6", width=2)
    #
    #             callout_1 = callout1_tel[number7]
    #             # callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 50, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((35, 558), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((35, 623), line, "#004ed6", font=font_family_2)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 12. Generate Flash Silver (780x1024) --------
    # def FunctionGen12(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_12, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Lock_Unlock'] = data['Lock_Unlock'].fillna("--")
    #     # data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     # data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     # data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     # data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     # data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     # data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     # data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     # data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     # data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     # data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     locked = data.Lock_Unlock.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     # callout3 = data.Eng_C3.tolist()
    #     # slant = data.Eng_Slant_Callout.tolist()
    #     # finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     # callout3_hin = data.Hindi_C3.tolist()
    #     # slant_hin = data.Hindi_Slant_Callout.tolist()
    #     # finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     # callout3_kan = data.Kannada_C3.tolist()
    #     # slant_kan = data.Kannada_Slant_Callout.tolist()
    #     # finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     # callout3_tam = data.Tamil_C3.tolist()
    #     # slant_tam = data.Tamil_Slant_Callout.tolist()
    #     # finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     # callout3_tel = data.Telugu_C3.tolist()
    #     # slant_tel = data.Telugu_Slant_Callout.tolist()
    #     # finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 600
    #     maxheight = 600
    #     veralign_height = 778
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Flash_Silver.jpg")
    #
    #             maxwidth = 752
    #             maxheight = 751
    #
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 752, 751))
    #             background.paste(fsn_cropped, (15, 15), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if locked[number7] == "Lock":
    #             lock_img = Image.open(fp="Images/Templates/Lock.png")
    #             background.paste(lock_img, (15, 15), lock_img)
    #
    #         if vernac_name_12 == "English":
    #             # if slant[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/2Grid_720x720_slant.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_font = finetext[number7]
    #             #     para_finetext = textwrap.wrap(finetext_font, width=100)
    #             #
    #             #     draw_finetext = ImageDraw.Draw(background)
    #             #     font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #             #
    #             #     for line in para_finetext:
    #             #         w, h = draw_finetext.textsize(line, font=font_family_finetext)
    #             #         draw_finetext.text(((bgwidth - 44 - w), 668), line, "#7e7e7e", font=font_family_finetext)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 45)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 55 - w), 903), line, "#0043ce", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 55 - w), 933), (725, 933)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#0043ce", width=3)
    #
    #             callout_1 = callout1[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 55)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 70)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((65, 809), line, "#302f2e", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((65, 879), line, "#004ed6", font=font_family_2)
    #
    #         elif vernac_name_12 == "Hindi":
    #             # if slant_hin[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_hin[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_hin[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_hin_font = finetext_hin[number7]
    #             #     para_finetext_hin = textwrap.wrap(finetext_hin_font, width=100)
    #             #
    #             #     draw_finetext_hin = ImageDraw.Draw(background)
    #             #     font_family_finetext_hin = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_hin:
    #             #         w, h = draw_finetext_hin.textsize(line, font=font_family_finetext_hin)
    #             #         draw_finetext_hin.text(((bgwidth - 44 - w), 668), line, "#7e7e7e",
    #             #                                font=font_family_finetext_hin)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_hin[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_12 == "Kannada":
    #             # if slant_kan[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_kan[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_kan[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_kan_font = finetext_kan[number7]
    #             #     para_finetext_kan = textwrap.wrap(finetext_kan_font, width=100)
    #             #
    #             #     draw_finetext_kan = ImageDraw.Draw(background)
    #             #     font_family_finetext_kan = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_kan:
    #             #         w, h = draw_finetext_kan.textsize(line, font=font_family_finetext_kan)
    #             #         draw_finetext_kan.text(((bgwidth - 44 - w), 668), line, "#7e7e7e", font=font_family_finetext_kan)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_kan[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_12 == "Tamil":
    #             # if slant_tam[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_tam[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_tam[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_tam_font = finetext_tam[number7]
    #             #     para_finetext_tam = textwrap.wrap(finetext_tam_font, width=100)
    #             #
    #             #     draw_finetext_tam = ImageDraw.Draw(background)
    #             #     font_family_finetext_tam = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_tam:
    #             #         w, h = draw_finetext_tam.textsize(line, font=font_family_finetext_tam)
    #             #         draw_finetext_tam.text(((bgwidth - 44 - w), 668), line, "#7e7e7e",
    #             #                                font=font_family_finetext_tam)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tam[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_12 == "Telugu":
    #             # if slant_tel[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_tel[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_tel[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_tel_font = finetext_tel[number7]
    #             #     para_finetext_tel = textwrap.wrap(finetext_tel_font, width=100)
    #             #
    #             #     draw_finetext_tel = ImageDraw.Draw(background)
    #             #     font_family_finetext_tel = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_tel:
    #             #         w, h = draw_finetext_tel.textsize(line, font=font_family_finetext_tel)
    #             #         draw_finetext_tel.text(((bgwidth - 44 - w), 668), line, "#7e7e7e",
    #             #                                font=font_family_finetext_tel)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tel[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1
    #
    # # 13. Generate Silver (720x720) --------
    # def FunctionGen13(self):
    #     file_path = QFileDialog.getSaveFileName(self.Gen_Card_13, 'Enter Filename & Save File')
    #     final_files = file_path[0]
    #     print(final_files)
    #     data = pandas.read_csv(path_data_1)
    #     # data['FSN2'] = data['FSN2'].fillna("null2")
    #     data['FSN_Size'] = data['FSN_Size'].fillna("Partial")
    #     data['Price_Cut'] = data['Price_Cut'].fillna("--")
    #     data['Lock_Unlock'] = data['Lock_Unlock'].fillna("--")
    #     # data['Eng_Slant_Callout'] = data['Eng_Slant_Callout'].fillna("--")
    #     # data['Hindi_Slant_Callout'] = data['Hindi_Slant_Callout'].fillna("--")
    #     # data['Kannada_Slant_Callout'] = data['Kannada_Slant_Callout'].fillna("--")
    #     # data['Tamil_Slant_Callout'] = data['Tamil_Slant_Callout'].fillna("--")
    #     # data['Telugu_Slant_Callout'] = data['Telugu_Slant_Callout'].fillna("--")
    #     # data['Eng_Fine_Text'] = data['Eng_Fine_Text'].fillna("--")
    #     # data['Hindi_Fine_Text'] = data['Hindi_Fine_Text'].fillna("--")
    #     # data['Kannada_Fine_Text'] = data['Kannada_Fine_Text'].fillna("--")
    #     # data['Tamil_Fine_Text'] = data['Tamil_Fine_Text'].fillna("--")
    #     # data['Telugu_Fine_Text'] = data['Telugu_Fine_Text'].fillna("--")
    #
    #     fsn_names1 = data.POC_FSN.tolist()
    #     imagesize = data.FSN_Size.tolist()
    #     locked = data.Lock_Unlock.tolist()
    #     pricecut = data.Price_Cut.tolist()
    #     callout1 = data.Eng_C1.tolist()
    #     callout2 = data.Eng_C2.tolist()
    #     # callout3 = data.Eng_C3.tolist()
    #     # slant = data.Eng_Slant_Callout.tolist()
    #     # finetext = data.Eng_Fine_Text.tolist()
    #     callout1_hin = data.Hindi_C1.tolist()
    #     callout2_hin = data.Hindi_C2.tolist()
    #     # callout3_hin = data.Hindi_C3.tolist()
    #     # slant_hin = data.Hindi_Slant_Callout.tolist()
    #     # finetext_hin = data.Hindi_Fine_Text.tolist()
    #     callout1_kan = data.Kannada_C1.tolist()
    #     callout2_kan = data.Kannada_C2.tolist()
    #     # callout3_kan = data.Kannada_C3.tolist()
    #     # slant_kan = data.Kannada_Slant_Callout.tolist()
    #     # finetext_kan = data.Kannada_Fine_Text.tolist()
    #     callout1_tam = data.Tamil_C1.tolist()
    #     callout2_tam = data.Tamil_C2.tolist()
    #     # callout3_tam = data.Tamil_C3.tolist()
    #     # slant_tam = data.Tamil_Slant_Callout.tolist()
    #     # finetext_tam = data.Tamil_Fine_Text.tolist()
    #     callout1_tel = data.Telugu_C1.tolist()
    #     callout2_tel = data.Telugu_C2.tolist()
    #     # callout3_tel = data.Telugu_C3.tolist()
    #     # slant_tel = data.Telugu_Slant_Callout.tolist()
    #     # finetext_tel = data.Telugu_Fine_Text.tolist()
    #
    #     d1 = []
    #     d2 = []
    #
    #     maxwidth = 500
    #     maxheight = 350
    #     veralign_height = 564
    #
    #     number1 = 0
    #     number2 = 0
    #     number3 = 0
    #     number4 = 0
    #     number5 = 0
    #     number6 = 0
    #     number7 = 0
    #
    #     filename = str(number7)
    #
    #     while number1 < len(fsn_names1):
    #         fsn_names1[number1] = fsn_names1[number1] + ".png"
    #         number1 = number1 + 1
    #
    #     while number5 < len(fsn_names1):
    #         myimg1 = fsn_names1[number5]
    #         fsn_image1 = Image.open(fp=fsnFolder + myimg1)
    #         fsn_width1, fsn_height1 = fsn_image1.size
    #         number5 = number5 + 1
    #         if fsn_width1 > fsn_height1 * 45:
    #             d1.append("--")
    #         elif fsn_width1 < fsn_height1:
    #             d1.append("1")
    #         elif fsn_width1 > fsn_height1:
    #             d1.append("2")
    #         elif fsn_width1 == fsn_height1:
    #             d1.append("3")
    #
    #     while number7 < len(fsn_names1):
    #         background = Image.open(path_bg_1)
    #         bgwidth, bgheight = background.size
    #
    #         if imagesize[number7] == "Full":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7 + 1)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_alpha = Image.open(fp="Images/Templates/Alpha_2Grid_Intrigue.jpg")
    #
    #             maxwidth = 630
    #             maxheight = 461
    #
    #             fsn_w, fsn_h = fsn.size
    #
    #             if fsn_w <= fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #                 fsn = fsn.resize((maxwidth, hsize))
    #             elif fsn_w > fsn_h:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #                 fsn = fsn.resize((wsize, maxheight))
    #             fsn_cropped = fsn.crop((0, 0, 630, 461))
    #             background.paste(fsn_cropped, (46, 46), fsn_alpha)
    #
    #         else: # elif d1[number7] == "--":
    #             myimg = fsn_names1[number7]
    #             filename = str(number7)
    #             fsn = Image.open(fp=fsnFolder + myimg)
    #             fsn_w, fsn_h = fsn.size
    #
    #             wpercent = (maxheight / float(fsn.size[1]))
    #             wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #             wpercent = (maxwidth / float(fsn.size[0]))
    #             hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #             if fsn_w > fsn_h:
    #                 wpercent = (maxwidth / float(fsn.size[0]))
    #                 hsize = int((float(fsn.size[1]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - maxwidth) / 2)
    #                 center_ver = int((veralign_height - hsize) / 2)
    #
    #                 fsn = fsn.resize((maxwidth, hsize))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #             else:
    #                 wpercent = (maxheight / float(fsn.size[1]))
    #                 wsize = int((float(fsn.size[0]) * float(wpercent)))
    #
    #                 center_hor = int((bgwidth - wsize) / 2)
    #                 center_ver = int((veralign_height - maxheight) / 2)
    #
    #                 fsn = fsn.resize((wsize, maxheight))
    #                 background.paste(fsn, (center_hor, center_ver), fsn)
    #
    #         if locked[number7] == "Lock":
    #             lock_img = Image.open(fp="Images/Templates/Lock_2grid.png")
    #             background.paste(lock_img, (46, 46), lock_img)
    #
    #         if vernac_name_13 == "English":
    #             # if slant[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/2Grid_720x720_slant.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_font = finetext[number7]
    #             #     para_finetext = textwrap.wrap(finetext_font, width=100)
    #             #
    #             #     draw_finetext = ImageDraw.Draw(background)
    #             #     font_family_finetext = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 20)
    #             #
    #             #     for line in para_finetext:
    #             #         w, h = draw_finetext.textsize(line, font=font_family_finetext)
    #             #         draw_finetext.text(((bgwidth - 44 - w), 668), line, "#7e7e7e", font=font_family_finetext)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 44)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 84 - w), 600), line, "#0043ce", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 84 - w), 630), (637, 630)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#0043ce", width=3)
    #
    #             callout_1 = callout1[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 44)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Roboto/Roboto-Bold.ttf", 52)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((65, 535), line, "#302f2e", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((65, 593), line, "#004ed6", font=font_family_2)
    #
    #         elif vernac_name_13 == "Hindi":
    #             # if slant_hin[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_hin[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_hin[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_hin_font = finetext_hin[number7]
    #             #     para_finetext_hin = textwrap.wrap(finetext_hin_font, width=100)
    #             #
    #             #     draw_finetext_hin = ImageDraw.Draw(background)
    #             #     font_family_finetext_hin = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_hin:
    #             #         w, h = draw_finetext_hin.textsize(line, font=font_family_finetext_hin)
    #             #         draw_finetext_hin.text(((bgwidth - 44 - w), 668), line, "#7e7e7e",
    #             #                                font=font_family_finetext_hin)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_hin[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_hin[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/Mukta/Mukta-Regular.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/Mukta/Mukta-SemiBold.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_13 == "Kannada":
    #             # if slant_kan[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_kan[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 40, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_kan[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_kan_font = finetext_kan[number7]
    #             #     para_finetext_kan = textwrap.wrap(finetext_kan_font, width=100)
    #             #
    #             #     draw_finetext_kan = ImageDraw.Draw(background)
    #             #     font_family_finetext_kan = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 20, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_kan:
    #             #         w, h = draw_finetext_kan.textsize(line, font=font_family_finetext_kan)
    #             #         draw_finetext_kan.text(((bgwidth - 44 - w), 668), line, "#7e7e7e", font=font_family_finetext_kan)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_kan[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_kan[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Regular-2020.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansKannada-Bold-2020.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 # w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 # w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_13 == "Tamil":
    #             # if slant_tam[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_tam[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_tam[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_tam_font = finetext_tam[number7]
    #             #     para_finetext_tam = textwrap.wrap(finetext_tam_font, width=100)
    #             #
    #             #     draw_finetext_tam = ImageDraw.Draw(background)
    #             #     font_family_finetext_tam = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_tam:
    #             #         w, h = draw_finetext_tam.textsize(line, font=font_family_finetext_tam)
    #             #         draw_finetext_tam.text(((bgwidth - 44 - w), 668), line, "#7e7e7e",
    #             #                                font=font_family_finetext_tam)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tam[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tam[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-ExtraCondensedMedium-2020.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTamilUI-CondensedSemiBold-2020.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         elif vernac_name_13 == "Telugu":
    #             # if slant_tel[number7] == "--":
    #             #     pass
    #             # else:
    #             #     bg_slanttext = Image.open("Images/Templates/bg_slanttext1.png")
    #             #     bg_slanttext_w, bg_slanttext_h = bg_slanttext.size
    #             #     bg_slanttext_horalign = int((bgwidth - bg_slanttext_w) / 2)
    #             #     background.paste(bg_slanttext, (bg_slanttext_horalign, 26), bg_slanttext)
    #             #
    #             #     slanttext_font = slant_tel[number7]
    #             #     para_slanttext = textwrap.wrap(slanttext_font, width=100)
    #             #
    #             #     draw_slanttext = ImageDraw.Draw(background)
    #             #     font_family_slanttext = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_slanttext:
    #             #         w, h = draw_slanttext.textsize(line, font=font_family_slanttext)
    #             #         draw_slanttext.text(((bgwidth - w) / 2, 29), line, "#5d5d5d", font=font_family_slanttext)
    #
    #             # if finetext_tel[number7] == "--":
    #             #     pass
    #             # else:
    #             #     finetext_tel_font = finetext_tel[number7]
    #             #     para_finetext_tel = textwrap.wrap(finetext_tel_font, width=100)
    #             #
    #             #     draw_finetext_tel = ImageDraw.Draw(background)
    #             #     font_family_finetext_tel = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 20, layout_engine=ImageFont.LAYOUT_RAQM)
    #             #
    #             #     for line in para_finetext_tel:
    #             #         w, h = draw_finetext_tel.textsize(line, font=font_family_finetext_tel)
    #             #         draw_finetext_tel.text(((bgwidth - 44 - w), 668), line, "#7e7e7e",
    #             #                                font=font_family_finetext_tel)
    #
    #             if pricecut[number7] == "--":
    #                 pass
    #             else:
    #                 pricecut_font = pricecut[number7]
    #                 para_pricecut = textwrap.wrap(pricecut_font, width=100)
    #
    #                 draw_pricecut = ImageDraw.Draw(background)
    #                 font_family_pricecut = ImageFont.truetype("Fonts/Roboto/Roboto-Regular.ttf", 40, layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #                 for line in para_pricecut:
    #                     w, h = draw_pricecut.textsize(line, font=font_family_pricecut)
    #                     draw_pricecut.text(((bgwidth - 36 - w), 620), line, "#7e7e7e", font=font_family_pricecut)
    #
    #                     line_shape = [((bgwidth - 36 - w), 637), (684, 637)]
    #                     line_img = ImageDraw.Draw(background)
    #                     line_img.line(line_shape, fill="#7e7e7e", width=3)
    #
    #             callout_1 = callout1_tel[number7]
    #             callout_1 = callout_1[0:18] + "..."
    #             para = textwrap.wrap(callout_1, width=100)
    #
    #             callout_2 = callout2_tel[number7]
    #             para_2 = textwrap.wrap(callout_2, width=100)
    #
    #             max_w = 720
    #
    #             draw_1 = ImageDraw.Draw(background)
    #             font_family_1 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Regular-2020.ttf", 44, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             draw_2 = ImageDraw.Draw(background)
    #             font_family_2 = ImageFont.truetype("Fonts/NotoSans/NotoSansTelugu-Bold-2020.ttf", 60, encoding='utf-8', layout_engine=ImageFont.LAYOUT_RAQM)
    #
    #             for line in para:
    #                 w, h = draw_1.textsize(line, font=font_family_1)
    #                 draw_1.text((45, 532), line, "black", font=font_family_1)
    #
    #             for line in para_2:
    #                 w, h = draw_2.textsize(line, font=font_family_2)
    #                 draw_2.text((45, 605), line, "#26a541", font=font_family_2)
    #
    #         background.save(final_files + filename + '.jpg', quality=100, subsampling=0)
    #         number7 = number7 + 1