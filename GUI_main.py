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
        self.vcf_table.setAlternatingRowColors(True)
        self.vcf_table.setStyleSheet("alternate-background-color: PowderBlue")


        self.actionLoad_File.triggered.connect(self.load_file_from_filebrowser)
        self.search_button.clicked.connect(self.button_action)
        self.button_close.clicked.connect(self.button_close_action)
        #self.vcf_table.clicked.connect(self.select_row)
        self.button_annotation.clicked.connect(self.display_selected_snv_annotations)



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

    def create_annotation_tab(self):
        """
        creates a second tab with the annotation table
        """
        self.annotation_tab = QWidget()
        self.tab_window_tables.addTab(self.annotation_tab, "Annotations")
        self.tab_window_tables.setTabText(0, 'VCF')
        # load annotations in table

    def display_selected_snv_annotations(self):
        """
        save selected row indices of the (annotation) table, search for each selected snv (row) all annotations and dis-
        playes annotations in a new table in a pop up window
        """
        indexes = self.vcf_table.selectionModel().selectedRows()
        for index in sorted(indexes):
            print('Row %d is selected' % index.row())
        # rest has to be implemented



if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
