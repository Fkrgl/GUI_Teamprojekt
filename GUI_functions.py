from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

'''
Figure out how to add minimize and maximize buttons to a dialog window
'''
class MyWindow(QMainWindow):

    def __init__(self):
        super(MyWindow, self).__init__()
        self.setGeometry(200, 200, 700, 600)        # self is the window itself!
        self.setWindowTitle("My window")
        self.ui_init()

    def ui_init(self):
        # label
        self.label = QtWidgets.QLabel(self)       # label should show up on the window
        self.label.setText("boring")
        self.label.move(50,50)                    # move label 50 50 starting at 0 0 (left upper corner)

        # Button
        self.b1 = QtWidgets.QPushButton(self)     # self because the object (QMainWindow) is the Window we are adding stuff on
        self.b2 = QtWidgets.QPushButton(self)
        self.b3 = QtWidgets.QPushButton(self)
        self.b1.setText("Change label")           # self in front of all widges: Thei are attributes of the instance and can be accessed in the whole code
        self.b2.move(0,100)
        self.b2.setText("Dialog")
        self.b3.move(0, 200)
        self.b3.setText("Search Dialog")

        # connect buttons with a functions
        self.b1.clicked.connect(self.button_function)                # clicked is an event
        self.b2.clicked.connect(self.button_dialog)
        self.b3.clicked.connect(self.button_extra_dialog)

    # change label
    def button_function(self):
        self.label.setText("You clicked the button")
        self.update()                                 # adjust label size

    def button_dialog(self):
        dw = QtWidgets.QDialog(self)                  # passing self so that the main window stops when dialog shows up
        dw.resize(100,100)
        dw.setWindowTitle("this is a dialog window")
        dw.setWindowFlag(Qt.WindowMaximizeButtonHint, True)
        dw.exec()

    '''Method sets up a search dialog window from qt designer'''
    def button_extra_dialog(self):
        search_dlg = QtWidgets.QDialog()
        ui = Ui_search_dlg()
        ui.setupUi(search_dlg)
        search_dlg.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        search_dlg.show()
        search_dlg.exec()



    # update the size of a label (e.g after the length of the text changed)
    def update(self):
        self.label.adjustSize()

# Set up a window
# this method works like a main method
def window():
    app = QApplication(sys.argv)
    win = MyWindow()                  # create an onject of that class
    win.show()
    sys.exit(app.exec_())

'''
This class contains the dialog window
'''
class Ui_search_dlg(object):
    def setupUi(self, search_dlg):
        search_dlg.setObjectName("search_dlg")
        search_dlg.resize(325, 460)
        search_dlg.setWindowFlag(Qt.WindowMinimizeButtonHint, True)
        self.verticalLayout = QtWidgets.QVBoxLayout(search_dlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(search_dlg)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(search_dlg)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 1, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.checkBox = QtWidgets.QCheckBox(search_dlg)
        self.checkBox.setObjectName("checkBox")
        self.gridLayout_2.addWidget(self.checkBox, 0, 0, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(search_dlg)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout_2.addWidget(self.lineEdit_2, 0, 1, 1, 1)
        self.checkBox_2 = QtWidgets.QCheckBox(search_dlg)
        self.checkBox_2.setObjectName("checkBox_2")
        self.gridLayout_2.addWidget(self.checkBox_2, 1, 0, 1, 1)
        self.comboBox = QtWidgets.QComboBox(search_dlg)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_2.addWidget(self.comboBox, 1, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)


        self.retranslateUi(search_dlg)
        QtCore.QMetaObject.connectSlotsByName(search_dlg)

    def retranslateUi(self, search_dlg):
        _translate = QtCore.QCoreApplication.translate
        search_dlg.setWindowTitle(_translate("search_dlg", "Dialog"))
        self.pushButton.setText(_translate("search_dlg", "Search"))
        self.checkBox.setText(_translate("search_dlg", "AF"))
        self.checkBox_2.setText(_translate("search_dlg", "impact"))
        self.comboBox.setCurrentText(_translate("search_dlg", "HIGH"))
        self.comboBox.setItemText(0, _translate("search_dlg", "HIGH"))
        self.comboBox.setItemText(1, _translate("search_dlg", "MEDIUM"))
        self.comboBox.setItemText(2, _translate("search_dlg", "LOW"))

if __name__ == '__main__':
    window()
