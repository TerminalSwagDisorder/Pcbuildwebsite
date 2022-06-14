import PCPartPicker_API
from PCPartPicker_API import pcpartpicker

print("Testing", pcpartpicker.productLists.getProductList("cpu"))

print("Total CPU pages:", pcpartpicker.productLists.totalPages("cpu"))
