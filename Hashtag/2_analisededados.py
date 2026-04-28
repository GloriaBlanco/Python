"""
# Python Insights - Analisando Dados com Python

### Case - Cancelamento de Clientes

Você foi contratado por uma empresa com mais de 800 mil clientes para um projeto de Dados. Recentemente a empresa percebeu que da sua base total de clientes, a maioria são clientes inativos, ou seja, que já cancelaram o serviço.

Precisando melhorar seus resultados ela quer conseguir entender os principais motivos desses cancelamentos e quais as ações mais eficientes para reduzir esse número.

O código automatiza o tratamento de uma base de dados de clientes, limpando informações inúteis ou incompletas e gerando gráficos para identificar padrões de comportamento. Ele serve para diagnosticar os motivos de cancelamento (churn) e simular como ações estratégicas (como eliminar planos mensais ou melhorar o atendimento) impactariam positivamente na retenção da empresa.
"""

# Passo a passo
# Passo 0: importar e instalar bibliotecas 
# Passo 1: Importar base de dados
# Passo 2: Visualizar base de dados
# Passo 3: Corrigir os erros e nulos da base de dados
# Passo 4: Análise dos cancelamentos
# Passo 5: Análise das causas dos cancelamentos (como as colunas da base impactam no cancelamento)
# Passo 6: Simulação do Cenário ideal, análise what-if, ou seja, filtrar os piores cenários


# Passo a passo do projeto

# Passo 0: Importar todas bibliotecas e instalar caso nao tenha instalado antes
# !pip install pandas numpy openpyxl nbformat ipykernel plotly
# !pip install plotly
# !pip install nbformat --upgrade

import pandas as pd # Importa a biblioteca Pandas para manipulação de tabelas
import plotly.express as px # Importa a biblioteca Plotly para criação de gráficos interativos
import seaborn as sns
import matplotlib.pyplot as plt


# Passo 1: Importar a base de dados
tabela = pd.read_csv("2_cancelamentos.csv") # Carrega o arquivo CSV para dentro de um DataFrame chamado 'tabela'
print(tabela) # Exibe a tabela no console para conferência inicial


# Passo 2: Visualizar a base de dados
tabela = tabela.drop(columns="CustomerID") # Remove a coluna 'CustomerID' que não serve para análise estatística
print(tabela) # Exibe a tabela no console para conferência inicial
# colunas inúteis - informações que não te ajudam, te acompanham


# Passo 3: Corrigir os erros e nulos  da base de dados

# 0. Informaçoes gerais
print("\n--- Info gerais do arquivo --------------------------------------------")
print(tabela.info()) # Exibe informações sobre as colunas e tipos de dados para identificar valores nulos

# 1. Ver apenas os nomes das colunas
print("--- Nomes das Colunas columns --------------------------------------------")
print(tabela.columns)

# 2. Contar a quantidade de cada tipo de dado (int, float, object, etc.)
print("\n--- Contagem de Tipos de Dados dtypes.value_counts() ------------------")
print(tabela.dtypes.value_counts())

# 3. Estatisticas descritivas
print("\n--- Estatísticas Descritivas  describe() ------------------------------")
print(tabela.describe())  # Mostra média, desvio padrão, min e max das colunas numéricas

# 4. Verificação de Dados Faltantes (Soma de nulos por coluna)
print("\n--- Valores Nulos por Coluna isnull().sum()----------------------------")
print(tabela.isnull().sum())

# 5. NaN -- valores vazios - excluir as linhas que têm valores vazios
tabela = tabela.dropna() # Comando que remove todas as linhas que possuem informações faltando (NaN)
print("\n--- Infor após dropna()  -----------------------------------------------")
print(tabela.info()) # Exibe novamente as informações para confirmar que a base está limpa



# Passo 4: Análise inicial dos cancelamentos
# quantas pessoas cancelaram e quantas não cancelaram
print("\n--- Contagem da coluna Cancelou ['cancelou'].value_counts() ----------------------")
print(tabela["cancelou"].value_counts()) # Conta a quantidade total de cada tipo da categoria da coluna = clientes que cancelaram (1) e não (0)

# em percentual, Verificação de Equilíbrio (Quantos % já cancelaram na base original?)
print("\n--- Proporção de Cancelamento (Base Bruta) --------------------------------------")
print(tabela["cancelou"].value_counts(normalize=True)) # Mostra a proporção de cancelamento (ex: 0.20 para 20%)
print(tabela["cancelou"].value_counts(normalize=True).map("{:.1%}".format))
# 1 sim = 28393 = 0.567905 / 56,8%
# 2 nao = 21603 = 0.432095 / 43.2%


# Passo 5: Análise das causas dos cancelamentos (como as colunas da base impactam no cancelamento)
# gráficos/dashboards
# !pip install plotly
# import plotly.express as px # Importa a biblioteca Plotly para criação de gráficos interativos

# GRÁGICOS
# 1. gráfico de Distribuição : entender quem sao os clientes, idade deles 
# Histograma da idade dos clientes para ver a faixa etária principal
fig_idade = px.histogram(tabela, x="idade", title="Distribuição de Idade dos Clientes", nbins=20)
fig_idade.show()

# 2. Gráfico de Distribuição de Idade vinculado a coluna cancelou
# Histograma com o parâmetro color="cancelou" cria a legenda e separa os dados visualmente
fig_idade = px.histogram(tabela, x="idade", color="cancelou", 
                         title="Distribuição de Idade por Status de Cancelamento", 
                         nbins=20)
# Exibe o gráfico
fig_idade.show()

# 3. junta os 2 gráficos acima num só 
# Exibe o gráfico único que já contém as duas informações comparadas
# Gráfico de Distribuição de Idade vinculado a coluna cancelou
# x="idade" define o eixo horizontal
# color="cancelou" separa as cores (quem saiu e quem ficou)
# barmode="group" coloca as barras uma ao lado da outra (em vez de uma em cima da outra)
fig = px.histogram(tabela, 
                   x="idade", 
                   color="cancelou", 
                   title="Comparação: Idade vs Cancelamento",
                   nbins=20,
                   barmode="group") 
fig.show()

# 4. Histograma comparando a coluna cancelou para ver o cancelamento
for coluna in tabela.columns: # Inicia um loop para criar um gráfico para cada coluna da base de dados
    grafico = px.histogram(tabela, x=coluna, color="cancelou", title=f"Comparação: {coluna} vs Cancelamento",) # Cria um histograma comparando a coluna com o cancelamento
    # exibir o grafico
    grafico.show() # Abre o gráfico no navegador ou no ambiente de execução

# 5. Mapa de calor
# Seleciona apenas as colunas que são números
colunas_numericas = tabela.select_dtypes(include=['number'])
correlacao = colunas_numericas.corr()
# Desenha o mapa de calor
sns.heatmap(correlacao, annot=True, cmap="coolwarm")
plt.show()

# 6. Correlação Básica : qual a relaçao entre o tipo/tempo de contrato x dias atraso x Cancelamento
tabela["cancelou"] = tabela["cancelou"].astype(str)
fig_contrato = px.box(tabela, x="duracao_contrato", y="dias_atraso", color="cancelou", 
                     title="Atraso por Tipo de Contrato x dias de atraso x Cancelamento")
fig_contrato.show()



# Passo 6: Simulação do Cenário ideal, análise what-if, ou seja, filtrar os piores cenários
""" 
Estes são os problemas a revolver papra o cenário ideal
. clientes do contrato mensal TODOS cancelam
. ofercer desconto nos planos anuais e trimestrais
. clientes que ligam mais do que 4 vezes para o call center, cancelam
. criar um processo para resolver o problema do cliente em no máximo 3 ligações
. clientes que atrasaram mais de 20 dias, cancelaram
. política de resolver atrasos em até 10 dias (equipe financeira)
"""

print("\n -----------------------------------------------------------")
print("\n--- Aplica o filtro: remove clientes com contrato mensal ---")
tabela = tabela[tabela["duracao_contrato"]!="Monthly"] # Aplica o filtro: remove clientes com contrato mensal
print("\n--- Aplica o filtro: remove clientes com mais de 4 ligações ---")
tabela = tabela[tabela["ligacoes_callcenter"]<=4] # Aplica o filtro: remove clientes com mais de 4 ligações
print("\n--- Aplica o filtro: remove clientes com mais de 20 dias de atraso ---")
tabela = tabela[tabela["dias_atraso"]<=20] # Aplica o filtro: remove clientes com mais de 20 dias de atraso
print("\n--- Os novos números após as correções sugeridas ---")
print(tabela["cancelou"].value_counts()) # Mostra os novos números após as correções sugeridas
# em percentual
print("\n--- Mostra a nova taxa de cancelamento após os filtros ---")
print(tabela["cancelou"].value_counts(normalize=True)) # Mostra a nova taxa de cancelamento após os filtros

# !pip install nbformat --upgrade


