"""
Salvando arquivo excel alterado em arquivo.csv
"""

import sqlite3
import pandas as pd

# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')
print(dados.columns)
print ("-----------------------------------")

###### TRATAMENTO SALÁRIO ####################3
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

###### TRATAMENTO SALÁRIO ####################
##############################################
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

################################
print(dados.head())

print('_______________________________________________')
arquivoCSV = 'analisededados.csv'
dados.to_csv(arquivoCSV, index=False, encoding='utf-8')

# carregar o arquivo analisededados.csv
dados = pd.read_csv('analise_dados.csv')
print ("-----------------------------------")
print(dados.head())
print('_______________________________________________')
# grupoo de salarios sexo marculino media
salario_homem = dados.loc[dados['GENERO'] == 'Masculino', 'SALARIO'].mean()
print('salário media / homem ', salario_homem)

