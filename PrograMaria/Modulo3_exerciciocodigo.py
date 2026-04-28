# Módulo 3 
## Exercício  Código , arquivo excel planilha_modulo3.xlsx

import pandas as pd

# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')

# imprimir arquivo
print(dados.head())

# tem 4271 linhas (ultima 4270) e 28 colunas
print(dados.shape)

# ultimas linhas
print(dados.tail())

print(len(dados))

print(dados.columns)

print(dados.info())

# so exibe valores numericos
print(dados.describe()) 


