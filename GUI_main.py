import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import *
from PyQt5 import uic
from TableModel import *
from API import *
import _thread, threading
import time


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('Qt_designer/test_0.ui', self)
        self.error_dialog1 = uic.loadUi('Qt_designer/error_dialog1.ui')
        self.seleceted_anno_dialog = uic.loadUi('Qt_designer/seleceted_anno_dialog.ui')

        # main window
        self.setWindowTitle('SNV Annotation Tool')
        # move main window to center of screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # menu bar

        # filter
        self.filter_window.hide()

        # table
        self.vcf_table.setAlternatingRowColors(True)
        self.vcf_table.setStyleSheet("alternate-background-color: PowderBlue")


        self.actionLoad_File.triggered.connect(self.load_file_from_filebrowser)
        self.search_button.clicked.connect(self.button_action)
        self.button_close.clicked.connect(self.button_close_action)
        self.error_dialog1.button_err_dlg.clicked.connect(self.hide_err_dlg_window)
        self.button_annotation.clicked.connect(self.display_selected_snv_annotations)  # this button should only work if a table is already diplayed


        self.show()

    def button_action(self):
        self.filter_window.show()

    def button_close_action(self):
        self.filter_window.hide()

    def show_err_dlg_window(self, error_message):
        self.error_dialog1.error_dlg_label.setText(error_message)
        self.error_dialog1.error_dlg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_dialog1.move(self.mapToGlobal(
            self.rect().center() - self.error_dialog1.rect().center()))  # move error dialog to main window center
        self.error_dialog1.show()

    def hide_err_dlg_window(self):
        self.error_dialog1.hide()


    def API_request_as_thread(self, variants):
        """
        starts api request as one thread for all annotations. Method informs user about status of the request after it
        is finished
        :param variants: snv information
        """
        try:
            thread1 = API_thread(1, "Thread-2", 2, variants)
            thread2 = Loading_thread(2, thread1, self)
            # Start new Threads
            thread1.start()
            thread2.start()
        except:
            self.show_err_dlg_window('annotation request failed!')




    def load_file_from_filebrowser(self):
        """
        Filebrowser loads vcf file in a table and diplays it
        """
        filename = QFileDialog.getOpenFileName()
        file_path = filename[0]
        if 'vcf' in file_path:
            if get_header_count(file_path) != None:
                header_count = get_header_count(file_path)
                data = create_data_frame(file_path, header_count)
                self.vcf_model = TableModel(data)
                self.vcf_table.setModel(self.vcf_model)
                # load annotations in second tab
                variants = get_variants_from_DataFrame(self.vcf_model._data)
                self.API_request_as_thread(variants)
                self.create_annotation_tab()
            else:
                self.show_err_dlg_window('selected file is not in VCF!')
        else:
            self.show_err_dlg_window('selected file is not in VCF!')

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
        # get annotations from annotation table
        # display annotations in dialog table view window





if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
