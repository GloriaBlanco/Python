#####################################
#### Módulo 5 
#### DESAFIO 
###################################
"""
Criar uma nova coluna de etnia : branca, nao-branca e outras
"""

import pandas as pd
import numpy as np

#################################################
# carregar o arquivo 
dados = pd.read_csv('planilha_modulo2.xlsx-Sheet1.csv')
# carregar o arquivo .csv
#dados2 = pd.read_csv('planilha_modulo5_parte2.xlsx.csv')

# mostrar dados gerais do arquivo
print(dados.head())
print ("-----------------------------------")
# mostrar dados gerais do arquivo 2
#print(dados2.head())
print ("-----------------------------------")

################# MERGE #######################
""" 
juntar as 2 colunas atraves de um DADO EM COMUM
neste caso o , como escolher o que vou juntar
mantenho a tabela dados, e escolho o dado em comum e 
como quer "MERGEAR'" quais dados voce quer
escolhemos so os dados da esquerda da tabela dados2

"""
#dados =dados.merge(dados2, on="ID", how='left')
print(dados.head())
print ("-----------------------------------")
print(dados.columns)
print ("-----------------------------------")
print(dados['COR/RACA/ETNIA'].value_counts())
# resultado  Branca=2744, Parda=1054, Preta=291, Amarela=128, nao inf=26, outra=17, indige=11
print ("-----------------------------------")

"""
Nova coluna ETNIA
COR/RACA/ETNIA  : Branca = Branca,  NaoBranca=Parda, Preta, Amarela, Indígena e 
Outra=Outra e Prefiro não informar = não informado
"""

def etnia(etnia):
    if etnia == "Branca":
        return "Branca"
    elif etnia == "Outra":
        return "Outra"
    elif etnia == "Prefiro não informar":
        return "Não informou"
    else:
        return "Não é Branca"
    
print ("--------------NOVA COLUNA ETNIA ---------------------")
# aplicar funçao
# nao preciso usar o lambda porque só um parametro
dados['ETNIA'] = dados['COR/RACA/ETNIA'].apply(etnia)
print(dados['ETNIA'].value_counts())
print ("-----------------------------------")
# RESULTADO Branca= 2744, Outra=17, Nao informou=26, NãoBranca=1484
# resultado  Branca=2744, Parda=1054, Preta=291, Amarela=128, nao inf=26, outra=17, indige=11

