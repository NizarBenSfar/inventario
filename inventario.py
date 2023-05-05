import streamlit as st
import pandas as pd
from datetime import datetime
import numpy as np
def read_excel(name = "db/Invetario.xlsx"):
    df = pd.read_excel(name) 
    return df


st.title("INVENTARIO")

df = read_excel()
edited_df = st.experimental_data_editor(df,num_rows="dynamic",use_container_width=True)

if st.button("SAVE"):
    edited_df.to_excel("db/Invetario.xlsx")