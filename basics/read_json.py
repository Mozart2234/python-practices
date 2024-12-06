import json

# with open("products.json", "r") as file:
#     products = json.load(file)
#
#     for product in products:
#         # print(product)
#         print(f"Product: {product['name']}, Price: {product['price']}")
#
with open("products.json", "r") as file:
    products = json.load(file)

products.append({"name": "Keyboard", "price": 20.0})

with open("products.json", "w") as file:
    json.dump(products, file, indent=4)
