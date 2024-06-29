import pandas as pd 
import sqlite3
from datetime import datetime

#### Criando um dataframe
df = pd.read_json('../data/data.json')

# Criando colunas
df['_source'] = 'https://lista.mercadolivre.com.br/tenis-masculino'
df['_data_coleta'] = datetime.now()

# Tratando os valores nulos 
df['old_price_reais'] = df['old_price_reais'].fillna(0).astype(float)
df['old_price_centavos'] = df['old_price_centavos'].fillna(0).astype(float)
df['new_price_reais'] = df['new_price_reais'].fillna(0).astype(float)
df['new_price_centavos'] = df['new_price_centavos'].fillna(0).astype(float)
df['reviews_rating_number'] = df['reviews_rating_number'].fillna(0).astype(float)

# Remover os parenteses das colunas e converter para int
df['reviews_amount'] = df['reviews_amount'].str.replace('[\\(\\)]', '', regex=True).fillna(0).astype(int)

# Calcular os preços totais 
df['old_price'] = df['old_price_reais'] + df['old_price_centavos'] / 100
df['new_price'] = df['new_price_reais'] + df['new_price_centavos'] / 100

# Remover as colunas antigas corretamente
df.drop(columns=['old_price_reais', 'old_price_centavos', 'new_price_reais', 'new_price_centavos'], inplace=True)

# Conectar ao banco de dados SQLite (ou criar um novo)
conn = sqlite3.connect('./data/quotes.db')

# Salvar o dataframe no banco de dados 
df.to_sql('mercadolivre_items', conn, if_exists='replace', index=False)

# Fechar conexão 
conn.close()

