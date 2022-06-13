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

print("Extracting data")

# extraction

pcpartpicker.set_region("de")
print("\nRegion changed to De")



def transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value


print("Total fan pages:", pcpartpicker.lists.total_pages("case-fan"))

# define metadata information
metadata = MetaData(bind=engine)

# table

fan = Table('fan', metadata,
    Column('name', TEXT),
    Column('color', TEXT),
    Column('size', TEXT),
    Column('rpm', TEXT),
    Column('airflow', TEXT),
    Column('noise-level', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

a = 0
tot_fan = pcpartpicker.lists.total_pages("case-fan")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_fan:
    print("\nPage #",a+1,"\n")
    a += 1
    
    fan_info = pcpartpicker.lists.get_list("case-fan", a)
    fan_info = [{
        key:transform(key,value) for key,value in fan.items()} for fan in fan_info]
    # insert
    i = insert(fan)
    i = i.values(fan_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = fan.delete().where(fan.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")


