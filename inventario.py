import streamlit as st
import pandas as pd

def read_excel(name = "db/Invetario.xlsx"):
    df = pd.read_excel(name) 
    return df


st.title("INVENTARIO")

df = read_excel()
edited_df = st.experimental_data_editor(df)