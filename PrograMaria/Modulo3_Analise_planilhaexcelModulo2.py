# Modulo 3
# Analise da Planilha excel Modulo2
# já transfomei arquivo em .csv = Copia_planilha_modulo2.xlsx-Sheet1.csv
import pandas as pd

# carregar o arquivo .csv
dados = pd.read_csv('planilha_modulo2.xlsx-Sheet1.csv')


# imprimir arquivo
print(dados.head())

# tem 4271 linhas 26 colunas
print(dados.shape)

# ultimas linhas
print(dados.tail())

print(len(dados))

print(dados.columns)

print(dados.info())

# so exibe valores numericos
print(dados.describe()) 

# coluna genero
print(dados['GENERO'])

# conta numero de valores unicos da coluna GENERO
print(dados['GENERO'].nunique())
print(dados['GENERO'].unique())
print(f"-----------------------------")

# filtrar IDADE > 18
print(dados[dados['IDADE'] > 18])
print(f"--------------------------------")


# agrupar por estado e morador id
print(dados.groupby('ESTADO ONDE MORA')['ID'].count())
print(f"--------------------------------")

# quantidade por estado
print(dados['ESTADO ONDE MORA'].value_counts())
print(f"--------------------------------")

