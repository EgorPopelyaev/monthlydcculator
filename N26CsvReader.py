# coding=utf-8
__author__ = 'Egor'

import csv
import numpy

path_to_file = ""


def calculate_credit(data_source):
    spent_amount = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for rows in csv_data:
            amount = float(rows['Betrag (EUR)'])
            if amount < 0:
                spent_amount.append(amount)

        print "Credit: %d" % numpy.sum(spent_amount)
        # TODO: return directly numpy.sum
    return spent_amount


def calculate_debit(data_source):
    income = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for rows in csv_data:
            amount = float(rows['Betrag (EUR)'])
            if amount > 0:
                income.append(amount)
        print "Debit: %d" % (numpy.sum(income))
    return income


def calculate_balance(data_source):
    debit = calculate_debit(data_source)
    credit = calculate_credit(data_source)
    balance = numpy.sum(debit) + numpy.sum(credit)
    print "Balance: %d" % balance
    return balance


def get_data_period(data_source):
    dates = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            dates.append(row['﻿"Datum"'])

    print 'Account state from: %r till: %r' % (dates[0], dates[len(dates) - 1])
    return dates


def get_categories_with_spent_amount(data_source):
    categories = {}

    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            categories.update({row['Kategorie']:row['Betrag (EUR)']})

    print 'Categories: %r' % categories
    return categories


def calculate_amount_spent_per_category(data_source):
    categories_with_amount = get_categories_with_spent_amount(data_source)
    categories = []

    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            categories.append(row['Kategorie'])

    categories_set = set(categories)
    category_with_amount = {}

    for category in categories_set:
        cat_amount = []
        for cat in categories_with_amount:
            cat_amount.append(categories_with_amount.get(category))

        #amount = numpy.sum(numpy.array(cat_amount).astype(numpy.float))
        category_with_amount.update({category: numpy.sum(numpy.array(cat_amount).astype(numpy.float))})

    print "Amount spent on each cat egory: %r" % category_with_amount
    return category_with_amount

# TODO: find all categories, than calculate spent amount for each categories and display
# TODO: change the way how the test data insert into the function. Input path to file dynamically from console.

get_data_period(path_to_file)
calculate_balance(path_to_file)
calculate_amount_spent_per_category(path_to_file)