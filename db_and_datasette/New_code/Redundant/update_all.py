from pypartpicker import Scraper
from time import sleep as sleep
import json
import os
import sqlite3
import itertools
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
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
	Column("Price", TEXT)
)

pcpartpicker = Scraper()
print("starting extraction")

#Add anything you want to find from https://fi.pcpartpicker.com/search/
#Primary part categories are "processsor", "video card", "cpu cooler", "motherboard", "memory", "internal hard drive", "solid state drive", "power supply", "case"
searchTerms = ["processor"]

#Extract data and insert to database
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
            partname = {
                "Name" : part.name,
            }
            partdict = {
                "Name" : part.name,                
                "Specs" : validpart.specs,
                "Price" : part.price,                
            }
            partprice = {
                "Price" : part.price,
            }            
            print(partdict)
            #Crude way to delete redundant dict columns
            validpart.specs.pop("Manufacturer")            
            validpart.specs.pop("Part #")
            validpart.specs.pop("Series")
            validpart.specs.pop("Microarchitecture")
            validpart.specs.pop("Core Family")
            validpart.specs.pop("Maximum Supported Memory")
            validpart.specs.pop("ECC Support")
            validpart.specs.pop("Packaging")
            validpart.specs.pop("Performance L1 Cache")
            validpart.specs.pop("Performance L2 Cache")
            #validpart.specs.pop("Efficiency L1 Cache")
            #validpart.specs.pop("Efficiency L2 Cache")            
            validpart.specs.pop("Lithography")            

            partsfin = dict(itertools.zip_longest(*[iter(validpart.specs)] * 2, fillvalue=""))

            print(partsfin)
            
            #with open(finPath + "\\" + partcategory + ".json", "r", encoding='utf-8') as rf:
            #    data = json.load(rf)
            #data.append(partdict)                              
            i = insert(cpu)
            i = i.values(partname)
            i = i.values(partsfin)
            i = i.values(partprice)            
            session.execute(i)
            session.commit()            
                
            #partdict.popitem()
        sleep(1)
        
print("completed")        
        
        
        
        
        
        
        
                
'''
            #second method to append data to json file
            
            with open(finPath + "\\" + partcategory + ".json", "r+", encoding='utf-8') as wf:
                data = json.load(wf)
                data.append(partdict)
                file.seek(0)
                json.dump(data, wf)
'''

    

'''
import sqlite3
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:///pcbuildwebsite_db.db', echo=True, pool_pre_ping=True)



Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session(bind=engine)

'''
'''
def transform(key,value):
    #remove characters at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    elif key == "price/gb":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    elif key == "socket":
        value = value[3:]
        return str(value)
    #remove characters at the end
    elif key == "tdp":
        value = value[:-2]
        return int(value)
    elif key == "wattage":
        value = value[:-2]
        return int(value)
    else:
        return value
'''
'''

print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

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
	Column("price", TEXT))


print("\nExtracting and updating data")
    
i = insert(cpu)
i = i.values(cpu_info[cursor:cursor+chunk_size])
session.execute(i)
session.commit()
cursor+=chunk_size

print("\nInsertion done")

print("Inserting data into database")
'''

