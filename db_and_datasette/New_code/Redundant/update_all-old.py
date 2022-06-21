import sqlite3
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:////home/benjaminlinux/github/pcbuildapp/pcbuildapp/pcbuildapp_new_db.db', echo=True, pool_pre_ping=True)
from PCPartPicker_API import pcpartpickerapi
from PCPartPicker_API import part_lists


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

'''
cpu = Table('cpu', metadata,
    Column('name', TEXT),
    Column('core-clock', TEXT),
    Column('boost-clock', TEXT),
    Column('core-count', TEXT),
    Column('tdp', Integer),
    Column('ratings-count', TEXT),
    Column('price', Integer),
	Column("integrated-graphics", TEXT),
	Column("simultaneous-multithreading", TEXT),
    Column('id', TEXT, primary_key=True)
)
'''

print("Total CPU pages:", part_lists.list_page_count("cpu", region="de"))

a = 0
tot_cpu = part_lists.list_page_count("cpu", region="de")

print("\nExtracting and updating data")

# extraction
#print("Page #",a)
#while a < tot_cpu:
#    print("\nPage #",a+1,"\n")
#    a += 1
    
cpu_info =  part_lists.get_list("cpu", page=0, region="de")
cpu_info = [{key:transform(key,value) for key,value in cpu.items()} for cpu in cpu_info]

        #insert in chunks
page_length = len(part_lists.get_list("cpu", a))
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

# define metadata information
metadata = MetaData(bind=engine)

# table

case = Table("case", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("type", TEXT),
	Column("color", TEXT),
	Column("power-supply", TEXT),
	Column("side-panel-window", INTEGER),
	Column("ext-5.25-bays", TEXT),
	Column("int-3.5-bays", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total case pages:", part_lists.list_page_count("case", region="de"))

a = 0
tot_case = part_lists.list_page_count("case", region="de")

print("\nExtracting and updating data")

# extraction

    
case_info =  part_lists.get_list("case", page=0, region="de")
case_info = [{key:transform(key,value) for key,value in case.items()} for case in case_info]

        #insert in chunks
page_length = len(part_lists.get_list("case", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
    # insert
    i = insert(case)
    i = i.values(case_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = case.delete().where(case.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")


print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

cpu_cooler = Table("cpu_cooler", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("fan-rpm", TEXT),
	Column("noise-level", TEXT),
	Column("color", TEXT),
	Column("radiator-size", INTEGER),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total cpu_cooler pages:", part_lists.list_page_count("cpu-cooler", region="de"))

a = 0
tot_cpu_cooler = part_lists.list_page_count("cpu-cooler", region="de")

print("\nExtracting and updating data")

# extraction
    
cpu_cooler_info =  part_lists.get_list("cpu-cooler", page=0, region="de")
cpu_cooler_info = [{key:transform(key,value) for key,value in cpu_cooler.items()} for cpu_cooler in cpu_cooler_info]

        #insert in chunks
page_length = len(part_lists.get_list("cpu-cooler", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(cpu_cooler)
    i = i.values(cpu_cooler_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = cpu_cooler.delete().where(cpu_cooler.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")


print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

storage = Table("storage", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("capacity", TEXT),
	Column("price/gb", INTEGER),
	Column("type", TEXT),
	Column("cache", INTEGER),
	Column("form-factor", TEXT),
	Column("interface", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total storage pages:", part_lists.list_page_count("internal-hard-drive", region="de"))

a = 0
tot_storage = part_lists.list_page_count("internal-hard-drive", region="de")

print("\nExtracting and updating data")

# extraction
    
storage_info =  part_lists.get_list("internal-hard-drive", page=0, region="de")
storage_info = [{key:transform(key,value) for key,value in storage.items()} for storage in storage_info]

        #insert in chunks
page_length = len(part_lists.get_list("internal-hard-drive", a))
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
print("\nInsertion done")

print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

memory = Table("memory", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("speed", TEXT),
	Column("type", TEXT),
	Column("modules", TEXT),
	Column("price/gb", INTEGER),
	Column("color", TEXT),
	Column("cas-latency", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total memory pages:", part_lists.list_page_count("memory", region="de"))

a = 0
tot_memory = part_lists.list_page_count("memory", region="de")

print("\nExtracting and updating data")

# extraction
    
memory_info =  part_lists.get_list("memory", page=0, region="de")
memory_info = [{key:transform(key,value) for key,value in memory.items()} for memory in memory_info]

        #insert in chunks
page_length = len(part_lists.get_list("memory", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(memory)
    i = i.values(memory_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = memory.delete().where(memory.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")


print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

motherboard = Table("motherboard", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("socket", TEXT),
	Column("form-factor", TEXT),
	Column("ram-slots", TEXT),
	Column("max-ram", INTEGER),
	Column("color", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total motherboard pages:", part_lists.list_page_count("motherboard", region="de"))

a = 0
tot_motherboard = part_lists.list_page_count("motherboard", region="de")

print("\nExtracting and updating data")

# extraction


motherboard_info =  part_lists.get_list("motherboard", page=0, region="de")
motherboard_info = [{ key:transform(key,value) for key,value in motherboard.items()} for motherboard in motherboard_info]

        #insert in chunks
page_length = len(part_lists.get_list("motherboard", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(motherboard)
    i = i.values(motherboard_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = motherboard.delete().where(motherboard.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")


print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

psu = Table("psu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("form-factor", TEXT),
	Column("efficiency-rating", TEXT),
	Column("wattage", TEXT),
	Column("modular", INTEGER),
	Column("color", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total psu pages:", part_lists.list_page_count("power-supply", region="de"))

a = 0
tot_psu = part_lists.list_page_count("power-supply", region="de")

print("\nExtracting and updating data")

# extraction
    
psu_info =  part_lists.get_list("power-supply", page=0, region="de")
psu_info = [{key:transform(key,value) for key,value in psu.items()} for psu in psu_info]

        #insert in chunks
page_length = len(part_lists.get_list("power-supply", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(psu)
    i = i.values(psu_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = psu.delete().where(psu.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")

print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

gpu = Table("gpu", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("chipset", TEXT),
	Column("memory", TEXT),
	Column("core-clock", TEXT),
	Column("boost-clock", INTEGER),
	Column("interface", TEXT),
	Column("color", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total gpu pages:", part_lists.list_page_count("video-card", region="de"))

a = 0
tot_gpu = part_lists.list_page_count("video-card", region="de")

print("\nExtracting and updating data")

# extraction
    
gpu_info =  part_lists.get_list("video-card", page=0, region="de")
gpu_info = [{key:transform(key,value) for key,value in gpu.items()} for gpu in gpu_info]

        #insert in chunks
page_length = len(part_lists.get_list("video-card", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
    # insert
    i = insert(gpu)
    i = i.values(gpu_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = gpu.delete().where(gpu.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")


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
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = wireless_network.delete().where(wireless_network.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")


print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

wired_network = Table("wired_network", metadata,
	Column("id", INTEGER, primary_key=True, autoincrement=True),
	Column("name", TEXT),
	Column("interface", TEXT),
	Column("ports", TEXT),
	Column("color", TEXT),
	Column("ratings-count", TEXT),
	Column("price", INTEGER)
)

print("Total wired_network pages:", part_lists.list_page_count("wired-network-card", region="de"))

a = 0
tot_wired_network = part_lists.list_page_count("wired-network-card", region="de")

print("\nExtracting and updating data")

# extraction
    
wired_network_info =  part_lists.get_list("wired-network-card", page=0, region="de")
wired_network_info = [{key:transform(key,value) for key,value in wired_network.items()} for wired_network in wired_network_info]

        #insert in chunks
page_length = len(part_lists.get_list("wired-network-card", a))
cursor = 0
chunk_size = 50
while cursor < page_length:
        # insert
    i = insert(wired_network)
    i = i.values(wired_network_info[cursor:cursor+chunk_size])
    session.execute(i)
    session.commit()
    cursor+=chunk_size

    # delete
    dlt = wired_network.delete().where(wired_network.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nInsertion done")
