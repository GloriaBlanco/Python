"""
Módulo 7
Visualização de Dados
Analise salário por idade
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_csv('analisededados.csv')
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

# qual tipo de dados tem em salarios
print(dados['SALARIO'].dtype)
# grupoo de salarios sexo marculino media
salario_homem = dados.loc[dados['GENERO'] == 'Masculino', 'SALARIO'].mean()
print('salário media / homem ', salario_homem)

# grupo de salarios por idade, media
salario_idade = dados.groupby('IDADE')['SALARIO'].mean()
print(salario_idade)
print('_______________________________________________')


# grafico PLOT|Matplot
"""
1o. rotulo eixo do X, o .index e p/ pegar os possiveis categorias de idades que vao aparecer
2o. eixo Y .values sao preenchidos com os valores exatamente da media salarios para cada idade
o mmarker vai marcar com circulo cada media das idades
linestyle é o tipo da linha que e continua
"""
plt.plot(salario_idade.index, salario_idade.values, marker='o', linestyle='--')
plt.title('1º - Matplot-Análise da média de Salários por Idade')
plt.xlabel('Idade')
plt.ylabel('Media de salários')
plt.grid(True)
plt.show()
print('_______________________________________________')


# grafico PLOTLY com LINE
"""
Este tipo coloca tudo numa linha só
1o. a media de salario por idade
2o. rotulo eixo do X, o reset_index coluna IDADE
3o. eixo Y coluna SALÁRIOS
o mmarker vai marcar com circulo cada media das idades
linestyle é o tipo da linha que e continua
"""
fig = px.line(salario_idade.reset_index(), x='IDADE', y='SALARIO', title='2º - PLOTLY-Análise da média de Salários por Idade', markers=True)
fig.show()
# obs: se passar cursor no grafico nas bolinhas vai aparecer o valor da média
print('_______________________________________________')

# grafico dispersão com SCATTER com PLOT|MATPLOT 
"""
1o. eixo X coluna IDADE
2o. eixo Y coluna SALÁRIO
3o. parametro alpha=transparencia dos pontinhos grafico quanto
+ perto 0 mais transparente e + perto de 1 mais visivel
"""
plt.figure(figsize=(15,5))
# plt.figure = sem definir tamanho
plt.scatter(dados['IDADE'], dados['SALARIO'], alpha=0.5)
plt.title('3º - Dispersão com SCATTER Matplot- Análise de Salários por Idade')
plt.xlabel('Idade')
plt.ylabel('Salário')
plt.grid(True)
plt.show()

# grafico dispersão com SCATTER com PLOTLY
"""
Este tipo coloca tudo numa linha só
1o. a media de salario por idade
2o. rotulo eixo do X, o reset_index coluna IDADE
3o. eixo Y coluna SALÁRIOS
o mmarker vai marcar com circulo cada media das idades
linestyle é o tipo da linha que e continua
"""
#fig = px.scatter(salario_idade.reset_index(), x='IDADE', y='SALARIO', title='4º - Dispersao com PLOTLY-Análise da média de Salários por Idade')
#fig.show()
# obs: se passar cursor no grafico nas bolinhas vai aparecer o valor da média
# quanto menos disperso@ padrão e maior quantidade de dados/bolinhas
print('_______________________________________________')

# grafico dispersão SCATTER com PLOTLY com as colunas do arquivo
"""
Este tipo coloca tudo numa linha só
1o. arquivo
2o. rotulo eixo do X, o reset_index coluna IDADE
3o. eixo Y coluna SALÁRIOS
o mmarker vai marcar com circulo cada media das idades
linestyle é o tipo da linha que e continua
"""
fig = px.scatter(dados, x='IDADE', y='SALARIO', title='5º - Dispersao com PLOTLY-Análise Dados de Salários por Idade')
fig.show()
# obs: se passar cursor no grafico nas bolinhas vai aparecer o valor da média
# quanto menos dispers padrão e maior quantidade de dados/bolinhas
print('_______________________________________________')

#########################
# para esta análise o grafico de linha e o quem melhor visualização
#########################