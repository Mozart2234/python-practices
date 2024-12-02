import csv

file_path = "products.csv"
updated_file_path = "products_updated.csv"

with open(file_path, mode="r") as file:
    csv_reader = csv.DictReader(file)

    # Handle fieldnames safely
    if csv_reader.fieldnames is not None:
        fieldnames = list(csv_reader.fieldnames) + ["total_value"]
    else:
        raise ValueError("CSV file does not contain headers.")

    with open(updated_file_path, mode="w", newline="") as updated_file:
        csv_writer = csv.DictWriter(updated_file, fieldnames=fieldnames)
        csv_writer.writeheader()

        for row in csv_reader:
            row["total_value"] = int(row["price"]) * int(row["quantity"])
            csv_writer.writerow(row)
