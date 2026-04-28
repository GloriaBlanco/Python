#################################################
#### OUTLIERS
import pandas as pd
import numpy as np
# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')

#### anteriormente tratamos os nulos na coluna salario
### se nao tratar os dados o boxplot nao exibe
# pegar os valores salários nulos e susbtituir pela mediana
salariomediana = dados['SALARIO'].median()
print ("-----------------------------------")
##agora usar o loc, pegar tudo que é salario nulo, mostrando a coluna salário
print(dados.loc[(dados['SALARIO'].isnull()),'SALARIO'])
print ("-----------------------------------")
# acima só mostra, agora de uma forma que substitua pela SALARIOMEDIANA
dados.loc[(dados['SALARIO'].isnull()),'SALARIO'] = salariomediana

import matplotlib.pyplot as plt
# boxplot da coluna salario
plt.boxplot(dados['SALARIO'])
plt.show()

# mostram valores de salarios muitos altos, que sao nossos OUTLIERS
# VAMOS calcular o limite superior e inferior com quartis
# 1º quartil (Q1) e 3º quartil (Q3)
Q1 = dados['SALARIO'].quantile(0.25) 
print(" 1 quartil=0.25 :", Q1)
# RESPOSTA 4.751,50
Q3 = dados['SALARIO'].quantile(0.75)
print(" 3 quartil=0.75 :", Q3)
# RESPOSTA 11.794,50
# INTERQUARTIL = IQR, que é q1 menos q3
IQR = Q3 - Q1
print("Interquartil = IQR: ", IQR)
# RESPOSTA 7043,00
# agora o limite superior
limitesuperior = Q3 + (1.5 * IQR)
print("Limite superior: ", limitesuperior)
# RESPOSTA 22359,00
# e limitee inferior
limiteinferior = Q1 - (1.5 * IQR)
print("Limite inferior: ", limiteinferior)
# RESPOSTA -5813,00

######## conclusão ########
## todos os salários acima de 22.359,00 (LIMITESUPERIOR) ESTSO ACIMA DO ESPERADO
## e salarios com limite inferior seria menos(-5813.00) mas nao existe salarário negativo, portanto, vamos considerar Zero(0)

# verificar as faixas salárias
print(dados['FAIXA SALARIAL'].value_counts())
print ("-----------------------------------")
# como temos salários acima dos 22.359,00 não podemos falar que todos acima desse valor sao outliers

################### vamos fazer OUTRO METODO de calculo ########

### outro metodos de calculo, calculando desvio padrao para ver quanto esta distante da média
# entao vamos ver qual a média
media =dados['SALARIO'].mean()
print(media)
print ("-----------------------------------")

desvio=dados['SALARIO'].std()
print(desvio)
print ("-----------------------------------")
#############
# media= 10517.53 e desvio = 18.096,21, então 
#############

######### agora #######
# limite superior, é media x um cert numer de desvio padrao
# temos que analisar  contexto, vamos fazer 3x, já que os OUTLIERS estao MUITO acima
limitesuperior3x = media + (3*desvio)
print(limitesuperior3x)
print ("-----------------------------------")
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

## Aqui vammos ver a coluna de faixa salárial, vendo se o salário discrepante corresponde a faixa salarial
print(dados[dados['SALARIO']>limitesuperior3x]['FAIXA SALARIAL'].value_counts())
print ("-----------------------------------")
# resultado: acima de 40mil tems 19 salários, e de 30 a 40 mil tems 3 salários



################# entre 30 e 40 mil ###############
# vamos fazer a media dos salários entre 30 a 40mil 
mediaentre30e40mil = dados[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']<limitesuperior3x)]['SALARIO'].mean()
print(mediaentre30e40mil)
#RESPOSTA = 39.002,19
print ("-----------------------------------")


# ENTAO A MEDIA dos valores abaixxo do limitesuperior entre 30 e 40 mil = 39mil

# LoCALIZAR os SALÁRIos entre 30 e 40 mil, vao aparecer os 3 salários 
print(dados.loc[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO'])
print ("-----------------------------------")
# agra substituir a media de 30 a 40 mil nesses 3 valores

(dados.loc[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO']) = mediaentre30e40mil

# verificar 
print(dados.loc[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO'])
print ("-----------------------------------")
print(dados[dados['SALARIO']>limitesuperior3x]['FAIXA SALARIAL'].value_counts())
print ("-----------------------------------")

################# acima de 40 mil ###############

# vamos fazer a media dos salários acima de 40mil mas que nao sejam outliers, e substituir os outliers por esse valor
mediaacima40mil = dados[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']<limitesuperior3x)]['SALARIO'].mean()
print(mediaacima40mil)
#RESPOSTA = 53.127,84
print ("-----------------------------------")

# ENTAO A MEDIA dos valores abaixxo do limitesuperior acima de 40 mil = 53.127,84 mil

# LoCALIZAR os SALÁRIos acima de 40 mil, vao aparecer os 19 salários 
print(dados.loc[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO'])
print ("-----------------------------------")

# agora substituir a media de acima de 40 mil nesses 19 valores de salarios
(dados.loc[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO']) = mediaacima40mil

# verificar 
print(dados.loc[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO'])
print ("-----------------------------------")


print(dados[dados['SALARIO']>limitesuperior3x]['FAIXA SALARIAL'].value_counts())
print ("-----------------------------------")

#########################################
# boxplot novamente
plt.boxplot(dados['SALARIO'])
plt.show()
