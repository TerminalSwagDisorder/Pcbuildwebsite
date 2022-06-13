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

cpu_info = pcpartpicker.lists.get_list("cpu", 1)
cpu_info = [{
    key:transform(key,value) for key,value in cpu.items()} for cpu in cpu_info]

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

'''
# update
dlt = cpu.update().where(cpu.c.price == '')
session.execute(dlt)
session.commit()
'''

print("Everything done, check database")
