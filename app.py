#Importar librerías
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
car_data = pd.read_csv("vehicles_us.csv")

# Title
st.title("Car Sales S7 - Análisis Interactivo")

st.write("Selecciona una opción para visualizar los datos del dataset.")