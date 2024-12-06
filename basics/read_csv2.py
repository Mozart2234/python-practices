import csv

new_product = {
    "name": "Laptop",
    "price": 1200,
    "quantity": 10,
    "brand": "Apple",
    "category": "Technology",
    "entry_date": "2021-09-01",
}

with open("products.csv", mode="a", newline="") as file:
    csv_writer = csv.DictWriter(file, fieldnames=new_product.keys())
    csv_writer.writerow(new_product)
