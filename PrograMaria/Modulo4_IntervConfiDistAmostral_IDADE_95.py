#######################################################
#### INTERVALOS DE CONFIANÇA E DISTRIBUIÇAO AMOSTRAL
#######################################################
## COM 95% DE CONFIANÇA --- IDADES
## Criar um palpite com uma amostra
## criar uma margem de erro
## quanto maior o intervalo de confiança mais confiavel sera a estimativa

import pandas as pd
import numpy as np
# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')

#############################################333
# NULOS vamos tratar a idade
# vamos ver se aas pessoas preencheram a faixa etária de idade
# vou ter a faixa etaria das pessoas que preencheram NaNs e quantas dessas preencheram a faixa etária
# todas preencheram a faixa etaria
# agora faremos a media da faixa de idade
#########################
### faixa etaria = de 17-21 anos
media1721=dados[dados['FAIXA IDADE']=='17-21']['IDADE'].mean()
# MÉDIA DEU 20,20
# agora vamoslocalizar com filtro das linhas de faixa etaria entre 17-21 e idade estej vazia=NaNs
# O LOC SÓ LOCALIZA 
# AGORA VAMOS SUSBSTITUIR esses que foram encontrados com a media da faixa idade de 17-21
dados.loc[(dados['FAIXA IDADE']=='17-21') & (dados['IDADE'].isnull()),'IDADE'] = media1721
print ("-----------------------------------")

#########################
## agora para faixa de idade +55
media55=dados[dados['FAIXA IDADE']=='55+']['IDADE'].mean()
## deu resultado nan 
## vamos visualizar o que tem sem o mean()
# vimos que NENHUMA da faixa 55+ marcou idade, entao nao consigo fazer media
# vamos ver a coluna de nivel já que a de idade esta vazia
# a resposta não deu pra resolver
## vou preencher com a media geral ja que nao consigo ela faixa idade
mediageral = dados['IDADE'].mean()
##### media geral foi de 31.15
# agora vamoslocalizar com filtro das linhas de faixa etaria 55+ e idade estej vazia=NaNs
# O LOC SÓ LOCALIZA 
# se no final nao colocar a ,IDADE, vai mostrar todas as colunas
# AGORA VAMOS SUSBSTITUIR esses que foram encontrados com a media da faixa idade de 17-21
dados.loc[(dados['FAIXA IDADE']=='55+') & (dados['IDADE'].isnull()),'IDADE'] = mediageral



###################################################
## AGORA intervalo de confiança 95% com as IDADES
###################################################

# todas as IDADES  que temos
idades =dados['IDADE']
print('Salários .....', idades)
print("-----------------------------------")

#calcular media com numpy funçAo mean
mediaamostral= np.mean(idades)
print('Média amostral: ', mediaamostral)
print("-----------------------------------")

# desvio padrao amostral
desvioamostral = np.std(idades)
print('Desvio Amostral: ', desvioamostral)
print("-----------------------------------")

# nível de confiança
niveldeconfianca = 0.95
tamanhoamostra=len(idades)
print("Tamanho amostra: ",tamanhoamostra)
print("-----------------------------------")

# vamos dividir os idades em varios grupinhos para calcular a media deles
# o erro padrao e a diferença dessa média entre eles
# biblioteca modulo da funçao scipy
from scipy import stats
erropadrao =stats.sem(idades)
print('Erro padrao das idades: ', erropadrao)
print("------s-----------------------------")

#  intervalo de conficança
intervaloconfianca =stats.t.interval(niveldeconfianca, tamanhoamostra-1, loc=mediaamostral, scale=erropadrao)
print('Intervalo de 95% de confiança, das idades :  ', intervaloconfianca)
print("-----------------------------------")


"""
significa que temos 95% de confiança que a media das idades das 
pessoas do arquivo planilha 3 é de 30 até 31 anos, isso na tendencia central

"""







#######################################################


