import os.path
import requests
import sys
import re

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



def region_caller(lineList):

    if lineList[0] != '':
        chromosome = re.findall(r'\d+', lineList[0]) # extracts only the integer from the chromosome-notation (e.g. if 'chr1' --> 1)
        chromosome = chromosome[0]

    if lineList[1] != '':
        pos = lineList[1]

    if lineList[2] != '' and lineList[2] != '.':
        specID = lineList[2]

    if lineList[4] in ['A', 'C', 'G', 'T', 'a', 'c', 'g', 't']:
        ref = lineList[4]
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'DUP' in lineList[4]:
        ref = 'DUP'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'DEL' in lineList[4]:
        ref = 'DEL'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    elif 'INV' in lineList[4]:
        ref = 'INV'
        variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
        #variantCall = "REST API does not know INV"
    else:
        variantCall = "Cant perform on this (ref-) notation"

        #else:
        #   variantCall = "False"

    #variantCall = "/vep/human/region/{}:{}-{}/{}?".format(chromosome,pos,pos,ref)
    return variantCall



''' performs actual task. Calls each item of the list of inquiries created in get_variants() in the REST API and prints out the resulting annotations as a list of dictionaries (?) '''

def fetch_annotation():

    server = "https://rest.ensembl.org"
    #ext = "/vep/human/region/21:25587758-25587758/A?"

    #ext = "/vep/human/hgvs/ENST00000366667:c.803C>T?"
    #ext =  "/vep/human/region/genomic region/" # vep/:species/region/:region/:allele/

    for variant in get_variants():
        currentID = variant

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
            print(repr(decoded)) # prints list as string





if __name__ == "__main__":
    fetch_annotation()

#getVariants()