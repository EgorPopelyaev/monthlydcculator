# coding=utf-8
__author__ = 'Egor'

import csv
import numpy


def calculate_credit(data_source):
    spent_amount = []
    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for rows in csv_data:
            amount = float(rows['Betrag (EUR)'])
            if amount < 0:
                spent_amount.append(amount)

        print "Credit: %d" % numpy.sum(spent_amount)
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


def get_categories(data_source):
    categories = []

    with open(data_source) as csv_file:
        csv_data = csv.DictReader(csv_file)
        for row in csv_data:
            categories.append(row['Kategorie'])

    print 'Categories: %r' % categories
    return categories


# TODO: find all categories, than calculate spent amount for each categories and display
# TODO: change the way how the test data insert into the function. Input path to file dynamically from console.

get_data_period("some file")
calculate_balance("some file")
get_categories("some file")
