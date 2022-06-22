from pypartpicker import Scraper
import json
import os

fPath = os.path.abspath(os.path.realpath(__file__))
dPath = os.path.dirname(fPath)
path = dPath + "\\json"

if not os.path.exists(path):
    os.makedirs(path)

searchTerms = ["processsor", "video card", "cpu cooler", "motherboard", "memory", "internal hard drive", "solid state drive", "power supply", "case"]

pcpartpicker = Scraper()

for x in searchTerms:
    parts = pcpartpicker.part_search(searchTerms, region="fi")
    for part in parts:
        if float(part.price.strip("€")) > 0:
            validpart = pcpartpicker.fetch_product(part.url)
            #print(part.type, part.name, part.price)
            sleep(3)
            partdict = {
                part.name : validpart.specs
            }
            with open(path + "\\" + searchTerms + ".json", "w", encoding='utf-8') as wf:
                json.dump(partdict, wf)
        sleep(3)
        #product = pcpartpicker.fetch_product(parts[0:].url)
        #print(product.specs)

    