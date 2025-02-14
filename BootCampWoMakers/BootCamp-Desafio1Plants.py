### Desafio 1
# Código do dataset: plantTraits
# Dicas: plantTraits é um dataset que contém a descrição, por meio de
#        atributos biológicos, de diferentes espécies de plantas;
#        função built-in (nativa da linguagem Python): type()
#        atributo do DataFrame: shape

# 1. Importe o dataset utilizando a seguinte função do pydataset:data(“Código”)
# terminal digital = pip install pydataset
from pydataset import data
import pandas as pd

df_Código= data('plantTraits')

# 2. Imprimir na tela o dataset;
print(df_Código.head()) # dataset
print(df_Código.columns) # colunas
print(df_Código.index) #linhas
print(df_Código)

# 3. Informe o tipo de dados retornado pela função data;
# funcao Data?print(dp.DataFrame(data))
print(df_Código.dtypes)
print(type(df_Código))

# 4. Informe o número de exemplos (linhas) e características (colunas) do dataset.
print(df_Código.shape)
# 136 linhas e 31 colunas
#outra forma
n_linhas = df_Código.shape[0]
n_colunas = df_Código.shape[1]

print(f"O dataset contém {n_linhas} exemplos (linhas) e {n_colunas} características (colunas).")


# 5. Crie uma função que ao receber um DataFrame retorna o número de linhas e colunas.

def funcao_return(df_Código):
    lin = len(df_Código.index)
    col = len(df_Código.columns)
    
    return lin,col

print(funcao_return(df_Código))
# ou outra forma imprimir
linhas, colunas = funcao_return(df_Código)
print(f"o DataFrame tem {linhas} linhas e {colunas} colunas")