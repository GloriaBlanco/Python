# Módulo 4
import pandas as pd
import numpy as np
# uma lista para os calculos
listaIdade = [26, 30, 32, 22, 26, 35, 40, 20, 43, 31, 23]
print ("-----------------------------------")
print ("Lista de Idades: ", listaIdade)

# somar as idades
somaIdade = np.sum(listaIdade)
print ("-----------------------------------")
print ("Soma das Idades: ", somaIdade)

# tamanho da lista
qtdeLista = len(listaIdade)
print ("-----------------------------------")
print ("Quantidade de Idades: ", qtdeLista)

# media das idades
mediaIdade = somaIdade / qtdeLista
print ("-----------------------------------")
print ("Média das Idades: ", mediaIdade)

# mediana e o meio da lista idades
listaIdade.sort()
print ("-----------------------------------")
print ("Lista de Idades ordenada: ", listaIdade)
medianalistidade = np.median(listaIdade)
print ("-----------------------------------")
print("Mediana das Idades: ", medianalistidade)

# desvio padrao
desvioPadrao = np.std(listaIdade)
print ("-----------------------------------")
print("Desvio Padrão das Idades: ", desvioPadrao)

# min e max
minIdade = np.min(listaIdade)
print ("-----------------------------------")
print("Idade Mínima: ", minIdade)
maxIdade = np.max(listaIdade)
print ("-----------------------------------")
print("Idade Máxima: ", maxIdade)

#################################################
# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')

# media das idades da planiha
mediaIdade = dados['IDADE'].mean()
print ("-----------------------------------")
print ("Média das Idades da Planilha: ", mediaIdade)

# mediana das idades da planilha
medianaIdade = dados['IDADE'].median()
print ("-----------------------------------")
print("Mediana das Idades da Planilha: ", medianaIdade)

# moda das idades d planilha
modaIdade = dados['IDADE'].mode()[0]
print ("-----------------------------------")
print("Moda das Idades da Planilha: ", modaIdade)

# desvio padrao
desvioPadrao = dados['IDADE'].std()
print ("-----------------------------------")
print("Desvio Padrão das Idades da Planilha: ", desvioPadrao)

# minimo e mximo das idades na planilha
minIdade = dados['IDADE'].min()
print ("-----------------------------------")
print("Idade Mínima da Planilha: ", minIdade)
maxIdade = dados['IDADE'].max()
print ("-----------------------------------")
print("Idade Máxima da Planilha: ", maxIdade)

# media das idade de pessoas genero feminino
mediaIdadeFeminino = dados[dados['GENERO'] == 'Feminino']['IDADE'].mean()
print ("-----------------------------------")
print("Média das Idades de Pessoas do Gênero Feminino: ", mediaIdadeFeminino)

# media das idade de pessoas genero masculino
mediaIdadeMasc = dados[dados['GENERO'] == 'Masculino']['IDADE'].mean()
print ("-----------------------------------")
print("Média das Idades de Pessoas do Gênero Masculino: ", mediaIdadeMasc)

###############################################
# coluna salário 
#################################################
# media dos salários
mediaIdade = dados['SALARIO'].mean()
print ("-----------------------------------")
print ("Média dos Salários: ", mediaIdade)

# mediana do Salário
medianaIdade = dados['SALARIO'].median()
print ("-----------------------------------")
print("Mediana do Salário: ", medianaIdade)

# moda do Salários
modaIdade = dados['SALARIO'].mode()[0]
print ("-----------------------------------")
print("Moda do Salário: ", modaIdade)

# desvio padrao
desvioPadrao = dados['SALARIO'].std()
print ("-----------------------------------")
print("Desvio Padrão do Salário: ", desvioPadrao)

# minimo e mximo do Salários
minIdade = dados['SALARIO'].min()
print ("-----------------------------------")
print("Menores salários ", minIdade)
maxIdade = dados['SALARIO'].max()
print ("-----------------------------------")
print("Maioroes salário ", maxIdade)

# media das idade de pessoas genero feminino
mediaIdadeFeminino = dados[dados['GENERO'] == 'Feminino']['SALARIO'].mean()
print ("-----------------------------------")
print("Média do Salário do Gênero Feminino: ", mediaIdadeFeminino)

# media das idade de pessoas genero masculino
mediaIdadeMasc = dados[dados['GENERO'] == 'Masculino']['SALARIO'].mean()
print ("-----------------------------------")
print("Média do Salário do Gênero Masculino: ", mediaIdadeMasc)
print ("-----------------------------------")
print ("-----------------------------------")

####################################################

######## tratamento de dados #########

####### dados NULOS NaNs  ###
print ("-----------------------------------")
print("Valores nulos ou faltantes")
print(dados.info())

print ("-----------------------------------")

## conferir valores faltantes
# verificar valores faltantes
print(dados.isnull().sum())
print ("-----------------------------------")

# valores categoricos podemos usar a moda 
# susbstituir os vaalores pela media

# coluna genero, verifica quantos NaNs, = os nulos e faltantes
print(dados.groupby('GENERO', dropna=False)["ID"].nunique())
print ("-------------------???????????????????/----------------")

# como aqui neste caso temos a opcao de genero "prefiro nao informar" vamos ccolocarr essa opcao nos NaNs
# e vamos substituir os NaNs pela moda do genero

dados['GENERO']= dados['GENERO'].fillna('Prefiro não informar')
## verificar se mudou
print(dados.groupby('GENERO', dropna=False)["ID"].nunique())
print ("-----------------------------------")

### agora tratamento de valores nulos da IDADE
print(dados.groupby('IDADE', dropna=False)["ID"].nunique())
print ("-----------------------------------")

# Metodo isnull .sum, qtde por cada idade, mostra false (preenchidos) e true (faltantes NaNs)
print(dados['IDADE'].isnull().sum())
print ("-----------------------------------")

# podemos mostras a quantidade de false(preenchidos) e true(NaNs)
print(dados['IDADE'].isnull().value_counts())
print ("-----------------------------------")

# vamos tratar a idade
# vamos ver se aas pessoas preencheram a faixa etária de idade
# vou ter a faixa etaria das pessoas que preencheram NaNs e quantas dessas preencheram a faixa etária
print(dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts())
print ("-----------------------------------")

# todas preencheram a faixa etaria
# agora faremos a media da faixa de idade
#######################
### faixa etaria = de 17-21 anos
media1721=dados[dados['FAIXA IDADE']=='17-21']['IDADE'].mean()
print("Media faixa etária de 17-21:", media1721)
print ("-----------------------------------")

# MÉDIA DEU 20,20
# agora vamoslocalizar com filtro das linhas de faixa etaria entre 17-21 e idade estej vazia=NaNs
# O LOC SÓ LOCALIZA 
print(dados.loc[(dados['FAIXA IDADE']=='17-21') & (dados['IDADE'].isnull()),'IDADE'])
print ("-----------------------------------")

# AGORA VAMOS SUSBSTITUIR esses que foram encontrados com a media da faixa idade de 17-21
dados.loc[(dados['FAIXA IDADE']=='17-21') & (dados['IDADE'].isnull()),'IDADE'] = media1721
# vamos CONFERIR
print(dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts())
print ("-----------------------------------")

print ("-----------------------------------")

######################3
## agora para faixa de idade +55
media55=dados[dados['FAIXA IDADE']=='55+']['IDADE'].mean()
print("Media faixa etária 55+ :", media55)
print ("-----------------------------------")

## deu resultado nan 
## vamos visualizar o que tem sem o mean()
print(dados[dados['FAIXA IDADE']=='55+']['IDADE'])
# vimos que NENHUMA da faixa 55+ marcou idade, entao nao consigo fazer media
print ("-----------------------------------")

# vamos ver a coluna de nivel já que a de idade esta vazia
print(dados[dados['FAIXA IDADE']=='55+']['NIVEL'])
# a resposta não deu pra resolver
print ("-----------------------------------")

## vou preencher com a media geral ja que nao consigo ela faixa idade
mediageral = dados['IDADE'].mean()
print("Media geral da idade:", mediageral)
print ("-----------------------------------")

##### media geral foi de 31.15
# agora vamoslocalizar com filtro das linhas de faixa etaria 55+ e idade estej vazia=NaNs
# O LOC SÓ LOCALIZA 
# se no final nao colocar a ,IDADE, vai mostrar todas as colunas
print(dados.loc[(dados['FAIXA IDADE']=='55+') & (dados['IDADE'].isnull()),'IDADE'])
print ("-----------------------------------")

# AGORA VAMOS SUSBSTITUIR esses que foram encontrados com a media da faixa idade de 17-21
dados.loc[(dados['FAIXA IDADE']=='55+') & (dados['IDADE'].isnull()),'IDADE'] = mediageral
# vamos CONFERIR
print ("-----------conferir se aparecem nulos NaNs------------------------")

print(dados[dados['IDADE'].isnull()]['FAIXA IDADE'].value_counts())
print ("-----------------------------------")

##### podemos explorar mais a planilha para encontrar uma outra forma

######### SALÁRIOS #########
print ("-----------------------------------")
# filtras os valores nulos da coluna FIXA SALARIAL

print(dados[dados['SALARIO'].isnull()])
print ("-----------------------------------")
# SAO 577 LINHAS NULAS

# vamos ver essas 577 que nao olocaram salário se colocaram faixa salarial
print(dados[dados['SALARIO'].isnull()]['FAIXA SALARIAL'].value_counts)
print ("-----------------------------------")
# vixi a coluna salários e fixa salarial estao vazias
# entao vamos pegar a mediana, porque para usar a media temos que antes ver se tem algum valor discrepante

# pegar os valores salários nulos e susbtituir pela mediana
salariomediana = dados['SALARIO'].median()
print("Media geral da idade:", salariomediana)
## resultado mediana = 7.625.50
print ("-----------------------------------")
# agora usar o loc, pegar tudo que é salario nulo, mostrando a coluna salário
print(dados.loc[(dados['SALARIO'].isnull()),'SALARIO'])
print ("-----------------------------------")

# acima só mostra, agora de uma forma que substitua pela SALARIOMEDIANA
dados.loc[(dados['SALARIO'].isnull()),'SALARIO'] = salariomediana

# vamos CONFERIR
print ("-----------conferir se ainda aparecem nulos NaNs------------------------")

print(dados[dados['SALARIO'].isnull()]['SALARIO'].value_counts())
print ("-----------------------------------")
import matplotlib.pyplot as plt

plt.boxplot(dados['SALARIO'])
plt.show()






