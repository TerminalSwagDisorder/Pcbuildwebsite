from pypartpicker import Scraper
from time import sleep as sleep
import os
import sqlite3
import itertools
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete, text
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine



fPath = os.path.abspath(os.path.realpath(__file__))
dPath = os.path.dirname(fPath)
finPath = dPath + "\\database"

#Create database folder if it does not exist
if not os.path.exists(finPath):
    os.makedirs(finPath)

engine = create_engine("sqlite:///" + finPath + "\\pcbuildwebsite_db.db", echo=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session(bind=engine)

#Define metadata information
metadata = MetaData(bind=engine)

#Create table in database       
cpu = Table("cpu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Core Count", TEXT),
	Column("Performance Core Clock", TEXT),
	Column("Performance Boost Clock", TEXT),
	Column("TDP", TEXT),
	Column("Integrated Graphics", TEXT),
	Column("L3 Cache", TEXT),
    Column("Simultaneous Multithreading", TEXT),
	Column("Includes CPU Cooler", TEXT),
	Column("Socket", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
gpu = Table("gpu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Chipset", TEXT),
	Column("Memory", TEXT),
	Column("Memory Type", TEXT),
	Column("Core Clock", TEXT),
	Column("Boost Clock", TEXT),
    Column("Effective Memory Clock", TEXT),
	Column("Interface", TEXT),
	Column("Color", TEXT),
	Column("Length", TEXT),
	Column("TDP", TEXT),
	Column("Expansion Slot Width", TEXT),
	Column("Cooling", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
cooler = Table("cpu cooler", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Fan RPM", TEXT),
	Column("Noise Level", TEXT),
	Column("Color", TEXT),
	Column("Height", TEXT),
    Column("Water Cooled", TEXT),
	Column("Fanless", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
motherboard = Table("motherboard", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Socket / CPU", TEXT),
	Column("Form Factor", TEXT),
	Column("Chipset", TEXT),
	Column("Memory Max", TEXT),
	Column("Memory Type", TEXT),
    Column("Memory Slots", TEXT),
	Column("Color", TEXT),
	Column("PCIe x16 Slots", TEXT),
	Column("PCIe x8 Slots", TEXT),
	Column("PCIe x4 Slots", TEXT),
	Column("PCIe x1 Slots", TEXT),
	Column("M.2 Slots", TEXT),
	Column("SATA 6.0 Gb/s", TEXT),
	Column("Onboard Ethernet", TEXT),
	Column("USB 2.0 Headers", TEXT),
	Column("USB 3.2 Gen 1 Headers", TEXT),
	Column("USB 3.2 Gen 2 Headers", TEXT),
	Column("USB 3.2 Gen 2x2 Headers", TEXT),
	Column("Wireless Networking", TEXT),
	Column("RAID Support", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
memory = Table("memory", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Form Factor", TEXT),
	Column("Modules", TEXT),
	Column("Color", TEXT),
	Column("CAS Latency", TEXT),
	Column("Voltage", TEXT),
    Column("ECC / Registered", TEXT),
	Column("Heat Spreader", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
storage = Table("storage", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Capacity", TEXT),
	Column("Type", TEXT),
	Column("Cache", TEXT),
	Column("Form Factor", TEXT),
	Column("Interface", TEXT),
	Column("NVME", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
psu = Table("psu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Form Factor", TEXT),
	Column("Efficiency Rating", TEXT),
	Column("Wattage", TEXT),
	Column("Length", TEXT),
    Column("Modular", TEXT),
	Column("Color", TEXT),
	Column("Type", TEXT),
	Column("Fanless", TEXT),
	Column("ATX Connectors", TEXT),
	Column("EPS Connectors", TEXT),
	Column("PCIe 12-Pin Connectors", TEXT),
	Column("PCIe 8-Pin Connectors", TEXT),
	Column("PCIe 6+2-Pin Connectors", TEXT),
	Column("PCIe 6-Pin Connectors", TEXT),
	Column("SATA Connectors", TEXT),
	Column("Molex 4-Pin Connectors", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
case = Table("case", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Manufacturer", TEXT),
	Column("Type", TEXT),
	Column("Color", TEXT),
	Column("Power Supply", TEXT),
	Column("Side Panel Window", TEXT),
    Column("Power Supply Shroud", TEXT),
	Column("Motherboard Form Factor", TEXT),
	Column("Maximum Video Card Length", TEXT),
	Column("Volume", TEXT),
	Column("Dimensions", TEXT),
	Column("Price", TEXT),
	Column("Url", TEXT)
)
metadata.create_all(engine)

pcpartpicker = Scraper()
print("starting extraction\n")

#Add anything you want to find from https://fi.pcpartpicker.com/search/
#Primary part categories are "processsor", "video card", "cpu cooler", "motherboard", "memory", "internal hard drive", "solid state drive", "power supply", "case"
searchTerms = ["video card gtx", "video card rtx", "video card radeon", "processor amd ryzen", "processor intel celeron", "processor intel pentium", "processor intel core i3", "processor intel core i5", "processor intel core i7", "processor intel core i9", "cpu cooler", "motherboard", "memory ddr4", "memory ddr5", "memory ddr3", "internal hard drive",  "solid state drive 2.5", "solid state drive m.2", "power supply certified", "atx case", "itx case", "htpc case"]

#Extract data and insert to database
for partcategory in searchTerms:
    print("\nstarting", partcategory)
    #A limit of 500 or below is ideal to try to not be rate limited by PCPP
    parts = pcpartpicker.part_search(partcategory, limit=500, region="fi")
    
    for part in parts:
        print("debug 1")
        #if float(part.price.strip("€")) >= 1:
        if not part.price is None:
            validpart = pcpartpicker.fetch_product(part.url)

            print("debug 2")
            #Need to wait a bit to also not be rate limited by PCPP
            #sleep(1)
            sleep(3)
            
            partname = {
                "Name" : part.name,
            }
            partprice = {
                "Price" : part.price,
            }
            parturl = {
                "Url" : part.url,
            }
            
            #Convert specs into only dict
            vs = [{new_k : new_val[r] for new_k, new_val in validpart.specs.items()} for r in range(1)]
            specsdict = {
                
            }
            
            for key, value in vs[0].items():
                specsdict[key] = value
            
            #Delete unecessary dict columns    
            delcol = ["Efficiency L1 Cache", "Efficiency L2 Cache", "Part #", "Series", "Microarchitecture", "Core Family", "Maximum Supported Memory", "ECC Support", "Packaging", "Performance L1 Cache", "Performance L2 Cache", "Lithography", "Frame Sync", "External Power", "HDMI Outputs", "DVI-D Dual Link Outputs", "DisplayPort Outputs", "CPU Socket", "Memory Speed", "PCI Slots", "Mini-PCIe Slots", "Half Mini-PCIe Slots", "Mini-PCIe / mSATA Slots", "mSATA Slots", "USB 2.0 Headers (Single Port)", "Supports ECC", "Price / GB", "First Word Latency", "Timing", "Model", "Front Panel USB", "Drive Bays", "Expansion Slots", "SLI/CrossFire", "Onboard Video", "Output", "HDMI 2.0b Outputs", "DisplayPort 1.4 Outputs", "DisplayPort 1.4a Outputs", "HDMI 2.1 Outputs", "VirtualLink Outputs", "Bearing", "SSD NAND Flash Type", "Power Loss Protection", "SSD Controller", "Efficiency", "Includes Cooler"]
                        
            for column in delcol:
                try:
                    specsdict.pop(column)
                except:
                    continue
                    
            print("\npartcategory =", partcategory)
            print(partname, specsdict, partprice, "\n")
            
            #Insert into database
            if partcategory == "processor amd ryzen" :
                i = insert(cpu)
                
            elif partcategory == "processor intel celeron":
                i = insert(cpu) 
                
            elif partcategory == "processor intel pentium":
                i = insert(cpu)
                
            elif partcategory == "processor intel core i3":
                i = insert(cpu)
                
            elif partcategory == "processor intel core i5":
                i = insert(cpu)
                
            elif partcategory == "processor intel core i7":
                i = insert(cpu)
                
            elif partcategory == "processor intel core i9":
                i = insert(cpu)
                
            elif partcategory == "video card gtx":
                i = insert(gpu)
                
            elif partcategory == "video card rtx":
                i = insert(gpu)
                
            elif partcategory == "video card radeon":
                i = insert(gpu)
                
            elif partcategory == "cpu cooler":
                i = insert(cooler)    

            elif partcategory == "motherboard":
                i = insert(motherboard)   

            elif partcategory == "memory ddr4":
                i = insert(memory) 
                
            elif partcategory == "memory ddr5":
                i = insert(memory) 
                
            elif partcategory == "memory ddr3":
                i = insert(memory) 

            elif partcategory == "internal hard drive":
                i = insert(storage)
                
            elif partcategory == "solid state drive 2.5":
                i = insert(storage)
                
            elif partcategory == "solid state drive m.2":
                i = insert(storage)
                
            elif partcategory == "power supply certified":
                i = insert(psu)
                
            elif partcategory == "atx case":
                i = insert(case)
                
            elif partcategory == "itx case":
                i = insert(case)
                
            elif partcategory == "htpc case":
                i = insert(case)
                
            i = i.values(partname)
            i = i.values(specsdict) 
            i = i.values(partprice)  
            i = i.values(parturl)
            session.execute(i)
            session.commit()     
            
        #Wait here again just in case
        #sleep(4)
        sleep(8)
        
print("\n\nCompleted")