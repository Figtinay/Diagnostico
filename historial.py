# historial.py
import streamlit as st
import pandas as pd

def show_history():
    df = pd.read_csv('diagnosticos.csv')
   
    #Mostrar datos en una tabla
    st.dataframe(df)