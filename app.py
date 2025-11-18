# Import libraries
import streamlit as st
import pandas as pd
import plotly.express as px

# Load data (CSV is in the project root)
car_data = pd.read_csv("vehicles_us.csv")

# Page title
st.title("Car Sales S7 - Análisis Interactivo")
st.write("Selecciona una opción para visualizar los datos del dataset.")

# Show a small preview
if st.checkbox("Mostrar tabla de datos (primeras 5 filas)"):
	st.dataframe(car_data.head())

# Histogram: toggle with checkbox
if st.checkbox("Mostrar histograma del odómetro"):
	fig = px.histogram(car_data, x="odometer", nbins=50, title="Distribución del odómetro")
	st.plotly_chart(fig, use_container_width=True)

# Scatter plot: button to display
if st.button("Mostrar dispersión: precio vs odómetro"):
	fig2 = px.scatter(car_data, x="odometer", y="price", title="Precio vs Odómetro")
	st.plotly_chart(fig2, use_container_width=True)

# Small footer
st.write("---")
st.write("Fuente: `vehicles_us.csv`")
