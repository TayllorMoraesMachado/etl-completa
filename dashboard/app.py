import streamlit as st 
import pandas as pd 
import sqlite3

# Conectar no banco de dados
conn = sqlite3.connect('./data/quotes.db')

# Carregar os dados da tabela 'mercadolivre_items' em um Dataframe pandas 
df = pd.read_sql_query('SELECT * FROM mercadolivre_items', conn)

# Fechar conexão com o db
conn.close()

# Titulo da aplicação 
st.title('Pesquisa de Mercado - Tênis Esportivos no Mercado Livre')

#
st.subheader('Principais KPIs do sistema')
col1, col2, col3 = st.columns(3)

# KPI - Total de items 
total_itens = df.shape[0]
col1.metric(label='Número Total de Itens', value=total_itens)

# KPI - Número de Marcas únicas
unique_brand = df['brand'].nunique()
col2.metric(label='Número de marcas únicas', value=unique_brand)

# KPI - Preço médio novo (em reais)
average_new_price = df['new_price'].mean()
col3.metric(label='Preço Médio Novo R$', value=f"{average_new_price:.2f}")

# MARCAS mais encontradas até a página 10 
st.subheader('Marcas mais encontradas até a página 10')
col1, col2 = st.columns([4,2])
top_10_pages_brands = df.head(500)['brand'].value_counts().sort_values(ascending=False)
col1.bar_chart(top_10_pages_brands)
col2.write(top_10_pages_brands)

# Preço médio por marca
st.subheader('Preço médio por marca')
col1, col2 = st.columns([4,2])
average_price_by_brand = df.groupby('brand')['new_price'].mean().sort_values(ascending=False)
col1.bar_chart(average_price_by_brand)
col2.write(average_price_by_brand)

# Satisfação total por marca
st.subheader('Satisfação por marca')
col1, col2 = st.columns([4, 2])
df_non_zero_reviews = df[df['reviews_rating_number'] > 0]
satisfaction_by_brand = df_non_zero_reviews.groupby('brand')['reviews_rating_number'].mean().sort_values(ascending=False)
col1.bar_chart(satisfaction_by_brand)
col2.write(satisfaction_by_brand)