#####################################
#### Módulo 5
###################################
## Featuring enginnering
## prepaara os dados para Machine Learning
##################

import pandas as pd
import numpy as np

#################################################
# carregar o arquivo 

# carregar o arquivo .csv
dados = pd.read_csv('planilha_modulo2.xlsx-Sheet1.csv')

# mostrar dados gerais do arquivo
print(dados.head())
print ("-----------------------------------")
print(dados.info())
print ("-----------------------------------")
print(dados.describe())
print ("-----------------------------------")
print(dados.dtypes)
print ("-----------------------------------")
print(dados.columns)
print ("-----------------------------------")
# verificar valores faltantes
print(dados.isnull().sum())
print ("-----------------------------------")
# mostra a quantidade de false(preenchidos) e true(NaNs)
print(dados['GESTOR?'].isnull().value_counts())
print ("-----------------------------------")
print(dados['NIVEL'].isnull().value_counts())
print ("-----------------------------------")
print(dados['NIVEL'].values)

### TRATAR IDADE ##############
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



#############################
## FEATURING ENGINEERING
## eNGENHARIA DE RECURSOS
#############################
"""
Vamos Criar uma coluna "NOVONIVEL" e criar uma função que 
vai receber os dados da coluna GESTOR e de NIVEL e vai retornar 
se a pessoa é gestora ou se tem o valor de nivel já definido
"""
# Criar funçao
def preenchernivel(gestor,nivel):
    if gestor==1:
        return "Pessoa Gestora"
    else:
        return nivel
# aplicar funçao
dados['NOVONIVEL'] = dados.apply(lambda x: preenchernivel(x['GESTOR?'], x['NIVEL']), axis=1)
print(dados['NOVONIVEL'].value_counts())
print ("-----------------------------------")


####################
## mudar variaveis categoricas em 1 indicador
## vai mostrar colunas no final com true ou false com os tipos de conteudo da coluna
## tipo estas 3 colunas niveljunior, nivelpleno, nivelsenior
print(pd.get_dummies(dados, columns=["NIVEL"]))
# acima so mostra, abaixo eu adiciono a tabela
dados = (pd.get_dummies(dados, columns=["NIVEL"]))
print(dados.columns)

####################
### alterar as variaveis continuas em discretas
###
def determinargeracao(idade):
    if 39 <idade<=58:
        return "GERACAO X"
    elif 29< idade <=39:
        return "MILLENIAL"
    elif 13< idade <=29:
        return "GERAÇAO Z"
    else:
        return "OUTRA GERACAO"
# nao preciso usar o lambda porque só um parametro
dados['GERACAO'] = dados['IDADE'].apply(determinargeracao)
print(dados['GERACAO'].value_counts())
print ("-----------------------------------")
# RESULTADO Z=1999, MILLE=1761, X=511