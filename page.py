import streamlit as st
import pandas as pd
import plotly.express as px

# Título da aplicação
st.title('Visualização Interativa de Dados')

# Carregar arquivo CSV
uploaded_file = st.file_uploader('Carregar arquivo CSV', type=['csv'])

if uploaded_file is not None:
    # Ler o arquivo CSV
    df = pd.read_csv(uploaded_file)

    # Exibir a tabela de dados
    st.write('Dados do arquivo CSV:')
    st.dataframe(df)

    # Seleção de colunas para o gráfico
    st.write('Seleção de colunas para o gráfico:')
    x_column = st.selectbox('Coluna para o eixo X', df.columns)
    y_column = st.selectbox('Coluna para o eixo Y', df.columns)

    # Criar gráfico com Plotly
    fig = px.scatter(df, x=x_column, y=y_column, title=f'{x_column} vs {y_column}')
    st.plotly_chart(fig)