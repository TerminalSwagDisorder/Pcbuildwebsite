from pcpartpickerapi import part_lists

print("Total CPU pages:", part_lists.list_page_count("cpu", region="de"))

print(part_lists.get_list("cpu", page=1, region="de"))
 
 
print('\n \n \n')

print("Total CPU-cooler pages:", part_lists.list_page_count("cpu-cooler", region="de"))

print(part_lists.get_list("cpu-cooler", page=1, region="de"))
 
 

print('\n \n \n')

print("Total Mobo pages:", part_lists.list_page_count("motherboard", region="de"))

print(part_lists.get_list("motherboard", page=1, region="de"))
 
 

print('\n \n \n')

print("Total RAM pages:", part_lists.list_page_count("memory", region="de"))

print(part_lists.get_list("memory", page=1, region="de"))
 

  

print('\n \n \n')

print("Total Storage pages:", part_lists.list_page_count("internal-hard-drive", region="de"))

print(part_lists.get_list("internal-hard-drive", page=1, region="de"))
 
 

print('\n \n \n')

print("Total GPU pages:", part_lists.list_page_count("video-card", region="de"))

print(part_lists.get_list("video-card", page=1, region="de"))
 
 

print('\n \n \n')

print("Total Case pages:", part_lists.list_page_count("case", region="de"))

print(part_lists.get_list("case", page=1, region="de"))
 
 

print('\n \n \n')

print("Total PSU pages:", part_lists.list_page_count("power-supply", region="de"))

print(part_lists.get_list("power-supply", page=1, region="de"))
 
 

print('\n \n \n')

print("Total Wired networking pages:", part_lists.list_page_count("wired-network-card", region="de"))

print(part_lists.get_list("wired-network-card", page=1, region="de"))
 
 

print('\n \n \n')

print("Total Wireless networking pages:", part_lists.list_page_count("wireless-network-card", region="de"))

print(part_lists.get_list("wireless-network-card", page=1, region="de"))

