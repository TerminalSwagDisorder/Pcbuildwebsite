import sqlite3
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:///E:\\Skola\\pcbuildapp\\pcbuildapp.db',echo=True)
from PCPartPicker_API import pcpartpicker

Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session(bind=engine)

def transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value


print("Extracting data")

# extraction

pcpartpicker.set_region("de")
print("\nRegion changed to De")


print("Total storage pages:", pcpartpicker.lists.total_pages("internal-hard-drive"))


# define metadata information
metadata = MetaData(bind=engine)

# table

storage = Table('storage', metadata,
    Column('name', TEXT),
    Column('series', TEXT),
    Column('form', TEXT),
    Column('type', TEXT),
    Column('capacity', TEXT),
    Column('cache', TEXT),
    Column('price/gb', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

a = 0
tot_storage = pcpartpicker.lists.total_pages("internal-hard-drive")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_storage:
    print("\nPage #",a+1,"\n")
    a += 1
    
    storage_info = pcpartpicker.lists.get_list("internal-hard-drive", a)
    storage_info = [{
        key:transform(key,value) for key,value in storage.items()} for storage in storage_info]

        #insert in chunks
    page_length = len(storage_info)
    cursor = 0
    chunk_size = 50
    while cursor < page_length:
        # insert
        i = insert(storage)
        i = i.values(storage_info[cursor:cursor+chunk_size])
        session.execute(i)
        session.commit()
        cursor+=chunk_size

    # delete
    dlt = storage.delete().where(storage.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")


