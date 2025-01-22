import streamlit as st
import pandas as pd
import plotly.express as px

git commit -m "Corrigindo requirements.txt"
git push
# Ler os dados
data = pd.read_csv('vehicles.csv')

# Criar um histograma
fig = px.histogram(data, x='odometer')
fig.show()

# Criar um gráfico de dispersão
fig = px.scatter(data, x='odometer', y='price')
fig.show()

# Ler o arquivo CSV
data = pd.read_csv('vehicles.csv')

# Cabeçalho do aplicativo
st.header('Análise de Dados de Veículos Usados')

# Botão para criar o histograma
if st.button('Criar histograma'):
    st.write('Histograma de odômetro')
    fig = px.histogram(data, x='odometer')
    st.plotly_chart(fig)

# Botão para criar o gráfico de dispersão
if st.button('Criar gráfico de dispersão'):
    st.write('Gráfico de preço vs odômetro')
    fig = px.scatter(data, x='odometer', y='price')
    st.plotly_chart(fig)
