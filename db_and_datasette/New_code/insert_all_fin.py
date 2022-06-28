from pypartpicker import Scraper
from time import sleep as sleep
import json
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

#Create json folder if it does not exist
if not os.path.exists(finPath):
    os.makedirs(finPath)

engine = create_engine("sqlite:///" + finPath + "\\pcbuildwebsite_db.db", echo=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session(bind=engine)

#Define metadata information
metadata = MetaData(bind=engine)

#Table       
cpu = Table("cpu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
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

pcpartpicker = Scraper()
print("starting extraction")

#Add anything you want to find from https://fi.pcpartpicker.com/search/
#Primary part categories are "processsor", "video card", "cpu cooler", "motherboard", "memory", "internal hard drive", "solid state drive", "power supply", "case"
searchTerms = ["processor i9"]

#Extract data and insert to database
for partcategory in searchTerms:
    print("starting ", partcategory)
    parts = pcpartpicker.part_search(partcategory, limit=5, region="fi")
    
    for part in parts:
        print("debug 1")
        #if float(part.price.strip("€")) >= 1:
        if not part.price is None:
            validpart = pcpartpicker.fetch_product(part.url)

            print("debug 2")
            sleep(2)
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
                
            #Crude way to delete unnecessary dict columns
            try:
                specsdict.pop("Efficiency L1 Cache")
                specsdict.pop("Efficiency L2 Cache")
                specsdict.pop("Manufacturer")            
                specsdict.pop("Part #")
                specsdict.pop("Series")
                specsdict.pop("Microarchitecture")
                specsdict.pop("Core Family")
                specsdict.pop("Maximum Supported Memory")
                specsdict.pop("ECC Support")
                specsdict.pop("Packaging")
                specsdict.pop("Performance L1 Cache")
                specsdict.pop("Performance L2 Cache")
                specsdict.pop("Lithography")
            except:    
                specsdict.pop("Manufacturer")            
                specsdict.pop("Part #")
                specsdict.pop("Series")
                specsdict.pop("Microarchitecture")
                specsdict.pop("Core Family")
                specsdict.pop("Maximum Supported Memory")
                specsdict.pop("ECC Support")
                specsdict.pop("Packaging")
                specsdict.pop("Performance L1 Cache")
                specsdict.pop("Performance L2 Cache")
                specsdict.pop("Lithography")
            
            print(partname, partprice)
            
            i = insert(cpu)
            i = i.values(partname)
            i = i.values(specsdict) 
            i = i.values(partprice)  
            i = i.values(parturl)
            session.execute(i)
            session.commit()            

        sleep(0.5)
        
print("completed")        
        
