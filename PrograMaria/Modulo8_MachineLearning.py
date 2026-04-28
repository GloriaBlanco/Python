# Modulo 8
# Machine learning
# Planilha analise_dados_mod7
###############################

import pandas as pd

# carregar o arquivo .excel
dados = pd.read_excel('analise_dados_mod7.xlsx')

# imprimir arquivo
print(dados.head())

print(dados.shape)
# tem 4271 linhas 46 colunas
print(len(dados))
# qtde 4271
print(dados.columns)
# 46 coolunas
print(dados.info())

# filtrar empregado = CLT
clt = dados[dados['QUAL SUA SITUAÇÃO ATUAL DE TRABALHO?'] == 'Empregado (CLT)']
print(clt.value_counts())
# resultado = 2762
print('________________________________________________')

print(dados['COR/RACA/ETNIA'].unique()) # mostra lista com os dados da coluna
qtdeetnia = dados['COR/RACA/ETNIA']
print(qtdeetnia.value_counts()) 
# resultado= branca = 1805 professora e 2744 meu .csv
# filtrar cor/raça/etnia = branca
branca = dados[dados['COR/RACA/ETNIA'] == 'Branca']
print(branca.value_counts())
lista_retirar = ['Prefiro não informar', 'Outra', 'Indígena']
# ISIN retira da lista, mas o ~(tio) faz o contrário, mantém o que está na lista
dados = dados[~dados['COR/RACA/ETNIA'].isin(lista_retirar)]
# agora criação de uma coluna oonde não branca recebe o valor 1 e se for branca recebe valor 0
dados['NAO_BRANCA'] = dados['COR/RACA/ETNIA'].apply(lambda x: 1 if x!= "Branca" else 0)
print(dados['NAO_BRANCA'].unique)
# resultado não branca = 4217
print('________________________________________________')


qtdeTempo= dados['QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?'].value_counts()
print(qtdeTempo)
# cria uma nova coluna 'TEMPO DE EXPERIENCIA' e extrai os strings, e só pega os 1os numeros da sequencia até um string ou vazio
# tipo se for 10 ele ve o 1 depois o 0 e armazena o 10 e na sequencia para 
dados['TEMPO_EXPERIENCIA']= dados['QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?'].str.extract(r'(\d+)')
print(dados['TEMPO_EXPERIENCIA'].unique())
# tirar os NAN do tempo de experiência
dados['TEMPO_EXPERIENCIA']= dados['TEMPO_EXPERIENCIA'].fillna(0)
print(dados['TEMPO_EXPERIENCIA'].unique())
print(dados['TEMPO_EXPERIENCIA'].dtype) 
# transformar NUMERO DE FUNCIONARIOS  em int
dados['TEMPO_EXPERIENCIA'] = dados['TEMPO_EXPERIENCIA'].astype (int)
print(dados['TEMPO_EXPERIENCIA'].unique())
print(dados['TEMPO_EXPERIENCIA'].dtype) 
print('_______________TEMPO_EXPERIENCIA_________________________')

# coluna NUMERO DE FUNCIONARIOS
# substituindo o . (ponto) por nada, para o valor ficar sem o .
dados['NUMERO DE FUNCIONARIOS'] = dados['NUMERO DE FUNCIONARIOS'].str.replace('.','')
# só armazeno o valor que for numerico, pego 1o. numero e continuo enqaunto for numero até um string
dados['NUMERO DE FUNCIONARIOS'] = dados['NUMERO DE FUNCIONARIOS'].str.extract(r'(\d+)')
# tirar os NAN do tempo de experiência
dados['NUMERO DE FUNCIONARIOS']= dados['NUMERO DE FUNCIONARIOS'].fillna(0)
print(dados['NUMERO DE FUNCIONARIOS'].unique())
print(dados['NUMERO DE FUNCIONARIOS'].dtype)
# transformar NUMERO DE FUNCIONARIOS  em int
dados['NUMERO DE FUNCIONARIOS'] = dados['NUMERO DE FUNCIONARIOS'].astype (int)
print(dados['NUMERO DE FUNCIONARIOS'].unique())
print(dados['NUMERO DE FUNCIONARIOS'].dtype) 
print('__________________NUMERO DE FUNCIONARIOS_______________________')

# coluna IDADE
print("Tipo de dados da coluna 'IDADE' antes da conversão:", dados['IDADE'].dtype)
# convertes a coluna 'IDADE' para string
dados['IDADEinteira'] = dados['IDADE'].astype(str)
# Use a função str.split('.') para separar a parte inteira da decimal
dados['IDADEinteira'] = dados['IDADEinteira'].str.split('.').str[0]
# Converta a parte inteira (que agora está como string) para um tipo inteiro numérico
# Use pd.to_numeric com errors='coerce' para lidar com possíveis erros de conversão
dados['IDADE'] = pd.to_numeric(dados['IDADEinteira'], errors='coerce').astype('Int64')
# Remova as colunas intermediárias (opcional)
#dados = dados.drop(columns=['IDADE_STR', 'IDADE_INTEIRA_STR'], errors='ignore')
print(dados[['IDADE']].head())
# transformar esta cooluna idade em numerica

print(dados['IDADE'].value_counts())
print((dados['IDADE'] < 0).any())
print('________________________________________________')

# coluna GENERO
# Exibir dados coluna genero
print(dados['GENERO'].value_counts())
# agora criação de uma coluna oonde não branca recebe o valor 1 e se for branca recebe valor 0
#dados['NAO_BRANCA'] = dados['COR/RACA/ETNIA'].apply(lambda x: 1 if x!= "Branca" else 0)
#print(dados['NAO_BRANCA'].unique)
# resultado não branca = 4217
print('_____________________________________________')



# criar a coluna nova INSATISFAÇAO
dados['INSATISFACAO']=0
print(dados['INSATISFACAO'].unique())
# localizando todos os dados nao nulos e filtrando, nome da coluna, se a coluna "qual o principal motivo da sua insatisfaçao com a empresa atua?" tiver palavra salario ele preenche com 1 e se nao tiver preenche com 0
dados.loc[dados['Qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(), 'INSATISFACAO'] = dados.loc[dados['Qual o principal motivo da sua insatisfação com a empresa atual?'].notnull(),'Qual o principal motivo da sua insatisfação com a empresa atual?'].apply(lambda x: 1 if 'Salário' in x else 0)
print(dados['INSATISFACAO'].unique())
print(dados['INSATISFACAO'].value_counts())
# resultado professora 0=2453 e 1=279 e meu 0=3848 e 1=369
print('________________________________________________')
    
# alterar os dados da coluna chamada nivel de ensino para numerica
print(dados['NIVEL DE ENSINO'].value_counts())
dados['NIVEL DE ENSINO'] = dados['NIVEL DE ENSINO'].apply(lambda x: 0 if x== 'Não tenho graduação formal' else 1 if x== 'Estudante de Graduação' else 2 if x== 'Gradução/Bacharelado' else 3 if x== 'Pós-graduação' else 4 if x== 'Mestrado' else 5 if x== 'Doutorado ou Phd' else -1)
print(dados['NIVEL DE ENSINO'].value_counts())
# resultado professora 0=2453 e 1=279 e meu 0=3848 e 1=369
print('________________________________________________')

#####################SEPARAR  X e y em TRAIN e TEST ####################################
# agora vamos selecionar as colunas para o MODELO
dados = dados[['IDADE', 'GENERO', 'NAO_BRANCA', 'TEMPO_EXPERIENCIA', 'INSATISFACAO','SETOR', 'REGIAO ONDE MORA', 'NIVEL DE ENSINO', 'NUMERO DE FUNCIONARIOS', 'SALARIO', 'NOVO_NIVEL']]
print(dados.head()) 

# usando get_dummies, porque essas variaveis sao string, e drop_first tirar a 1a. coluna
# resultado tabela com dados true ou false
dados = pd.get_dummies(dados, columns=['GENERO', 'SETOR', 'NOVO_NIVEL', 'REGIAO ONDE MORA'], drop_first=True)
# imprimir todos os tipos que existem em todas as colunnas
print(dados.dtypes)
print(dados.head()) 

# separar o conjunto de dados em 2 = 1 em treino e 1 em teste  
# lembrando que o objetivo| target é o salário
# no X eu tiro o target                          
X = dados.drop('SALARIO', axis=1)
# só nosso target
y =dados['SALARIO']

# fazer o conjuntos de treino e teste, importar a biblioteca da funçao de train|test
# 1o. o atributos e depois o target
# separar test em 20% e 80% para oo de treinamento, e o random_state=42 para sempre obter o mesmo resultado
from sklearn.model_selection import train_test_split
# 2 conjuntos para test e 2 conjuntos para treinamento|target
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.2, random_state=42)

# biblioteca para padronizar as caracteristicas, normalizando nossos dados, criando uma escala uniforme
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
# atributos da parte de treino normalizados na variavel X_train_scaled
X_train_scaled = scaler.fit_transform(X_train)
# atributos da parte de test normalizados na variavel y_test_scaled
X_test_scaled = scaler.transform(X_test)

################# treinar o modelo #################
# carregar a biblioteca para criar o modelo
from sklearn.linear_model import LinearRegression
model = LinearRegression()
# treinar o modelo com os dados de treino
model.fit(X_train_scaled, y_train)
# imprimir o model.fit
print('____________X_train e y_train _________________')
print(model.fit(X_train_scaled, y_train))
print('_______________________________________________')

# agora fazer as prediçoes do nosso conjunto de teste utilizando a funçao predict
y_pred = model.predict(X_test_scaled)


# 2 métricas comuns para avalição do modelo de regressão sao, 
# 1a.) mettrica é o E2 médio (e quadrático médio) = MSE onde calculo a media de diferença entre o valor predito e o valor real, e a diferença é elevada ao quadrado, dessa maneira penaliza valores que sejam muito diferentes entre o valor previstoo e o valor real.
# 2a.) a segunda métrica é o R2 (coeficiente de determinação) é uma medida estatistica de quao proximos os dados estao da linha de regressao/da reta. A definiçao do R2 é a porcentagem da variação da variavel resposta que é explicado por um modelo linear OU R2 é igual a variaçao explicada dividido pela variaçao total. O R2 está sempre entre 0% e 100%. 
# O 0% indica que o modelo não explica nada da variabilidade dos dados de respoosta ao redoor da sua média
# O 100% indica que o modelo explica toda a variabilidade dos dados de resposta ao redor da sua média
# após treinar o modelo de machine learning vou avaliar seu desemprenhoo para entender o quao bem ele esta fazendo previsoes
# biblioteca para avaliar o modelo
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error

# 1a.) métrica o MSE = o erroo quadrático médioo, para avaliar o modelo com o conjunto de teste
# vai calcular o erro quadratico médio=MSE dos valores reais=y_test e os valores preditos=y_pred
# quanto menor o valor do MSE mais precisa é a predição do modelo
# idela é um valor baixo
mse = mean_squared_error(y_test, y_pred)
print(' _______MSE =',mse,'___________')
# resultado ABSURDAMENTE ALTO, indicando que o modelo não está com predicao precisa


# outra opcao da 1a.) metrica,  entao em vez do mse vamos calcular o MAE, metria que é o erro obsoluto, o erro medio absoluto, qual calcula a media da diferença absoluta, ou seja, nao vamos elevar ao quadrado coomo a MSE
# vai calcular a diferença entre os valores reais=y_test e os valores preditos=y_pred, sem elevar ao quadrado
mae = mean_absolute_error(y_test, y_pred)
print(' _______MAE =',mae,'___________')

# 2a.) metrica, calcular o R2
r2 = r2_score(y_test, y_pred)
print(' ________R2 =',r2,'____________')

# IDEAL É analisar com as 3 métricas em conjunto
# para conclusao vamos plotar gráficos dos valores reais e os valores preditos

# plotar os gráficos dos valores reais versus os valores preditos pelo modelo
import matplotlib.pyplot as plt
plt.figure(figsize=(8,4))
plt.scatter(y_test, y_pred, alpha=0.5) # grafico dispersão, alpha=transparencia dos poontos
plt.xlabel('Valores Real') # bolinhas azuis
plt.ylabel('Valores Preditos') # linha vermelha
plt.title('Dispersão do dados - valores reais X valores preditos')
plt.plot([min(y_test), max(y_test)], [min(y_test), max(y_test)], color='red', linewidth=2) # linewidth=espessura da linha
plt.show()

# analisar quais atributos tiveram mais peso positivo ou negativo para o resultado do modelo
# em moodelode de regressao temos que compreender os coeficientes e ver quais tem mais significativa 
# nome das colunas de atributos e atribuir a uma variável
atributos = X_train.columns
# printar atributos
print('_________Atributos _________ ',atributos)

# Vamos criar um dataframe com o pandas, adicionamos os coeficientes do modelo, 
# indicamos qual o nome dessa coluna que acabamos de criar e qual vai ser o nome 
# das linhas, ou seja, dos index. E vamos armazenar o resultado em uma variável.
coefs = pd.DataFrame(model.coef_, columns=['coeficientes'], index=atributos)
print('_________Coeficientes _________ ',coefs)

# Vamos ordenar essa coluna de coeficientes pra gente conseguir ver melhor o que 
# ta influenciando mais ou menos. Fazemos isso usando a função de sort_values: 
coefs = coefs.sort_values(by='coeficientes', ascending=False)
print('_________Coeficientes ordenados _________ ',coefs)

# Vamos plotar um gráfico de barras horizontal para visualizar melhor e 
# adicionamos uma linha na vertical no ponto 0 para termos como referência
coefs.plot.barh(figsize=(10,7))
# dimunir oo tamanho da letra do grafico
plt.xticks(fontsize=70)
plt.axvline(x=0, color='red')
plt.show()
# neste grafico vemos que todas as barras antes do zero tem um valor negativo, diminuindo o valor do salario
# e todas as barras acima de zero tem um valor positivo, aumentando o valor do salário
# o que mais influencia para o salario ser alto é a pessoa gestora= maior barra positiva
# e assim por diante pelo tamanho das barras
# assim como o que menos influencia são as menores barras = moram regiao sul

"""
################# CONCLUSAO ANALISE #####################
O modelo foi treinado com base nos dados de treinamento e testados com os dados de teste. 
O modelo foi avaliado com base nas métricas MSE, MAE e R2. 
O modelo apresentou um resultado ruim, com um MSE e MAE altos e um R2 baixo. 
Isso indica que o modelo não está fazendo uma boa previsão dos valores. 
Além disso, o gráfico de dispersãodos valores reais versus os valores preditos mostra que o modelo
está fazendo previsões muito ruins. 
O gráfico de barras horizontal dos coeficientes do modelo mostra que os atributos têm um 
peso positivo muito grande no modelo, enquanto os atributos que têm um peso negativo.
Isso indica que os atributos positivos estão influenciando positivamente o modelo, 
enquanto os atributos negativos estão influenciando negativamente o modelo.
"""








