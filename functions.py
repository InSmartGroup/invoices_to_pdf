import pandas as pd
from fpdf import FPDF


# read a dataset
def read_data(path):
    df = pd.read_excel(path)
    return df


# convert to pdf
