"""
Módulo 7
Visualização de Dados
📌Vamos olhar mais um notebook do Kaggle, tentem repetir as análises feitas 
e gerar os gráficos com outros estilos e formatos:
 https://www.kaggle.com/code/educfrio/an-lise-explorat-ria-de-dados/input
Quando chegar aqui, mostre no grupo da turma que concluiu a atividade do 
Faça Você Mesme | Visualização de dados em python ✅
Nosso código será a hashtag: #VisualizaçãoCheck
"""

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import seaborn as sns

# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_csv('municipios_brasileiros.csv')
# print(dados.head())
print(dados.columns)
print ("-----------------------------------")
""" Index(
['codigo_ibge', 'nome_municipio', 'codigo_uf', 
'uf', 'estado', 'capital', 'latitude', 'longitude'],
dtype='object')
"""
print(dados.head())
print('_______________________________________________')

""" 
Tipos de análises que posso fazer com esse arquivo
📌 quantidade de Municipios por estado
"""
qtdeestado = dados.groupby('estado')['nome_municipio'].nunique()
print(qtdeestado)
print('_______________________________________________')

qtdeuf = dados.groupby('uf')['nome_municipio'].nunique()
print(qtdeuf)
print('_______________________________________________')


# grafico PLOT|Matplot
plt.figure(figsize=(8, 6))  
plt.plot(qtdeuf.index, qtdeuf.values, marker='o', linestyle='-')
plt.title('1º - Matplot-Análise qtde de Municípios por Estado')
plt.xlabel('Estado', fontsize=12)
plt.ylabel('Qtde de Cidade')
maisy = [0, 100, 200, 300, 400, 500, 600, 700, 800, 900]
plt.yticks(maisy)
plt.xticks(rotation=45)
plt.tight_layout() # Ajusta o espaçamento para que tudo caiba bem
plt.grid(True)
plt.show()
print('____________________________')


# grafico PLOTLY com LINE
fig = px.line(qtdeuf.reset_index(), x='uf', y='nome_municipio', title='2º - PLOTLY-Quantidade de Municípios por Estado', markers=True)
fig.show()
# obs: se passar cursor no grafico nas bolinhas vai aparecer o valor da média
print('_____________________________')

# grafico dispersão com SCATTER com PLOT|MATPLOT 
# não ficou bom são muitos dados 

# histograma da qtde de municipios por uf, já agrupei qtde de municipios por estado(uf) na variavel qtde
plt.bar(qtdeuf.index, qtdeuf.values, color='lightskyblue', edgecolor='black')
plt.xlabel('Estado')
plt.ylabel('Qtde Municípios')
plt.xticks(rotation=45, ha='right')
plt.title('3º - Histograma da quantidade de Municípios por Estado')
plt.show()


