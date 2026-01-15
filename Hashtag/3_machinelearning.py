"""
# Projeto Python IA: Inteligência Artificial e Previsões

### Case: Score de Crédito dos Clientes

Você foi contratado por um banco para conseguir definir o score de crédito dos clientes. Você precisa analisar todos os clientes do banco e, com base nessa análise, criar um modelo que consiga ler as informações do cliente e dizer automaticamente o score de crédito dele: Ruim, Ok, Bom = Poor, Standard, Good

Resumo do código:
Limpeza e Codificação: Transformamos categorias de texto em números para que os algoritmos matemáticos pudessem processá-las.
Treinamento: Ensinamos dois modelos diferentes a identificar padrões que levam a uma nota de crédito.
Avaliação: Testamos qual modelo era mais preciso.
Predição: Aplicamos o vencedor para dizer qual seria a nota de crédito de clientes que a empresa ainda não conhecia.

Quero prever a coluna Score de Crédito
Passos do código:
0 - Entender o problema a ser resolvido
1 - Importar a base de dados
2 - Preparar a base de dados para a IA/Modelo
3 - Criar o modelo de previsao ou modelo de IA = Ruim, Ok, Boa


"""
# Instala as bibliotecas necessárias: pandas para dados e scikit-learn para Machine Learning
# !pip install pandas scikit-learn

############ Passo 0 - Entender a empresa e o desafio da empresa
""" 
Prever o Score de uma pessoa
Score e a nota dos Bancos para o perfil de pagador de um cliente
"""

############ Passo 1 - Importar a base de dados
import pandas as pd # Importa a biblioteca pandas para manipulação de tabelas

tabela = pd.read_csv("3_clientes.csv") # Lê o arquivo CSV e armazena na variável 'tabela'

print(tabela) # Exibe a tabela na tela 
print("----------------------------------------------------")

# Score de crédito = Nota de crédito
# Good = Boa
# Standard = OK
# Poor = Ruim


##################################################################################
# Passo 2 - Preparar a base de dados para a Inteligência Artificial
###########  PREPARAR O MODELO
print(tabela.info()) # Exibe informações da tabela (colunas, tipos de dados e valores vazios)
print("----------------------------------------------------")

# int -> numero inteiro
# float -> numero com casa decimal
# object -> texto

print(tabela['score_credito'].value_counts())
print("----------------------------------------------------")

# LabelEncoder
from sklearn.preprocessing import LabelEncoder 
# import sklearn === poderia importar tudo mas ue acima escolhi importar apenas o que vou usar que é o LabelEncoder
# Importa a ferramenta que transforma texto em números
""" colunas que sao texto e preciso transformar 
profissao : dentista, bombeiro, engenheiro, marceneiro, pedreiroo, mecânico, etc
        Exemplo de transformação:
        cientista - 1
        bombeiro - 2
        engenheiro - 3
        dentista - 4
        artista - 5
mix_credito
comportamento_pagamento : alto_gasto_pagamento_baixos
a única que vou deixar texto é o cara que voce quer prever "score_credito"
"""

#coluna profissao
codificador_profissao = LabelEncoder() # Cria o objeto codificador para a profissão
# Aplica a transformação na coluna 'profissao' substituindo nomes por números
# o novo valor da cooluna profissao da tabela seja a substituicao do texto para numero atraves do labelEncoder
tabela["profissao"] = codificador_profissao.fit_transform(tabela["profissao"])

# coluna mix_credito
codificador_credito = LabelEncoder() # Cria o objeto codificador para o mix de crédito
# Aplica a transformação na coluna 'mix_credito'
tabela["mix_credito"] = codificador_credito.fit_transform(tabela["mix_credito"])

# coluna comportamento_pagamento
codificador_pagamento = LabelEncoder() # Cria o objeto codificador para o comportamento de pagamento
# Aplica a transformação na coluna 'comportamento_pagamento'
tabela["comportamento_pagamento"] = codificador_pagamento.fit_transform(tabela["comportamento_pagamento"])

# Exibe novamente as informações para conferir se os textos viraram números
print(tabela.info()) 
print("----------------------------------------------------")

# se eu quiser voltar essas colunas para texto
# codificador_mix.inverse_transform

""" 
Agora vamos separar quem vai usar para fazer a separacao e quem ele vai prever
Separo da seguinte forma:
x=todas as colunas menos a coluna que vou prever que será o y
y=quem eu vou prever, coluna "score_credito" que será o y

"""
# y -> é a coluna da base de dados que eu quero prever (meu alvo/target)
y = tabela["score_credito"]

# x -> as demais colunas da base de dados que eu vou usar pra fazer a previsão (minhas características/features)
# Remove a coluna alvo e o ID (que não ajuda a prever) para criar o conjunto de entrada
# ou eu posso colocar todos os nomes das colunas
# x = tabela["idade","mix_credito","comportamento", etc.... ]
# nunca usar a coloca que eu quero prever que é o y
x = tabela.drop(columns=["score_credito", "id_cliente"])


""" 
TREINO e TESTE
vou dividir a bse de dados em 2 pedaços, treino e teste
Treino = ele vai treinar com todos os dados reais que ele tem
Depois dele aprender eu dou dados que ja sei a resposta para ver se ele acerta
teste = outros dados da tabela para ver se ele aprendeu/acertou
Resumo:
x_treino = dados pra ele treinar, todas colunas exceto o alvo y = "score_credito"e tambem colunas irrelevantes
y_treino = dados da coluna alvo "score-credito"
x_teste  = dados que foram separados para testar
y_teste  = dados que foram separados para testar

"""
# essa função train_test_split do sklearn já separa em dados de treino e dados de teste
from sklearn.model_selection import train_test_split # Importa a função de divisão de dados

# Divide os dados para aprender e testar
# x_treino, x_teste, y_treino, y_teste = train_test_split(x, y)  = NAO ESCOLHI  qual % treino e % teste
# ou x_train, x_test, y_train, y_train = train_test_split(x,y), ou seja escolho o nome que quiser

# aqui eu defini: 70% para treinar a IA e 30% para testar 
x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.1)

"""
COMO SABER SE DEU CERTO
eu vou comparar com o gabarito da previsao
ele ele errou muito entao nao deu certo
se ele acertou muito deu certo

"""

# Margem de erro: uso metricas de precisao ou de variaçao de resposta ou etc...


########################################################################3
#  passo 3 - Treinar a Inteligência Artificial = treinar o modelo
############ TREINAR o MODELO / INTELIGÊNCIA ARTIFICIAL
"""
criar o modelo: Nota de crédito: Boa, Ok, Ruim
Passos para INETLIGÊNCIA ARTIFICIAL:
1 - Importar a IA/modelo -  import sklearn
2 - Criar a IA/modelo - arvore de descisao/RandomForest e o KNN/Nearest Neighbors(vizinhos próximos) e muitos outros
3 - Treinar a IA/modelo
Escolhi estes 2 modelos, mas existem vários
Modelos: regressao linear, regressao logistica, arvore descisão, svm, inferencia beisiana, gradiente/descendente, e muitos outros 
Para escolher o modelo, você deve testar vários algoritmos com seus dados
e selecionar aquele que apresentar a maior acurácia (maior taxa de acertos) nos testes.
Arvore descisao = cria várias perguntas pra sua base de dados e vai respondendo em sim ou nao e cria ramificacoes
KNN = ele define algumas pessoas Boa, Ok e Ruim e depois verifica quais os vizinhos mais proximos de cada tipo


"""
## IA/modelo 
##### importar a IA (Inteligencia Artificial)
from sklearn.ensemble import RandomForestClassifier # Importa o algoritmo de Árvore de Decisão
from sklearn.neighbors import KNeighborsClassifier # Importa o algoritmo KNN

## IA/Modelo 
###### criar a IA = criar modelo
## escolhi 2 modelos, mas existem vários
modelo_arvoredecisao = RandomForestClassifier() # Inicializa o modelo de Árvore, modelo vazio = ()
modelo_knn = KNeighborsClassifier() # Inicializa o modelo KNN, modelo vazio = ()

## IA/Modelo 
##### treinar a IA = treinar modelo
modelo_arvoredecisao.fit(x_treino, y_treino) # A IA da árvore estuda os dados de treino
modelo_knn.fit(x_treino, y_treino) # A IA do KNN estuda os dados de treino

### até aqui ele está treinando os 2 modelos ppassando pela base de dados toda e pode demorar
### importa, cria e treina. Estes sao passos para criar IA


#############################################
#### Passo 4 - Escolher qual o melhor modelo
# vou comparar qual melhor modelo
""" 
Arvore descisao = cria várias perguntas pra sua base de dados e vai respondendo em sim ou nao e cria ramificacoes
KNN = ele define algumas pessoas Boa, Ok e Ruim e depois verifica quais os vizinhos mais proximos de cada tipo
Para comparar o melhor modelo entre estes 2, pegar os dados de teste so o x e pedir uma previsao pra mim, ai
voce compara a arvore com o Knn e ver os acertos das 2
Neste caso a arvore foi melhor porque acertou mais 
qual valor deu Acurácia?
""" 
# previsao dos modelos : arvore descisao e do knn
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste) # Faz previsões usando os dados de teste (Árvore)
previsao_knn = modelo_knn.predict(x_teste) # Faz previsões usando os dados de teste (KNN)

# acurácia (medir a porcentagem de acerto)
# agora vouo calcular
from sklearn.metrics import accuracy_score # Importa a função que calcula a precisão
print(f"Acurácia Arvore de descisao = {accuracy_score(y_teste, previsao_arvoredecisao)}")
#print(accuracy_score(y_teste, previsao_knn)) # Exibe a precisão do KNN
print(f"Acurácia Knn = {accuracy_score(y_teste, previsao_knn)}") # Exibe a precisão do 
print("----------------------------------------------------")

"""
Meus Resultados com modelo de 70% treino e 30% teste
acurácia da árvore = 0.823%
acurácia da knn = 0.74%

"""
"""
Meus Resultados com modelo de 90% treino e 10% teste
acurácia da árvore = 0.83%
acurácia da knn = 0.756%

"""
"""
Meus Resultados com modelo de 50% treino e 50% teste
acurácia da árvore = 0.836%
acurácia da knn = 0.76%

"""
"""
CONCLUSÃO - O MELHOR MODELO É A ÁRVORE DE DESCISÃO
Para melhorar a IA, melhorar modelo paraa acima de 82% se voce precisar, temos alguns métodos.
. Fazer FAZER O processo de grid search, é voce fazer vários treinamentos e varios testes com varias bases de dados e com parametros diferentes, chegando numa combinaçao para melhorar o modelo
. Colocar mais dados para tentar melhorar o modelo
. Testar outros parametros

"""

#############################################
# Passo 5 - Usar o melhor modelo para fazer previsão de novos clientes
 
"""
FAZER nova previsao COM NOVA BASE DE DADOS
Passos:
. Ler a base de novos clientes
. transformar colunas texto em numeros conforme fiz anteriormente:
nao preciso fazer o fit.transform eu ja fiz, agora apenas uso o codificador
. 

melhor modelo é o modelo_arvoredecisao
"""

# importar os novos clientes para fazer a previsao
tabela_novos_clientes = pd.read_csv("3_novos_clientes.csv") # Carrega o arquivo com clientes sem "score"

# profissao
# Usa o mesmo codificador anterior para transformar o texto dos novos clientes em números
tabela_novos_clientes["profissao"] = codificador_profissao.transform(
    tabela_novos_clientes["profissao"])


# mix_credito
tabela_novos_clientes["mix_credito"] = codificador_credito.transform(
    tabela_novos_clientes["mix_credito"])

# comportamento_pagamento
tabela_novos_clientes["comportamento_pagamento"] = codificador_pagamento.transform(
    tabela_novos_clientes["comportamento_pagamento"])


print(tabela_novos_clientes) # Exibe a nova tabela preparada
print("----------------------------------------------------")

# Faz a previsão final para os novos clientes usando o modelo treinado
# utilizando a arvore de decisao
nova_previsaoarvore = modelo_arvoredecisao.predict(tabela_novos_clientes)
print(f"Nova previsão com árvore de decisão {nova_previsaoarvore} ") # Exibe os resultados previstos (Good, Standard ou Poor)
print("----------------------------------------------------")

# utilizando a Knn
nova_previsaoknn = modelo_knn.predict(tabela_novos_clientes)
print(f"Nova previsao com KNN = {nova_previsaoknn}") # Exibe os resultados previstos (Good, Standard ou Poor)
print("----------------------------------------------------")

"""
Resultados
Nova previsão com árvore de decisão ['Poor' 'Poor' 'Standard'] 
Nova previsao com KNN = ['Poor' 'Poor' 'Standard']

OBS: se mudar alguma informacao em alguma das colunas tipo uma profissao que nao existia voce deve refazer o modelo do zero

"""