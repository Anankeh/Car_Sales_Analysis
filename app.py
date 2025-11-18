import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv('vehicles_us.csv')

# Header
st.header('Car Sales Analysis')

# Histogram button
if st.button('Show Odometer Histogram'):
    fig = px.histogram(df, x='odometer', nbins=30, title='Odometer Distribution')
    st.plotly_chart(fig)
    st.write('This histogram shows the distribution of odometer values in the dataset.')

# Scatter plot button
if st.button('Show Odometer vs Price'):
    fig = px.scatter(df, x='odometer', y='price', title='Odometer vs Price')
    st.plotly_chart(fig)
    st.write('This scatter plot shows the relationship between odometer readings and price.')
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