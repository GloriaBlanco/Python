#📑 Garmin Performance Analytics & Predictive Modeling

###🏃‍♀️ Sobre o Projeto

####Este projeto nasceu do desejo de unir a paixão pela corrida de rua com minha habilidade na organização de dados e Machine Learning. 

####Utilizando dados exportados do meu Garmin, este repositório demonstra um pipeline completo de dados: desde a limpeza de dados brutos - Wrangling - até a predição de performance futura.

###🛠️ Stack Tecnológica

#### Linguagem: Python

#### Bibliotecas de Dados: Pandas, Numpy

#### Visualização: Matplotlib, Seaborn e Power BI / Looker

#### Machine Learning: Scikit-Learn (Regressão Linear / Random Forest)


###📈 Pipeline de Execução

#####0. Importar Bibliotecas

#####1. Carregar o arquivo e visualizar: 
###########. abrir arquivo Garmin Connect, Arquivo com corridas de rua
###########. visualizar os 1ºs registros e os tipos de dados

#####2. Dicionário padrão snake_case
###########. renomear as colunas
    
#####3. ETL-Extract, Transform, Load  | Limpeza de dados | Data Cleaning | Wrangling 
###########. Criação de um novo dataframe apenas com os dados que vou usar = atividades de corridas+corridasemesteira, descartando demais atividades
###########. verificar erros como -- 
###########. remover vírgulas e/ou trocar por vazio ''
###########. converter tipos de texto para números : int, float, datatime.
###########. criar novas colunas com tempo em minutos

#####4. Análise EAD - Exploratory Data Analysis | Análise exploratória
###########. Análise descritiva : médias, desvio padrao, correlação
###########. Tratamento de outliers (erros de leitura de GPS ou frequência cardíaca).
###########. Análise visual: gráficos

#####5.Machine Learning (Predição)
Desenvolvimento de um modelo preditivo para estimar o Tempo Final de Prova (5k, 10k, 21k) baseado no histórico de treinos das últimas 8 semanas.
Métrica de Sucesso: [Ex: Erro Médio Absoluto de X segundos].

#####6.📊 Visualização de Resultados
O projeto conta com um dashboard no Power BI que apresenta:
Visão Executiva de Performance (KM totais, Recordes).
Análise de Desgaste de Equipamento (Tênis).
Predição de Performance em tempo real.
