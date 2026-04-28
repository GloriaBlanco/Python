#######################################################
#### INTERVALOS DE CONFIANÇA E DISTRIBUIÇAO AMOSTRAL
#######################################################
## COM 95% DE CONFIANÇA
## Criar um palpite com uma amostra
## criar uma margem de erro
## quanto maior o intervalo de confiança mais confiavel sera a estimativa

import pandas as pd
import numpy as np
# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')


#### anteriormente tratamos os nulos na coluna salario
# pegar os valores salários nulos e susbtituir pela mediana
salariomediana = dados['SALARIO'].median()
# substitua pela SALARIOMEDIANA
dados.loc[(dados['SALARIO'].isnull()),'SALARIO'] = salariomediana
#################################
### outro metodos de calculo, calculando desvio padrao para ver quanto esta distante da média
# entao vamos ver qual a média
media =dados['SALARIO'].mean()
desvio=dados['SALARIO'].std()
#############
# media= 10517.53 e desvio = 18.096,21, então 
#############
######### agora #######
# limite superior, é media x um cert numer de desvio padrao
# temos que analisar  contexto, vamos fazer 3x, já que os OUTLIERS estao MUITO acima
limitesuperior3x = media + (3*desvio)
# RESPOSTA  64.806,00
######### conclusão ##########
## PELO BOXPLOT analisando esse valor de 64.806,00 podemos ver que sim, então
# É UM VALOR BOM para limite superior, então acima desse valor podemos considerar OUTLIER
# será que os salarios muitos altos foram erro de preenchimento, ou faz sentido esses salários estão OK?
###########################################
## tratando os valores discrepantes
##########################################
## remover, nao é indicado
## podemos substituir como nos NaNs/Faltantes
## ou substituir plos valores máximos
## ou ainda o caso de manter caso ejam necessários
################# entre 30 e 40 mil ###############
# vamos fazer a media dos salários entre 30 a 40mil 
mediaentre30e40mil = dados[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']<limitesuperior3x)]['SALARIO'].mean()
# ENTAO A MEDIA dos valores abaixxo do limitesuperior entre 30 e 40 mil = 39mil
# agra substituir a media de 30 a 40 mil nesses 3 valores
(dados.loc[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO']) = mediaentre30e40mil
################# acima de 40 mil ###############
# vamos fazer a media dos salários acima de 40mil mas que nao sejam outliers, e substituir os outliers por esse valor
mediaacima40mil = dados[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']<limitesuperior3x)]['SALARIO'].mean()
#RESPOSTA = 53.127,84
# ENTAO A MEDIA dos valores abaixxo do limitesuperior acima de 40 mil = 53.127,84 mil
# agora substituir a media de acima de 40 mil nesses 19 valores de salarios
(dados.loc[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO']) = mediaacima40mil

#########################################
## AGORA intervalo de confiança

# todos os salarios que temoos
salarios =dados['SALARIO']
print('Salários .....')
print("-----------------------------------")

#calcular media com numpy funçAo mean
mediaamostral= np.mean(salarios)
print('Média amostral: ', mediaamostral)
print("-----------------------------------")

# desvio padrao amostral
desvioamostral = np.std(salarios)
print('Desvio Amostral: ', desvioamostral)
print("-----------------------------------")

# nível de confiança
niveldeconfianca = 0.95
tamanhoamostra=len(salarios)
print("Tamanho amostra: ",tamanhoamostra)
print("-----------------------------------")

# vamos dividir os salarios em varios grupinhos para calcular a media deles
# o erro padrao e a diferença dessa média entre eles
# biblioteca modulo da funçao scipy
from scipy import stats
erropadrao =stats.sem(salarios)
print('Erro padrao : ', erropadrao)
print("------s-----------------------------")

#  intervalo de conficança
intervaloconfianca =stats.t.interval(niveldeconfianca, tamanhoamostra-1, loc=mediaamostral, scale=erropadrao)
print('Intervalo de confiança 95%:  ', intervaloconfianca)
print("-----------------------------------")


#### significa que temos 95% de confiança que a media salarial das pessoas do Brasil é de 9655,18 até 10.153,59, isso na tendencia central

###








#######################################################


