# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '../Qt_designer/test_0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ui_MainWindow(object):
    def setupUi(self, ui_MainWindow):
        ui_MainWindow.setObjectName("ui_MainWindow")
        ui_MainWindow.resize(1101, 905)
        ui_MainWindow.setStyleSheet("border-top-color: rgb(173, 127, 168);")
        self.centralwidget = QtWidgets.QWidget(ui_MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetFixedSize)
        self.horizontalLayout.setContentsMargins(0, 3, 3, 3)
        self.horizontalLayout.setSpacing(3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_button = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.search_button.sizePolicy().hasHeightForWidth())
        self.search_button.setSizePolicy(sizePolicy)
        self.search_button.setMinimumSize(QtCore.QSize(30, 30))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../Qt_designer/../resources/search_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.button_annotation = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_annotation.sizePolicy().hasHeightForWidth())
        self.button_annotation.setSizePolicy(sizePolicy)
        self.button_annotation.setMinimumSize(QtCore.QSize(30, 30))
        self.button_annotation.setObjectName("button_annotation")
        self.horizontalLayout.addWidget(self.button_annotation)
        self.toolButton = QtWidgets.QToolButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButton.sizePolicy().hasHeightForWidth())
        self.toolButton.setSizePolicy(sizePolicy)
        self.toolButton.setMinimumSize(QtCore.QSize(30, 30))
        self.toolButton.setObjectName("toolButton")
        self.horizontalLayout.addWidget(self.toolButton)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.label_loading = QtWidgets.QLabel(self.centralwidget)
        self.label_loading.setObjectName("label_loading")
        self.horizontalLayout.addWidget(self.label_loading)
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setMaximumSize(QtCore.QSize(200, 20))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 2, 4)
        self.filter_window = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.filter_window.sizePolicy().hasHeightForWidth())
        self.filter_window.setSizePolicy(sizePolicy)
        self.filter_window.setMinimumSize(QtCore.QSize(375, 0))
        self.filter_window.setMaximumSize(QtCore.QSize(16777215, 1666666))
        self.filter_window.setStyleSheet("")
        self.filter_window.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.filter_window.setFrameShadow(QtWidgets.QFrame.Raised)
        self.filter_window.setObjectName("filter_window")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.filter_window)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_2 = QtWidgets.QFrame(self.filter_window)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_2.setMaximumSize(QtCore.QSize(16777215, 20))
        self.frame_2.setStyleSheet("background-color:rgb(245, 245, 245)")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.button_close = QtWidgets.QToolButton(self.frame_2)
        self.button_close.setGeometry(QtCore.QRect(355, 1, 18, 18))
        self.button_close.setMaximumSize(QtCore.QSize(18, 18))
        self.button_close.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../Qt_designer/../resources/minimize_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.button_close.setIcon(icon1)
        self.button_close.setObjectName("button_close")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(2, 2, 67, 16))
        self.label_2.setObjectName("label_2")
        self.verticalLayout_5.addWidget(self.frame_2)
        self.groupBox = QtWidgets.QGroupBox(self.filter_window)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout_2.addWidget(self.comboBox)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.toolButton_4 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_4.setObjectName("toolButton_4")
        self.horizontalLayout_2.addWidget(self.toolButton_4)
        self.toolButton_5 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_5.setObjectName("toolButton_5")
        self.horizontalLayout_2.addWidget(self.toolButton_5)
        self.toolButton_3 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_3.setObjectName("toolButton_3")
        self.horizontalLayout_2.addWidget(self.toolButton_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.toolButton_6 = QtWidgets.QToolButton(self.groupBox)
        self.toolButton_6.setObjectName("toolButton_6")
        self.horizontalLayout_2.addWidget(self.toolButton_6)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout_2.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_2.addWidget(self.lineEdit_3)
        self.verticalLayout_5.addWidget(self.groupBox)
        self.groupBox_2 = QtWidgets.QGroupBox(self.filter_window)
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayout = QtWidgets.QFormLayout(self.groupBox_2)
        self.formLayout.setObjectName("formLayout")
        self.checkBox = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox.setObjectName("checkBox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.checkBox_2)
        self.checkBox_3 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_3.setObjectName("checkBox_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.checkBox_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_2.setObjectName("comboBox_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.comboBox_2)
        self.checkBox_7 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_7.setObjectName("checkBox_7")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.checkBox_7)
        self.checkBox_8 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_8.setObjectName("checkBox_8")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.checkBox_8)
        self.checkBox_5 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_5.setObjectName("checkBox_5")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_5)
        self.comboBox_3 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_3.setObjectName("comboBox_3")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.comboBox_3)
        self.comboBox_4 = QtWidgets.QComboBox(self.groupBox_2)
        self.comboBox_4.setObjectName("comboBox_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.comboBox_4)
        self.checkBox_4 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_4.setObjectName("checkBox_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.checkBox_4)
        self.checkBox_6 = QtWidgets.QCheckBox(self.groupBox_2)
        self.checkBox_6.setObjectName("checkBox_6")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.checkBox_6)
        self.spinBox_3 = QtWidgets.QSpinBox(self.groupBox_2)
        self.spinBox_3.setStepType(QtWidgets.QAbstractSpinBox.AdaptiveDecimalStepType)
        self.spinBox_3.setObjectName("spinBox_3")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.spinBox_3)
        self.doubleSpinBox = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox.setSingleStep(0.01)
        self.doubleSpinBox.setObjectName("doubleSpinBox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox)
        self.doubleSpinBox_2 = QtWidgets.QDoubleSpinBox(self.groupBox_2)
        self.doubleSpinBox_2.setSingleStep(0.01)
        self.doubleSpinBox_2.setObjectName("doubleSpinBox_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.doubleSpinBox_2)
        self.verticalLayout_5.addWidget(self.groupBox_2)
        self.groupBox_3 = QtWidgets.QGroupBox(self.filter_window)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.groupBox_3)
        self.scrollArea.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 333, 136))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton)
        self.pushButton_3 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout_3.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_4.setObjectName("pushButton_4")
        self.verticalLayout_3.addWidget(self.pushButton_4)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_3.addWidget(self.pushButton_2)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.horizontalLayout_3.addWidget(self.scrollArea)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.filter_window)
        self.groupBox_4.setObjectName("groupBox_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.groupBox_4)
        self.comboBox_5.setObjectName("comboBox_5")
        self.verticalLayout_4.addWidget(self.comboBox_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.toolButton_8 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_8.setObjectName("toolButton_8")
        self.horizontalLayout_4.addWidget(self.toolButton_8)
        self.toolButton_7 = QtWidgets.QToolButton(self.groupBox_4)
        self.toolButton_7.setObjectName("toolButton_7")
        self.horizontalLayout_4.addWidget(self.toolButton_7)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.gridLayout.addWidget(self.filter_window, 3, 1, 1, 2)
        self.tab_window_tables = QtWidgets.QTabWidget(self.centralwidget)
        self.tab_window_tables.setStyleSheet("")
        self.tab_window_tables.setElideMode(QtCore.Qt.ElideNone)
        self.tab_window_tables.setObjectName("tab_window_tables")
        self.vcf_tab = QtWidgets.QWidget()
        self.vcf_tab.setObjectName("vcf_tab")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.vcf_tab)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.vcf_table = QtWidgets.QTableView(self.vcf_tab)
        self.vcf_table.setStyleSheet("")
        self.vcf_table.setAlternatingRowColors(True)
        self.vcf_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.vcf_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.vcf_table.setTextElideMode(QtCore.Qt.ElideNone)
        self.vcf_table.setObjectName("vcf_table")
        self.vcf_table.verticalHeader().setVisible(True)
        self.vcf_table.verticalHeader().setHighlightSections(True)
        self.vcf_table.verticalHeader().setSortIndicatorShown(False)
        self.vcf_table.verticalHeader().setStretchLastSection(False)
        self.horizontalLayout_5.addWidget(self.vcf_table)
        self.tab_window_tables.addTab(self.vcf_tab, "")
        self.gridLayout.addWidget(self.tab_window_tables, 3, 0, 1, 1)
        self.grid_filter_window = QtWidgets.QGridLayout()
        self.grid_filter_window.setSpacing(0)
        self.grid_filter_window.setObjectName("grid_filter_window")
        self.gridLayout.addLayout(self.grid_filter_window, 3, 3, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setText("")
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 4, 0, 1, 4)
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.gridLayout.addLayout(self.formLayout_2, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        ui_MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ui_MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1101, 22))
        self.menubar.setStyleSheet("background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1,\n"
"                                      stop:0 white, stop:1 lightblue);   spacing: 3px;")
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        ui_MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ui_MainWindow)
        self.statusbar.setObjectName("statusbar")
        ui_MainWindow.setStatusBar(self.statusbar)
        self.actionLoad_File = QtWidgets.QAction(ui_MainWindow)
        self.actionLoad_File.setObjectName("actionLoad_File")
        self.menuFile.addAction(self.actionLoad_File)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(ui_MainWindow)
        self.tab_window_tables.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ui_MainWindow)

    def retranslateUi(self, ui_MainWindow):
        _translate = QtCore.QCoreApplication.translate
        ui_MainWindow.setWindowTitle(_translate("ui_MainWindow", "MainWindow"))
        self.search_button.setToolTip(_translate("ui_MainWindow", "Filter"))
        self.search_button.setText(_translate("ui_MainWindow", "..."))
        self.button_annotation.setToolTip(_translate("ui_MainWindow", "Annotations"))
        self.button_annotation.setText(_translate("ui_MainWindow", "A"))
        self.toolButton.setText(_translate("ui_MainWindow", "..."))
        self.label_loading.setText(_translate("ui_MainWindow", "loading...  "))
        self.label_2.setText(_translate("ui_MainWindow", "Filters"))
        self.groupBox.setTitle(_translate("ui_MainWindow", "GroupBox"))
        self.toolButton_4.setText(_translate("ui_MainWindow", "..."))
        self.toolButton_5.setText(_translate("ui_MainWindow", "..."))
        self.toolButton_3.setText(_translate("ui_MainWindow", "..."))
        self.toolButton_6.setText(_translate("ui_MainWindow", "..."))
        self.groupBox_2.setTitle(_translate("ui_MainWindow", "GroupBox"))
        self.checkBox.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_2.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_3.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_7.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_8.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_5.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_4.setText(_translate("ui_MainWindow", "CheckBox"))
        self.checkBox_6.setText(_translate("ui_MainWindow", "CheckBox"))
        self.doubleSpinBox.setSuffix(_translate("ui_MainWindow", "%"))
        self.doubleSpinBox_2.setSuffix(_translate("ui_MainWindow", "%"))
        self.groupBox_3.setTitle(_translate("ui_MainWindow", "GroupBox"))
        self.pushButton.setText(_translate("ui_MainWindow", "PushButton"))
        self.pushButton_3.setText(_translate("ui_MainWindow", "PushButton"))
        self.pushButton_4.setText(_translate("ui_MainWindow", "PushButton"))
        self.pushButton_2.setText(_translate("ui_MainWindow", "PushButton"))
        self.groupBox_4.setTitle(_translate("ui_MainWindow", "GroupBox"))
        self.toolButton_8.setText(_translate("ui_MainWindow", "..."))
        self.toolButton_7.setText(_translate("ui_MainWindow", "..."))
        self.menuFile.setTitle(_translate("ui_MainWindow", "File"))
        self.actionLoad_File.setText(_translate("ui_MainWindow", "Load File"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui_MainWindow = QtWidgets.QMainWindow()
    ui = Ui_ui_MainWindow()
    ui.setupUi(ui_MainWindow)
    ui_MainWindow.show()
    sys.exit(app.exec_())