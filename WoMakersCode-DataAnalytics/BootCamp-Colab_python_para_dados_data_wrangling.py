# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np

df = pd.read_csv("collected research people.csv")

print(df.head())

df = df.drop(columns=['Unnamed: 0'])
print(df.columns)

#substituindo nome das colunas
novas_cols = {'Endereerço': 'Endereço',
              'phone': 'Telefone',
              'anual_income': 'Renda Anual',
              'AAge': 'Idade',
              'n_filhos': 'N Filhos',
              'diariamente_sun blocker': 'Usa protetor solar diariamente',
              'Food_restrictions': 'Restrição alimentar',
              'streaming': 'Streaming'
              }

# Insira aqui seu código
df.rename(columns=novas_cols, inplace=True)
print(df.head())
print(df.columns)

# substituir caracteres espeiais \W** equivale a [^a-zA-Zà-úÀ-Ú0-9_]."""

#print(df.Nome.str.replace('\W', ''))
print(df.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9 ]', '', regex=True))
print(df.Nome)
# sõ muda se atribuir ao df.Nome
#df.Nome=df.Nome.str.replace('\W', '')
# Remover caracteres especiais, mantendo letras, números e espaços
df.Nome=df.Nome.str.replace('[^a-zA-Zà-úÀ-Ú0-9 ]', '',  regex=True)
print(df.Nome)

# coluna telefone baguncada
print(df.Telefone)
#substituir caracteres esquisitos exceto numeros de 0 ate 9 que devem permanecer
print(df.Telefone.str.replace('[^0-9]', '',  regex=True))
# mesmo assim ainda existem numeros de telefones que faltam numeros
# tambem nao vou excluir, espaco, - e ()
df.Telefone = df.Telefone.str.replace('[^0-9() +-]', '*',  regex=True)
print(df.Telefone)

# mesmo assim ainda existem numeros de telefones que faltam numeros
print(df.Telefone.str.contains('[*]', na=False))
df.loc[df.Telefone.str.contains('[*]', na=False), "Telefone"] = np.nan
print(df.Telefone.str.contains('[*]', na=False))
print(df.Telefone)


#"""Cenário 1:
#A empresa Carri Construtora contratou a empresa que você trabalha para encontrar possíveis compradores para o seus novos empreendimentos.
#A empresa quer entender as necessidades dos clientes, e quer informações com:
#*   Quais cliente devemos abordar;
#*   Qual empreendimento nós devemos mostrá-los;
#*   Esse cliente está em busca em investir em um imóvel ou comprar para moradia?
# Se renda anual > 104 = pode participar do Minha casa minha vida

print(df.head())
# vamos fazre drop das colunas que vamos usar
# 1º copiar colunas
df_carri = df.copy()
# 2º dropar colunas
drop_carri  = ['Restrição alimentar',        
       'Streaming', 'Usa protetor solar diariamente',
       'Quantidade de Livros Comprados',
       'Autor Favorito']
# remover colunas e com inplace=True muda no dataframe original
df_carri.drop(columns=drop_carri, inplace=True)
print(df_carri)
# verificar renda 8mil mes x 13 = 104mil
# describe = mostra os tipos de valores que tem no arquivo
# tipo renda minima = 22826 e renda maxima 95433, ou seja
print(df_carri.describe())
# incluir uma coluna "minha casa minha vida" 
df_carri['Minha casa minha vida'] = True

# se Moradia for igua a Quitada e 
#np.where()

#"""Cenário 2: Uma empresa chamada Hillo, é uma empresa que está estudando o mercado e quer encontrar uma parceria com uma empresa de Streeming (netflix, Disney plus etc), mas gostaria de saber quais as empresas dariam o maior retorno de investimento.
#Eles podem fazer análise de machine learning também com esses dados.





#Cenário 3: Uma influenciadora digital de bem estar gostaria de analisar possíveis empreendimentos dentro de diferentes propostas que recebe. Essas propostas podem ser excludentes ou somatórias."""

