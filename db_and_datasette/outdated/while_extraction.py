from PCPartPicker_API import pcpartpicker

a = 0
tot = pcpartpicker.lists.total_pages("cpu")

print("Run #",a)

while a < tot+1:
    print("\nRun #",a+1,"\n")
    a += 1
    cpu_info = pcpartpicker.lists.get_list("cpu", a)
    for cpu in cpu_info:
        print(cpu["name"], ":", cpu["price"])
        
print("\nExtraction done")
