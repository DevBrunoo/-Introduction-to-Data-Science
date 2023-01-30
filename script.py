import csv

files = ["sociais.csv", "vendas.csv", "paises.csv"]

for filename in files:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
