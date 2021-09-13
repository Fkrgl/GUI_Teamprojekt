import os.path
import requests
import sys, re, threading
import time
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

server = "http://localhost:5000"

def get_variants_from_DataFrame(DataFrame):
    variants = [region_caller(DataFrame.iloc[i,:]) for i in range(len(DataFrame))]
    return variants



def region_caller(snv):
    """
    Creates server request for each Variant in vcf file
    :param: Pandas df representing vcf
    :rtype: String representing server request
    """

    possibleCharacters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']
    chromosome = ""
    pos = ""
    alt = ""


    if snv['chrom'] != '':
        chromosome = re.findall(r'\d+', str(snv['chrom'])) # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if snv['pos'] != '':
        pos = snv['pos']

    if len(snv['ref']) > 1: # DELETION
        pos = pos +1
        alt = '-'

    else:
        if len(snv['alt']) == 1:
            if snv['alt'] in possibleCharacters:
                alt = snv['alt']


        elif len(snv['alt']) > 1:

            matched_list = [characters in possibleCharacters for characters in snv[4]]
            if all(matched_list) == True:
                alt = snv['alt']


    variantCall = "/annotate/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)


    return variantCall

    '''possibleCharacters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']

    if snv['chrom'] != '':
        chromosome = re.findall(r'\d+', str(snv['chrom'])) # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if snv['pos'] != '':
        pos = snv['pos']

    if len(snv['alt']) == 1:
        if snv['alt'] in possibleCharacters:
            alt = snv['alt']
            variantCall = "/annotate/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)

    elif len(snv['alt']) > 1:

        matched_list = [characters in possibleCharacters for characters in snv[4]]
        if all(matched_list) == True:
            alt = snv['alt']
            variantCall = "/annotate/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)

    elif 'DUP' in snv['alt']:
        alt = 'DUP'
        variantCall = "/annotate/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)
    elif 'DEL' in snv['alt']:
        alt = 'DEL'
        variantCall = "/annotate/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)
    elif 'INV' in snv['alt']:
        alt = 'INV'
        variantCall = "/annotate/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)
        #variantCall = "REST API does not know INV"
    else:
        variantCall = "Cant perform on this (ref-) notation"

    return variantCall'''



''' performs actual task. Calls each item of the list of inquiries created in get_variants() in the REST API and prints out the resulting annotations as a list of dictionaries (?) '''



class Worker(QObject):
    finished = pyqtSignal()
    change_progress_value = pyqtSignal(int)
    result = pyqtSignal(list)

    def __init__(self, variants, parent=None):
        QObject.__init__(self, parent)
        self.dataForTable = []
        self.variants = variants
        # or some other needed attributes


    def run(self):
        """
        sends Annotation requests to localhost REST API server
        :param: String -> variant request string (created in get_variants_from_DataFrame
        :rtype: List of Annotation results from Server
        """
        #server = "http://localhost:5000/"

        progress_count = 0
        errorDict = {}
        print("run called")

        for variant in self.variants:
            try:
                if variant == "Cant perform on this (ref-) notation" or variant == "REST API does not know INV":
                    #print("Can't perform annotation. Wrong datatype")
                    print(variant)
                    pass
                else:
                    ext = variant
                    try:
                        r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})
                    except requests.exceptions.ConnectionError:
                        requests.status_code = "Connection refused"

                    decoded = r.json() # list
                    print(repr(decoded))
                    if 'error' not in decoded[1]:
                        self.dataForTable.append(decoded[1])

                    if type(decoded[1]) == dict:
                        if 'error' in decoded[1].keys():
                            errorDict.update({variant : decoded[1]})
            except:
                pass
            progress_count += 1
            self.change_progress_value.emit(progress_count)

        self.finished.emit()
        self.result.emit(self.dataForTable)
        print(self.dataForTable)

    # find out what this emmit can do
    # it seems to pass infromation to the gui, you could try to use it as a return signal after the process emmits a
    # finished signal


if __name__ == "__main__":
    pass

