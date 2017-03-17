from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage
from cStringIO import StringIO
import re
import numpy

prompt = 'Please enter path to the file >'
path = raw_input(prompt)


def get_spent_amount_from_pdf(path):
    rsrcmgr = PDFResourceManager()
    retstr = StringIO()
    codec = 'utf-8'
    laparams = LAParams()
    device = TextConverter(rsrcmgr, retstr, codec=codec, laparams=laparams)
    fp = file(path, 'rb')
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    password = ""
    maxpages = 0
    caching = True
    pagenos=set()

    for page in PDFPage.get_pages(fp, pagenos, maxpages=maxpages, password=password,caching=caching, check_extractable=True):
        interpreter.process_page(page)

    text = retstr.getvalue()

    pattern = '-\d*,\d\d'
    amount_spent = re.findall(pattern, text)

    fp.close()
    device.close()
    retstr.close()
    return amount_spent


def calculate_amount_spent_per_month(path):
    monthly_spent_amount = get_spent_amount_from_pdf(path)

    float_credit_array = []
    for amount in monthly_spent_amount:
        amount = amount.replace(',', '.')
        float_credit_array.append(float(amount))

    credit = numpy.sum(float_credit_array)

    print 'Amount spent  during last month: ', credit
    return credit


calculate_amount_spent_per_month(path)

