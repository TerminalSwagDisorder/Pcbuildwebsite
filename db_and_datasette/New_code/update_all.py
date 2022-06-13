import sqlite3
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:////home/benjaminlinux/github/pcbuildapp/pcbuildapp/pcbuildapp_new_db.db', echo=True, pool_pre_ping=True)
from PCPartPicker_API import pcpartpicker as part_lists
#from PCPartPicker_API import part_lists


Session = sessionmaker(bind=engine)
Session.configure(bind=engine)
session = Session(bind=engine)



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

part_lists.setRegion("de")
print("\nRegion changed to De")
'''
for i in cpu_info:
    print(i)
'''


print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

cpu = Table("cpu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("core-count", TEXT),
	Column("core-clock", TEXT),
	Column("boost-clock", TEXT),
	Column("tdp", INTEGER),
	Column("integrated-graphics", TEXT),
	Column("simultaneous-multithreading", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)


print("Total CPU pages:", part_lists.productLists.totalPages("cpu"))

a = 0
tot_cpu = part_lists.productLists.totalPages("cpu")

print("\nExtracting and updating data")

# extraction
#print("Page #",a)
#while a < tot_cpu:
#    print("\nPage #",a+1,"\n")
#    a += 1
    
cpu_info =  part_lists.getProductList("cpu", page=0)
cpu_info = [{key:transform(key,value) for key,value in cpu.items()} for cpu in cpu_info]

        #insert in chunks
page_length = len(part_lists.getProductList("cpu", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(cpu)
    i = i.values(cpu_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = cpu.delete().where(cpu.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")

print("Inserting data into database")


