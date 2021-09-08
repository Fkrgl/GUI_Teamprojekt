import sys

from PySide6.QtUiTools import QUiLoader
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QFile, QIODevice
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import uic
from TableModel import *
from API import *
import pandas as pd
import _thread, threading
import concurrent.futures
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
        self.label_loading.setHidden(True)
        self.progressBar.setHidden(True)

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

            else:
                self.show_err_dlg_window('selected file is not in VCF or empty!', 'Error')
        else:
            self.show_err_dlg_window('selected file is not in VCF or empty!', 'Error')




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
        cells_data = []
        tester = []

        try:
            indexes = self.vcf_table.selectionModel().selectedRows()
            for index in sorted(indexes):
                print('Row %d is selected' % index.row())
                #print(index.data())
                cells_data.append([index.sibling(index.row(), c).data() for c in range(10)]) # creates a list of all items of selected row

            chr = re.findall(r'\d+', str(cells_data[0][0]))[0]
            pos = cells_data[0][1]
            self.find_annotations(chr, pos)

            # get annotations from annotation table
            # display annotations in dialog table view window
        except AttributeError:
            self.show_err_dlg_window('No Row selected', 'Error')

        except IndexError:
            self.show_err_dlg_window('Wait until Annotation is complete', 'Error')


    def find_annotations(self, chr, pos):
        selectedRowAnnotationList = []
        annotationData = self.annotation_table_model._data
        pos = int(pos)
        print(annotationData.loc[(annotationData['seq_region_name'] == chr) & (annotationData['start'] == pos)])





    def create_annotation_table(self, data):
        self.annotation_table = QTableView()
        self.annotation_table.setAlternatingRowColors(True)
        self.annotation_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.annotation_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.annotation_table.setStyleSheet("alternate-background-color: PowderBlue")
        self.annotation_table_model = TableModel(data)
        self.annotation_table.setModel(self.annotation_table_model)


    def check_if_from_cache(self, annotation):
        """
        checks whether single annotation is from cache or from VEP Server
        :param: single annotation (either list of dic or list of list of dic)
        :rtype: inner dictionary containing all annotation data
        """
        if type(annotation) == dict:
            annotationResult = annotation.get('data')
        else:
            annotationResult = annotation[0]

        return annotationResult


    def add_annotation_to_table(self, annotations):
        """
        extracts important features from annotations of API and adds them as a new annotation to the annotation table
        :param annotation: return dictionary from REST API for one SNP request
        """
        entries = []
        print("add_annotation_to_table")

        try:
            # parse the annotations for the table
            for annos in annotations:
                '''if "_id" in annos.keys():
                    print("true")
                    annotationResult = annotations[0].get('data')
                    print(type(annotationResult), ' from cache')

                else:
                    annotationResult = annotations[0]
                    print("from VEP")

                if type(annos) == dict:
                    annotationResult = annos.get('data')
                else:
                    annotationResult = annos[0]'''

                annotationResult = self.check_if_from_cache(annos)

                entry = {'seq_region_name': annotationResult['seq_region_name'],
                        'start': annotationResult['start'],
                        'strand': annotationResult['strand'],
                        'input': annotationResult['input'],
                        'allele_string': annotationResult['allele_string'],
                        'transcript_id' : '.',
                        'biotype' : '.',
                        'impact' : '.',
                        'consequnce_terms' : '.'}


                if 'transcript_consequences' in annotationResult:
                    for consequences in annotationResult.get('transcript_consequences'):
                        print(consequences)
                        entry = {'seq_region_name': annotationResult['seq_region_name'],
                                 'start': annotationResult['start'],
                                 'strand': annotationResult['strand'],
                                 'input': annotationResult['input'],
                                 'allele_string': annotationResult['allele_string'],
                                 'transcript_id' : consequences['transcript_id'],
                                 'biotype' : consequences['biotype'],
                                 'impact' : consequences['impact'],
                                 'consequnce_terms' : ''.join(consequences['consequence_terms'])}

                        entries.append(entry)

                else: entries.append(entry)


                #print(consequences)
            data = pd.DataFrame(data=entries, columns=['seq_region_name','start', 'input', 'allele_string', 'transcript_id', 'biotype', 'impact', 'consequnce_terms'])

            #create table model with given data

            self.create_annotation_table(data)
            self.create_annotation_tab()


        except IndexError:
            self.show_err_dlg_window('Server is down', 'Error')

        except AttributeError:
            self.show_err_dlg_window('NoneType object has not attribute get', 'Error')

    def save_annotation_frame(self,data):
        return data

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
        # Step 5: Connect signals and slots
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        #self.worker.progress.connect(self.reportProgress)
        # Step 6: Start the thread
        self.thread.start()

        # Final resets
        self.thread.finished.connect(self.get_annotation_data_from_thread)

    def get_annotation_data_from_thread(self):
        self.add_annotation_to_table(self.worker.dataForTable)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    UIWindow = UI()
    sys.exit(app.exec_())