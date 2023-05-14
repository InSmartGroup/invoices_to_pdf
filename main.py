from fpdf import FPDF
import functions
import pandas as pd
import streamlit as st

# GUI layout
st.set_page_config(layout="wide")
st.title("Excel to PDF Invoice Converter")

# download an excel dataset
file = st.file_uploader("Download an invoice in Excel", key='file_name')

# create a pdf object
pdf = FPDF(orientation='L', unit="mm", format='a4')

# read the dataset and show 10 first rows
df = functions.read_data(file)
st.write(df.head(10))

# convert the file to pdf
button_convert = st.button("Convert to PDF")

# todo add a convert to pdf function

# download the file in pdf
if button_convert:
    st.write("Download the PDF file")  # delete it once the convert function is added
    # st.download_button("Download the PDF file")
