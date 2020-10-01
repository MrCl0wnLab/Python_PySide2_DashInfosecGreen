import sys
from ui_DashInfoSec import Ui_MainWindow
from assets import files

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui_main = Ui_MainWindow()
        self.ui_main.setupUi(self)

        # CLICK SELECT DASHBOARD
        self.ui_main.pushButton_DashBoard.clicked.connect(lambda: self.click_select_tab(0))
        # CLICK SELECT QUICKSTART
        self.ui_main.pushButton_QuickStart.clicked.connect(lambda: self.click_select_tab(1))
        # CLICK SELECT ASSETS
        self.ui_main.pushButton_Assets.clicked.connect(lambda: self.click_select_tab(2))
        # CLICK SELECT REPORT
        self.ui_main.pushButton_Report.clicked.connect(lambda: self.click_select_tab(3))
        # CLICK SELECT CONFIG
        self.ui_main.pushButton_Config.clicked.connect(lambda: self.click_select_tab(4))
        # CLICK SELECT ABOUT
        self.ui_main.pushButton_About.clicked.connect(lambda: self.click_select_tab(5))
        # SHOW FORM
        self.show()

    def click_select_tab(self,index_int:int):
        self.ui_main.stackedWidget_Control.setCurrentIndex(index_int)

if __name__ == "__main__":
    try:
        app = QApplication(sys.argv)
        window = MainWindow()
        sys.exit(app.exec_())
    except KeyboardInterrupt:
        pass
