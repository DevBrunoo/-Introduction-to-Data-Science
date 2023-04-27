import csv

files = ["/dados1/sociais.csv", "/dados1/paises.csv", "/dados/vendas.csv"]

for filename in files:
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            print(row)
