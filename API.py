import os.path
import requests
import sys, re, threading
import time
from PyQt5.QtWidgets import *


def get_variants_from_DataFrame(DataFrame):
    variants = [region_caller(DataFrame.iloc[i,:]) for i in range(len(DataFrame))]
    return variants



def region_caller(snv):
    possibleCharacters = ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']

    if snv['chrom'] != '':
        chromosome = re.findall(r'\d+', str(snv['chrom'])) # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if snv['pos'] != '':
        pos = snv['pos']

    if snv['id'] != '' and snv['id'] != '.':
        specID = snv['id']
        
    if len(snv['alt']) == 1:
        if snv['alt'] in possibleCharacters:
            alt = snv['alt']
            variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)

    elif len(snv['alt']) > 1:

        matched_list = [characters in possibleCharacters for characters in snv[4]]
        if all(matched_list) == True:
            alt = snv['alt']
            variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,alt)

    elif 'DUP' in snv['alt']:
        ref = 'DUP'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'DEL' in snv['alt']:
        ref = 'DEL'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'INV' in snv['alt']:
        ref = 'INV'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
        #variantCall = "REST API does not know INV"
    else:
        variantCall = "Cant perform on this (ref-) notation"

    return variantCall



''' performs actual task. Calls each item of the list of inquiries created in get_variants() in the REST API and prints out the resulting annotations as a list of dictionaries (?) '''

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

    return results # results


if __name__ == "__main__":
    fetch_annotation_new()

