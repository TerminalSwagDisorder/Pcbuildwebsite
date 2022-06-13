import sqlite3
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:////home/benjaminlinux/github/pcbuildapp/pcbuildapp/pcbuildapp_new_db.db', echo=True, pool_pre_ping=True)
from pcpartpickerapi import part_lists


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



print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

wireless_network = Table("wireless_network", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("protocol", TEXT),
	Column("interface", TEXT),
	Column("color", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total wireless_network pages:", part_lists.list_page_count("wireless-network-card", region="de"))

a = 0
tot_wireless_network = part_lists.list_page_count("wireless-network-card", region="de")

print("\nExtracting and updating data")

# extraction
    
wireless_network_info =  part_lists.get_list("wireless-network-card", page=0, region="de")
wireless_network_info = [{key:transform(key,value) for key,value in wireless_network.items()} for wireless_network in wireless_network_info]

        #insert in chunks
page_length = len(part_lists.get_list("wireless-network-card", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(wireless_network)
    i = i.values(wireless_network_info[cursor:cursor+chunk_size])
    session.add_all
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = wireless_network.delete().where(wireless_network.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")

