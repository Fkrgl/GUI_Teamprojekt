import json
import os.path
import requests
import sys
import re
from pymongo import MongoClient
import time
import threading

############################ thread hadeling #####################################

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

###################################### API #############################################

def get_variants_from_DataFrame(DataFrame):
    variants = [region_caller(DataFrame.iloc[i,:]) for i in range(len(DataFrame))]
    return variants



def mult_region_caller(lineList):

    if lineList[0] != '':
        chromosome = re.findall(r'\d+', lineList[0]) # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if lineList[1] != '':
        pos = lineList[1]

    if lineList[3] != '':
        ref = lineList[3]

    if lineList[4] != '':
        alt = lineList[4]

    variantCall = "{} {} . {} {} . . .".format(chromosome, pos, ref, alt)

    return variantCall



'''  reads a line of the given vcf file and returns REST API inquiry for that line '''


def region_caller(snv):
    possibleCharacters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']

    if snv['CHROM'] != '':
        chromosome = re.findall(r'\d+', str(
            snv['CHROM']))  # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if snv['POS'] != '':
        pos = snv['POS']

    if snv['ID'] != '' and snv['ID'] != '.':
        specID = snv['ID']

    if len(snv['ALT']) == 1:
        if snv['ALT'] in possibleCharacters:
            alt = snv['ALT']
            variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome, pos, pos, alt)

    elif len(snv['ALT']) > 1:

        matched_list = [characters in possibleCharacters for characters in snv[4]]
        if all(matched_list) == True:
            alt = snv['ALT']
            variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome, pos, pos, alt)

    elif 'DUP' in snv['ALT']:
        ref = 'DUP'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome, pos, pos, ref)
    elif 'DEL' in snv['ALT']:
        ref = 'DEL'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome, pos, pos, ref)
    elif 'INV' in snv['ALT']:
        ref = 'INV'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome, pos, pos, ref)
        # variantCall = "REST API does not know INV"
    else:
        variantCall = "Cant perform on this (ref-) notation"

    return variantCall



def write_to_db(currentVar, ApiResultList, database):
    print("writing {} to cache".format(currentVar))
    cacheDic = {"_id" : currentVar, "data" : ApiResultList[0]}
    database.variantsCollection.insert_one(cacheDic)

def variantAnnotation_exists_in_cache(currentVar, db):
    if db.variantsCollection.count_documents({"_id": currentVar}) > 0:
        return True
    else: return False


def rerun_api_request_503(request, server, currentVar):
    print("called")
    for i in range(3):
        print("Try no.: ", i+1, " ", request.status_code)
        time.sleep(2)
        r = requests.get(server + currentVar, headers={ "Content-Type" : "application/json"})

        if request.status_code != 503:
            print(r.status_code)
            decoded = request.json()
        #break # would move out first try, however server could somehow malfunction and incorrectly assign it as 400 even though its correct
        else:
            print("else called")
            if r.ok:
                print("ok")
                decoded = request.json()
                break

    return decoded


''' performs actual task. Calls each item of the list of inquiries created in get_variants() in the REST API and prints out the resulting annotations as a list of dictionaries (?) '''

def fetch_annotation(variants, QMainWindow):

    client = MongoClient("mongodb://91.89.90.5:27017/")
    db = client.variantsDB
    collection = db.variantsCollection


    server = "https://rest.ensembl.org"
    progress_count = 0
    for currentVar in variants:
        #currentID = "/vep/human/region/1:62728838-62728838/V?"
        print(currentVar)


        if currentVar == "Cant perform on this (ref-) notation" or currentVar == "REST API does not know INV":
            print(currentVar)
            pass

        else:

            if variantAnnotation_exists_in_cache(currentVar, db):
                print("in cache")

                specItem = db.variantsCollection.find({"_id" : currentVar})

                for document in specItem:
                    print(document)

            else:
                print("not in cache")

                r = requests.get(server + currentVar, headers={ "Content-Type" : "application/json"})
                print(r)

                if not r.ok:
                    #if r.status_code == 503:
                        #rerun_api_request_503(r,server,currentVar)
                    if r.status_code == 503:
                        for i in range(3):
                            print("Try no.: ", i+1, " ", r.status_code)
                            time.sleep(2)
                            r = requests.get(server + currentVar, headers={ "Content-Type" : "application/json"})
                            if r.status_code != 503 or r.status_code != 200:
                                print(r.status_code)
                                #break # would move out first try, however server could somehow malfunction and incorrectly assign it as 400 even though its correct
                            else:
                                print("else called")
                                if r.ok:
                                    print("ok")
                                    break
                    else:
                        print(r.status_code)
                else:
                    print(r.status_code)

                #if not r.ok:
                 #   r.raise_for_status()
                  #  sys.exit()
                decoded = r.json() # list
                #if type(decoded) == list:
                 #   decoded.insert(0, currentVar) # inserts id at front of list (use to access specific file id in db respectively to  check whether id is already present in db or if api has to be called)

                print(repr(decoded)) # prints list as string

                if type(decoded) == list:
                    write_to_db(currentVar,decoded,db)
                # update progress bar
                progress_count += 1
                QMainWindow.set_progressbar_value(progress_count)



if __name__ == "__main__":
    fetch_annotation()
    #get_variants()


