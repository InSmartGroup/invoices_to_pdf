import pandas as pd
from fpdf import FPDF


# read a dataset
def read_data(path):
    df = pd.read_excel(path)
    return df


# convert to pdf
def convert(data):
    for item in data:
        pdf = FPDF(orientation='L', format="a4", unit='mm')
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=12)
