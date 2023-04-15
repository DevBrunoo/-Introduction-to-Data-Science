import csv

files = ["paises.csv", "sociais.csv"]

for filename in files:
  with open(filename, "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row['company'], row['Name'])