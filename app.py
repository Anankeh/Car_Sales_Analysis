import streamlit as st
import pandas as pd
import plotly.express as px

st.header("Car Sales S7 - Análisis Interactivo")

# Cargar datos
df = pd.read_csv("vehicles_us.csv")

# Botón para histograma
if st.button("Mostrar histograma (odometer)"):
    st.write("Histograma del odómetro")
    fig = px.histogram(df, x="odometer")
    st.plotly_chart(fig)

# Botón para scatter plot
if st.button("Mostrar gráfico de dispersión (odometer vs price)"):
    st.write("Gráfico de dispersión")
    fig = px.scatter(df, x="odometer", y="price")
    st.plotly_chart(fig)