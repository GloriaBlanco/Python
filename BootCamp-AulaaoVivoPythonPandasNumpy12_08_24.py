# aula ao vivo 13/08/24

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""**Importando dados do Quadro de Medalhas 1896 a 2022**"""

# Caminho para o arquivo com os dados
file_path = 'game_medal_tally.csv.gz'

# Importando os dados para um DataFrame
df = pd.read_csv(file_path, compression='gzip')

# Exibindo as primeiras linhas do DataFrame
print(df.head())

"""**Data prep**

"""

df.info()

df.describe()

#Verificando se tem nulos
df.isnull().sum()

#Preenche valores ausentes
df.fillna(0, inplace=True)

#Remoção de duplicados
df.drop_duplicates(inplace=True)

"""**Análise Exploratória de Dados (EDA)**"""

#Distribuição de Medalhas por País

medalhas_por_pais = df.groupby('country')[['gold','silver','bronze']].sum()
print(medalhas_por_pais)

#Ordenando por quantidade de ouros
medalhas_por_pais.sort_values(by='gold', ascending=False)

#Top 10 países com mais medalhas

top_10_paises = medalhas_por_pais.sort_values(by='gold', ascending=False).head(10)
print(top_10_paises)

#Selecionando um range de datas, trazer dados após 1989.
df_novo = df[df['year'] >= 1989]

print(df_novo.head())

df_novo.info()

#Distribuição de Medalhas por País

medalhas_por_pais = df_novo.groupby('country')[['gold', 'silver', 'bronze', 'total']].sum()
print(medalhas_por_pais)

#Ordenando por quantidade de ouros

medalhas_por_pais.sort_values(by='gold', ascending=False)

#Top 10 países com mais medalhas de ouro

top_10_paises = medalhas_por_pais.sort_values(by='gold', ascending=False).head(10)
print(top_10_paises)

#Top 10 países com mais medalhas

top_10_paises_tt = medalhas_por_pais.sort_values(by='total', ascending=False).head(10)
print(top_10_paises_tt)

# Ordenar o DataFrame por tipo de medalha
df_ordena = df_novo.sort_values(by=['gold', 'silver', 'bronze'], ascending=[False, False, False])

df_ordena.head()

"""Paramos aqui"""

#Tirar colunas year, edition, edition_id para criar ranking limpo por país

df_ordena = df_ordena.drop(columns=['year', 'edition', 'edition_id', 'country_noc'])
df_ordena.head()

#Agrupando por país por soma

df_ordena = df_ordena.groupby('country', as_index=False).sum()
df_ordena.head()

# Ordenar o DataFrame por tipo de medalha
df_ordena = df_ordena.sort_values(by=['total'], ascending=[False])

df_ordena.head()

# Criar a coluna de ranking
df_ordena['rank'] = df_ordena.reset_index(drop=True).index + 1

df_ordena.head()

# Encontrar a posição do Brasil
brazil_rank = df_ordena[df_ordena['country'] == 'Brazil']['rank'].values[0]
print(f'O Brasil está na posição {brazil_rank}')

# Exibir o DataFrame com a coluna de Ranking
print(df)

df_ordena.head(24)

"""**Manipulação de Dados com Numpy**"""

# Média de medalhas por país

avg_medals= np.mean(medalhas_por_pais, axis=1)
avg_medals = avg_medals.sort_values(ascending=False)
print(avg_medals)

#País com mais medalhas em 2022

ano_filtro = df[df['year'] == 2022]
pais_top_2008 = ano_filtro[ano_filtro['total'] == np.max(ano_filtro['total'])]

print(pais_top_2008[['country', 'total']])

"""**Plotando de Dados com MatplotLib Pyplot**"""

#Gráfico de Barras para Medalhas de Ouro, Prata e Bronze


top_countries = df.groupby('country').sum().sort_values('total', ascending=False).head(10)
top_countries[['gold', 'silver', 'bronze']].plot(kind='bar', figsize=(10, 6), color=['gold', 'silver', 'brown'])
plt.title('Top 10 Países por Medalhas (Ouro, Prata, Bronze)')
plt.xlabel('País')
plt.ylabel('Número de Medalhas')
plt.show()

#Quadro de medalhas do Brazil
df_brazil = df[(df['country'] == 'Brazil') & (df['year'] >= 2000)]

df_brazil.head()

# Configurar o gráfico
years = df_brazil['year'].unique()
gold_medals = df_brazil.groupby('year')['gold'].sum()
silver_medals = df_brazil.groupby('year')['silver'].sum()
bronze_medals = df_brazil.groupby('year')['bronze'].sum()

bar_width = 0.2  # Largura das barras
index = np.arange(len(years))

# Criar as barras
plt.bar(index, gold_medals, bar_width, label='Ouro', color='gold')
plt.bar(index + bar_width, silver_medals, bar_width, label='Prata', color='silver')
plt.bar(index + 2 * bar_width, bronze_medals, bar_width, label='Bronze', color='brown')

# Configurar os rótulos e título
plt.xlabel('Ano')
plt.ylabel('Número de Medalhas')
plt.title('Número de Medalhas do Brasil (2010 - Presente)')
plt.xticks(index + bar_width, years)
plt.legend()

# Mostrar o gráfico
plt.show()