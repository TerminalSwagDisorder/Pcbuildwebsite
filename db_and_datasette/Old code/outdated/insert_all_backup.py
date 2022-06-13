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

print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))


def cpu_transform(key,value):
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

cpu_info = pcpartpicker.lists.get_list("cpu")
cpu_info = [{
    key:cpu_transform(key,value) for key,value in cpu.items()} for cpu in cpu_info]

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


# insert

i = insert(cpu)
i = i.values(cpu_info)
session.execute(i)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt = cpu.delete().where(cpu.c.price == '')
session.execute(dlt)
session.commit()

print("Deletion done")






print("Total CPU-cooler pages:", pcpartpicker.lists.total_pages("cpu-cooler"))

cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler")



def cpu_cooler_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler")
cpu_cooler_info = [{
    key:cpu_cooler_transform(key,value) for key,value in cpu_cooler.items()} for cpu-cooler in cpu_cooler_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i2 = insert(cpu_cooler)
i2 = i2.values(cpu_cooler_info)
session.execute(i2)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt2 = cpu_cooler.delete().where(cpu_cooler.c.price == '')
session.execute(dlt2)
session.commit()

print("Deletion done")






print("Total motherboard pages:", pcpartpicker.lists.total_pages("motherboard"))

motherboard_info = pcpartpicker.lists.get_list("motherboard")



def motherboard_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

motherboard_info = pcpartpicker.lists.get_list("motherboard")
motherboard_info = [{
    key:motherboard_transform(key,value) for key,value in motherboard.items()} for motherboard in motherboard_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i3 = insert(motherboard)
i3 = i3.values(motherboard_info)
session.execute(i3)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt3 = motherboard.delete().where(motherboard.c.price == '')
session.execute(dlt3)
session.commit()

print("Deletion done")






print("Total memory pages:", pcpartpicker.lists.total_pages("memory"))

memory_info = pcpartpicker.lists.get_list("memory")



def memory_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

memory_info = pcpartpicker.lists.get_list("memory")
memory_info = [{
    key:memory_transform(key,value) for key,value in memory.items()} for memory in memory_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i4 = insert(memory)
i4 = i4.values(memory_info)
session.execute(i4)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt4 = memory.delete().where(memory.c.price == '')
session.execute(dlt4)
session.commit()

print("Deletion done")






print("Total storage pages:", pcpartpicker.lists.total_pages("internal-hard-drive"))

storage_info = pcpartpicker.lists.get_list("internal-hard-drive")



def storage_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

storage_info = pcpartpicker.lists.get_list("internal-hard-drive")
storage_info = [{
    key:storage_transform(key,value) for key,value in storage.items()} for storage in storage_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i5 = insert(storage)
i5 = i5.values(storage_info)
session.execute(i5)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt5 = storage.delete().where(storage.c.price == '')
session.execute(dlt5)
session.commit()

print("Deletion done")






print("Total gpu pages:", pcpartpicker.lists.total_pages("video-card"))

gpu_info = pcpartpicker.lists.get_list("video-card")



def gpu_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

gpu_info = pcpartpicker.lists.get_list("video-card")
gpu_info = [{
    key:gpu_transform(key,value) for key,value in gpu.items()} for gpu in gpu_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i6 = insert(gpu)
i6 = i6.values(gpu_info)
session.execute(i6)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt6 = gpu.delete().where(gpu.c.price == '')
session.execute(dlt6)
session.commit()

print("Deletion done")






print("Total psu pages:", pcpartpicker.lists.total_pages("power-supply"))

psu_info = pcpartpicker.lists.get_list("power-supply")



def psu_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

psu_info = pcpartpicker.lists.get_list("power-supply")
psu_info = [{
    key:psu_transform(key,value) for key,value in psu.items()} for psu in psu_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i7 = insert(psu)
i7 = i7.values(psu_info)
session.execute(i7)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt7 = psu.delete().where(psu.c.price == '')
session.execute(dlt7)
session.commit()

print("Deletion done")






print("Total case pages:", pcpartpicker.lists.total_pages("case"))

case_info = pcpartpicker.lists.get_list("case")



def case_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

case_info = pcpartpicker.lists.get_list("case")
case_info = [{
    key:case_transform(key,value) for key,value in case.items()} for case in case_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i8 = insert(case)
i8 = i8.values(case_info)
session.execute(i8)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt8 = case.delete().where(case.c.price == '')
session.execute(dlt8)
session.commit()

print("Deletion done")






print("Total fan pages:", pcpartpicker.lists.total_pages("case-fan"))

fan_info = pcpartpicker.lists.get_list("case-fan")



def fan_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

fan_info = pcpartpicker.lists.get_list("case-fan")
fan_info = [{
    key:fan_transform(key,value) for key,value in fan.items()} for fan in fan_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i9 = insert(fan)
i9 = i9.values(fan_info)
session.execute(i9)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt9 = fan.delete().where(fan.c.price == '')
session.execute(dlt9)
session.commit()

print("Deletion done")






print("Total wired pages:", pcpartpicker.lists.total_pages("wired-network-card"))

wired_info = pcpartpicker.lists.get_list("wired-network-card")



def wired_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

wired_info = pcpartpicker.lists.get_list("wired-network-card")
wired_info = [{
    key:wired_transform(key,value) for key,value in wired.items()} for wired in wired_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i10 = insert(wired)
i10 = i10.values(wired_info)
session.execute(i10)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt10 = wired.delete().where(wired.c.price == '')
session.execute(dlt10)
session.commit()

print("Deletion done")






print("Total wireless pages:", pcpartpicker.lists.total_pages("wireless-network-card"))

wireless_info = pcpartpicker.lists.get_list("wireless-network-card")



def wireless_transform(key,value):
    #remove one character at the beginning
    if key == "price":
        value = value[1:]
        return str(value)
        if value == str(value):
            return float(str(value))
    else:
        return value

wireless_info = pcpartpicker.lists.get_list("wireless-network-card")
wireless_info = [{
    key:wireless_transform(key,value) for key,value in wireless.items()} for wireless in wireless_info]


print("Extraction done")

print("Inserting data into database")

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


# insert

i11 = insert(wireless)
i11 = i11.values(wireless_info)
session.execute(i11)
session.commit()

print("Insertion done")

print("Deleting Null prices")

# delete
dlt11 = wireless.delete().where(wireless.c.price == '')
session.execute(dlt11)
session.commit()

print("Deletion done")
print("Everything done")
