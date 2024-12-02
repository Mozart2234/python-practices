import csv

# with open("products.csv", mode="r") as file:
#     csv_reader = csv.DictReader(file)
#     for row in csv_reader:
#         print(row)

with open("products.csv", mode="r") as file:
    csv_reader = csv.DictReader(file)
    for row in csv_reader:
        print(f"Producto: {row['name']}, Precio: {row['price']}")