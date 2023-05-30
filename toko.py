import csv

with open('hoje.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)