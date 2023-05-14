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
if file is not None:
    df = functions.read_data(file)
    display_rows = st.checkbox("Display the document?")
    if display_rows:
        number_rows_to_display = st.text_input("How many rows do you want to display?")
        if number_rows_to_display:
            st.write(df.head(int(number_rows_to_display)))

# convert the file to pdf
button_convert = st.button("Convert to PDF")

# todo add a convert to pdf function

# download the file in pdf
if button_convert:
    file_name = st.text_input("Name the file")  # check if naming is allowed when downloading
    st.write("Download the PDF file")  # delete it once the convert function is added
    # st.download_button("Download the PDF file")
