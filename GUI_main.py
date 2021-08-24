import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import *
from PyQt5 import uic


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('Qt_designer/test_0.ui', self)
        self.serach_button = self.findChild(QToolButton, 'search_button')
        self.filter_window = self.findChild(QFrame, 'filter_window')
        self.b2 = self.findChild(QToolButton, 'button_close')
        self.table = self.findChild(QTableWidget, 'tableWidget')
        self.grid_filter_window = self.findChild(QGridLayout, 'grid_filter_window')
        self.filter_window.hide()
        self.serach_button.clicked.connect(self.button_action)
        self.b2.clicked.connect(self.button_close_action)
        self.show()

    def button_action(self):
        self.filter_window.show()

    def button_close_action(self):
        self.filter_window.hide()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
333333333333333333333333333333333333333333