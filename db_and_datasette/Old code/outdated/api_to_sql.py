import sqlite3
import json
from PCPartPicker_API import pcpartpicker

conn = sqlite3.connect('E:\\Skola\\pcbuildapp\\pcbuildapp.db')
cursor = conn.cursor()

'''
def data_insert():
	conn = sqlite3.connect('E:\\Skola\\pcbuildapp\\pcbuildapp.db')
	cursor = conn.cursor()
	if request.method == 'POST':
		cpus2 = request.get_json(force=True)
		post_kund(cursor,cpus2)
		conn.commit()
		conn.close()
		return "" + str(cpus2)
		
def insert(database_cursor,cpus2):
	kontrakt_tuple = kontraktdict_to_tuple(cpus2)
	database_cursor.execute('INSERT INTO cpu (name,speed,cores,tdp,ratings,price,id) VALUES (?,?,?,?,?,?,?);', cpu_info)
	return
	
def kontrakttuple_to_dict(kontrakt_tuple):
    return{
    "name":kontrakt_tuple[0],
    "speed":kontrakt_tuple[1], 
    "cores":kontrakt_tuple[2],
    "tdp":kontrakt_tuple[3],    
    "ratings":kontrakt_tuple[4],
	"price":kontrakt_tuple[5],
	"id":kontrakt_tuple[6]
    }	
	
def kontraktdict_to_tuple(kontrakt_dict):
	return (kontrakt_dict['KundID'],kontrakt_dict['TjänstID'],kontrakt_dict['Lokation'],kontrakt_dict['Datum'])
'''



pcpartpicker.set_region("de")
print("\nRegion changed to De")

print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))

cpu_info = pcpartpicker.lists.get_list("cpu", 1)

cpu_info_2 = pcpartpicker.lists.get_list("cpu")

c.executemany('INSERT INTO cpu VALUES (?,?,?,?,?,?,?)', cpu_info)




print("Total CPU-cooler pages:", pcpartpicker.lists.total_pages("cpu-cooler"))

cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler", 1)

cpu_cooler_info_2 = pcpartpicker.lists.get_list("cpu-cooler")





print("Total motherboard pages:", pcpartpicker.lists.total_pages("motherboard"))

motherboard_info = pcpartpicker.lists.get_list("motherboard", 1)

motherboard_info_2 = pcpartpicker.lists.get_list("motherboard")





print("Total memory pages:", pcpartpicker.lists.total_pages("memory"))

memory_info = pcpartpicker.lists.get_list("memory", 1)

memory_info_2 = pcpartpicker.lists.get_list("memory")





print("Total storage pages:", pcpartpicker.lists.total_pages("internal-hard-drive"))

storage_info = pcpartpicker.lists.get_list("internal-hard-drive", 1)

storage_info_2 = pcpartpicker.lists.get_list("internal-hard-drive")


	

	
print("Total gpu pages:", pcpartpicker.lists.total_pages("video-card"))

gpu_info = pcpartpicker.lists.get_list("video-card", 1)

gpu_info_2 = pcpartpicker.lists.get_list("video-card")


	

	
print("Total psu pages:", pcpartpicker.lists.total_pages("power-supply"))

psu_info = pcpartpicker.lists.get_list("power-supply", 1)

psu_info_2 = pcpartpicker.lists.get_list("power-supply")



	
	
print("Total case pages:", pcpartpicker.lists.total_pages("case"))

case_info = pcpartpicker.lists.get_list("case", 1)

case_info_2 = pcpartpicker.lists.get_list("case")



	
	
print("Total fan pages:", pcpartpicker.lists.total_pages("case-fan"))

fan_info = pcpartpicker.lists.get_list("case-fan", 1)

fan_info_2 = pcpartpicker.lists.get_list("case-fan")



	
	
print("Total wired pages:", pcpartpicker.lists.total_pages("wired-network-card"))

wired_info = pcpartpicker.lists.get_list("wired-network-card", 1)

wired_info_2 = pcpartpicker.lists.get_list("wired-network-card")



	
	
print("Total wireless pages:", pcpartpicker.lists.total_pages("wireless-network-card"))

wireless_info = pcpartpicker.lists.get_list("wireless-network-card", 1)

wireless_info_2 = pcpartpicker.lists.get_list("wireless-network-card")

	
