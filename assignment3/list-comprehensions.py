import csv
file_path = "../csv/employees.csv"

with open(file_path, newline="") as f:
    reader = list(csv.reader(f))
data = reader[1:]

names = [row[0] + " " + row[1] for row in data]
print(names)

names_with_e = [name for name in names if "e" in name.lower()] # names containing "e"
print(names_with_e)