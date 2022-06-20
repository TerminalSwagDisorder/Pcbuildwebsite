#PCPartPicker_API = __import__("PCPartPicker_API")
#import PCPartPicker_API
from PCPartPicker_API import pcpartpicker

#print("Total CPU pages:", pcpartpicker.lists.total_pages("cpu"))

cpu_info = pcpartpicker.productLists.getProductList("cpu", 1)

# Print the names and prices of all the CPUs on the page
for cpu in cpu_info:
    print(cpu["name"], ":", cpu["price"])


'''
print("Testing", pcpartpicker.productLists.getProductList("cpu"))

print("Total CPU pages:", pcpartpicker.productLists.totalPages("cpu"))

'''

#pcpp site error: An unknown error occurred while fetching list: /qapi/product/category/ 200: SyntaxError: Unexpected token < in JSON at position 0
