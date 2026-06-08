import csv
import os
import custom_module
from datetime import datetime

#2
def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv", "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(row)
        data["rows"] = rows
        return data

    except Exception as e:
        print(type(e).__name__, str(e))
        exit()
employees = read_employees()
print(employees)

#3
def column_index(column_name):
    return employees["fields"].index(column_name)
employee_id_column = column_index("employee_id")

#4
def first_name(row_number):
    col = column_index("first_name")
    return employees["rows"][row_number][col]

#5
def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    return list(filter(employee_match, employees["rows"]))

#6
def employee_find_2(employee_id):
    return list(filter(lambda row: int(row[employee_id_column]) == employee_id, employees["rows"]))

#7
def sort_by_last_name():
    col = column_index("last_name")
    employees["rows"].sort(key=lambda row: row[col])
    return employees["rows"]

#8
def employee_dict(row):
    result = {}
    for i, field in enumerate(employees["fields"]):
        if field != "employee_id":
            result[field] = row[i]
    return result

#9
def all_employees_dict():
    result = {}
    for row in employees["rows"]:
        emp_id = row[employee_id_column]
        result[emp_id] = employee_dict(row)
    return result

#10
def get_this_value():
    return os.getenv("THISVALUE")

#11
def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

#12
def read_minutes():
    def read_file(path):
        data = {}
        rows = []
        with open(path, "r") as f:
            reader = csv.reader(f)
            for i, row in enumerate(reader):
                if i == 0:
                    data["fields"] = row
                else:
                    rows.append(tuple(row))
        data["rows"] = rows
        return data
    m1 = read_file("../csv/minutes1.csv")
    m2 = read_file("../csv/minutes2.csv")
    return m1, m2
minutes1, minutes2 = read_minutes()

#13
def create_minutes_set():
    return set(minutes1["rows"]) | set(minutes2["rows"])
minutes_set = create_minutes_set()

#14
def create_minutes_list():
    lst = list(minutes_set)
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), lst))
minutes_list = create_minutes_list()

#15
def write_sorted_list():
    global minutes_list
    minutes_list.sort(key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), minutes_list))

    with open("./minutes.csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)

    return converted