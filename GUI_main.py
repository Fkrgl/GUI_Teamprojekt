import sys
from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from TableModel import *
from API import *
import _thread, threading
import concurrent.futures
import time



'''Think about making a own script for this class'''
# class Worker(QObject):
#     finished = pyqtSignal()
#     progress = pyqtSignal(int)
#     result = pyqtSignal(list)
#
#     def __init__(self, variants, parent=None):
#         QObject.__init__(self, parent)
#         self.dataForTable = []
#         self.variants = variants
#         # or some other needed attributes
#
#
#     def run(self):
#         self.dataForTable = fetch_annotation_new(self.variants, QMainWindow)
#         self.finished.emit()
#         self.result.emit(self.dataForTable)

    # find out what this emmit can do
    # it seems to pass infromation to the gui, you could try to use it as a return signal after the process emmits a
    # finished signal


class UI(QMainWindow):

    def __init__(self):
        super(UI, self).__init__()
        uic.loadUi('Qt_designer/test_0.ui', self)
        self.error_dialog1 = uic.loadUi('Qt_designer/error_dialog1.ui')
        self.selected_anno_dialog = uic.loadUi('Qt_designer/selected_anno_dialog.ui')

        # main window
        self.setWindowTitle('SNV Annotation Tool')
        # move main window to center of screen
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

        # menu bar
        self.button_annotation.setDisabled(True)
        self.button_export.setDisabled(True)
        self.label_loading.setHidden(True)
        self.progressBar.setHidden(True)

        # filter
        self.filter_window.hide()

        # table
        self.vcf_table.setAlternatingRowColors(True)
        self.vcf_table.setStyleSheet("alternate-background-color: PowderBlue")
        self.tables_loaded = False


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

    def show_err_dlg_window(self, error_message, window_title):
        self.error_dialog1.setWindowTitle(window_title)
        self.error_dialog1.error_dlg_label.setText(error_message)
        self.error_dialog1.error_dlg_label.setAlignment(QtCore.Qt.AlignCenter)
        self.error_dialog1.move(self.mapToGlobal(
            self.rect().center() - self.error_dialog1.rect().center()))  # move error dialog to main window center
        self.error_dialog1.show()

    def hide_err_dlg_window(self):
        self.error_dialog1.hide()

    def set_progressbar_maximum(self, maximum):
        self.progressBar.setMaximum(maximum)

    def set_progressbar_value(self, counter):
        self.progressBar.setValue(counter)

    def set_progressbar_visibility(self, isHidden):
        self.progressBar.setHidden(isHidden)
        self.label_loading.setHidden(isHidden)

    def load_file_from_filebrowser(self):
        """
        Filebrowser loads vcf file in a table and diplays it. Also starts API request and displayes the annotations in
        the annotation table
        """
        # check if a file is already loaded, if so reset annotation functionalities
        if self.tables_loaded:
            self.tab_window_tables.removeTab(1)
            self.button_annotation.setDisabled(True)
        # open file browser
        filename = QFileDialog.getOpenFileName()
        file_path = filename[0]
        if 'vcf' in file_path:
            if get_header_count(file_path) != None:

                # set up vcf table
                header_count = get_header_count(file_path)
                data_vcf = create_data_frame(file_path, header_count)
                self.vcf_model = TableModel(data_vcf)
                self.vcf_table.setModel(self.vcf_model)
                variants = get_variants_from_DataFrame(self.vcf_model._data)

                # set name of annotation tab
                self.tab_window_tables.setTabText(0, 'VCF')

                # call API and display annotation table
                self.call_server_as_therad(variants)
                self.tables_loaded = True

            else:
                self.show_err_dlg_window('selected file is not in VCF!', 'Error')
        else:
            self.show_err_dlg_window('selected file is not in VCF!', 'Error')




    def create_annotation_tab(self):
        self.annotation_tab = QWidget()
        self.annotation_tab.layout = QVBoxLayout()
        self.annotation_tab.layout.setContentsMargins(0, 0, 0, 0)
        self.annotation_tab.layout.addWidget(self.annotation_table)
        self.annotation_tab.setLayout(self.annotation_tab.layout)
        self.tab_window_tables.addTab(self.annotation_tab, "Annotations")

    def display_selected_snv_annotations(self):
        """
        save selected row indices of the (annotation) table, search for each selected snv (row) all annotations and dis-
        playes annotations in a new table in a pop up window
        """
        indices = self.vcf_table.selectionModel().selectedRows()
        selected_annotations = pd.DataFrame(columns=self.annotation_table_model._data.columns)
        for index in indices:
            snv = self.vcf_model.get_row(index.row())
            selected_data = self.get_annotations_of_selected_snv(snv)
            selected_annotations = selected_annotations.append(selected_data, ignore_index=True)

        # set up table with annotations
        print(selected_annotations)
        self.selected_anno_table_model = TableModel(selected_annotations)
        self.selected_anno_dialog.selected_anno_table.setModel(self.selected_anno_table_model)
        self.selected_anno_dialog.selected_anno_table.setAlternatingRowColors(True)
        self.selected_anno_dialog.selected_anno_table.setStyleSheet("alternate-background-color: PowderBlue")
        self.selected_anno_dialog.show()


    def get_annotations_of_selected_snv(self, snv):
        anno_data = self.annotation_table_model._data
        selected_data = anno_data.loc[(anno_data['pos'] == snv['pos'])
                            & (anno_data['chrom'] == snv['chrom'])
                            & (anno_data['ref'] == snv['ref'])
                            & (anno_data['alt'] == snv['alt'])]
        return selected_data


    def create_annotation_table(self, data):
        self.annotation_table = QTableView()
        self.annotation_table.setAlternatingRowColors(True)
        self.annotation_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.annotation_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.annotation_table.setStyleSheet("alternate-background-color: PowderBlue")
        self.annotation_table_model = TableModel(data)
        self.annotation_table.setModel(self.annotation_table_model)

    def add_annotation_to_table(self, annotations):
        """
        extracts important features from annotations of API and adds them as a new annotation to the annotation table
        :param annotation: return dictionary from REST API for one SNP request
        """
        entries = []
        print("add_annotation_to_table")
        # parse the annotations for the table
        for anno in annotations:
            for conseqeunces in anno['transcript_consequences']:
                bases = anno['allele_string'].split('/')
                ref = bases[0]
                alt = bases[1]
                entry = {'chr': 'chr' + str(anno['seq_region_name']),
                         'pos': anno['start'],
                         'strand' : anno['strand'],
                         'input': anno['input'],
                         'ref': ref,
                         'alt' : alt,
                         'transcript_id' : conseqeunces['transcript_id'],
                         'biotype' : conseqeunces['biotype'],
                         'impact' : conseqeunces['impact'],
                         'consequnce_terms' : ''.join(conseqeunces['consequence_terms'])}
                entries.append(entry)
                print('chr' + str(anno['seq_region_name']))

                print(conseqeunces)
        data = pd.DataFrame(data=entries, columns=['chr', 'pos', 'input', 'ref', 'alt', 'transcript_id', 'biotype', 'impact', 'consequnce_terms'])
        data = data.rename(columns={'chr' : 'chrom'})
        #create table model with given data
        self.create_annotation_table(data)
        self.create_annotation_tab()


    def call_server_as_therad(self, variants):
        """
        send the SNVs to the server and siplay the results in an annotation table
        :param variants: rows of vcf file
        """
        # Step 2: Create a QThread object
        self.thread = QThread()
        # Step 3: Create a worker object
        self.worker = Worker(variants)
        # Step 4: Move worker to the thread
        self.worker.moveToThread(self.thread)
        # progress bar
        self.set_progressbar_maximum(len(variants))
        self.set_progressbar_visibility(False)
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.change_progress_value.connect(self.set_progressbar_value)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        isHidden = True
        message = 'Annotations finished!'
        title = 'Notification'
        # get data
        self.thread.finished.connect(self.get_annotation_data_from_thread)
        # hide progress bar
        self.thread.finished.connect(lambda: self.set_progressbar_visibility(isHidden))
        # display notification window after thread finished
        self.thread.finished.connect(lambda: self.show_err_dlg_window(error_message=message, window_title=title))
        # make annotation button available
        self.thread.finished.connect(self.unlock_annotation_button)

    def get_annotation_data_from_thread(self):
        self.add_annotation_to_table(self.worker.dataForTable)

    def unlock_annotation_button(self):
        self.button_annotation.setEnabled(True)

    def safe_variants_to_file(self):
        """

        """
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())
