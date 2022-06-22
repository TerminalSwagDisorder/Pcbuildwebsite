from pypartpicker import Scraper
from time import sleep as sleep
import json
import os
import sqlite3
import itertools
import pickle
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

engine = create_engine("sqlite:///" + finPath + "\\pcbuildwebsite_db_nameandprice.db", echo=True, pool_pre_ping=True)
Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session(bind=engine)

#Define metadata information
metadata = MetaData(bind=engine)

def transform(key,value):
    #remove characters at the beginning
    if key == "Price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))

#Table       
cpu = Table("cpu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("Name", TEXT),
	Column("Price", INTEGER)
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
            
            print(partname, partprice)
            
            i = insert(cpu)
            i = i.values(partname)
            i = i.values(partprice)            
            session.execute(i)
            session.commit()            

        sleep(0.5)
        
print("completed")        
        