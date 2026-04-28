# Modulo 3
# Analise arquivo licitacoes.csv

import pandas as pd

# carregar o arquivo licitacoes.csv
dados = pd.read_csv('licitacoes.csv')



# imprimir arquivo
print(dados.head())

# tem 4271 linhas (ultima 4270) e 28 colunas
print(dados.shape)

# ultimas linhas
print(dados.tail())

print(len(dados))

print(dados.columns)

print(dados.info())

# so exibe valores numericos
print(dados.describe()) 

# todas as colunas genero que contenha a palavra nao
print(f"------------------------------")
#print(dados[dados['GENERO'].str.contains("não", na=False)])

# filtrar IDADE > 30
print(f"--------------------------------")
#print(dados[dados['IDADE'] > 30])


# filtrar Situacao Licitaacao = ENCERRADO
print(f"--------------------------------")
print(dados[dados['Situação Licitação'] == 'Encerrado'])

# COMBINAR FILTROS todos GENERO=Feminino e IDADE > 30
print(f"--------------------------------")
#print(dados[(dados['IDADE']>30) & (dados['GENERO'] == 'Feminino')])

# quais dados da coluna COR/RACA/ETNIA
print(f"--------------------------------")
#print(dados['COR/RACA/ETNIA'].unique())

# filtro para quem tem a idade menor que 40 anos
print(f"------------IDADE < 40 ANOS --------------------")
#print(dados[(dados['IDADE']<40)])

# filtro para quem tem cor raça = Amarela
print(f"-------COR/RACA/ETNIA = AMARELA----------------------")
#print(dados[(dados['COR/RACA/ETNIA'] == "Amarela")])

# filtro para quem tem  os 2, a idade menor que 40 anos e  cor raça = Amarela
print(f"---------IDADE < 40 ANOS E COR/RACA/ETNIA = AMARELA ---------")
#print(dados[(dados['IDADE']<40) & (dados['COR/RACA/ETNIA'] == "Amarela")])

    