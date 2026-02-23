#####################################
#### Módulo 5 parte2
###################################
## Featuring enginnering
## prepaara os dados para Machine Learning
####################################

import pandas as pd
import numpy as np

#################################################
# carregar o arquivo 
dados = pd.read_csv('planilha_modulo2.xlsx-Sheet1.csv')
# carregar o arquivo .csv
dados2 = pd.read_csv('planilha_modulo5_parte2.xlsx.csv')

# mostrar dados gerais do arquivo
print(dados.head())
print ("-----------------------------------")
# mostrar dados gerais do arquivo 2
print(dados2.head())
print ("-----------------------------------")

###### MERGE #######################
""" 
juntar as 2 colunas atraves de um DADO EM COMUM
neste caso o ID
como escolher o que vou juntar
mantenho a tabela dados, e escolho o dado em comum e 
como quer "MERGEAR'" quais dados voce quer
escolhemos so os dados da esquerda da tabela dados2

"""
dados =dados.merge(dados2, on="ID", how='left')
print(dados.head())
print ("-----------------------------------")
print(dados.columns)
print ("-----------------------------------")
print(dados.value_counts())
print ("-----------------------------------")

### em busca = em busca
print(dados['Você pretende mudar de emprego nos próximos 6 meses?'].value_counts())
print ("-----------------------------------")
dados['EM-BUSCA']= dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains("em busca", case=False)
print(dados["EM-BUSCA"].value_counts())
print ("-----------------------------------")
# resultado TRUE= 1364 E FALSE 2332

### aberto a oportunidades = aberto
dados['ABERTOOPORTUNIDADES']= dados['Você pretende mudar de emprego nos próximos 6 meses?'].str.contains("aberto", case=False)
print(dados["ABERTOOPORTUNIDADES"].value_counts())
print ("-----------------------------------")
# resultado TRUE= 1354 E FALSE 2342


