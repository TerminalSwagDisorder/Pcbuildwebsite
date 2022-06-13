# Import pcpartpicker
from PCPartPicker_API import pcpartpicker

print("Extracting data from first side and printing it")

# Change the region to De
pcpartpicker.set_region("de")
print("\nRegion changed to De")

# Print the total amount of pages for CPUs
print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))

# Pull info from page 1 of CPUs
cpu_info = pcpartpicker.lists.get_list("cpu", 1)

# Print the names and prices of all the CPUs on the page
for cpu in cpu_info:
    print(cpu["name"], ":", cpu["price"])

    

print("Total CPU-cooler pages:", pcpartpicker.lists.total_pages("cpu-cooler"))

cpu_cooler_info = pcpartpicker.lists.get_list("cpu-cooler", 1)

for cpu_cooler in cpu_cooler_info:
    print(cpu_cooler["name"], ":", cpu_cooler["price"])

    

print("Total motherboard pages:", pcpartpicker.lists.total_pages("motherboard"))

motherboard_info = pcpartpicker.lists.get_list("motherboard", 1)

for motherboard in motherboard_info:
    print(motherboard["name"], ":", motherboard["price"])

    

print("Total memory pages:", pcpartpicker.lists.total_pages("memory"))

memory_info = pcpartpicker.lists.get_list("memory", 1)

for memory in memory_info:
    print(memory["name"], ":", memory["price"])

    

print("Total storage pages:", pcpartpicker.lists.total_pages("internal-hard-drive"))

storage_info = pcpartpicker.lists.get_list("internal-hard-drive", 1)

for storage in storage_info:
    print(storage["name"], ":", storage["price"])

    

print("Total gpu pages:", pcpartpicker.lists.total_pages("video-card"))

gpu_info = pcpartpicker.lists.get_list("video-card", 1)

for gpu in gpu_info:
    print(gpu["name"], ":", gpu["price"])



print("Total psu pages:", pcpartpicker.lists.total_pages("power-supply"))

psu_info = pcpartpicker.lists.get_list("power-supply", 1)

for psu in psu_info:
    print(psu["name"], ":", psu["price"])



print("Total case pages:", pcpartpicker.lists.total_pages("case"))

case_info = pcpartpicker.lists.get_list("case", 1)

for case in case_info:
    print(case["name"], ":", case["price"])



print("Total fan pages:", pcpartpicker.lists.total_pages("case-fan"))

fan_info = pcpartpicker.lists.get_list("case-fan", 1)

for fan in fan_info:
    print(fan["name"], ":", fan["price"])



print("Total wired pages:", pcpartpicker.lists.total_pages("wired-network-card"))

wired_info = pcpartpicker.lists.get_list("wired-network-card", 1)

for wired in wired_info:
    print(wired["name"], ":", wired["price"])



print("Total wireless pages:", pcpartpicker.lists.total_pages("wireless-network-card"))

wireless_info = pcpartpicker.lists.get_list("wireless-network-card", 1)

for wireless in wireless_info:
    print(wireless["name"], ":", wireless["price"])



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
