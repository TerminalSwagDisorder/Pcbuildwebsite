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

#Primary part categories are "processsor", "video card", "cpu cooler", "motherboard", "memory", "internal hard drive", "solid state drive", "power supply", "case"
searchTerms = ["video card gtx", "video card rtx", "video card radeon", "cpu cooler", "motherboard", "memory ddr4", "memory ddr5", "memory ddr3", "internal hard drive", "solid state drive 2.5", "solid state drive m.2", "power supply", "atx case", "itx case", "htpc case"]

for partcategory in searchTerms:
    print("starting ", partcategory)
    parts = pcpartpicker.part_search(partcategory, limit=10, region="fi")
    
    for part in parts:
        print("debug 1")
        #if float(part.price.strip("€")) >= 1:
        if not part.price is None:        
            validpart = pcpartpicker.fetch_product(part.url)
            print("debug 2")
            sleep(2)
            partdict = {
                "Name" : part.name,
                "Specs" : validpart.specs, 
            }
                        
            #thisdict = dict.fromkeys(validpart.specs)
            #td2 = dict.items(validpart.specs)
            
            #for key in validpart.specs.keys():
            #   print(key, ":", validpart.specs[key])
            vs = [{new_k : new_val[r] for new_k, new_val in validpart.specs.items()} for r in range(1)]

            specsdict = {
                
            }
            
            for key, value in vs[0].items():
                specsdict[key] = value
            '''
            for value in vs[0].values():
                print(value)
            
            for key in vs[0].keys():
                print(key)
            '''
            print(specsdict)
            print(type(specsdict))
            
            #vstodict = {key: [i[key] for i in vs] for key in vs[0]}
            #vsp = pickle.dumps(vs)
            #print(vsp)
            #print(".")
            #vsp2 = pickle.dumps(validpart.specs)
            #print(vsp2)

            #with open(finPath + "\\" + partcategory + ".json", "r", encoding='utf-8') as rf:
            #    data = json.load(rf)
            #data.append(partdict)
            with open(finPath + "\\" + partcategory + ".json", "w", encoding='utf-8') as wf:
                json.dump(validpart.specs, wf)
            #with open(finPath + "\\" + partcategory + "_2.json", "w", encoding='utf-8') as wf:
            #    json.dump(vs, wf)
            #with open(finPath + "\\" + partcategory + "_pretty.json", "w", encoding='utf-8') as wf:
            #    json.dump(validpart.specs, wf, indent=4)
            #with open(finPath + "\\" + partcategory + "_2pretty.json", "w", encoding='utf-8') as wf:
            #    json.dump(vs, wf, indent=4)
            #with open(finPath + "\\" + partcategory + "_final.json", "w", encoding='utf-8') as wf:
            #    json.dump(specsdict, wf)
            with open(finPath + "\\" + partcategory + "_finalpretty.json", "w", encoding='utf-8') as wf:
                json.dump(specsdict, wf, indent=4)
                
            #with open(finPath + "\\" + partcategory + "_test.json", "w", encoding='utf-8') as wf:
            #    json.dump(thisdict, wf)
            #print(thisdict)
                
            #partdict.popitem()

                
            sleep(0.5)

print("completed")
    
