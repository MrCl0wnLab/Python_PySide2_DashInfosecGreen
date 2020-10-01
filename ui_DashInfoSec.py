# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'DashInfoSecZuArnP.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1752, 1234)
        icon = QIcon()
        icon.addFile(u":/icons/view.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_LeftControlBar = QFrame(self.centralwidget)
        self.frame_LeftControlBar.setObjectName(u"frame_LeftControlBar")
        self.frame_LeftControlBar.setMinimumSize(QSize(200, 0))
        self.frame_LeftControlBar.setMaximumSize(QSize(200, 16777215))
        self.frame_LeftControlBar.setStyleSheet(u"QFrame{\n"
"background-color: #ffffff;\n"
"border:1px solid #edf2fa;\n"
"}")
        self.frame_LeftControlBar.setFrameShape(QFrame.StyledPanel)
        self.frame_LeftControlBar.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame_LeftControlBar)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 9, 0, -1)
        self.frame_Logo = QFrame(self.frame_LeftControlBar)
        self.frame_Logo.setObjectName(u"frame_Logo")
        self.frame_Logo.setMinimumSize(QSize(0, 100))
        self.frame_Logo.setMaximumSize(QSize(16777215, 100))
        self.frame_Logo.setStyleSheet(u"QFrame{\n"
"	background-color:#fff;\n"
"	border:0px;\n"
"	color:#070000;\n"
"}\n"
"")
        self.frame_Logo.setFrameShape(QFrame.StyledPanel)
        self.frame_Logo.setFrameShadow(QFrame.Raised)
        self.label_LogoNameDesc = QLabel(self.frame_Logo)
        self.label_LogoNameDesc.setObjectName(u"label_LogoNameDesc")
        self.label_LogoNameDesc.setGeometry(QRect(0, 60, 191, 15))
        self.label_LogoNameDesc.setMaximumSize(QSize(16777215, 15))
        self.label_LogoNameDesc.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:16px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")
        self.label_LogoNameDesc.setAlignment(Qt.AlignCenter)
        self.label_LogoName = QLabel(self.frame_Logo)
        self.label_LogoName.setObjectName(u"label_LogoName")
        self.label_LogoName.setGeometry(QRect(0, 20, 191, 42))
        self.label_LogoName.setStyleSheet(u"QLabel{\n"
"color:#04c9b7;\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"  text-align:center;\n"
"\n"
"}")
        self.label_LogoName.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.frame_Logo)

        self.pushButton_DashBoard = QPushButton(self.frame_LeftControlBar)
        self.pushButton_DashBoard.setObjectName(u"pushButton_DashBoard")
        self.pushButton_DashBoard.setMinimumSize(QSize(0, 50))
        self.pushButton_DashBoard.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_DashBoard.setStyleSheet(u"QPushButton{\n"
"	background-color:#e5faf8;\n"
"	border:0px;\n"
"	color:#0bc9b7;\n"
"    font-weight: bold;\n"
"font-size:15px;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/stopwatch-3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_DashBoard.setIcon(icon1)
        self.pushButton_DashBoard.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_DashBoard)

        self.pushButton_QuickStart = QPushButton(self.frame_LeftControlBar)
        self.pushButton_QuickStart.setObjectName(u"pushButton_QuickStart")
        self.pushButton_QuickStart.setMinimumSize(QSize(0, 50))
        self.pushButton_QuickStart.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_QuickStart.setStyleSheet(u"QPushButton{\n"
"	background-color:#fff;\n"
"	border:0px;\n"
"	color:#070000;\n"
"font-size:15px;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#e5faf8;\n"
"	border:0px;\n"
"	color:#070000;\n"
"    font-weight: bold;\n"
"font-size:15px;\n"
"text-align:left;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u":/icons/target.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_QuickStart.setIcon(icon2)
        self.pushButton_QuickStart.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_QuickStart)

        self.pushButton_Assets = QPushButton(self.frame_LeftControlBar)
        self.pushButton_Assets.setObjectName(u"pushButton_Assets")
        self.pushButton_Assets.setMinimumSize(QSize(0, 50))
        self.pushButton_Assets.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Assets.setStyleSheet(u"QPushButton{\n"
"	background-color:#fff;\n"
"	border:0px;\n"
"	color:#070000;\n"
"font-size:15px;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#e5faf8;\n"
"	border:0px;\n"
"	color:#070000;\n"
"    font-weight: bold;\n"
"font-size:15px;\n"
"text-align:left;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u":/icons/windows-4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Assets.setIcon(icon3)
        self.pushButton_Assets.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_Assets)

        self.pushButton_Report = QPushButton(self.frame_LeftControlBar)
        self.pushButton_Report.setObjectName(u"pushButton_Report")
        self.pushButton_Report.setMinimumSize(QSize(0, 50))
        self.pushButton_Report.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Report.setStyleSheet(u"QPushButton{\n"
"	background-color:#fff;\n"
"	border:0px;\n"
"	color:#070000;\n"
"font-size:15px;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#e5faf8;\n"
"	border:0px;\n"
"	color:#070000;\n"
"    font-weight: bold;\n"
"font-size:15px;\n"
"text-align:left;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/icons/list.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Report.setIcon(icon4)
        self.pushButton_Report.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_Report)

        self.pushButton_Config = QPushButton(self.frame_LeftControlBar)
        self.pushButton_Config.setObjectName(u"pushButton_Config")
        self.pushButton_Config.setMinimumSize(QSize(0, 50))
        self.pushButton_Config.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_Config.setStyleSheet(u"QPushButton{\n"
"	background-color:#fff;\n"
"	border:0px;\n"
"	color:#070000;\n"
"font-size:15px;\n"
"text-align:left;\n"
"padding-left:10px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#e5faf8;\n"
"	border:0px;\n"
"	color:#070000;\n"
"    font-weight: bold;\n"
"font-size:15px;\n"
"text-align:left;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/icons/settings-5.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Config.setIcon(icon5)
        self.pushButton_Config.setIconSize(QSize(20, 20))

        self.verticalLayout.addWidget(self.pushButton_Config)

        self.frame_LeftControlBarSpace = QFrame(self.frame_LeftControlBar)
        self.frame_LeftControlBarSpace.setObjectName(u"frame_LeftControlBarSpace")
        self.frame_LeftControlBarSpace.setStyleSheet(u"QFrame{\n"
"\n"
"border:0px;\n"
"}")
        self.frame_LeftControlBarSpace.setFrameShape(QFrame.StyledPanel)
        self.frame_LeftControlBarSpace.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_LeftControlBarSpace)
        self.formLayout.setObjectName(u"formLayout")

        self.verticalLayout.addWidget(self.frame_LeftControlBarSpace)

        self.pushButton_About = QPushButton(self.frame_LeftControlBar)
        self.pushButton_About.setObjectName(u"pushButton_About")
        self.pushButton_About.setMinimumSize(QSize(0, 50))
        self.pushButton_About.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_About.setStyleSheet(u"QPushButton{\n"
"	background-color:#fff;\n"
"	border:0px;\n"
"	color:rgb(186, 189, 182);\n"
"\n"
"font-size:15px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	background-color:#e5faf8;\n"
"	border:0px;\n"
"	color:#070000;\n"
"    font-weight: bold;\n"
"font-size:15px;\n"
"}")

        self.verticalLayout.addWidget(self.pushButton_About)


        self.horizontalLayout.addWidget(self.frame_LeftControlBar)

        self.frame_Control = QFrame(self.centralwidget)
        self.frame_Control.setObjectName(u"frame_Control")
        self.frame_Control.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_Control.setFrameShape(QFrame.StyledPanel)
        self.frame_Control.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_Control)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(9, 9, 9, 9)
        self.frame_TopBar = QFrame(self.frame_Control)
        self.frame_TopBar.setObjectName(u"frame_TopBar")
        self.frame_TopBar.setMinimumSize(QSize(0, 55))
        self.frame_TopBar.setMaximumSize(QSize(16777215, 55))
        self.frame_TopBar.setLayoutDirection(Qt.RightToLeft)
        self.frame_TopBar.setStyleSheet(u"QFrame{\n"
"background-color: #ffffff;\n"
"border:1px solid #edf2fa;\n"
"}")
        self.frame_TopBar.setFrameShape(QFrame.StyledPanel)
        self.frame_TopBar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_TopBar)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_PerfilName = QLabel(self.frame_TopBar)
        self.label_PerfilName.setObjectName(u"label_PerfilName")
        self.label_PerfilName.setMaximumSize(QSize(110, 16777215))
        self.label_PerfilName.setStyleSheet(u"QLabel{\n"
"color:rgb(204, 207, 211);\n"
"	font-size:15px;\n"
"	border:0px;\n"
"\n"
"}\n"
"\n"
"")
        self.label_PerfilName.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_PerfilName)

        self.pushButton_Perfil = QPushButton(self.frame_TopBar)
        self.pushButton_Perfil.setObjectName(u"pushButton_Perfil")
        self.pushButton_Perfil.setMinimumSize(QSize(30, 30))
        self.pushButton_Perfil.setMaximumSize(QSize(30, 30))
        self.pushButton_Perfil.setStyleSheet(u"QPushButton{\n"
"background-color:#e5faf8;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon6 = QIcon()
        icon6.addFile(u":/icons/user-3.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Perfil.setIcon(icon6)
        self.pushButton_Perfil.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_Perfil)

        self.pushButton_Notifications = QPushButton(self.frame_TopBar)
        self.pushButton_Notifications.setObjectName(u"pushButton_Notifications")
        self.pushButton_Notifications.setMinimumSize(QSize(50, 30))
        self.pushButton_Notifications.setMaximumSize(QSize(50, 30))
        self.pushButton_Notifications.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_Notifications.setStyleSheet(u"QPushButton{\n"
"background-color:#e5faf8;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon7 = QIcon()
        icon7.addFile(u":/icons/alarm.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_Notifications.setIcon(icon7)
        self.pushButton_Notifications.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_Notifications)

        self.frame_TopBarSpace = QFrame(self.frame_TopBar)
        self.frame_TopBarSpace.setObjectName(u"frame_TopBarSpace")
        self.frame_TopBarSpace.setStyleSheet(u"QFrame{border:0px;}")
        self.frame_TopBarSpace.setFrameShape(QFrame.StyledPanel)
        self.frame_TopBarSpace.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_TopBarSpace)

        self.label_LastAccess = QLabel(self.frame_TopBar)
        self.label_LastAccess.setObjectName(u"label_LastAccess")
        self.label_LastAccess.setMinimumSize(QSize(160, 0))
        self.label_LastAccess.setMaximumSize(QSize(250, 16777215))
        self.label_LastAccess.setStyleSheet(u"QLabel{\n"
"color:rgb(204, 207, 211);\n"
"	font-size:15px;\n"
"	border:0px;\n"
"\n"
"}\n"
"\n"
"")
        self.label_LastAccess.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_LastAccess)

        self.pushButton_LastAccess = QPushButton(self.frame_TopBar)
        self.pushButton_LastAccess.setObjectName(u"pushButton_LastAccess")
        self.pushButton_LastAccess.setMinimumSize(QSize(30, 30))
        self.pushButton_LastAccess.setMaximumSize(QSize(30, 30))
        self.pushButton_LastAccess.setStyleSheet(u"QPushButton{\n"
"background-color:#e5faf8;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon8 = QIcon()
        icon8.addFile(u":/icons/clock-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_LastAccess.setIcon(icon8)
        self.pushButton_LastAccess.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_LastAccess)

        self.label_IpInfo = QLabel(self.frame_TopBar)
        self.label_IpInfo.setObjectName(u"label_IpInfo")
        self.label_IpInfo.setMinimumSize(QSize(160, 0))
        self.label_IpInfo.setMaximumSize(QSize(250, 16777215))
        self.label_IpInfo.setStyleSheet(u"QLabel{\n"
"color:rgb(204, 207, 211);\n"
"	font-size:15px;\n"
"	border:0px;\n"
"\n"
"}\n"
"\n"
"")
        self.label_IpInfo.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_5.addWidget(self.label_IpInfo)

        self.pushButton_InfoIo = QPushButton(self.frame_TopBar)
        self.pushButton_InfoIo.setObjectName(u"pushButton_InfoIo")
        self.pushButton_InfoIo.setMinimumSize(QSize(30, 30))
        self.pushButton_InfoIo.setMaximumSize(QSize(30, 30))
        self.pushButton_InfoIo.setStyleSheet(u"QPushButton{\n"
"background-color:#e5faf8;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/icons/placeholder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_InfoIo.setIcon(icon9)
        self.pushButton_InfoIo.setIconSize(QSize(20, 20))

        self.horizontalLayout_5.addWidget(self.pushButton_InfoIo)


        self.verticalLayout_8.addWidget(self.frame_TopBar)

        self.stackedWidget_Control = QStackedWidget(self.frame_Control)
        self.stackedWidget_Control.setObjectName(u"stackedWidget_Control")
        self.stackedWidget_Control.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"\n"
"}")
        self.page_DashBoard = QWidget()
        self.page_DashBoard.setObjectName(u"page_DashBoard")
        self.page_DashBoard.setStyleSheet(u"QWidget{\n"
"	background-color:#fafbfd;\n"
"    border:0px;\n"
"}")
        self.verticalLayout_9 = QVBoxLayout(self.page_DashBoard)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_CentralControl = QFrame(self.page_DashBoard)
        self.frame_CentralControl.setObjectName(u"frame_CentralControl")
        self.frame_CentralControl.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_CentralControl.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralControl.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_CentralControl)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_CentralControl)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_Hello = QLabel(self.frame)
        self.label_Hello.setObjectName(u"label_Hello")
        self.label_Hello.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"\n"
"}")

        self.horizontalLayout_4.addWidget(self.label_Hello)


        self.verticalLayout_2.addWidget(self.frame)

        self.frame_CentralTop = QFrame(self.frame_CentralControl)
        self.frame_CentralTop.setObjectName(u"frame_CentralTop")
        self.frame_CentralTop.setMinimumSize(QSize(0, 220))
        self.frame_CentralTop.setMaximumSize(QSize(16777215, 220))
        self.frame_CentralTop.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralTop.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_CentralTop)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame_DashHostDiscovered = QFrame(self.frame_CentralTop)
        self.frame_DashHostDiscovered.setObjectName(u"frame_DashHostDiscovered")
        self.frame_DashHostDiscovered.setLayoutDirection(Qt.LeftToRight)
        self.frame_DashHostDiscovered.setStyleSheet(u"QFrame{\n"
"border:1px solid #edf2fa;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"text-align:center;\n"
"}")
        self.frame_DashHostDiscovered.setFrameShape(QFrame.StyledPanel)
        self.frame_DashHostDiscovered.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_DashHostDiscovered)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_DashHostDiscovered = QLabel(self.frame_DashHostDiscovered)
        self.label_DashHostDiscovered.setObjectName(u"label_DashHostDiscovered")
        self.label_DashHostDiscovered.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:20px;\n"
"	border:0px;\n"
"\n"
"}")
        self.label_DashHostDiscovered.setAlignment(Qt.AlignCenter)

        self.verticalLayout_19.addWidget(self.label_DashHostDiscovered)

        self.frame_8 = QFrame(self.frame_DashHostDiscovered)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame{border:0px;}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.pushButton_DashHostDiscovered = QPushButton(self.frame_8)
        self.pushButton_DashHostDiscovered.setObjectName(u"pushButton_DashHostDiscovered")
        self.pushButton_DashHostDiscovered.setMinimumSize(QSize(0, 65))
        self.pushButton_DashHostDiscovered.setLayoutDirection(Qt.LeftToRight)
        self.pushButton_DashHostDiscovered.setStyleSheet(u"QPushButton{\n"
"background-color:#04c9b7;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/icons/star-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_DashHostDiscovered.setIcon(icon10)
        self.pushButton_DashHostDiscovered.setIconSize(QSize(55, 55))

        self.horizontalLayout_16.addWidget(self.pushButton_DashHostDiscovered)

        self.label_CountDashHostDiscovered = QLabel(self.frame_8)
        self.label_CountDashHostDiscovered.setObjectName(u"label_CountDashHostDiscovered")
        self.label_CountDashHostDiscovered.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:30px;\n"
"	border:0px;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.label_CountDashHostDiscovered.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.label_CountDashHostDiscovered)


        self.verticalLayout_19.addWidget(self.frame_8)

        self.frame_Line = QFrame(self.frame_DashHostDiscovered)
        self.frame_Line.setObjectName(u"frame_Line")
        self.frame_Line.setMaximumSize(QSize(16777215, 1))
        self.frame_Line.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
"background-color:#edf2fa;\n"
"border-radius:0px;\n"
"}")
        self.frame_Line.setFrameShape(QFrame.StyledPanel)
        self.frame_Line.setFrameShadow(QFrame.Raised)

        self.verticalLayout_19.addWidget(self.frame_Line)

        self.label_DescDashHostDiscovered = QLabel(self.frame_DashHostDiscovered)
        self.label_DescDashHostDiscovered.setObjectName(u"label_DescDashHostDiscovered")
        self.label_DescDashHostDiscovered.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:16px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_19.addWidget(self.label_DescDashHostDiscovered)


        self.horizontalLayout_2.addWidget(self.frame_DashHostDiscovered)

        self.frame_CentralSpace1 = QFrame(self.frame_CentralTop)
        self.frame_CentralSpace1.setObjectName(u"frame_CentralSpace1")
        self.frame_CentralSpace1.setMaximumSize(QSize(10, 16777215))
        self.frame_CentralSpace1.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralSpace1.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_CentralSpace1)

        self.frame_DashScanExecuted = QFrame(self.frame_CentralTop)
        self.frame_DashScanExecuted.setObjectName(u"frame_DashScanExecuted")
        self.frame_DashScanExecuted.setStyleSheet(u"QFrame{\n"
"border:1px solid #edf2fa;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"}")
        self.frame_DashScanExecuted.setFrameShape(QFrame.StyledPanel)
        self.frame_DashScanExecuted.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_DashScanExecuted)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_DashScanExecuted = QLabel(self.frame_DashScanExecuted)
        self.label_DashScanExecuted.setObjectName(u"label_DashScanExecuted")
        self.label_DashScanExecuted.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:20px;\n"
"	border:0px;\n"
"\n"
"}")
        self.label_DashScanExecuted.setAlignment(Qt.AlignCenter)

        self.verticalLayout_20.addWidget(self.label_DashScanExecuted)

        self.frame_9 = QFrame(self.frame_DashScanExecuted)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setStyleSheet(u"QFrame{border:0px;}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.pushButton_DashScanExecuted = QPushButton(self.frame_9)
        self.pushButton_DashScanExecuted.setObjectName(u"pushButton_DashScanExecuted")
        self.pushButton_DashScanExecuted.setMinimumSize(QSize(0, 65))
        self.pushButton_DashScanExecuted.setStyleSheet(u"QPushButton{\n"
"background-color:#04c9b7;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon11 = QIcon()
        icon11.addFile(u":/icons/search-1.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_DashScanExecuted.setIcon(icon11)
        self.pushButton_DashScanExecuted.setIconSize(QSize(55, 55))

        self.horizontalLayout_17.addWidget(self.pushButton_DashScanExecuted)

        self.label_CountDashScanExecuted = QLabel(self.frame_9)
        self.label_CountDashScanExecuted.setObjectName(u"label_CountDashScanExecuted")
        self.label_CountDashScanExecuted.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:30px;\n"
"	border:0px;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.label_CountDashScanExecuted.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.label_CountDashScanExecuted)


        self.verticalLayout_20.addWidget(self.frame_9)

        self.frame_Line_3 = QFrame(self.frame_DashScanExecuted)
        self.frame_Line_3.setObjectName(u"frame_Line_3")
        self.frame_Line_3.setMaximumSize(QSize(16777215, 1))
        self.frame_Line_3.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
"background-color:#edf2fa;\n"
"border-radius:0px;\n"
"}")
        self.frame_Line_3.setFrameShape(QFrame.StyledPanel)
        self.frame_Line_3.setFrameShadow(QFrame.Raised)

        self.verticalLayout_20.addWidget(self.frame_Line_3)

        self.label_DescDashScanExecuted = QLabel(self.frame_DashScanExecuted)
        self.label_DescDashScanExecuted.setObjectName(u"label_DescDashScanExecuted")
        self.label_DescDashScanExecuted.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:16px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_20.addWidget(self.label_DescDashScanExecuted)


        self.horizontalLayout_2.addWidget(self.frame_DashScanExecuted)

        self.frame_CentralSpace2 = QFrame(self.frame_CentralTop)
        self.frame_CentralSpace2.setObjectName(u"frame_CentralSpace2")
        self.frame_CentralSpace2.setMaximumSize(QSize(10, 16777215))
        self.frame_CentralSpace2.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralSpace2.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_CentralSpace2)

        self.frame_DashDomains = QFrame(self.frame_CentralTop)
        self.frame_DashDomains.setObjectName(u"frame_DashDomains")
        self.frame_DashDomains.setStyleSheet(u"QFrame{\n"
"border:1px solid #edf2fa;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"}")
        self.frame_DashDomains.setFrameShape(QFrame.StyledPanel)
        self.frame_DashDomains.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_DashDomains)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_DashDomains = QLabel(self.frame_DashDomains)
        self.label_DashDomains.setObjectName(u"label_DashDomains")
        self.label_DashDomains.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:20px;\n"
"	border:0px;\n"
"\n"
"}")
        self.label_DashDomains.setAlignment(Qt.AlignCenter)

        self.verticalLayout_21.addWidget(self.label_DashDomains)

        self.frame_10 = QFrame(self.frame_DashDomains)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setStyleSheet(u"QFrame{border:0px;}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.pushButton_DashDomains = QPushButton(self.frame_10)
        self.pushButton_DashDomains.setObjectName(u"pushButton_DashDomains")
        self.pushButton_DashDomains.setMinimumSize(QSize(0, 65))
        self.pushButton_DashDomains.setStyleSheet(u"QPushButton{\n"
"background-color:#04c9b7;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon12 = QIcon()
        icon12.addFile(u":/icons/cloud-computing-4.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_DashDomains.setIcon(icon12)
        self.pushButton_DashDomains.setIconSize(QSize(55, 55))

        self.horizontalLayout_18.addWidget(self.pushButton_DashDomains)

        self.label_CountDashDomains = QLabel(self.frame_10)
        self.label_CountDashDomains.setObjectName(u"label_CountDashDomains")
        self.label_CountDashDomains.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:30px;\n"
"	border:0px;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.label_CountDashDomains.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.label_CountDashDomains)


        self.verticalLayout_21.addWidget(self.frame_10)

        self.frame_Line_6 = QFrame(self.frame_DashDomains)
        self.frame_Line_6.setObjectName(u"frame_Line_6")
        self.frame_Line_6.setMaximumSize(QSize(16777215, 1))
        self.frame_Line_6.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
"background-color:#edf2fa;\n"
"border-radius:0px;\n"
"}")
        self.frame_Line_6.setFrameShape(QFrame.StyledPanel)
        self.frame_Line_6.setFrameShadow(QFrame.Raised)

        self.verticalLayout_21.addWidget(self.frame_Line_6)

        self.label_DescDashDomains = QLabel(self.frame_DashDomains)
        self.label_DescDashDomains.setObjectName(u"label_DescDashDomains")
        self.label_DescDashDomains.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:16px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_21.addWidget(self.label_DescDashDomains)


        self.horizontalLayout_2.addWidget(self.frame_DashDomains)

        self.frame_CentralSpace3 = QFrame(self.frame_CentralTop)
        self.frame_CentralSpace3.setObjectName(u"frame_CentralSpace3")
        self.frame_CentralSpace3.setMaximumSize(QSize(10, 16777215))
        self.frame_CentralSpace3.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralSpace3.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_2.addWidget(self.frame_CentralSpace3)

        self.frame_DashTotalVuln = QFrame(self.frame_CentralTop)
        self.frame_DashTotalVuln.setObjectName(u"frame_DashTotalVuln")
        self.frame_DashTotalVuln.setStyleSheet(u"QFrame{\n"
"border:1px solid #edf2fa;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"}")
        self.frame_DashTotalVuln.setFrameShape(QFrame.StyledPanel)
        self.frame_DashTotalVuln.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_DashTotalVuln)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_DashHostDiscovered_8 = QLabel(self.frame_DashTotalVuln)
        self.label_DashHostDiscovered_8.setObjectName(u"label_DashHostDiscovered_8")
        self.label_DashHostDiscovered_8.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:20px;\n"
"	border:0px;\n"
"\n"
"}")
        self.label_DashHostDiscovered_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout_22.addWidget(self.label_DashHostDiscovered_8)

        self.frame_11 = QFrame(self.frame_DashTotalVuln)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setStyleSheet(u"QFrame{border:0px;}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.pushButton_DashTotalVuln = QPushButton(self.frame_11)
        self.pushButton_DashTotalVuln.setObjectName(u"pushButton_DashTotalVuln")
        self.pushButton_DashTotalVuln.setMinimumSize(QSize(0, 65))
        self.pushButton_DashTotalVuln.setStyleSheet(u"QPushButton{\n"
"background-color:#04c9b7;\n"
"border:0px;\n"
"border-radius:10px;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/icons/unlocked.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_DashTotalVuln.setIcon(icon13)
        self.pushButton_DashTotalVuln.setIconSize(QSize(55, 55))

        self.horizontalLayout_19.addWidget(self.pushButton_DashTotalVuln)

        self.label_CountDashTotalVuln = QLabel(self.frame_11)
        self.label_CountDashTotalVuln.setObjectName(u"label_CountDashTotalVuln")
        self.label_CountDashTotalVuln.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:30px;\n"
"	border:0px;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.label_CountDashTotalVuln.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.label_CountDashTotalVuln)


        self.verticalLayout_22.addWidget(self.frame_11)

        self.frame_Line_7 = QFrame(self.frame_DashTotalVuln)
        self.frame_Line_7.setObjectName(u"frame_Line_7")
        self.frame_Line_7.setMaximumSize(QSize(16777215, 1))
        self.frame_Line_7.setStyleSheet(u"QFrame{\n"
"border:0px;\n"
"background-color:#edf2fa;\n"
"border-radius:0px;\n"
"}")
        self.frame_Line_7.setFrameShape(QFrame.StyledPanel)
        self.frame_Line_7.setFrameShadow(QFrame.Raised)

        self.verticalLayout_22.addWidget(self.frame_Line_7)

        self.label_DescDashTotalVuln = QLabel(self.frame_DashTotalVuln)
        self.label_DescDashTotalVuln.setObjectName(u"label_DescDashTotalVuln")
        self.label_DescDashTotalVuln.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:16px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_22.addWidget(self.label_DescDashTotalVuln)


        self.horizontalLayout_2.addWidget(self.frame_DashTotalVuln)


        self.verticalLayout_2.addWidget(self.frame_CentralTop)

        self.frame_CentralBottom = QFrame(self.frame_CentralControl)
        self.frame_CentralBottom.setObjectName(u"frame_CentralBottom")
        self.frame_CentralBottom.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralBottom.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_CentralBottom)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.frame_CentralLeft = QFrame(self.frame_CentralBottom)
        self.frame_CentralLeft.setObjectName(u"frame_CentralLeft")
        self.frame_CentralLeft.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralLeft.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_CentralLeft)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_Vulnerabilities = QFrame(self.frame_CentralLeft)
        self.frame_Vulnerabilities.setObjectName(u"frame_Vulnerabilities")
        self.frame_Vulnerabilities.setStyleSheet(u"QFrame{\n"
"border:1px solid #edf2fa;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"}")
        self.frame_Vulnerabilities.setFrameShape(QFrame.StyledPanel)
        self.frame_Vulnerabilities.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_Vulnerabilities)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lbl_Vulnerabilities = QLabel(self.frame_Vulnerabilities)
        self.lbl_Vulnerabilities.setObjectName(u"lbl_Vulnerabilities")
        self.lbl_Vulnerabilities.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:25px;\n"
"	border:0px;\n"
"\n"
"}")
        self.lbl_Vulnerabilities.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_3.addWidget(self.lbl_Vulnerabilities)

        self.lbl_VulnerabilitiesDesc = QLabel(self.frame_Vulnerabilities)
        self.lbl_VulnerabilitiesDesc.setObjectName(u"lbl_VulnerabilitiesDesc")
        self.lbl_VulnerabilitiesDesc.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:16px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_3.addWidget(self.lbl_VulnerabilitiesDesc)

        self.tableWidget_Vulnerabilities = QTableWidget(self.frame_Vulnerabilities)
        if (self.tableWidget_Vulnerabilities.columnCount() < 4):
            self.tableWidget_Vulnerabilities.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget_Vulnerabilities.rowCount() < 23):
            self.tableWidget_Vulnerabilities.setRowCount(23)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(16, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(17, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(18, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(19, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(20, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(21, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setVerticalHeaderItem(22, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(0, 0, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(0, 1, __qtablewidgetitem28)
        brush = QBrush(QColor(150, 24, 55, 255))
        brush.setStyle(Qt.NoBrush)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setForeground(brush);
        self.tableWidget_Vulnerabilities.setItem(0, 2, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(0, 3, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(1, 0, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(1, 1, __qtablewidgetitem32)
        brush1 = QBrush(QColor(150, 24, 55, 255))
        brush1.setStyle(Qt.NoBrush)
        brush2 = QBrush(QColor(238, 238, 236, 255))
        brush2.setStyle(Qt.NoBrush)
        font = QFont()
        font.setBold(False)
        font.setWeight(50)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font);
        __qtablewidgetitem33.setBackground(brush2);
        __qtablewidgetitem33.setForeground(brush1);
        self.tableWidget_Vulnerabilities.setItem(1, 2, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(1, 3, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(2, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(2, 1, __qtablewidgetitem36)
        brush3 = QBrush(QColor(32, 74, 135, 255))
        brush3.setStyle(Qt.NoBrush)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setForeground(brush3);
        self.tableWidget_Vulnerabilities.setItem(2, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(2, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(3, 0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(3, 1, __qtablewidgetitem40)
        brush4 = QBrush(QColor(150, 24, 55, 255))
        brush4.setStyle(Qt.NoBrush)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setForeground(brush4);
        self.tableWidget_Vulnerabilities.setItem(3, 2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(3, 3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(4, 0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(4, 1, __qtablewidgetitem44)
        brush5 = QBrush(QColor(32, 74, 135, 255))
        brush5.setStyle(Qt.NoBrush)
        __qtablewidgetitem45 = QTableWidgetItem()
        __qtablewidgetitem45.setForeground(brush5);
        self.tableWidget_Vulnerabilities.setItem(4, 2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(4, 3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(5, 0, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(5, 1, __qtablewidgetitem48)
        brush6 = QBrush(QColor(150, 24, 55, 255))
        brush6.setStyle(Qt.NoBrush)
        __qtablewidgetitem49 = QTableWidgetItem()
        __qtablewidgetitem49.setForeground(brush6);
        self.tableWidget_Vulnerabilities.setItem(5, 2, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(5, 3, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(6, 0, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(6, 1, __qtablewidgetitem52)
        brush7 = QBrush(QColor(150, 24, 55, 255))
        brush7.setStyle(Qt.NoBrush)
        __qtablewidgetitem53 = QTableWidgetItem()
        __qtablewidgetitem53.setForeground(brush7);
        self.tableWidget_Vulnerabilities.setItem(6, 2, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(6, 3, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(7, 0, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(7, 1, __qtablewidgetitem56)
        brush8 = QBrush(QColor(32, 74, 135, 255))
        brush8.setStyle(Qt.NoBrush)
        __qtablewidgetitem57 = QTableWidgetItem()
        __qtablewidgetitem57.setForeground(brush8);
        self.tableWidget_Vulnerabilities.setItem(7, 2, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(7, 3, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(8, 0, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(8, 1, __qtablewidgetitem60)
        brush9 = QBrush(QColor(32, 74, 135, 255))
        brush9.setStyle(Qt.NoBrush)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setForeground(brush9);
        self.tableWidget_Vulnerabilities.setItem(8, 2, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(8, 3, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(9, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(9, 1, __qtablewidgetitem64)
        brush10 = QBrush(QColor(32, 74, 135, 255))
        brush10.setStyle(Qt.NoBrush)
        __qtablewidgetitem65 = QTableWidgetItem()
        __qtablewidgetitem65.setForeground(brush10);
        self.tableWidget_Vulnerabilities.setItem(9, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(9, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(10, 0, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(10, 1, __qtablewidgetitem68)
        brush11 = QBrush(QColor(150, 24, 55, 255))
        brush11.setStyle(Qt.NoBrush)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setForeground(brush11);
        self.tableWidget_Vulnerabilities.setItem(10, 2, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(10, 3, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(11, 0, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(11, 1, __qtablewidgetitem72)
        brush12 = QBrush(QColor(150, 24, 55, 255))
        brush12.setStyle(Qt.NoBrush)
        __qtablewidgetitem73 = QTableWidgetItem()
        __qtablewidgetitem73.setForeground(brush12);
        self.tableWidget_Vulnerabilities.setItem(11, 2, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(11, 3, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(12, 0, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(12, 1, __qtablewidgetitem76)
        brush13 = QBrush(QColor(150, 24, 55, 255))
        brush13.setStyle(Qt.NoBrush)
        __qtablewidgetitem77 = QTableWidgetItem()
        __qtablewidgetitem77.setForeground(brush13);
        self.tableWidget_Vulnerabilities.setItem(12, 2, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(12, 3, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(13, 0, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(13, 1, __qtablewidgetitem80)
        brush14 = QBrush(QColor(150, 24, 55, 255))
        brush14.setStyle(Qt.NoBrush)
        __qtablewidgetitem81 = QTableWidgetItem()
        __qtablewidgetitem81.setForeground(brush14);
        self.tableWidget_Vulnerabilities.setItem(13, 2, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(13, 3, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(14, 0, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(14, 1, __qtablewidgetitem84)
        brush15 = QBrush(QColor(150, 24, 55, 255))
        brush15.setStyle(Qt.NoBrush)
        __qtablewidgetitem85 = QTableWidgetItem()
        __qtablewidgetitem85.setForeground(brush15);
        self.tableWidget_Vulnerabilities.setItem(14, 2, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(14, 3, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(15, 0, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(15, 1, __qtablewidgetitem88)
        brush16 = QBrush(QColor(32, 74, 135, 255))
        brush16.setStyle(Qt.NoBrush)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setForeground(brush16);
        self.tableWidget_Vulnerabilities.setItem(15, 2, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(15, 3, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(16, 0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(16, 1, __qtablewidgetitem92)
        brush17 = QBrush(QColor(32, 74, 135, 255))
        brush17.setStyle(Qt.NoBrush)
        __qtablewidgetitem93 = QTableWidgetItem()
        __qtablewidgetitem93.setForeground(brush17);
        self.tableWidget_Vulnerabilities.setItem(16, 2, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(16, 3, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(17, 0, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(17, 1, __qtablewidgetitem96)
        brush18 = QBrush(QColor(32, 74, 135, 255))
        brush18.setStyle(Qt.NoBrush)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setForeground(brush18);
        self.tableWidget_Vulnerabilities.setItem(17, 2, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(17, 3, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(18, 0, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(18, 1, __qtablewidgetitem100)
        brush19 = QBrush(QColor(32, 74, 135, 255))
        brush19.setStyle(Qt.NoBrush)
        __qtablewidgetitem101 = QTableWidgetItem()
        __qtablewidgetitem101.setForeground(brush19);
        self.tableWidget_Vulnerabilities.setItem(18, 2, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(18, 3, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(19, 0, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(19, 1, __qtablewidgetitem104)
        brush20 = QBrush(QColor(32, 74, 135, 255))
        brush20.setStyle(Qt.NoBrush)
        __qtablewidgetitem105 = QTableWidgetItem()
        __qtablewidgetitem105.setForeground(brush20);
        self.tableWidget_Vulnerabilities.setItem(19, 2, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(19, 3, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(20, 0, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(20, 1, __qtablewidgetitem108)
        brush21 = QBrush(QColor(150, 24, 55, 255))
        brush21.setStyle(Qt.NoBrush)
        __qtablewidgetitem109 = QTableWidgetItem()
        __qtablewidgetitem109.setForeground(brush21);
        self.tableWidget_Vulnerabilities.setItem(20, 2, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(20, 3, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(21, 0, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(21, 1, __qtablewidgetitem112)
        brush22 = QBrush(QColor(32, 74, 135, 255))
        brush22.setStyle(Qt.NoBrush)
        __qtablewidgetitem113 = QTableWidgetItem()
        __qtablewidgetitem113.setForeground(brush22);
        self.tableWidget_Vulnerabilities.setItem(21, 2, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(21, 3, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(22, 0, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(22, 1, __qtablewidgetitem116)
        brush23 = QBrush(QColor(150, 24, 55, 255))
        brush23.setStyle(Qt.NoBrush)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setForeground(brush23);
        self.tableWidget_Vulnerabilities.setItem(22, 2, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_Vulnerabilities.setItem(22, 3, __qtablewidgetitem118)
        self.tableWidget_Vulnerabilities.setObjectName(u"tableWidget_Vulnerabilities")
        self.tableWidget_Vulnerabilities.setStyleSheet(u"QTableWidget {	\n"
"	background-color: #fff;\n"
"	padding: 10px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(204, 207, 211);\n"
"	color:#000;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #e5faf8;\n"
"	color:#000;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView{\n"
"   background-color:#04c9b7;\n"
"	border: 1px solid rgb(204, 207, 211);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(204, 207, 211);\n"
"    border-right: 1px solid rgb(204, 207, 211);\n"
"    color:#fff;\n"
"	font-size:15px;\n"
""
                        "    border-radius: 0px;\n"
"}\n"
"")
        self.tableWidget_Vulnerabilities.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_Vulnerabilities.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_Vulnerabilities.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_Vulnerabilities.setShowGrid(True)
        self.tableWidget_Vulnerabilities.setGridStyle(Qt.DotLine)
        self.tableWidget_Vulnerabilities.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Vulnerabilities.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Vulnerabilities.verticalHeader().setVisible(False)
        self.tableWidget_Vulnerabilities.verticalHeader().setHighlightSections(True)

        self.verticalLayout_3.addWidget(self.tableWidget_Vulnerabilities)


        self.verticalLayout_5.addWidget(self.frame_Vulnerabilities)


        self.horizontalLayout_3.addWidget(self.frame_CentralLeft)

        self.frame_CentralRight = QFrame(self.frame_CentralBottom)
        self.frame_CentralRight.setObjectName(u"frame_CentralRight")
        self.frame_CentralRight.setMinimumSize(QSize(351, 0))
        self.frame_CentralRight.setMaximumSize(QSize(400, 16777215))
        self.frame_CentralRight.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralRight.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_CentralRight)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_DashExtraInfo = QFrame(self.frame_CentralRight)
        self.frame_DashExtraInfo.setObjectName(u"frame_DashExtraInfo")
        self.frame_DashExtraInfo.setMinimumSize(QSize(351, 201))
        self.frame_DashExtraInfo.setMaximumSize(QSize(400, 16777215))
        self.frame_DashExtraInfo.setStyleSheet(u"QFrame{\n"
"border:1px solid #edf2fa;\n"
"background-color:#fff;\n"
"border-radius:10px;\n"
"}")
        self.frame_DashExtraInfo.setFrameShape(QFrame.StyledPanel)
        self.frame_DashExtraInfo.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_DashExtraInfo)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lbl_DomainsScan = QLabel(self.frame_DashExtraInfo)
        self.lbl_DomainsScan.setObjectName(u"lbl_DomainsScan")
        self.lbl_DomainsScan.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:25px;\n"
"	border:0px;\n"
"\n"
"}")
        self.lbl_DomainsScan.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_DomainsScan)

        self.lbl_DomainsScanDesc = QLabel(self.frame_DashExtraInfo)
        self.lbl_DomainsScanDesc.setObjectName(u"lbl_DomainsScanDesc")
        self.lbl_DomainsScanDesc.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:14px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.lbl_DomainsScanDesc)

        self.tableWidget_DomainsScan = QTableWidget(self.frame_DashExtraInfo)
        if (self.tableWidget_DomainsScan.columnCount() < 2):
            self.tableWidget_DomainsScan.setColumnCount(2)
        __qtablewidgetitem119 = QTableWidgetItem()
        __qtablewidgetitem119.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_DomainsScan.setHorizontalHeaderItem(0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        __qtablewidgetitem120.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_DomainsScan.setHorizontalHeaderItem(1, __qtablewidgetitem120)
        if (self.tableWidget_DomainsScan.rowCount() < 5):
            self.tableWidget_DomainsScan.setRowCount(5)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_DomainsScan.setVerticalHeaderItem(0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_DomainsScan.setVerticalHeaderItem(1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_DomainsScan.setVerticalHeaderItem(2, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_DomainsScan.setVerticalHeaderItem(3, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_DomainsScan.setVerticalHeaderItem(4, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        __qtablewidgetitem126.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_DomainsScan.setItem(0, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        __qtablewidgetitem127.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_DomainsScan.setItem(0, 1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        __qtablewidgetitem128.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_DomainsScan.setItem(1, 0, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        __qtablewidgetitem129.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_DomainsScan.setItem(1, 1, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        __qtablewidgetitem130.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_DomainsScan.setItem(2, 0, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_DomainsScan.setItem(2, 1, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_DomainsScan.setItem(3, 0, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        __qtablewidgetitem133.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_DomainsScan.setItem(3, 1, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        __qtablewidgetitem134.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_DomainsScan.setItem(4, 0, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        __qtablewidgetitem135.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_DomainsScan.setItem(4, 1, __qtablewidgetitem135)
        self.tableWidget_DomainsScan.setObjectName(u"tableWidget_DomainsScan")
        self.tableWidget_DomainsScan.setStyleSheet(u"QTableWidget {	\n"
"	background-color: #fff;\n"
"	padding: 10px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(204, 207, 211);\n"
"	color:#000;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #e5faf8;\n"
"	color:#000;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView{\n"
"   background-color:#04c9b7;\n"
"	border: 1px solid rgb(204, 207, 211);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(204, 207, 211);\n"
"    border-right: 1px solid rgb(204, 207, 211);\n"
"    color:#fff;\n"
"	font-size:15px;\n"
""
                        "    border-radius: 0px;\n"
"}\n"
"")
        self.tableWidget_DomainsScan.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_DomainsScan.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_DomainsScan.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_DomainsScan.setTextElideMode(Qt.ElideLeft)
        self.tableWidget_DomainsScan.setShowGrid(True)
        self.tableWidget_DomainsScan.setGridStyle(Qt.DotLine)
        self.tableWidget_DomainsScan.horizontalHeader().setHighlightSections(True)
        self.tableWidget_DomainsScan.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_DomainsScan.verticalHeader().setVisible(False)
        self.tableWidget_DomainsScan.verticalHeader().setHighlightSections(True)

        self.verticalLayout_6.addWidget(self.tableWidget_DomainsScan)

        self.lbl_NetWorkScan = QLabel(self.frame_DashExtraInfo)
        self.lbl_NetWorkScan.setObjectName(u"lbl_NetWorkScan")
        self.lbl_NetWorkScan.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:25px;\n"
"	border:0px;\n"
"\n"
"}")
        self.lbl_NetWorkScan.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_NetWorkScan)

        self.lbl_NetWorkScanDesc = QLabel(self.frame_DashExtraInfo)
        self.lbl_NetWorkScanDesc.setObjectName(u"lbl_NetWorkScanDesc")
        self.lbl_NetWorkScanDesc.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:14px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.lbl_NetWorkScanDesc)

        self.tableWidget_Networks = QTableWidget(self.frame_DashExtraInfo)
        if (self.tableWidget_Networks.columnCount() < 2):
            self.tableWidget_Networks.setColumnCount(2)
        __qtablewidgetitem136 = QTableWidgetItem()
        __qtablewidgetitem136.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Networks.setHorizontalHeaderItem(0, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        __qtablewidgetitem137.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_Networks.setHorizontalHeaderItem(1, __qtablewidgetitem137)
        if (self.tableWidget_Networks.rowCount() < 5):
            self.tableWidget_Networks.setRowCount(5)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_Networks.setVerticalHeaderItem(0, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_Networks.setVerticalHeaderItem(1, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_Networks.setVerticalHeaderItem(2, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_Networks.setVerticalHeaderItem(3, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_Networks.setVerticalHeaderItem(4, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        __qtablewidgetitem143.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Networks.setItem(0, 0, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        __qtablewidgetitem144.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_Networks.setItem(0, 1, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Networks.setItem(1, 0, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_Networks.setItem(1, 1, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        __qtablewidgetitem147.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Networks.setItem(2, 0, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        __qtablewidgetitem148.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_Networks.setItem(2, 1, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        __qtablewidgetitem149.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Networks.setItem(3, 0, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        __qtablewidgetitem150.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_Networks.setItem(3, 1, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        __qtablewidgetitem151.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_Networks.setItem(4, 0, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        __qtablewidgetitem152.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_Networks.setItem(4, 1, __qtablewidgetitem152)
        self.tableWidget_Networks.setObjectName(u"tableWidget_Networks")
        self.tableWidget_Networks.setStyleSheet(u"QTableWidget {	\n"
"	background-color: #fff;\n"
"	padding: 10px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(204, 207, 211);\n"
"	color:#000;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #e5faf8;\n"
"	color:#000;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView{\n"
"   background-color:#04c9b7;\n"
"	border: 1px solid rgb(204, 207, 211);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(204, 207, 211);\n"
"    border-right: 1px solid rgb(204, 207, 211);\n"
"    color:#fff;\n"
"	font-size:15px;\n"
""
                        "    border-radius: 0px;\n"
"}\n"
"")
        self.tableWidget_Networks.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_Networks.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_Networks.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_Networks.setTextElideMode(Qt.ElideLeft)
        self.tableWidget_Networks.setShowGrid(True)
        self.tableWidget_Networks.setGridStyle(Qt.DotLine)
        self.tableWidget_Networks.horizontalHeader().setHighlightSections(True)
        self.tableWidget_Networks.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_Networks.verticalHeader().setVisible(False)
        self.tableWidget_Networks.verticalHeader().setHighlightSections(True)

        self.verticalLayout_6.addWidget(self.tableWidget_Networks)

        self.lbl_LiveHost = QLabel(self.frame_DashExtraInfo)
        self.lbl_LiveHost.setObjectName(u"lbl_LiveHost")
        self.lbl_LiveHost.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:25px;\n"
"	border:0px;\n"
"\n"
"}")
        self.lbl_LiveHost.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_6.addWidget(self.lbl_LiveHost)

        self.lbl_LiveHostDesc = QLabel(self.frame_DashExtraInfo)
        self.lbl_LiveHostDesc.setObjectName(u"lbl_LiveHostDesc")
        self.lbl_LiveHostDesc.setStyleSheet(u"QLabel{\n"
"\n"
"	font-size:14px;\n"
"	border:0px;\n"
"color:rgb(204, 207, 211);\n"
"\n"
"}")

        self.verticalLayout_6.addWidget(self.lbl_LiveHostDesc)

        self.tableWidget_LiveHost = QTableWidget(self.frame_DashExtraInfo)
        if (self.tableWidget_LiveHost.columnCount() < 2):
            self.tableWidget_LiveHost.setColumnCount(2)
        __qtablewidgetitem153 = QTableWidgetItem()
        __qtablewidgetitem153.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setHorizontalHeaderItem(0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        __qtablewidgetitem154.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setHorizontalHeaderItem(1, __qtablewidgetitem154)
        if (self.tableWidget_LiveHost.rowCount() < 9):
            self.tableWidget_LiveHost.setRowCount(9)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(0, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(1, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(2, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(3, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(4, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(5, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(6, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(7, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_LiveHost.setVerticalHeaderItem(8, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        __qtablewidgetitem164.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(0, 0, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        __qtablewidgetitem165.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(0, 1, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        __qtablewidgetitem166.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(1, 0, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        __qtablewidgetitem167.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(1, 1, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        __qtablewidgetitem168.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(2, 0, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        __qtablewidgetitem169.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(2, 1, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        __qtablewidgetitem170.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(3, 0, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        __qtablewidgetitem171.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(3, 1, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        __qtablewidgetitem172.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(4, 0, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        __qtablewidgetitem173.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(4, 1, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        __qtablewidgetitem174.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(5, 0, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        __qtablewidgetitem175.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(5, 1, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        __qtablewidgetitem176.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(6, 0, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        __qtablewidgetitem177.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(6, 1, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        __qtablewidgetitem178.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(7, 0, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        __qtablewidgetitem179.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(7, 1, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        __qtablewidgetitem180.setTextAlignment(Qt.AlignCenter);
        self.tableWidget_LiveHost.setItem(8, 0, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        __qtablewidgetitem181.setTextAlignment(Qt.AlignTrailing|Qt.AlignVCenter);
        self.tableWidget_LiveHost.setItem(8, 1, __qtablewidgetitem181)
        self.tableWidget_LiveHost.setObjectName(u"tableWidget_LiveHost")
        self.tableWidget_LiveHost.setStyleSheet(u"QTableWidget {	\n"
"	background-color: #fff;\n"
"	padding: 10px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"	border-bottom: 1px solid rgb(204, 207, 211);\n"
"	color:#000;\n"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(44, 49, 60);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(44, 49, 60);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: #e5faf8;\n"
"	color:#000;\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 21px 0 21px 0;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView{\n"
"   background-color:#04c9b7;\n"
"	border: 1px solid rgb(204, 207, 211);\n"
"	border-style: none;\n"
"    border-bottom: 1px solid rgb(204, 207, 211);\n"
"    border-right: 1px solid rgb(204, 207, 211);\n"
"    color:#fff;\n"
"	font-size:15px;\n"
""
                        "    border-radius: 0px;\n"
"}\n"
"")
        self.tableWidget_LiveHost.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_LiveHost.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_LiveHost.setSizeAdjustPolicy(QAbstractScrollArea.AdjustIgnored)
        self.tableWidget_LiveHost.setTextElideMode(Qt.ElideLeft)
        self.tableWidget_LiveHost.setShowGrid(True)
        self.tableWidget_LiveHost.setGridStyle(Qt.DotLine)
        self.tableWidget_LiveHost.horizontalHeader().setHighlightSections(True)
        self.tableWidget_LiveHost.horizontalHeader().setStretchLastSection(True)
        self.tableWidget_LiveHost.verticalHeader().setVisible(False)
        self.tableWidget_LiveHost.verticalHeader().setHighlightSections(True)

        self.verticalLayout_6.addWidget(self.tableWidget_LiveHost)


        self.verticalLayout_4.addWidget(self.frame_DashExtraInfo)


        self.horizontalLayout_3.addWidget(self.frame_CentralRight)


        self.verticalLayout_2.addWidget(self.frame_CentralBottom)


        self.verticalLayout_9.addWidget(self.frame_CentralControl)

        self.stackedWidget_Control.addWidget(self.page_DashBoard)
        self.page_QuickStart = QWidget()
        self.page_QuickStart.setObjectName(u"page_QuickStart")
        self.page_QuickStart.setStyleSheet(u"QWidget{\n"
"	background-color:#fafbfd;\n"
"    border:0px;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.page_QuickStart)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.frame_CentralControl_3 = QFrame(self.page_QuickStart)
        self.frame_CentralControl_3.setObjectName(u"frame_CentralControl_3")
        self.frame_CentralControl_3.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_CentralControl_3.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralControl_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_CentralControl_3)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.frame_CentralControl_3)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"\n"
"}")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_4)


        self.verticalLayout_10.addWidget(self.frame_3)

        self.frame_CentralBottom_3 = QFrame(self.frame_CentralControl_3)
        self.frame_CentralBottom_3.setObjectName(u"frame_CentralBottom_3")
        self.frame_CentralBottom_3.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralBottom_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.frame_CentralBottom_3)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")

        self.verticalLayout_10.addWidget(self.frame_CentralBottom_3)


        self.verticalLayout_11.addWidget(self.frame_CentralControl_3)

        self.stackedWidget_Control.addWidget(self.page_QuickStart)
        self.page_Assets = QWidget()
        self.page_Assets.setObjectName(u"page_Assets")
        self.page_Assets.setStyleSheet(u"QWidget{\n"
"	background-color:#fafbfd;\n"
"    border:0px;\n"
"}")
        self.verticalLayout_14 = QVBoxLayout(self.page_Assets)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.frame_CentralControl_4 = QFrame(self.page_Assets)
        self.frame_CentralControl_4.setObjectName(u"frame_CentralControl_4")
        self.frame_CentralControl_4.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_CentralControl_4.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralControl_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_CentralControl_4)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_4 = QFrame(self.frame_CentralControl_4)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_5 = QLabel(self.frame_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"\n"
"}")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_5)


        self.verticalLayout_13.addWidget(self.frame_4)

        self.frame_CentralBottom_4 = QFrame(self.frame_CentralControl_4)
        self.frame_CentralBottom_4.setObjectName(u"frame_CentralBottom_4")
        self.frame_CentralBottom_4.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralBottom_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_CentralBottom_4)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")

        self.verticalLayout_13.addWidget(self.frame_CentralBottom_4)


        self.verticalLayout_14.addWidget(self.frame_CentralControl_4)

        self.stackedWidget_Control.addWidget(self.page_Assets)
        self.page_Report = QWidget()
        self.page_Report.setObjectName(u"page_Report")
        self.page_Report.setStyleSheet(u"QWidget{\n"
"	background-color:#fafbfd;\n"
"    border:0px;\n"
"}")
        self.verticalLayout_16 = QVBoxLayout(self.page_Report)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_CentralControl_5 = QFrame(self.page_Report)
        self.frame_CentralControl_5.setObjectName(u"frame_CentralControl_5")
        self.frame_CentralControl_5.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_CentralControl_5.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralControl_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_CentralControl_5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.frame_5 = QFrame(self.frame_CentralControl_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_6 = QLabel(self.frame_5)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"\n"
"}")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_12.addWidget(self.label_6)


        self.verticalLayout_15.addWidget(self.frame_5)

        self.frame_CentralBottom_5 = QFrame(self.frame_CentralControl_5)
        self.frame_CentralBottom_5.setObjectName(u"frame_CentralBottom_5")
        self.frame_CentralBottom_5.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralBottom_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_CentralBottom_5)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")

        self.verticalLayout_15.addWidget(self.frame_CentralBottom_5)


        self.verticalLayout_16.addWidget(self.frame_CentralControl_5)

        self.stackedWidget_Control.addWidget(self.page_Report)
        self.page_Config = QWidget()
        self.page_Config.setObjectName(u"page_Config")
        self.page_Config.setStyleSheet(u"QWidget{\n"
"	background-color:#fafbfd;\n"
"    border:0px;\n"
"}")
        self.verticalLayout_18 = QVBoxLayout(self.page_Config)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_CentralControl_6 = QFrame(self.page_Config)
        self.frame_CentralControl_6.setObjectName(u"frame_CentralControl_6")
        self.frame_CentralControl_6.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_CentralControl_6.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralControl_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_CentralControl_6)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.frame_6 = QFrame(self.frame_CentralControl_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"}")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.label_7)


        self.verticalLayout_17.addWidget(self.frame_6)

        self.frame_CentralBottom_6 = QFrame(self.frame_CentralControl_6)
        self.frame_CentralBottom_6.setObjectName(u"frame_CentralBottom_6")
        self.frame_CentralBottom_6.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralBottom_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_CentralBottom_6)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")

        self.verticalLayout_17.addWidget(self.frame_CentralBottom_6)


        self.verticalLayout_18.addWidget(self.frame_CentralControl_6)

        self.stackedWidget_Control.addWidget(self.page_Config)
        self.page_About = QWidget()
        self.page_About.setObjectName(u"page_About")
        self.page_About.setStyleSheet(u"QWidget{\n"
"	background-color:#fafbfd;\n"
"    border:0px;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.page_About)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_CentralControl_2 = QFrame(self.page_About)
        self.frame_CentralControl_2.setObjectName(u"frame_CentralControl_2")
        self.frame_CentralControl_2.setStyleSheet(u"QFrame{\n"
"\n"
"	background-color:#fafbfd;\n"
"   border:0px;\n"
"}")
        self.frame_CentralControl_2.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralControl_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_CentralControl_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_2 = QFrame(self.frame_CentralControl_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"		font-size:30px;\n"
"	    border:0px;\n"
"	font-weight: bold;\n"
"\n"
"\n"
"}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_6.addWidget(self.label_3)


        self.verticalLayout_7.addWidget(self.frame_2)

        self.frame_CentralBottom_2 = QFrame(self.frame_CentralControl_2)
        self.frame_CentralBottom_2.setObjectName(u"frame_CentralBottom_2")
        self.frame_CentralBottom_2.setFrameShape(QFrame.StyledPanel)
        self.frame_CentralBottom_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_CentralBottom_2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.verticalLayout_7.addWidget(self.frame_CentralBottom_2)


        self.verticalLayout_12.addWidget(self.frame_CentralControl_2)

        self.stackedWidget_Control.addWidget(self.page_About)

        self.verticalLayout_8.addWidget(self.stackedWidget_Control)


        self.horizontalLayout.addWidget(self.frame_Control)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget_Control.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DashPriv8 - Tramontinas tool", None))
        self.label_LogoNameDesc.setText(QCoreApplication.translate("MainWindow", u"Tramontinas tool", None))
        self.label_LogoName.setText(QCoreApplication.translate("MainWindow", u"DashPriv8", None))
        self.pushButton_DashBoard.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.pushButton_QuickStart.setText(QCoreApplication.translate("MainWindow", u"Quick Start", None))
        self.pushButton_Assets.setText(QCoreApplication.translate("MainWindow", u"Assets", None))
        self.pushButton_Report.setText(QCoreApplication.translate("MainWindow", u"Report", None))
        self.pushButton_Config.setText(QCoreApplication.translate("MainWindow", u"Config", None))
        self.pushButton_About.setText(QCoreApplication.translate("MainWindow", u"About", None))
        self.label_PerfilName.setText(QCoreApplication.translate("MainWindow", u"MrCl0wnLab", None))
        self.pushButton_Perfil.setText("")
        self.pushButton_Notifications.setText(QCoreApplication.translate("MainWindow", u"25", None))
        self.label_LastAccess.setText(QCoreApplication.translate("MainWindow", u"Last access: 30-09-2020 05:01", None))
        self.pushButton_LastAccess.setText("")
        self.label_IpInfo.setText(QCoreApplication.translate("MainWindow", u"185.88.181.4  | Amsterdam | NL", None))
        self.pushButton_InfoIo.setText("")
        self.label_Hello.setText(QCoreApplication.translate("MainWindow", u"> Hello Mr. Cl0wn", None))
        self.label_DashHostDiscovered.setText(QCoreApplication.translate("MainWindow", u"Hosts Discovered", None))
        self.pushButton_DashHostDiscovered.setText("")
        self.label_CountDashHostDiscovered.setText(QCoreApplication.translate("MainWindow", u"1506", None))
        self.label_DescDashHostDiscovered.setText(QCoreApplication.translate("MainWindow", u"Since Last Assessment", None))
        self.label_DashScanExecuted.setText(QCoreApplication.translate("MainWindow", u"Scans Executed", None))
        self.pushButton_DashScanExecuted.setText("")
        self.label_CountDashScanExecuted.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.label_DescDashScanExecuted.setText(QCoreApplication.translate("MainWindow", u"Since Last System Reset", None))
        self.label_DashDomains.setText(QCoreApplication.translate("MainWindow", u"Domains", None))
        self.pushButton_DashDomains.setText("")
        self.label_CountDashDomains.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_DescDashDomains.setText(QCoreApplication.translate("MainWindow", u"Since Last Assessment", None))
        self.label_DashHostDiscovered_8.setText(QCoreApplication.translate("MainWindow", u"Total Vulnerabilities", None))
        self.pushButton_DashTotalVuln.setText("")
        self.label_CountDashTotalVuln.setText(QCoreApplication.translate("MainWindow", u"658", None))
        self.label_DescDashTotalVuln.setText(QCoreApplication.translate("MainWindow", u"Since Last Assessment", None))
        self.lbl_Vulnerabilities.setText(QCoreApplication.translate("MainWindow", u"Vulnerabilities", None))
        self.lbl_VulnerabilitiesDesc.setText(QCoreApplication.translate("MainWindow", u"Last Scanned", None))
        ___qtablewidgetitem = self.tableWidget_Vulnerabilities.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Target", None));
        ___qtablewidgetitem1 = self.tableWidget_Vulnerabilities.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Port", None));
        ___qtablewidgetitem2 = self.tableWidget_Vulnerabilities.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Severity", None));
        ___qtablewidgetitem3 = self.tableWidget_Vulnerabilities.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem4 = self.tableWidget_Vulnerabilities.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget_Vulnerabilities.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget_Vulnerabilities.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget_Vulnerabilities.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget_Vulnerabilities.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem9 = self.tableWidget_Vulnerabilities.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem10 = self.tableWidget_Vulnerabilities.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem11 = self.tableWidget_Vulnerabilities.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem12 = self.tableWidget_Vulnerabilities.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem13 = self.tableWidget_Vulnerabilities.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem14 = self.tableWidget_Vulnerabilities.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem15 = self.tableWidget_Vulnerabilities.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem16 = self.tableWidget_Vulnerabilities.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem17 = self.tableWidget_Vulnerabilities.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem18 = self.tableWidget_Vulnerabilities.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem19 = self.tableWidget_Vulnerabilities.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem20 = self.tableWidget_Vulnerabilities.verticalHeaderItem(16)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem21 = self.tableWidget_Vulnerabilities.verticalHeaderItem(17)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem22 = self.tableWidget_Vulnerabilities.verticalHeaderItem(18)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem23 = self.tableWidget_Vulnerabilities.verticalHeaderItem(19)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem24 = self.tableWidget_Vulnerabilities.verticalHeaderItem(20)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem25 = self.tableWidget_Vulnerabilities.verticalHeaderItem(21)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem26 = self.tableWidget_Vulnerabilities.verticalHeaderItem(22)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled = self.tableWidget_Vulnerabilities.isSortingEnabled()
        self.tableWidget_Vulnerabilities.setSortingEnabled(False)
        ___qtablewidgetitem27 = self.tableWidget_Vulnerabilities.item(0, 0)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"192.168.0.1", None));
        ___qtablewidgetitem28 = self.tableWidget_Vulnerabilities.item(0, 1)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"445", None));
        ___qtablewidgetitem29 = self.tableWidget_Vulnerabilities.item(0, 2)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem30 = self.tableWidget_Vulnerabilities.item(0, 3)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Checks for SBM Ports", None));
        ___qtablewidgetitem31 = self.tableWidget_Vulnerabilities.item(1, 0)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"192.168.0.55", None));
        ___qtablewidgetitem32 = self.tableWidget_Vulnerabilities.item(1, 1)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem33 = self.tableWidget_Vulnerabilities.item(1, 2)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem34 = self.tableWidget_Vulnerabilities.item(1, 3)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Checks if SSH password authentication is supported", None));
        ___qtablewidgetitem35 = self.tableWidget_Vulnerabilities.item(2, 0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"192.168.0.1", None));
        ___qtablewidgetitem36 = self.tableWidget_Vulnerabilities.item(2, 1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem37 = self.tableWidget_Vulnerabilities.item(2, 2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem38 = self.tableWidget_Vulnerabilities.item(2, 3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem39 = self.tableWidget_Vulnerabilities.item(3, 0)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"192.168.0.140", None));
        ___qtablewidgetitem40 = self.tableWidget_Vulnerabilities.item(3, 1)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"139", None));
        ___qtablewidgetitem41 = self.tableWidget_Vulnerabilities.item(3, 2)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem42 = self.tableWidget_Vulnerabilities.item(3, 3)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Checks for Remote Management Ports", None));
        ___qtablewidgetitem43 = self.tableWidget_Vulnerabilities.item(4, 0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"192.168.0.11", None));
        ___qtablewidgetitem44 = self.tableWidget_Vulnerabilities.item(4, 1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem45 = self.tableWidget_Vulnerabilities.item(4, 2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem46 = self.tableWidget_Vulnerabilities.item(4, 3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem47 = self.tableWidget_Vulnerabilities.item(5, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"192.168.0.54", None));
        ___qtablewidgetitem48 = self.tableWidget_Vulnerabilities.item(5, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem49 = self.tableWidget_Vulnerabilities.item(5, 2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem50 = self.tableWidget_Vulnerabilities.item(5, 3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Checks if SSH password authentication is supported", None));
        ___qtablewidgetitem51 = self.tableWidget_Vulnerabilities.item(6, 0)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"200.10.0.10", None));
        ___qtablewidgetitem52 = self.tableWidget_Vulnerabilities.item(6, 1)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"445", None));
        ___qtablewidgetitem53 = self.tableWidget_Vulnerabilities.item(6, 2)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem54 = self.tableWidget_Vulnerabilities.item(6, 3)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Checks for SBM Ports", None));
        ___qtablewidgetitem55 = self.tableWidget_Vulnerabilities.item(7, 0)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"200.10.0.15", None));
        ___qtablewidgetitem56 = self.tableWidget_Vulnerabilities.item(7, 1)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"8080", None));
        ___qtablewidgetitem57 = self.tableWidget_Vulnerabilities.item(7, 2)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem58 = self.tableWidget_Vulnerabilities.item(7, 3)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem59 = self.tableWidget_Vulnerabilities.item(8, 0)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"200.10.0.5", None));
        ___qtablewidgetitem60 = self.tableWidget_Vulnerabilities.item(8, 1)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem61 = self.tableWidget_Vulnerabilities.item(8, 2)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem62 = self.tableWidget_Vulnerabilities.item(8, 3)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem63 = self.tableWidget_Vulnerabilities.item(9, 0)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"200.10.0.113", None));
        ___qtablewidgetitem64 = self.tableWidget_Vulnerabilities.item(9, 1)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem65 = self.tableWidget_Vulnerabilities.item(9, 2)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem66 = self.tableWidget_Vulnerabilities.item(9, 3)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem67 = self.tableWidget_Vulnerabilities.item(10, 0)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"200.10.0.29", None));
        ___qtablewidgetitem68 = self.tableWidget_Vulnerabilities.item(10, 1)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"139", None));
        ___qtablewidgetitem69 = self.tableWidget_Vulnerabilities.item(10, 2)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem70 = self.tableWidget_Vulnerabilities.item(10, 3)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"Checks for Remote Management Ports", None));
        ___qtablewidgetitem71 = self.tableWidget_Vulnerabilities.item(11, 0)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"200.10.0.201", None));
        ___qtablewidgetitem72 = self.tableWidget_Vulnerabilities.item(11, 1)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem73 = self.tableWidget_Vulnerabilities.item(11, 2)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem74 = self.tableWidget_Vulnerabilities.item(11, 3)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Checks if SSH password authentication is supported", None));
        ___qtablewidgetitem75 = self.tableWidget_Vulnerabilities.item(12, 0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"200.10.0.92", None));
        ___qtablewidgetitem76 = self.tableWidget_Vulnerabilities.item(12, 1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"445", None));
        ___qtablewidgetitem77 = self.tableWidget_Vulnerabilities.item(12, 2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem78 = self.tableWidget_Vulnerabilities.item(12, 3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"Checks for SBM Ports", None));
        ___qtablewidgetitem79 = self.tableWidget_Vulnerabilities.item(13, 0)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"216.58.202.14", None));
        ___qtablewidgetitem80 = self.tableWidget_Vulnerabilities.item(13, 1)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem81 = self.tableWidget_Vulnerabilities.item(13, 2)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem82 = self.tableWidget_Vulnerabilities.item(13, 3)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"Checks if SSH password authentication is supported", None));
        ___qtablewidgetitem83 = self.tableWidget_Vulnerabilities.item(14, 0)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"216.58.202.14", None));
        ___qtablewidgetitem84 = self.tableWidget_Vulnerabilities.item(14, 1)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"22", None));
        ___qtablewidgetitem85 = self.tableWidget_Vulnerabilities.item(14, 2)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem86 = self.tableWidget_Vulnerabilities.item(14, 3)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"Checks if SSH password authentication is supported", None));
        ___qtablewidgetitem87 = self.tableWidget_Vulnerabilities.item(15, 0)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"216.58.202.200", None));
        ___qtablewidgetitem88 = self.tableWidget_Vulnerabilities.item(15, 1)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem89 = self.tableWidget_Vulnerabilities.item(15, 2)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem90 = self.tableWidget_Vulnerabilities.item(15, 3)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem91 = self.tableWidget_Vulnerabilities.item(16, 0)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"216.58.202.101", None));
        ___qtablewidgetitem92 = self.tableWidget_Vulnerabilities.item(16, 1)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem93 = self.tableWidget_Vulnerabilities.item(16, 2)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem94 = self.tableWidget_Vulnerabilities.item(16, 3)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem95 = self.tableWidget_Vulnerabilities.item(17, 0)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"216.58.202.128", None));
        ___qtablewidgetitem96 = self.tableWidget_Vulnerabilities.item(17, 1)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem97 = self.tableWidget_Vulnerabilities.item(17, 2)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem98 = self.tableWidget_Vulnerabilities.item(17, 3)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem99 = self.tableWidget_Vulnerabilities.item(18, 0)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"216.58.202.129", None));
        ___qtablewidgetitem100 = self.tableWidget_Vulnerabilities.item(18, 1)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem101 = self.tableWidget_Vulnerabilities.item(18, 2)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem102 = self.tableWidget_Vulnerabilities.item(18, 3)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem103 = self.tableWidget_Vulnerabilities.item(19, 0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"216.58.202.135", None));
        ___qtablewidgetitem104 = self.tableWidget_Vulnerabilities.item(19, 1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"80", None));
        ___qtablewidgetitem105 = self.tableWidget_Vulnerabilities.item(19, 2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem106 = self.tableWidget_Vulnerabilities.item(19, 3)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem107 = self.tableWidget_Vulnerabilities.item(20, 0)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"216.58.202.137", None));
        ___qtablewidgetitem108 = self.tableWidget_Vulnerabilities.item(20, 1)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"139", None));
        ___qtablewidgetitem109 = self.tableWidget_Vulnerabilities.item(20, 2)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem110 = self.tableWidget_Vulnerabilities.item(20, 3)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Checks for Remote Management Ports", None));
        ___qtablewidgetitem111 = self.tableWidget_Vulnerabilities.item(21, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"216.58.202.138", None));
        ___qtablewidgetitem112 = self.tableWidget_Vulnerabilities.item(21, 1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"8080", None));
        ___qtablewidgetitem113 = self.tableWidget_Vulnerabilities.item(21, 2)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"Informational", None));
        ___qtablewidgetitem114 = self.tableWidget_Vulnerabilities.item(21, 3)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Checks if Security Headers exist", None));
        ___qtablewidgetitem115 = self.tableWidget_Vulnerabilities.item(22, 0)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"216.58.202.139", None));
        ___qtablewidgetitem116 = self.tableWidget_Vulnerabilities.item(22, 1)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"445", None));
        ___qtablewidgetitem117 = self.tableWidget_Vulnerabilities.item(22, 2)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem118 = self.tableWidget_Vulnerabilities.item(22, 3)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Checks for SBM Ports", None));
        self.tableWidget_Vulnerabilities.setSortingEnabled(__sortingEnabled)

        self.lbl_DomainsScan.setText(QCoreApplication.translate("MainWindow", u"Domains Scanned", None))
        self.lbl_DomainsScanDesc.setText(QCoreApplication.translate("MainWindow", u"Your last assessment included these domains", None))
        ___qtablewidgetitem119 = self.tableWidget_DomainsScan.horizontalHeaderItem(0)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"View", None));
        ___qtablewidgetitem120 = self.tableWidget_DomainsScan.horizontalHeaderItem(1)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Domains", None));
        ___qtablewidgetitem121 = self.tableWidget_DomainsScan.verticalHeaderItem(0)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem122 = self.tableWidget_DomainsScan.verticalHeaderItem(1)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem123 = self.tableWidget_DomainsScan.verticalHeaderItem(2)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem124 = self.tableWidget_DomainsScan.verticalHeaderItem(3)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem125 = self.tableWidget_DomainsScan.verticalHeaderItem(4)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"5", None));

        __sortingEnabled1 = self.tableWidget_DomainsScan.isSortingEnabled()
        self.tableWidget_DomainsScan.setSortingEnabled(False)
        ___qtablewidgetitem126 = self.tableWidget_DomainsScan.item(0, 0)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem127 = self.tableWidget_DomainsScan.item(0, 1)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"google.com", None));
        ___qtablewidgetitem128 = self.tableWidget_DomainsScan.item(1, 0)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem129 = self.tableWidget_DomainsScan.item(1, 1)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"fbi.gov", None));
        ___qtablewidgetitem130 = self.tableWidget_DomainsScan.item(2, 0)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem131 = self.tableWidget_DomainsScan.item(2, 1)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"abin.gov.br", None));
        ___qtablewidgetitem132 = self.tableWidget_DomainsScan.item(3, 0)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem133 = self.tableWidget_DomainsScan.item(3, 1)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"nsa.gov", None));
        ___qtablewidgetitem134 = self.tableWidget_DomainsScan.item(4, 0)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem135 = self.tableWidget_DomainsScan.item(4, 1)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"att.com", None));
        self.tableWidget_DomainsScan.setSortingEnabled(__sortingEnabled1)

        self.lbl_NetWorkScan.setText(QCoreApplication.translate("MainWindow", u"Networks Scanned", None))
        self.lbl_NetWorkScanDesc.setText(QCoreApplication.translate("MainWindow", u"Your last assessment included these networks", None))
        ___qtablewidgetitem136 = self.tableWidget_Networks.horizontalHeaderItem(0)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"View", None));
        ___qtablewidgetitem137 = self.tableWidget_Networks.horizontalHeaderItem(1)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"Networks", None));
        ___qtablewidgetitem138 = self.tableWidget_Networks.verticalHeaderItem(0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem139 = self.tableWidget_Networks.verticalHeaderItem(1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem140 = self.tableWidget_Networks.verticalHeaderItem(2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem141 = self.tableWidget_Networks.verticalHeaderItem(3)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"New Row", None));
        ___qtablewidgetitem142 = self.tableWidget_Networks.verticalHeaderItem(4)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"New Row", None));

        __sortingEnabled2 = self.tableWidget_Networks.isSortingEnabled()
        self.tableWidget_Networks.setSortingEnabled(False)
        ___qtablewidgetitem143 = self.tableWidget_Networks.item(0, 0)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem144 = self.tableWidget_Networks.item(0, 1)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"216.58.202.0-255", None));
        ___qtablewidgetitem145 = self.tableWidget_Networks.item(1, 0)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem146 = self.tableWidget_Networks.item(1, 1)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"204.79.197.0-255", None));
        ___qtablewidgetitem147 = self.tableWidget_Networks.item(2, 0)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem148 = self.tableWidget_Networks.item(2, 1)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"204.79.0-255.10", None));
        ___qtablewidgetitem149 = self.tableWidget_Networks.item(3, 0)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem150 = self.tableWidget_Networks.item(3, 1)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"204.79.0-255.0-255", None));
        ___qtablewidgetitem151 = self.tableWidget_Networks.item(4, 0)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem152 = self.tableWidget_Networks.item(4, 1)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"170.66.11.0-255", None));
        self.tableWidget_Networks.setSortingEnabled(__sortingEnabled2)

        self.lbl_LiveHost.setText(QCoreApplication.translate("MainWindow", u"Live Hosts", None))
        self.lbl_LiveHostDesc.setText(QCoreApplication.translate("MainWindow", u"These hosts were identified to be alive", None))
        ___qtablewidgetitem153 = self.tableWidget_LiveHost.horizontalHeaderItem(0)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"View", None));
        ___qtablewidgetitem154 = self.tableWidget_LiveHost.horizontalHeaderItem(1)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"IP Addresses", None));
        ___qtablewidgetitem155 = self.tableWidget_LiveHost.verticalHeaderItem(0)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem156 = self.tableWidget_LiveHost.verticalHeaderItem(1)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem157 = self.tableWidget_LiveHost.verticalHeaderItem(2)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem158 = self.tableWidget_LiveHost.verticalHeaderItem(3)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem159 = self.tableWidget_LiveHost.verticalHeaderItem(4)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem160 = self.tableWidget_LiveHost.verticalHeaderItem(5)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem161 = self.tableWidget_LiveHost.verticalHeaderItem(6)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem162 = self.tableWidget_LiveHost.verticalHeaderItem(7)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem163 = self.tableWidget_LiveHost.verticalHeaderItem(8)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"9", None));

        __sortingEnabled3 = self.tableWidget_LiveHost.isSortingEnabled()
        self.tableWidget_LiveHost.setSortingEnabled(False)
        ___qtablewidgetitem164 = self.tableWidget_LiveHost.item(0, 0)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem165 = self.tableWidget_LiveHost.item(0, 1)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"216.58.202.14", None));
        ___qtablewidgetitem166 = self.tableWidget_LiveHost.item(1, 0)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem167 = self.tableWidget_LiveHost.item(1, 1)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"216.58.202.20", None));
        ___qtablewidgetitem168 = self.tableWidget_LiveHost.item(2, 0)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem169 = self.tableWidget_LiveHost.item(2, 1)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"216.58.202.21", None));
        ___qtablewidgetitem170 = self.tableWidget_LiveHost.item(3, 0)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem171 = self.tableWidget_LiveHost.item(3, 1)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"216.58.202.51", None));
        ___qtablewidgetitem172 = self.tableWidget_LiveHost.item(4, 0)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem173 = self.tableWidget_LiveHost.item(4, 1)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"216.58.202.200", None));
        ___qtablewidgetitem174 = self.tableWidget_LiveHost.item(5, 0)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem175 = self.tableWidget_LiveHost.item(5, 1)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"216.58.25.64", None));
        ___qtablewidgetitem176 = self.tableWidget_LiveHost.item(6, 0)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem177 = self.tableWidget_LiveHost.item(6, 1)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"216.58.25.97", None));
        ___qtablewidgetitem178 = self.tableWidget_LiveHost.item(7, 0)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem179 = self.tableWidget_LiveHost.item(7, 1)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"216.58.25.101", None));
        ___qtablewidgetitem180 = self.tableWidget_LiveHost.item(8, 0)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"[ + ]", None));
        ___qtablewidgetitem181 = self.tableWidget_LiveHost.item(8, 1)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"216.58.25.108", None));
        self.tableWidget_LiveHost.setSortingEnabled(__sortingEnabled3)

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"QUICK START", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"ASSETS", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"REPORT", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"CONFIG", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ABOUT", None))
    # retranslateUi

