from pypartpicker import Scraper

pcpartpicker = Scraper()
parts = pcpartpicker.part_search("i7")

for part in parts:
    print(part.name)

first_product_url = parts[0].url
product = pcpartpicker.fetch_product(first_product_url)
print(product.specs)