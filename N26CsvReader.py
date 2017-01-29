# coding=utf-8
from collections import defaultdict

__author__ = 'Egor'

import csv
import numpy

path_to_file = ""


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


def get_data_period(data_source):
    dates = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            dates.append(row['﻿"Datum"'])

    print 'Account state from: %r till: %r' % (dates[0], dates[len(dates) - 1])
    return dates


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


def calculate_balance(data_source):
    debit = calculate_debit(data_source)
    credit = calculate_credit(data_source)
    balance = debit + credit

    print "Balance: %.2f" % balance
    return balance


def calculate_amount_spent_per_category(data_source):
    categories_with_amount = get_categories_with_spent_amount(data_source)
    categories = []

    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            categories.append(row['Kategorie'])

    category_with_amount = {}

    for cat in set(categories):
        category_with_amount.update({cat: numpy.sum(categories_with_amount.get(cat))})
        print "Amount spent on each category: %r :: %.2f" % (cat, category_with_amount.get(cat))

    return category_with_amount

# TODO: change the way how the test data insert into the function. Input path to file dynamically from console.

get_data_period(path_to_file)
calculate_balance(path_to_file)
calculate_amount_spent_per_category(path_to_file)