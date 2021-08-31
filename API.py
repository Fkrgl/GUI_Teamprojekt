import os.path
import requests
import sys, re, threading
import time
from PyQt5.QtWidgets import *


class API_thread(threading.Thread):
    def __init__(self, threadID, name, counter, variants, QMainWindow):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        self.varaints = variants
        self.QMainWindow = QMainWindow

    def run(self):
        fetch_annotation(self.varaints, self.QMainWindow)


class Loading_thread(threading.Thread):
    def __init__(self, threadID, thread, QMainWindow):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.thread = thread
        self.QMainWindow = QMainWindow

    def run(self):
        wait_for_loading(self.thread, self.QMainWindow)


def wait_for_loading(thread, QMainWindow):
    while thread.is_alive():
        time.sleep(1)
    QMainWindow.show_err_dlg_window('Annotation requests finished!', 'Message')
    QMainWindow.set_progressbar_visibility(True)


def get_variants():
    annotationList = []

    f = open('/home/mp/Documents/Teamprojekt/API/ensembl-vep/examples/homo_sapiens_GRCh38.vcf') # has to be softcoded!
    #f = open('/home/mp/Documents/Teamprojekt/API/vcf_files/cnvnator.vcf')


    for line in f:

        if line.startswith("#") or line.startswith("\""):
            pass
        else:
            eachCol = line.split("\t")
            idLine = eachCol[2]

            '''if(idLine != '' or idLine != ''): # if line has a ID
                annotationCall = id_caller(eachCol)

            else:'''
            annotationCall = region_caller(eachCol) # builds string necessary for the REST API

            #print(annotationCall)


            annotationList.append(annotationCall)

    return annotationList


def get_variants_from_DataFrame(DataFrame):
    variants = [region_caller(DataFrame.iloc[i,:]) for i in range(len(DataFrame))]
    return variants




def region_caller(snv):
    possibleCharacters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']

    if snv['CHROM'] != '':
        chromosome = re.findall(r'\d+', str(snv['CHROM'])) # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if snv['POS'] != '':
        pos = snv['POS']

    if snv['ID'] != '' and snv['ID'] != '.':
        specID = snv['ID']
        
    if len(snv['ALT']) == 1:
        if snv['ALT'] in possibleCharacters:
            alt = snv['ALT']
            variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)

    elif len(snv['ALT']) > 1:

        matched_list = [characters in possibleCharacters for characters in snv[4]]
        if all(matched_list) == True:
            alt = snv['ALT']
            variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)

    elif 'DUP' in snv['ALT']:
        ref = 'DUP'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'DEL' in snv['ALT']:
        ref = 'DEL'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'INV' in snv['ALT']:
        ref = 'INV'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
        #variantCall = "REST API does not know INV"
    else:
        variantCall = "Cant perform on this (ref-) notation"

    return variantCall



''' performs actual task. Calls each item of the list of inquiries created in get_variants() in the REST API and prints out the resulting annotations as a list of dictionaries (?) '''

def fetch_annotation(variants, QMainWindow):

    server = "https://grch37.rest.ensembl.org"
    #server = "https://rest.ensembl.org"
    #ext = "/vep/human/region/21:25587758-25587758/A?"

    #ext = "/vep/human/hgvs/ENST00000366667:c.803C>T?"
    #ext =  "/vep/human/region/genomic region/" # vep/:species/region/:region/:allele/
    progress_count = 0
    for variant in variants:
        currentID = variant
        print(variant)
        try:
            if variant == "Cant perform on this (ref-) notation" or variant == "REST API does not know INV":
                #print("Can't perform annotation. Wrong datatype")
                print(currentID)
                pass
            else:
                ext = currentID
                r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

                if not r.ok:
                    r.raise_for_status()
                    sys.exit()

                decoded = r.json() # list
                decoded.insert(0, currentID) # inserts id at front of list (use to access specific file id in db respectively to  check whether id is already present in db or if api has to be called)
                #print(repr(decoded[1])) # prints list as string
                print(decoded[1])
                for key in decoded[1]:
                    print(key, ' :')
                    print(decoded[1][key])
                    print()
                # maybe give each result to a function in the main function to splice them and directly saves them in the annotation data frame
                QMainWindow.add_annotation_to_table(decoded[1])
        except:
            pass
        progress_count += 1
        QMainWindow.set_progressbar_value(progress_count)


def fetch_annotation_new(variants, QMainWindow):

    server = "https://grch37.rest.ensembl.org"
    #server = "https://rest.ensembl.org"
    results = []
    progress_count = 0
    for variant in variants:
        currentID = variant
        print(variant)
        try:
            if variant == "Cant perform on this (ref-) notation" or variant == "REST API does not know INV":
                #print("Can't perform annotation. Wrong datatype")
                print(currentID)
                pass
            else:
                ext = currentID
                r = requests.get(server+ext, headers={ "Content-Type" : "application/json"})

                if not r.ok:
                    r.raise_for_status()
                    sys.exit()

                decoded = r.json() # list
                decoded.insert(0, currentID) # inserts id at front of list (use to access specific file id in db respectively to  check whether id is already present in db or if api has to be called)
                #print(repr(decoded[1])) # prints list as string
                print(decoded[1])
                results.append(decoded[1])
        except:
            pass

    return results


if __name__ == "__main__":
    fetch_annotation()

