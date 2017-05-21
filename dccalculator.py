import n26csvreader as n26csv
import spardapdfreader as sppdf

prompt1 = 'Please enter path to the n26 csv file >'
path_to_csv = raw_input(prompt1)
prompt2 = 'Please enter path to the sparda k pdf file >'
path_to_k_pdf = raw_input(prompt2)
prompt3 = 'Please enter path to the sparda v pdf file >'
path_to_v_pdf = raw_input(prompt3)


def calculate_dc(csv_f, pdf_f1, pdf_f2):
    n26_credit = n26csv.calculate_credit(csv_f)
    n26_debit = n26csv.calculate_debit(csv_f)

    sp_konto_credit = sppdf.calculate_amount_spent_per_month(pdf_f1)
    sp_visa_credit = sppdf.calculate_amount_spent_per_month(pdf_f2)

    sp_credit_from_pdf = sp_konto_credit + sp_visa_credit

    print "Credit sum from pdf: %.2f" % sp_credit_from_pdf

    sp_credit = sp_credit_from_pdf + n26_debit

    return n26_credit + sp_credit

print "Total amount spent for months: %.2f" % calculate_dc(path_to_csv, path_to_k_pdf, path_to_v_pdf)
n26csv.calculate_amount_spent_per_category(path_to_csv)