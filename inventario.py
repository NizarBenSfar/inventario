import streamlit as st
import pandas as pd

def read_excel(name = "db/Invetario.xlsx"):
    df = pd.read_excel(name) 
    return df


st.title("INVENTARIO")
st.write("INVENTARIO")

df = read_excel()
st.dataframe(df)