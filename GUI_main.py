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
        # menu bar

        # filter
        self.filter_window.hide()

        # table

        self.actionLoad_File.triggered.connect(self.load_file_from_filebrowser)
        self.search_button.clicked.connect(self.button_action)
        self.button_close.clicked.connect(self.button_close_action)
        self.func_mappingSignal()


        self.show()

    def button_action(self):
        self.filter_window.show()

    def button_close_action(self):
        self.filter_window.hide()

    def load_file_from_filebrowser(self):
        filename = QFileDialog.getOpenFileName()
        file_path = filename[0]
        if 'vcf' in file_path:
            self.fill_table(file_path)
        else:
            print("The selected file is not in variant call format!")
            # open Error dialog window

    def fill_table(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                if not line.startswith('##'):
                    if line.startswith('#'):
                        table_header = line[1:-1].split('\t')
                        self.vcf_table.setColumnCount(len(table_header))
                        self.vcf_table.setHorizontalHeaderLabels(table_header)
                    else:
                        table_items = line.strip().split('\t')
                        rowPosition = self.vcf_table.rowCount()
                        self.vcf_table.insertRow(rowPosition)
                        for n_col in range(len(table_header)):
                            self.vcf_table.setItem(rowPosition, n_col, QTableWidgetItem(table_items[n_col]))

    def func_mappingSignal(self):
        self.vcf_table.clicked.connect(self.func_test)

    def func_test(self, item):
        sf = "You clicked on {}".format(item.data())
        print(sf)
        item = self.vcf_table.selectedItems()
        for i in item:
            print(i.text())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())

    lalalalal