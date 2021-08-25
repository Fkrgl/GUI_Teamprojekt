import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
import pandas as pd

class TableModel(QtCore.QAbstractTableModel):
    def __init__(self, data):
        super(TableModel, self).__init__()
        self._data = data

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._data.iloc[index.row(), index.column()]
            return str(value)

    def rowCount(self, index):
        return self._data.shape[0]

    def columnCount(self, index):
        return self._data.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._data.columns[section])

            if orientation == Qt.Vertical:
                return str(self._data.index[section])

def get_header_count( path):
    header_count = 0
    with open(path, 'r') as file:
        for line in file:
            if line.startswith('##'):
                header_count += 1
            else:
                if line.startswith('#'):
                    return header_count
    return None


def create_data_frame(path, header_count):
    data = pd.read_csv(path, sep='\t', header=header_count)
    return data