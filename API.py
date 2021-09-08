import os.path
import requests
import sys, re, threading
import time
from PyQt5.QtWidgets import *


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

    return variantCall



''' performs actual task. Calls each item of the list of inquiries created in get_variants() in the REST API and prints out the resulting annotations as a list of dictionaries (?) '''

def fetch_annotation_new(variants, QMainWindow):
    """
    sends Annotation requests to localhost REST API server
    :param: String -> variant request string (created in get_variants_from_DataFrame
    :rtype: List of Annotation results from Server
    """
    server = "http://192.168.178.95:5000"

    results = []
    progress_count = 0
    errorDict = {}

    for variant in variants:
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
                    results.append(decoded[1])

                if type(decoded[1]) == dict:
                    if 'error' in decoded[1].keys():
                        errorDict.update({variant : decoded[1]})
        except:
            pass


    return results # results


if __name__ == "__main__":
    fetch_annotation_new()

