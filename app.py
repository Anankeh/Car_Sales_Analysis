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
