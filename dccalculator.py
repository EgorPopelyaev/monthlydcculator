import n26csvreader as n26csv
import spardapdfreader as sppdf

prompt = 'Please enter path to the file >'
path_to_csv = raw_input(prompt)
path_to_pdf = raw_input(prompt)


def calculate_dc(csv_f, pdf_f):
    n26_credit = n26csv.calculate_credit(csv_f)
    n26_debit = n26csv.calculate_debit(csv_f)

    sp_credit_from_pdf = sppdf.calculate_amount_spent_per_month(pdf_f)

    sp_credit = sp_credit_from_pdf + n26_debit

    return n26_credit + sp_credit

print calculate_dc(path_to_csv, path_to_pdf)