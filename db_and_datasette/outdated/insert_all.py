import sqlite3
import json
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql.expression import ColumnClause
from sqlalchemy.sql import table, column, select, update, insert, delete
from sqlalchemy.ext.declarative import *
from sqlalchemy import create_engine
engine = create_engine('sqlite:////home/benjaminlinux/github/pcbuildapp/pcbuildapp/pcb.db', echo=True, pool_pre_ping=True)
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
    #remove one character at the end
    elif key == "tdp":
        value = value[:-1]
        return int(value)
    else:
        return value



'''
for i in cpu_info:
    print(i)
'''

print("Extraction done")

print("Inserting data into database")

# define metadata information
metadata = MetaData(bind=engine)

# table

cpu = Table('cpu', metadata,
    Column('name', TEXT),
    Column('speed', TEXT),
    Column('cores', TEXT),
    Column('tdp', Integer),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))

a = 0
tot_cpu = pcpartpicker.lists.total_pages("cpu")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_cpu:
    print("\nPage #",a+1,"\n")
    a += 1
    
    cpu_info = pcpartpicker.lists.get_list("cpu", a)
    cpu_info = [{
        key:transform(key,value) for key,value in cpu.items()} for cpu in cpu_info]
    # insert
    i = insert(cpu)
    i = i.values(cpu_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = cpu.delete().where(cpu.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")






print("Total CPU-cooler pages:", pcpartpicker.lists.total_pages("cpu-cooler"))


# define metadata information
metadata = MetaData(bind=engine)

# table

cpu_cooler = Table('cpu-cooler', metadata,
    Column('name', TEXT),
    Column('fan-rpm', TEXT),
    Column('noise level', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

a = 0
tot_cpu_cooler = pcpartpicker.lists.total_pages("cpu-cooler")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_cpu_cooler:
    print("\nPage #",a+1,"\n")
    a += 1
    
    cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler", a)
    cpu_cooler_info = [{
        key:transform(key,value) for key,value in cpu_cooler.items()} for cpu_cooler in cpu_cooler_info]
    # insert
    i = insert(cpu_cooler)
    i = i.values(cpu_cooler_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = cpu_cooler.delete().where(cpu_cooler.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")






print("Total motherboard pages:", pcpartpicker.lists.total_pages("motherboard"))





# define metadata information
metadata = MetaData(bind=engine)

# table

motherboard = Table('motherboard', metadata,
    Column('name', TEXT),
    Column('socket', TEXT),
    Column('form-factor', TEXT),
    Column('ram-slots', TEXT),
    Column('max-ram', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)


a = 0
tot_motherboard = pcpartpicker.lists.total_pages("motherboard")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_motherboard:
    print("\nPage #",a+1,"\n")
    a += 1
    
    motherboard_info = pcpartpicker.lists.get_list("motherboard", a)
    motherboard_info = [{
        key:transform(key,value) for key,value in motherboard.items()} for motherboard in motherboard_info]
    # insert
    i = insert(motherboard)
    i = i.values(motherboard_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = motherboard.delete().where(motherboard.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")


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



print("Total memory pages:", pcpartpicker.lists.total_pages("memory"))


# define metadata information
metadata = MetaData(bind=engine)

# table

memory = Table('memory', metadata,
    Column('name', TEXT),
    Column('speed', TEXT),
    Column('type', TEXT),
    Column('cas', TEXT),
    Column('modules', TEXT),
    Column('size', TEXT),
    Column('price/gb', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

a = 0
tot_memory = pcpartpicker.lists.total_pages("memory")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_memory:
    print("\nPage #",a+1,"\n")
    a += 1
    
    memory_info = pcpartpicker.lists.get_list("memory", a)
    memory_info = [{
        key:transform(key,value) for key,value in memory.items()} for memory in memory_info]

    #insert in chunks
    page_length = len(memory_info)
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
print("\nExtraction and insertion done")


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








print("Total gpu pages:", pcpartpicker.lists.total_pages("video-card"))



# define metadata information
metadata = MetaData(bind=engine)

# table

gpu = Table('gpu', metadata,
    Column('name', TEXT),
    Column('series', TEXT),
    Column('chipset', TEXT),
    Column('memory', TEXT),
    Column('core-clock', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)


a = 0
tot_gpu = pcpartpicker.lists.total_pages("video-card")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_gpu:
    print("\nPage #",a+1,"\n")
    a += 1
    
    gpu_info = pcpartpicker.lists.get_list("video-card", a)
    gpu_info = [{
        key:transform(key,value) for key,value in gpu.items()} for gpu in gpu_info]
    # insert
    i = insert(gpu)
    i = i.values(gpu_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = gpu.delete().where(gpu.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")



print("Total psu pages:", pcpartpicker.lists.total_pages("power-supply"))



# define metadata information
metadata = MetaData(bind=engine)

# table

psu = Table('psu', metadata,
    Column('name', TEXT),
    Column('series', TEXT),
    Column('form', TEXT),
    Column('efficiency', TEXT),
    Column('watts', TEXT),
    Column('modular', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)


a = 0
tot_psu = pcpartpicker.lists.total_pages("power-supply")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_psu:
    print("\nPage #",a+1,"\n")
    a += 1
    
    psu_info = pcpartpicker.lists.get_list("power-supply", a)
    psu_info = [{
        key:transform(key,value) for key,value in psu.items()} for psu in psu_info]
    # insert
    i = insert(psu)
    i = i.values(psu_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = psu.delete().where(psu.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")






print("Total case pages:", pcpartpicker.lists.total_pages("case"))



# define metadata information
metadata = MetaData(bind=engine)

# table

case = Table('case', metadata,
    Column('name', TEXT),
    Column('type', TEXT),
    Column('ext525b', TEXT),
	Column('int35b', TEXT),
	Column('power-supply', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)


a = 0
tot_case = pcpartpicker.lists.total_pages("case")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_case:
    print("\nPage #",a+1,"\n")
    a += 1
    
    case_info = pcpartpicker.lists.get_list("case", a)
    case_info = [{
        key:transform(key,value) for key,value in case.items()} for case in case_info]
    # insert
    i = insert(case)
    i = i.values(case_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = case.delete().where(case.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")




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
while a < 11:
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





print("Total wired pages:", pcpartpicker.lists.total_pages("wired-network-card"))



# define metadata information
metadata = MetaData(bind=engine)

# table

wired = Table('wired', metadata,
    Column('name', TEXT),
    Column('interface', TEXT),
    Column('ports', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

a = 0
tot_wired = pcpartpicker.lists.total_pages("wired-network-card")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_wired:
    print("\nPage #",a+1,"\n")
    a += 1
    
    wired_info = pcpartpicker.lists.get_list("wired-network-card", a)
    wired_info = [{
        key:transform(key,value) for key,value in wired.items()} for wired in wired_info]
    # insert
    i = insert(wired)
    i = i.values(wired_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = wired.delete().where(wired.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")





print("Total wireless pages:", pcpartpicker.lists.total_pages("wireless-network-card"))


# define metadata information
metadata = MetaData(bind=engine)

# table

wireless = Table('wireless', metadata,
    Column('name', TEXT),
    Column('interface', TEXT),
    Column('protocols', TEXT),
    Column('ratings', TEXT),
    Column('price', Integer),
    Column('id', TEXT, primary_key=True),
    autoload=True
)

a = 0
tot_wireless = pcpartpicker.lists.total_pages("wireless-network-card")

print("\nExtracting and inserting data")

# extraction
print("Page #",a)
while a < tot_wireless:
    print("\nPage #",a+1,"\n")
    a += 1
    
    wireless_info = pcpartpicker.lists.get_list("wireless-network-card", a)
    wireless_info = [{
        key:transform(key,value) for key,value in wireless.items()} for wireless in wireless_info]
    # insert
    i = insert(wireless)
    i = i.values(wireless_info)
    session.execute(i)
    session.commit()

    # delete
    dlt = wireless.delete().where(wireless.c.price == '')
    session.execute(dlt)
    session.commit()
print("\nExtraction and insertion done")
