#Data file Input/Ouput

import csv

header = ['Name', 'Age', 'Occupation']
data = [
        ['John', '25', 'Engineer'],
        ['Anna', '30', 'Doctor'],
        ['Mike', '22', 'Student']
]
extraData = [
        ['Cindy', '27', 'Nurse'],
        ['Jake', '32', 'Teacher']
]

filename = 'CSV files/people.csv'
with open(filename, mode='w', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

print("\n")

with open(filename, mode='a', newline='') as file:
    csvwriter = csv.writer(file)
    csvwriter.writerows(extraData)

with open(filename, mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)