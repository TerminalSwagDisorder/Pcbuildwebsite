from pypartpicker import Scraper
from time import sleep as sleep
import json
import os



fPath = os.path.abspath(os.path.realpath(__file__))
dPath = os.path.dirname(fPath)
finPath = dPath + "\\json"

if not os.path.exists(finPath):
    os.makedirs(finPath)

pcpartpicker = Scraper()
print("starting extraction")


searchTerms = ["processor"]

for partcategory in searchTerms:
    print("starting ", partcategory)
    parts = pcpartpicker.part_search(partcategory, region="fi")
    
    for part in parts:
        print("debug 1")
        #if float(part.price.strip("€")) >= 1:
        if not part.price is None:        
            validpart = pcpartpicker.fetch_product(part.url)
            print("debug 2")
            sleep(3)
            partdict = {
                "Name" : part.name,
                "Specs" : validpart.specs, 
            }
            print(partdict)
            
            #with open(finPath + "\\" + partcategory + ".json", "r", encoding='utf-8') as rf:
            #    data = json.load(rf)
            #data.append(partdict)
            with open(finPath + "\\" + partcategory + ".json", "w", encoding='utf-8') as wf:
                json.dump(partdict, wf)
                
            #partdict.popitem()
        sleep(1)
                
'''
            #second method to append data to json file
            
            with open(finPath + "\\" + partcategory + ".json", "r+", encoding='utf-8') as wf:
                data = json.load(wf)
                data.append(partdict)
                file.seek(0)
                json.dump(data, wf)
'''
print("completed")
    