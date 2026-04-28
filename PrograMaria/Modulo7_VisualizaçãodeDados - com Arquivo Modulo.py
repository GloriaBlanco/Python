"""
Módulo 7
Visualização de Dados
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_csv('analise_dados.csv')
print(dados.columns)
print ("-----------------------------------")
""" 
ID', 'IDADE', 'FAIXA IDADE', 'GENERO', 'COR/RACA/ETNIA',
'PCD', 'EXPERIENCIA_PROFISSIONAL_PREJUDICADA', 'ASPECTOS_PREJUDICADOS',
'VIVE_NO_BRASIL', 'ESTADO ONDE MORA', 'UF ONDE MORA',
'REGIAO ONDE MORA', 'MUDOU DE ESTADO?', 'REGIAO DE ORIGEM',        
'NIVEL DE ENSINO', 'ÁREA DE FORMAÇÃO',
'QUAL SUA SITUAÇÃO ATUAL DE TRABALHO?', 'SETOR',
'NUMERO DE FUNCIONARIOS', 'GESTOR?', 'CARGO COMO GESTOR', 'CARGO ATUAL',
'NIVEL', 'FAIXA SALARIAL',
'QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?',
'QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE TI/ENGENHARIA DE SOFTWARE VOCÊ TEVE ANTES DE COMEÇAR A TRABALHAR NA ÁREA DE DADOS?',
'SALARIO'],
"""
print(dados.head())

print('_______________________________________________')

# grupoo de salarios sexo marculino media
salario_homem = dados.loc[dados['GENERO'] == 'MASCULINO', 'SALARIO'].mean()
print('salário media / homem ', salario_homem)

# quantidade da coluna genero
qtdegenero=(dados['GENERO'].value_counts())
print(qtdegenero)

print('_______________________________________________')

# grafico Matplot
plt.figure()
plt.bar(height=qtdegenero.values, x = qtdegenero.index)
plt.title('Matplot-Análise da quantidade de pessooas por Genero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.show()


print('_______________________________________________')

# grafico Seaborn
plt.figure()
sns.countplot(data=dados, x='GENERO', palette='pastel')
plt.title('Seaborn-Análise da quantidade de pessoas por Genero')
plt.xlabel('Gênero')
plt.ylabel('Contagem')
plt.grid(True) # mostra linhas de grade
plt.show()
