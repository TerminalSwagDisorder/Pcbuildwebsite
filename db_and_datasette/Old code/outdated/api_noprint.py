# Import pcpartpicker
from PCPartPicker_API import pcpartpicker

print("Extracting data without printing it")

# Change the region to De
pcpartpicker.set_region("de")
print("\nRegion changed to De")

# Print the total amount of pages for CPUs
print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))

# Pull info from page 1 of CPUs
cpu_info = pcpartpicker.lists.get_list("cpu", 1)

# Pull info from all CPU pages (this may take a minute)
cpu_info_2 = pcpartpicker.lists.get_list("cpu")

print("CPUs done")



print("Total CPU-cooler pages:", pcpartpicker.lists.total_pages("cpu-cooler"))

cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler", 1)

cpu_cooler_info_2 = pcpartpicker.lists.get_list("cpu-cooler")

print("CPU-coolers done")




print("Total motherboard pages:", pcpartpicker.lists.total_pages("motherboard"))

motherboard_info = pcpartpicker.lists.get_list("motherboard", 1)

motherboard_info_2 = pcpartpicker.lists.get_list("motherboard")

print("Mobos done")




print("Total memory pages:", pcpartpicker.lists.total_pages("memory"))

memory_info = pcpartpicker.lists.get_list("memory", 1)

memory_info_2 = pcpartpicker.lists.get_list("memory")

print("RAM done")




print("Total storage pages:", pcpartpicker.lists.total_pages("internal-hard-drive"))

storage_info = pcpartpicker.lists.get_list("internal-hard-drive", 1)

storage_info_2 = pcpartpicker.lists.get_list("internal-hard-drive")

print("Storage done")

	

	
print("Total gpu pages:", pcpartpicker.lists.total_pages("video-card"))

gpu_info = pcpartpicker.lists.get_list("video-card", 1)

gpu_info_2 = pcpartpicker.lists.get_list("video-card")

print("GPUs done")

	

	
print("Total psu pages:", pcpartpicker.lists.total_pages("power-supply"))

psu_info = pcpartpicker.lists.get_list("power-supply", 1)

psu_info_2 = pcpartpicker.lists.get_list("power-supply")

print("PSUs done")


	
	
print("Total case pages:", pcpartpicker.lists.total_pages("case"))

case_info = pcpartpicker.lists.get_list("case", 1)

case_info_2 = pcpartpicker.lists.get_list("case")

print("Cases done")


	
	
print("Total fan pages:", pcpartpicker.lists.total_pages("case-fan"))

fan_info = pcpartpicker.lists.get_list("case-fan", 1)

fan_info_2 = pcpartpicker.lists.get_list("case-fan")

print("Fans done")


	
	
print("Total wired pages:", pcpartpicker.lists.total_pages("wired-network-card"))

wired_info = pcpartpicker.lists.get_list("wired-network-card", 1)

wired_info_2 = pcpartpicker.lists.get_list("wired-network-card")

print("Ethernet done")


	
	
print("Total wireless pages:", pcpartpicker.lists.total_pages("wireless-network-card"))

wireless_info = pcpartpicker.lists.get_list("wireless-network-card", 1)

wireless_info_2 = pcpartpicker.lists.get_list("wireless-network-card")

print("WiFi done")

	

cpus = cpu_info = pcpartpicker.lists.get_list("cpu", 1)
cooler = cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler", 1)
mobo = motherboard_info = pcpartpicker.lists.get_list("motherboard", 1)
ram = memory_info = pcpartpicker.lists.get_list("memory", 1)
hdd = storage_info = pcpartpicker.lists.get_list("internal-hard-drive", 1)
gpu = gpu_info = pcpartpicker.lists.get_list("video-card", 1)
psu = psu_info = pcpartpicker.lists.get_list("power-supply", 1)
case = case_info = pcpartpicker.lists.get_list("case", 1)
fan = fan_info = pcpartpicker.lists.get_list("case-fan", 1)
wired = wired_info = pcpartpicker.lists.get_list("wired-network-card", 1)
wireless = wireless_info = pcpartpicker.lists.get_list("wireless-network-card", 1)


print("Everything done!")
print("Use for data: cpus[0], cooler[0], mobo[0], ram[0], hdd[0], gpu[0], psu[0], case[0], fan[0], wired[0], wireless[0]")
print("Use for names without values: ' [key for key in cpus[0]] ' OR ' for key in cpus[0]: print(key) ' ")
