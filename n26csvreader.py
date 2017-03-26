# coding=utf-8
from collections import defaultdict
import csv
import numpy

__author__ = 'Egor'


# This function calculates all expenses for the period of time given in the csv file
def calculate_credit(data_source):
    credit = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for rows in csv_data:
            amount = float(rows['Betrag (EUR)'])
            if amount < 0:
                credit.append(amount)

        credit_sum = numpy.sum(credit)
        print "Credit: %.2f" % credit_sum
    return credit_sum


# This function calculates all incomes for the period of time given in the csv file
def calculate_debit(data_source):
    debit = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for rows in csv_data:
            amount = float(rows['Betrag (EUR)'])
            if amount > 0:
                debit.append(amount)

        debit_sum = numpy.sum(debit)
        print "Debit: %.2f" % debit_sum
    return debit_sum


# This function returns a period of time given in the csv file
def get_data_period(data_source):
    dates = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            dates.append(row['﻿"Datum"'])

    print 'Account state from: %r till: %r' % (dates[0], dates[len(dates) - 1])
    return dates


# This function returns all categories with amount spent for each category
def get_categories_with_spent_amount(data_source):
    categories = []

    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            categories.append((row['Kategorie'], float(row['Betrag (EUR)'])))

    mapped_categories = defaultdict(list)
    for k, v in categories:
        mapped_categories[k].append(v)

    return mapped_categories


# This function calculates an account balance for the period of time given in csv file
def calculate_balance(data_source):
    debit = calculate_debit(data_source)
    credit = calculate_credit(data_source)
    balance = debit + credit

    print "Balance: %.2f" % balance
    return balance


# This function calculates spent amount for each category
def calculate_amount_spent_per_category(data_source):
    categories_with_amount = get_categories_with_spent_amount(data_source)
    categories = []

    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            categories.append(row['Kategorie'])

    category_with_amount = {}

    print "Amount spent on each category:"
    for cat in set(categories):
        category_with_amount.update({cat: numpy.sum(categories_with_amount.get(cat))})
        print "%r :: %.2f" % (cat, category_with_amount.get(cat))

    return category_with_amount


# TODO: develop a web interface to enter data source and show calculation
# TODO: check for API's to download files
# TODO: add db connection to store monthly results (not sure)
# TODO: add graphics visualisation
