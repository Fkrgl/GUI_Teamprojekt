import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import *
from PyQt5 import uic
from TableModel import *


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


        self.show()

    def button_action(self):
        self.filter_window.show()

    def button_close_action(self):
        self.filter_window.hide()

    def load_file_from_filebrowser(self):

        """
        Filebrowser loads vcf file in a table and diplays it
        """

        filename = QFileDialog.getOpenFileName()
        file_path = filename[0]
        if 'vcf' in file_path:
            header_count = get_header_count(file_path)
            data = create_data_frame(file_path, header_count)
            self.model = TableModel(data)
            self.vcf_table.setModel(self.model)
            # load annotations in second tab
            self.create_annotation_tab()
        else:
            print("The selected file is not in variant call format!")
            # open Error dialog window

    # def fill_table(self, file_path):
    #     with open(file_path, 'r') as file:
    #         for line in file:
    #             if not line.startswith('##'):
    #                 if line.startswith('#'):
    #                     table_header = line[1:-1].split('\t')
    #                     self.vcf_table.setColumnCount(len(table_header))
    #                     self.vcf_table.setHorizontalHeaderLabels(table_header)
    #                 else:
    #                     table_items = line.strip().split('\t')
    #                     rowPosition = self.vcf_table.rowCount()
    #                     self.vcf_table.insertRow(rowPosition)
    #                     for n_col in range(len(table_header)):
    #                         self.vcf_table.setItem(rowPosition, n_col, QTableWidgetItem(table_items[n_col]))

    def create_annotation_tab(self):
        self.annotation_tab = QWidget()
        self.tab_window_tables.addTab(self.annotation_tab, "Annotations")
        self.tab_window_tables.setTabText(0, 'VCF')

    def select_row(self):
        indexes = self.vcf_table.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
