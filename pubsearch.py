import sys
from Bio import Entrez
from Bio import Medline

query = input("Enter search query: ")
MAX_COUNT = input("Maximum number of entries: ")
print("\n")

Entrez.email = "jorik.vanrijn@gmail.com"     # Always tell NCBI who you are
print("Searching...")
handle = Entrez.esearch(db="pubmed", term=query, retmax=MAX_COUNT, usehistory="y")
record = Entrez.read(handle)
webenv = record["WebEnv"]
query_key = record["QueryKey"]
count = int(record["Count"])

print('Total number of publications containing {0}: {1}'.format(query, record["Count"]))
idlist = record["IdList"]
handle = Entrez.efetch(db="pubmed", retmax=MAX_COUNT, webenv=webenv, query_key=query_key, rettype="medline", retmode="text")
input("---Press ENTER to continue---\n")
print("Parsing...")
records = Medline.parse(handle)


keywords = []
for record in records:
    # print(record.keys())
    # for keys in record.keys():
        # print(keys+" : "+record[keys])
    # print("YEAR: "+record["DP"])
    # print("AUTHORS: "+", ".join(record["AU"]))
    print("TITLE: "+record["TI"])
    # if record.get("AB", "NA") != "NA": # Test if there is an abstract recorded
        # print("ABSTRACT: "+record["AB"])

    if record.get("OT", "NA") != "NA": # Test if there are actually keywords recorded
        # print("KEYWORDS: "+", ".join(record["OT"]))
        for key in record["OT"]:
            keywords.append(key)

    print("\n")
    
print(keywords)
