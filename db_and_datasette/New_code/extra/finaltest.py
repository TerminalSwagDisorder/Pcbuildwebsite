from pypartpicker import Scraper
from time import sleep as sleep
import json
import os
import pickle


fPath = os.path.abspath(os.path.realpath(__file__))
dPath = os.path.dirname(fPath)
finPath = dPath + "\\json"

if not os.path.exists(finPath):
    os.makedirs(finPath)

pcpartpicker = Scraper()
print("starting extraction")


searchTerms = ["processor i9"]

for partcategory in searchTerms:
    print("starting ", partcategory)
    parts = pcpartpicker.part_search(partcategory, limit=1, region="fi")
    
    for part in parts:
        print("debug 1")
        #if float(part.price.strip("€")) >= 1:
        if not part.price is None:        
            validpart = pcpartpicker.fetch_product(part.url)
            print("debug 2")
            sleep(1)
            partdict = {
                "Name" : part.name,
                "Specs" : validpart.specs, 
            }
                        
            vs = [{new_k : new_val[r] for new_k, new_val in validpart.specs.items()} for r in range(1)]
            #vstodict = {key: [i[key] for i in vs] for key in vs[0]}
            vsp = pickle.dumps(vs)
            print(vsp)
            print(".")
            print(pickle.dumps(validpart.specs))

            #with open(finPath + "\\" + partcategory + ".json", "r", encoding='utf-8') as rf:
            #    data = json.load(rf)
            #data.append(partdict)
            with open(finPath + "\\" + partcategory + ".json", "w", encoding='utf-8') as wf:
                json.dump(vs, wf)
                
            #partdict.popitem()

                
'''
            #second method to append data to json file
            
            with open(finPath + "\\" + partcategory + ".json", "r+", encoding='utf-8') as wf:
                data = json.load(wf)
                data.append(partdict)
                file.seek(0)
                json.dump(data, wf)
'''
print("completed")
    
