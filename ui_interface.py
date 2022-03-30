# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'interfaceQhpcho.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1167, 791)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"	background-color:transparent;\n"
"	background:transparent;\n"
"	padding:0;\n"
"	margin:0;\n"
"	color:#fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #1f232a;\n"
"}\n"
"#leftMenuContainer{\n"
"	background-color: #16191d;\n"
"}\n"
"#leftMenuSubcontainer QPushButton{\n"
"	text-align:left;\n"
"	padding:2px 10px;\n"
"	border-top-left-radius: 10px;\n"
"	border-bottom-left-radius: 10px;\n"
"}\n"
"#centerMenuContainer, #rightMenuContainer{\n"
"	background-color:#2c313c;\n"
"}\n"
"#frame_4, #frame_5{\n"
"	background-color:#16191d;\n"
"	border-radius: 10px;\n"
"}\n"
"#headerContainer{\n"
"	background-color: #2c313c;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.leftMenuContainer.setObjectName(u"leftMenuContainer")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leftMenuContainer.sizePolicy().hasHeightForWidth())
        self.leftMenuContainer.setSizePolicy(sizePolicy)
        self.leftMenuContainer.setMaximumSize(QSize(193, 16777215))
        self.leftMenuContainer.setStyleSheet(u"background-color: #16191d")
        self.verticalLayout = QVBoxLayout(self.leftMenuContainer)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.leftMenuSubcontainer = QWidget(self.leftMenuContainer)
        self.leftMenuSubcontainer.setObjectName(u"leftMenuSubcontainer")
        self.verticalLayout_2 = QVBoxLayout(self.leftMenuSubcontainer)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 0, 0, 0)
        self.frame = QFrame(self.leftMenuSubcontainer)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menuBtn = QPushButton(self.frame)
        self.menuBtn.setObjectName(u"menuBtn")
        icon = QIcon()
        icon.addFile(u":/icons/icons/align-justify.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menuBtn.setIcon(icon)
        self.menuBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_2.addWidget(self.menuBtn)


        self.verticalLayout_2.addWidget(self.frame, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.leftMenuSubcontainer)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 10, 0, 10)
        self.homeBtn = QPushButton(self.frame_2)
        self.homeBtn.setObjectName(u"homeBtn")
        self.homeBtn.setStyleSheet(u"background-color:#1f232a;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.homeBtn.setIcon(icon1)
        self.homeBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.homeBtn)

        self.ExperimentBtn = QPushButton(self.frame_2)
        self.ExperimentBtn.setObjectName(u"ExperimentBtn")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/clipboard.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.ExperimentBtn.setIcon(icon2)
        self.ExperimentBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.ExperimentBtn)

        self.DigitalTwinBtn = QPushButton(self.frame_2)
        self.DigitalTwinBtn.setObjectName(u"DigitalTwinBtn")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.DigitalTwinBtn.setIcon(icon3)
        self.DigitalTwinBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_3.addWidget(self.DigitalTwinBtn)


        self.verticalLayout_2.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.frame_3 = QFrame(self.leftMenuSubcontainer)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 10, 0, 10)
        self.settingBtn = QPushButton(self.frame_3)
        self.settingBtn.setObjectName(u"settingBtn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/icons/settings.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settingBtn.setIcon(icon4)
        self.settingBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.settingBtn)

        self.infoBtn = QPushButton(self.frame_3)
        self.infoBtn.setObjectName(u"infoBtn")
        icon5 = QIcon()
        icon5.addFile(u":/icons/icons/info.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.infoBtn.setIcon(icon5)
        self.infoBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.infoBtn)

        self.helpBtn = QPushButton(self.frame_3)
        self.helpBtn.setObjectName(u"helpBtn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/icons/help-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.helpBtn.setIcon(icon6)
        self.helpBtn.setIconSize(QSize(40, 40))

        self.verticalLayout_4.addWidget(self.helpBtn)


        self.verticalLayout_2.addWidget(self.frame_3, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.leftMenuSubcontainer)


        self.horizontalLayout.addWidget(self.leftMenuContainer, 0, Qt.AlignLeft)

        self.centerMenuContainer = QCustomSlideMenu(self.centralwidget)
        self.centerMenuContainer.setObjectName(u"centerMenuContainer")
        self.centerMenuContainer.setMinimumSize(QSize(0, 0))
        self.centerMenuContainer.setStyleSheet(u"")
        self.verticalLayout_5 = QVBoxLayout(self.centerMenuContainer)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.centerMenuSubcontainer = QFrame(self.centerMenuContainer)
        self.centerMenuSubcontainer.setObjectName(u"centerMenuSubcontainer")
        self.centerMenuSubcontainer.setMinimumSize(QSize(200, 0))
        self.centerMenuSubcontainer.setLayoutDirection(Qt.LeftToRight)
        self.centerMenuSubcontainer.setFrameShape(QFrame.StyledPanel)
        self.centerMenuSubcontainer.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.centerMenuSubcontainer)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.centerMenuSubcontainer)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, -1)
        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.closeCenterMenu = QPushButton(self.frame_4)
        self.closeCenterMenu.setObjectName(u"closeCenterMenu")
        icon7 = QIcon()
        icon7.addFile(u":/icons/icons/x-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeCenterMenu.setIcon(icon7)
        self.closeCenterMenu.setIconSize(QSize(35, 35))

        self.horizontalLayout_3.addWidget(self.closeCenterMenu, 0, Qt.AlignRight)


        self.verticalLayout_6.addWidget(self.frame_4)

        self.MenuStackedWidgets = QCustomStackedWidget(self.centerMenuSubcontainer)
        self.MenuStackedWidgets.setObjectName(u"MenuStackedWidgets")
        self.settingPage = QWidget()
        self.settingPage.setObjectName(u"settingPage")
        self.verticalLayout_7 = QVBoxLayout(self.settingPage)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_2 = QLabel(self.settingPage)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.label_2)

        self.MenuStackedWidgets.addWidget(self.settingPage)
        self.infoPage = QWidget()
        self.infoPage.setObjectName(u"infoPage")
        self.verticalLayout_8 = QVBoxLayout(self.infoPage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_3 = QLabel(self.infoPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.label_3)

        self.MenuStackedWidgets.addWidget(self.infoPage)
        self.helpPage = QWidget()
        self.helpPage.setObjectName(u"helpPage")
        self.verticalLayout_9 = QVBoxLayout(self.helpPage)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_4 = QLabel(self.helpPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_9.addWidget(self.label_4)

        self.MenuStackedWidgets.addWidget(self.helpPage)

        self.verticalLayout_6.addWidget(self.MenuStackedWidgets)


        self.verticalLayout_5.addWidget(self.centerMenuSubcontainer, 0, Qt.AlignLeft)


        self.horizontalLayout.addWidget(self.centerMenuContainer)

        self.mainBodyContainer = QWidget(self.centralwidget)
        self.mainBodyContainer.setObjectName(u"mainBodyContainer")
        sizePolicy.setHeightForWidth(self.mainBodyContainer.sizePolicy().hasHeightForWidth())
        self.mainBodyContainer.setSizePolicy(sizePolicy)
        self.mainBodyContainer.setStyleSheet(u"")
        self.verticalLayout_10 = QVBoxLayout(self.mainBodyContainer)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.headerContainer = QWidget(self.mainBodyContainer)
        self.headerContainer.setObjectName(u"headerContainer")
        self.horizontalLayout_4 = QHBoxLayout(self.headerContainer)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.widget = QWidget(self.headerContainer)
        self.widget.setObjectName(u"widget")
        font1 = QFont()
        font1.setFamily(u"AcmeFont")
        font1.setPointSize(24)
        font1.setBold(True)
        font1.setWeight(75)
        self.widget.setFont(font1)
        self.horizontalLayout_6 = QHBoxLayout(self.widget)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(110, 70))
        self.label_5.setPixmap(QPixmap(u":/image/logo.png"))
        self.label_5.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.label_5)

        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        font2 = QFont()
        font2.setFamily(u"Trebuchet MS")
        font2.setPointSize(18)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_6.setFont(font2)

        self.horizontalLayout_6.addWidget(self.label_6)


        self.horizontalLayout_4.addWidget(self.widget, 0, Qt.AlignLeft)

        self.widget_2 = QWidget(self.headerContainer)
        self.widget_2.setObjectName(u"widget_2")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_7.setSpacing(30)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.pushButton_6 = QPushButton(self.widget_2)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon8 = QIcon()
        icon8.addFile(u":/icons/icons/gitlab.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon8)
        self.pushButton_6.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.pushButton_6)

        self.rightContainerBtn = QPushButton(self.widget_2)
        self.rightContainerBtn.setObjectName(u"rightContainerBtn")
        icon9 = QIcon()
        icon9.addFile(u":/icons/icons/users.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.rightContainerBtn.setIcon(icon9)
        self.rightContainerBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_7.addWidget(self.rightContainerBtn)


        self.horizontalLayout_4.addWidget(self.widget_2, 0, Qt.AlignHCenter)

        self.widget_3 = QWidget(self.headerContainer)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout_5 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.widget_3)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon10 = QIcon()
        icon10.addFile(u":/icons/icons/minus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon10)
        self.minimize_window_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.minimize_window_button)

        self.restore_window_button = QPushButton(self.widget_3)
        self.restore_window_button.setObjectName(u"restore_window_button")
        self.restore_window_button.setMaximumSize(QSize(110, 70))
        icon11 = QIcon()
        icon11.addFile(u":/icons/icons/square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon11)
        self.restore_window_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.restore_window_button)

        self.close_window_button = QPushButton(self.widget_3)
        self.close_window_button.setObjectName(u"close_window_button")
        icon12 = QIcon()
        icon12.addFile(u":/icons/icons/x.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_window_button.setIcon(icon12)
        self.close_window_button.setIconSize(QSize(35, 35))

        self.horizontalLayout_5.addWidget(self.close_window_button)


        self.horizontalLayout_4.addWidget(self.widget_3, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.headerContainer, 0, Qt.AlignTop)

        self.mainBodySubContainer = QWidget(self.mainBodyContainer)
        self.mainBodySubContainer.setObjectName(u"mainBodySubContainer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.mainBodySubContainer.sizePolicy().hasHeightForWidth())
        self.mainBodySubContainer.setSizePolicy(sizePolicy1)
        self.mainBodySubContainer.setMinimumSize(QSize(0, 0))
        self.mainBodySubContainer.setStyleSheet(u"")
        self.horizontalLayout_8 = QHBoxLayout(self.mainBodySubContainer)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.mainContentsContainer = QWidget(self.mainBodySubContainer)
        self.mainContentsContainer.setObjectName(u"mainContentsContainer")
        self.mainContentsContainer.setStyleSheet(u"background-color: #16191d")
        self.verticalLayout_15 = QVBoxLayout(self.mainContentsContainer)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.centerStackedWidgets = QCustomStackedWidget(self.mainContentsContainer)
        self.centerStackedWidgets.setObjectName(u"centerStackedWidgets")
        self.homePage = QWidget()
        self.homePage.setObjectName(u"homePage")
        self.verticalLayout_17 = QVBoxLayout(self.homePage)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_10 = QLabel(self.homePage)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout_17.addWidget(self.label_10)

        self.centerStackedWidgets.addWidget(self.homePage)
        self.ExperimentPage = QWidget()
        self.ExperimentPage.setObjectName(u"ExperimentPage")
        self.verticalLayout_18 = QVBoxLayout(self.ExperimentPage)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_12 = QLabel(self.ExperimentPage)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout_18.addWidget(self.label_12)

        self.centerStackedWidgets.addWidget(self.ExperimentPage)
        self.dtPage = QWidget()
        self.dtPage.setObjectName(u"dtPage")
        self.verticalLayout_16 = QVBoxLayout(self.dtPage)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_13 = QLabel(self.dtPage)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout_16.addWidget(self.label_13)

        self.centerStackedWidgets.addWidget(self.dtPage)

        self.verticalLayout_15.addWidget(self.centerStackedWidgets)


        self.horizontalLayout_8.addWidget(self.mainContentsContainer)

        self.rightMenuContainer = QCustomSlideMenu(self.mainBodySubContainer)
        self.rightMenuContainer.setObjectName(u"rightMenuContainer")
        self.rightMenuContainer.setMinimumSize(QSize(200, 0))
        self.rightMenuContainer.setMaximumSize(QSize(16777215, 9999999))
        self.verticalLayout_11 = QVBoxLayout(self.rightMenuContainer)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.widget_6 = QWidget(self.rightMenuContainer)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_12 = QVBoxLayout(self.widget_6)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.widget_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_7 = QLabel(self.frame_5)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setScaledContents(False)
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_7, 0, Qt.AlignLeft)

        self.closeRightMenuBtn = QPushButton(self.frame_5)
        self.closeRightMenuBtn.setObjectName(u"closeRightMenuBtn")
        icon13 = QIcon()
        icon13.addFile(u":/icons/icons/x-square.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeRightMenuBtn.setIcon(icon13)
        self.closeRightMenuBtn.setIconSize(QSize(35, 35))

        self.horizontalLayout_9.addWidget(self.closeRightMenuBtn, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.frame_5)

        self.rightStackWidgets = QCustomStackedWidget(self.widget_6)
        self.rightStackWidgets.setObjectName(u"rightStackWidgets")
        self.morePage = QWidget()
        self.morePage.setObjectName(u"morePage")
        self.morePage.setMaximumSize(QSize(2000, 2000))
        self.verticalLayout_13 = QVBoxLayout(self.morePage)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_8 = QLabel(self.morePage)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_13.addWidget(self.label_8)

        self.rightStackWidgets.addWidget(self.morePage)
        self.profilePage = QWidget()
        self.profilePage.setObjectName(u"profilePage")
        self.verticalLayout_14 = QVBoxLayout(self.profilePage)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_9 = QLabel(self.profilePage)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.label_9)

        self.rightStackWidgets.addWidget(self.profilePage)

        self.verticalLayout_12.addWidget(self.rightStackWidgets)


        self.verticalLayout_11.addWidget(self.widget_6)


        self.horizontalLayout_8.addWidget(self.rightMenuContainer, 0, Qt.AlignRight)


        self.verticalLayout_10.addWidget(self.mainBodySubContainer)

        self.footContainer = QFrame(self.mainBodyContainer)
        self.footContainer.setObjectName(u"footContainer")
        self.footContainer.setStyleSheet(u"background-color: #16191d")
        self.footContainer.setFrameShape(QFrame.StyledPanel)
        self.footContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.footContainer)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.notficationContainer = QFrame(self.footContainer)
        self.notficationContainer.setObjectName(u"notficationContainer")
        self.notficationContainer.setFrameShape(QFrame.StyledPanel)
        self.notficationContainer.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.notficationContainer)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_11 = QLabel(self.notficationContainer)
        self.label_11.setObjectName(u"label_11")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy2)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_11)

        self.closeNotificationBtn = QPushButton(self.notficationContainer)
        self.closeNotificationBtn.setObjectName(u"closeNotificationBtn")
        icon14 = QIcon()
        icon14.addFile(u":/icons/icons/arrow-down-left.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.closeNotificationBtn.setIcon(icon14)
        self.closeNotificationBtn.setIconSize(QSize(40, 40))

        self.horizontalLayout_11.addWidget(self.closeNotificationBtn)


        self.horizontalLayout_10.addWidget(self.notficationContainer)

        self.sizeGrip = QFrame(self.footContainer)
        self.sizeGrip.setObjectName(u"sizeGrip")
        self.sizeGrip.setMinimumSize(QSize(50, 50))
        self.sizeGrip.setMaximumSize(QSize(50, 50))
        self.sizeGrip.setFrameShape(QFrame.StyledPanel)
        self.sizeGrip.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.sizeGrip)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.pushButton_2 = QPushButton(self.sizeGrip)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(28, 28))
        icon15 = QIcon()
        icon15.addFile(u":/icons/icons/maximize-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon15)
        self.pushButton_2.setIconSize(QSize(35, 35))

        self.verticalLayout_19.addWidget(self.pushButton_2)


        self.horizontalLayout_10.addWidget(self.sizeGrip)


        self.verticalLayout_10.addWidget(self.footContainer)


        self.horizontalLayout.addWidget(self.mainBodyContainer)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.centerStackedWidgets.setCurrentIndex(2)
        self.rightStackWidgets.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        self.menuBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Menu", None))
#endif // QT_CONFIG(tooltip)
        self.menuBtn.setText("")
#if QT_CONFIG(tooltip)
        self.homeBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Home", None))
#endif // QT_CONFIG(tooltip)
        self.homeBtn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
#if QT_CONFIG(tooltip)
        self.ExperimentBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Experiment", None))
#endif // QT_CONFIG(tooltip)
        self.ExperimentBtn.setText(QCoreApplication.translate("MainWindow", u"Experiment Design", None))
#if QT_CONFIG(tooltip)
        self.DigitalTwinBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Digital Twin", None))
#endif // QT_CONFIG(tooltip)
        self.DigitalTwinBtn.setText(QCoreApplication.translate("MainWindow", u"Digital Twin", None))
#if QT_CONFIG(tooltip)
        self.settingBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Go to Setting", None))
#endif // QT_CONFIG(tooltip)
        self.settingBtn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
#if QT_CONFIG(tooltip)
        self.infoBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Information", None))
#endif // QT_CONFIG(tooltip)
        self.infoBtn.setText(QCoreApplication.translate("MainWindow", u"Information", None))
#if QT_CONFIG(tooltip)
        self.helpBtn.setToolTip(QCoreApplication.translate("MainWindow", u"Get help", None))
#endif // QT_CONFIG(tooltip)
        self.helpBtn.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"More Menu", None))
        self.closeCenterMenu.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Information", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Help", None))
        self.label_5.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Frida", None))
        self.pushButton_6.setText("")
        self.rightContainerBtn.setText("")
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_window_button.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Experiment", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Digital Twin", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Right Menu", None))
        self.closeRightMenuBtn.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"More...", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Profile", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Notification Message", None))
        self.closeNotificationBtn.setText("")
        self.pushButton_2.setText("")
    # retranslateUi

