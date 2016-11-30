__author__ = 'Egor'


import csv
import numpy

with open("number.csv") as csvfile:
    spent_amount = []
    csv_data = csv.DictReader(csvfile)
    for rows in csv_data:
        spent_amount.append(float(rows['Betrag (EUR)']))

    print(numpy.sum(spent_amount))