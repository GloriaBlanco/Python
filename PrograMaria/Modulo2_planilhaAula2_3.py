"""
Nome	    Cor da blusa	Vestimenta	Cor da vestimenta	Nos pés	Altura
Raissa	    Azul	Calça	Azul	Tênis	1,6
Yuri	    Azul	Calça	Azul	Tênis	1,72
Mariana	    Azul	Calça	Azul	Tênis	1,75
Iana	    Azul	Calça	Roxo	Sandália	1,8
Gabriele 	Azul	Calça	Azul	Tênis	1,68
Ester	    Azul	Calça	Azul	Tênis	1,58
Stefani	    Preta	Saia	Preto	Tênis	1,7


Algumas análises
arquivo PlanilhaAula2.3Dados.csv

"""

### tabelas usam dados esttruturados, sao organizados
### nao estruturados sao videos, mudam, redes sociais


### incluir uma coluna quem usa oculos
### incluir uma coluna quem esta usando cinto


# importar bibliotecas
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# carregar dados
df = pd.read_csv('PlanilhaAula2.3Dados.csv')
print(df.head()) # mostrar as primeiras linhas do arquivo

# tamanho do arquivo
print(df.shape)
print("____________________________________________________________________")
# verifica nulos
print(df.isnull().sum())
print("____________________________________________________________________")
print(df.isnull().any())      # Verifica se há algum valor nulo em cada coluna (True/False)
print("____________________________________________________________________")
print(df.isnull().sum().sum()) # Conta o número total de valores nulos no DataFrame
print("____________________________________________________________________")

# descriçao completo
print(df.describe())            # Estatísticas para colunas numéricas
print("____________________________________________________________________")

print(df.describe(include='all')) # Estatísticas para todas as colunas (incluindo objetos)
print("____________________________________________________________________")

print(df.describe(include=['object'])) # Estatísticas apenas para colunas de tipo objeto
print("____________________________________________________________________")

# quero os minimos e maximos
print(df[['Altura']].min())
print("____________________________________________________________________")

print(df[['Altura']].max())
print("____________________________________________________________________")

# informacoes gerais do dataframe
print(df.info())
print("____________________________________________________________________")

# informaçoes de types
print(df.dtypes)
print("____________________________________________________________________")

print(df['Vestimenta'])        # Seleciona uma única coluna (como uma Series)
print("____________________________________________________________________")

print(df[['Nome', 'Nos pés']]) # Seleciona múltiplas colunas (como um DataFrame)
print("____________________________________________________________________")

## filtar dados

# quem usa cor da vestimenta preta
print(df.loc[df['Vestimenta'] == 'Preto'])
print("___________  Preto _________________________________________________________")

# quem tem mais de 1,60 Altura
# altura esta como string
print(df.loc[df['Altura'] > '1,60'])
print("_________________altura > 1.6___________________________________________________")
### incluir uma coluna quem usa oculos, essa coluna deve ter sim ou nao, já sei que os nome Yuri e Iana usam oculos os demais nomes nao usam oculos
df['Usa óculos'] = df.apply(lambda row: 'Sim' if row['Nome'] in ['Yuri','Iana']else 'Não', axis=1)
print(df)
print("____________________________________________________________________")

### incluir uma coluna quem usa cinto, essa coluna deve ter sim ou nao, já sei que os nome Iana Gabriele e Ester usam cinto os demais nomes nao usam
df['Usa cinto'] = df.apply(lambda row: 'Sim' if row['Nome'] in ['Iana','Gabriele','Ester'] else 'Não', axis=1)
print(df)
print("____________________________________________________________________")

