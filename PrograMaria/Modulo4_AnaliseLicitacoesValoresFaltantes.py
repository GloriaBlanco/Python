# Módulo 4
# anallise de valores faltantes no arquivo Licitacoes.csv
"""
> Identifique qual coluna possui valores faltantes

> Identifique o tipo de dados desta coluna

> Substitua os valores faltantes pelo mesmo formato 

*com a possibilidade de substituir por datas inexistentes.

"""
import pandas as pd
import numpy as np

#################################################
# carregar o arquivo 
dados = pd.read_csv('licitacoes.csv')

# mostrar dados gerais do arquivo
print(dados.head())
print ("-----------------------------------")
print(dados.info())
print ("-----------------------------------")
print(dados.describe())
print ("-----------------------------------")
print(dados.dtypes)
print ("-----------------------------------")
# verificar valores faltantes
print(dados.isnull().sum())
print ("-----------------------------------")
# mostra a quantidade de false(preenchidos) e true(NaNs)
print(dados['Data Abertura'].isnull().value_counts())
print ("-----------------------------------")

### valores faltantes sao 10648 na coluna Data Abertura
## no arq geral sao 15336 linhas e 17 colunas
## coluna Data Abertura é tipoo object
## VOU SUBSTITUIR pela moda da coluna data de abertura, data que mais se repete
modadata=dados['Data Abertura'].mode()
print(modadata)
print ("-----------------------------------")

# a data dee abertura que mais aparece (moda) é 04/12/2018

# agora vou substituir os valores faltantes pela moda da coluna Data Abertura
dados['Data Abertura']= dados['Data Abertura'].fillna('04/12/2018')
## verificar se mudou  CONFERENCIA
# mostra a quantidade de false(preenchidos) e true(NaNs)
print(dados['Data Abertura'].isnull().value_counts())
print ("-----------------------------------")
# verificar valores faltantes
print(dados.isnull().sum())
print ("-----------------------------------")


