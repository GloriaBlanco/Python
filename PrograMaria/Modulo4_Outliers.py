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

# media com numpy
mediaIdadeNumpy = np.mean(listaIdade)
print ("-----------------------------------")
print("Média das Idades com Numpy: ", mediaIdadeNumpy)


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

### valores discrepantes OUTLIERS


# media das idades
# media com numpy
mediaIdadeNumpy = np.mean(listaIdade)
print ("-----------------------------------")
print("Média das Idades com Numpy: ", mediaIdadeNumpy)
# RESPOSTA 29,81

# ALTEREI a idade de 40 para 400
# # assim ficou um valor discrepante
# agora media das idades
listaIdade = [26, 30, 32, 22, 26, 35, 400, 20, 43, 31, 23]
print ("-----------------------------------")
# media com numpy
mediaIdade = np.mean(listaIdade)
print ("-----------------------------------")
print("Média das Idades: ", mediaIdade)
# RESPOSTA 62,54

##### este 400 é um valor discrepante OUTLIER

# vamos identificar os outliers
# calculando o desvio padrao, quanto mais próximo de Zero melhores sao nossos dados

# desvio padrao
desvioPadrao = np.std(listaIdade)
print ("-----------------------------------")
print("Desvio Padrão das Idades: ", desvioPadrao)
# RESPOSTA 106,89, MUITO alto

# vamos conferir, qual o maior valor, pela (média+3 vezes o desvio padrao)
mediaIdade = mediaIdade + 3*desvioPadrao
print ("-----------------------------------")
print("Média das Idades cm 3x desvio padrão: ", mediaIdade)
# RESPOSTA 383,23

# vamos conferir, qual a menor valor,  pela (média+3 vezes o desvio padrao)
# calcular novamente a mediaIdade
mediaIdade = np.mean(listaIdade)
# RESPOSTA 62,54
mediaIdade = mediaIdade - 3*desvioPadrao
print ("-----------------------------------")
print("Média das Idades cm 3x desvio padrão: ", mediaIdade)
# RESPOSTA -258,14

# vamos verificar o que esta acontecendo
# vamos dividir em Quartis
# vamos visualizar os dados, quartis, com boxplot
import matplotlib.pyplot as plt
plt.boxplot(listaIdade)
plt.show()

######################################












