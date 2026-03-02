"""
Projeto Detecção de Fraude (Classificação)
O objetivo aqui é ensinar o computador a olhar para uma transação (valor, hora, local) e dizer: 
Isso é Legítimo/naoo fraude ou "Isso é Fraude".
Usei como base o arquivo creditard.csv do site da Kaggle, mas tive que diminuir o numero de registros para poder baixar no github

1. Histórico
Para este projeto:
. modelo supervisionado de classificaçao
. Random Forest: Para lidar com a complexidade e evitar pequenos erros do modelo.
  - Matriz de Confusão ------ Essencial para saber se seu modelo está errando mais o "falso positivo" (bloquear um cliente honesto) ou o "falso negativo" (deixar passar um bandido).
    diz onde modelo errou
  - Features ------ Gráfico de Importância das Variáveis/features
    diz o porquê. 
    Se a variável V14 está no topo, você sabe que o comportamento dessa variável é o maior "dedo-duro" da fraude.
    Como você usou RandomForestClassifier, o modelo "sabe" quais colunas foram mais importantes para decidir se era fraude ou não. 
    Isso ajuda a entender o modelo.
  - CURVA PRECISION-RECALL -----
    O melhor gráfico para dados desbalanceados, como este
    diz a estabilidade. Se a linha cair muito rápido, o modelo é instável para casos raros.
  - VISUALIZAÇÃO DE UMA ÁRVORE  -----
    O Random Forest cria várias árvores. 
    Vamos ver apenas a primeira que é o index 0
    mostra a lógica. É aqui dá pra ver o modelo fazendo perguntas do tipo: "O valor da compra é maior que X? Se sim, vá para a esquerda...".
    É a melhor forma de entender como ele pensa
  - BoxPlot da variável importante
 . Logistic Regression: Para entender a probabilidade base (0 a 1).


2. O Fluxo do Projeto
. Coleta: Baixar o dataset do Kaggle.
. diminuir o dataset Kaggle para poder baixar no github
. Limpeza: Remover dados nulos e normalizar os valores. Exemplo: transformar R$ 1,00 e R$ 10.000,00 para uma escala entre 0 e 1.
. Separar 80% dos dados para o modelo aprender e 20% para testar se ele aprendeu mesmo.
. Treino: usaar fit para treinar

Avaliação: Ver a precisão do modelo.
O passo crucial é entender como medir se o seu modelo é realmente bom.
Em problemas de classificação, não basta olhar apenas para a "acurácia" (a porcentagem de acertos totais).
Imagine que em um banco, 99% das transações são legítimas. 
Se o modelo simplesmente disser que "tudo é legítimo", ele terá 99% de acurácia, mas falhará em detectar todas as fraudes. 
É aqui que entra a Matriz de Confusão.

Entendendo a Matriz de Confusão
Ela divide os resultados do seu modelo em quatro quadrantes:
SUCESSO=Verdadeiro Positivo (TP): Era fraude e o modelo acertou.
SUCESSO=Verdadeiro Negativo (TN): Era uma compra normal e o modelo liberou.
ERRO=Falso Positivo (FP): Era uma compra normal, mas o modelo bloqueou. (Gera atrito com o cliente).
ERRO=Falso Negativo (FN): Era fraude, mas o modelo deixou passar. (Prejuízo financeiro).

Métricas para este projeto:
Precision (Precisão): De todas as vezes que o modelo disse ser "Fraude", quantas eram mesmo? Para evitar o Falso Positivo.
Recall (Revocação): De todas as fraudes que realmente aconteceram, quantas o modelo conseguiu pegar? Evitar o Falso Negativo, era fraude mas nao marcou como fraude.
F1-Score: Um equilíbrio (média harmônica) entre Precisão e Recall. É a melhor métrica para esse tipo de projeto.

O que observar no resultado:
O Quadrante "Fraude x Fraude": Este é o seu Recall. Se houver muitos casos onde o valor real era Fraude, mas o modelo previu como Legítimo (Falso Negativo), seu banco está perdendo dinheiro.
O Quadrante "Legítimo x Fraude": Este é o Falso Positivo. Se esse número for muito alto, você está bloqueando o cartão de clientes bons, o que gera reclamações no suporte.
Métrica F1-Score: Como as fraudes são poucas (dados desbalanceados), foque nesta métrica. 
Ela resume se o modelo está equilibrado.
Este código, a resposta nao será de  "sim" ou "não". 
Várias métricas coom uma visão analítica completa da "inteligência" do seu modelo.

Aqui estão os três tipos de respostas :
1. 
A Resposta Visual: Matriz de Confusão, essa é a parte mais importante. 
Gráfico de calor (heatmap) que mostra onde o modelo acertou e onde ele "se confundiu".Eixo Vertical: 
O que aconteceu de verdade (Realidade).Eixo Horizontal: O que o modelo previu (Previsão).
Visualize:
Canto superior esquerdo: O número de clientes honestos que o modelo identificou corretamente.
Canto inferior direito: O número de criminosos (fraudes) que o modelo conseguiu capturar.
Canto inferior esquerdo (O perigo): Fraudes que o modelo achou que eram compras normais (Prejuízo!).
Canto superior direito : Compras normais que o modelo achou que era fraude (Cartão bloqueado indevidamente).
2. 
A Resposta Estatística: Relatório de ClassificaçãoO comando classification_report vai imprimir uma tabela com números de 0 a 1 (0% a 100%). 
As respostas principais serão:
Precision (Precisão): "Quando meu modelo diz que é fraude, qual a chance de ele estar certo?"
Recall (Revocação): "De todas as fraudes que existiam no arquivo, qual a porcentagem que eu realmente peguei?"
F1-Score: É a "nota final" do modelo. Se este número estiver baixo, seu modelo precisa de mais treino ou melhores dados.3.
A Resposta Prática: Predição IndividualNo final do código, depois podemos testar o modelo com dados novos (como se uma transação estivesse acontecendo agora). 
A resposta será direta:[0]: Transação Legítima.[1]: Transação Suspeita/Fraude.
Resumo Se o seu Recall for de 0.95, você terá a satisfação de saber que sua IA pegaria 95% dos bandidos. 
Mas se sua Precisão for de 0.30, você verá que está bloqueando muita gente inocente e precisaria ajustar o modelo.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report, PrecisionRecallDisplay, RocCurveDisplay
from sklearn.tree import plot_tree

# 1. Carregar os dados reais
df = pd.read_csv('creditcard_reduzido10milfraudes.csv')
print("\n ^^^^^^^^^^^ Dados Arquivo ^^^^^^^^^^")
print(df.head(10))
print(df.info())
print(df['Class'].value_counts())
print(df['Class'].value_counts(normalize=True))

# 2. Preparação (X = características, y = alvo/fraude)
X = df.drop('Class', axis=1) # Remove a coluna target Class
y = df['Class']              # Define a coluna resposta/target (0=Bom, 1=Fraude)

# 3. Divisão Treino e Teste (80% treina, 20% testa)
# todo modelo utiliza sempre esta linha de separaçao treino, teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)


# ----- 1º modelo
# 4. ------  Random Forrest ------- 
# Criando e treinando o modelo / algoritimo 
# algoritmo com nome RandomForestClassifier, modelo de aprendizado por conjunto
# segue regras de If/then, classifica
# mais lento
# n_estimators = 100 é o padrao, mas posso aumentar o modelo vai demorar mas ficara mais preciso,
# se dimuinuir o modelo ficará mais rápido e menos preciso
# mas 100 já está ótimo 
modelo = RandomForestClassifier(n_estimators=100, random_state=42)
modelo.fit(X_train, y_train) # treino

#  ------- 2º modelo
# 5. --------- Regression logistic / Regressao logistica ------- 
# Criando o modelo de Regressão Logística
# segue uma fórmula matemática de soma e pesos
# mais rápido
# max_iter = 1000 é o limite de tentativa e erro
modelo_log = LogisticRegression(max_iter=1000)
modelo_log.fit(X_train, y_train) # treino


# 6. Previsões com os dados de teste
# previsao random forest
y_pred = modelo.predict(X_test)
# previsao modelo regressao logistica^
y_pred_log = modelo_log.predict(X_test)


# 7. Relatório de Métricas (Precision, Recall e F1-Score)
print("\n ^^^^^^^^^^^ Random Forest ^^^^^^^^^^")
print(classification_report(y_test, y_pred))
print("\n ^^^^^^^^^^^ Logistic Regression ^^^^^^^^^^")
print(classification_report(y_test, y_pred_log))


# 8. Gráficos --------- Random Forest --------
#  Matriz de Confusão visual
# diz onde modelo errou
cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Legítimo', 'Fraude'], yticklabels=['Legítimo', 'Fraude'])
plt.xlabel('Previsão do Modelo')
plt.ylabel('Valor Real (Gabarito)')
plt.title('Matriz de Confusão: Detecção de Fraude')
plt.show()

#  Features --- Gráfico de Importância das Variáveis/features
# diz o porquê. 
# Se a variável V14 está no topo, você sabe que o comportamento dessa variável é o maior "dedo-duro" da fraude.
"""  Como você usou RandomForestClassifier, o modelo "sabe" quais colunas foram mais importantes para decidir se era fraude ou não. 
Isso ajuda a entender o modelo.
"""
importancias = modelo.feature_importances_
df_importancia = pd.DataFrame({'Feature/Variavel': X.columns, 'Importancia': importancias}).sort_values(by='Importancia', ascending=False)
plt.figure(figsize=(10, 6))
sns.barplot(x='Importancia', y='Feature/Variavel', data=df_importancia.head(10), palette='viridis', hue='Feature/Variavel')
plt.title('Top 10 Variáveis mais importantes para detectar Fraude')
plt.show()

# CURVA PRECISION-RECALL ----
# O melhor gráfico para dados desbalanceados, como este
# diz a estabilidade. Se a linha cair muito rápido, o modelo é instável para casos raros.
plt.figure(figsize=(8, 6))
# ax = plt.gca()
PrecisionRecallDisplay.from_estimator(modelo, X_test, y_test, ax=plt.gca(), color='red')
plt.title('Curva Precision-Recall')
plt.show()

# VISUALIZAÇÃO DE UMA ÁRVORE  ---
# O Random Forest cria várias árvores. 
# Vamos ver apenas a primeira que é o index 0
# mostra a lógica. É aqui dá pra ver o modelo fazendo perguntas do tipo: "O valor da compra é maior que X? Se sim, vá para a esquerda...". É a melhor forma de entender como ele pensa
plt.figure(figsize=(20, 10))
plot_tree(modelo.estimators_[0], 
          feature_names=X.columns, 
          class_names=['Normal', 'Fraude'], 
          filled=True, 
          max_depth=3) # Limitamos a profundidade para conseguir enxergar
plt.title('Visualização de 1 Árvore da Floresta-- Nível 3')
plt.show()


# 9  Comparando uma variável específica entre as classes
# Boxplot de Distribuição (Outliers)
# Para entender por que o modelo escolheu certas variáveis, escolha a variável mais importante 
# (geralmente a V17, V14 ou V12 nesse dataset) e veja como ela se comporta em transações normais vs. fraudes.

plt.figure(figsize=(10, 6))
sns.boxplot(x='Class', y='V14', data=df) # V14 costuma ser muito relevante
plt.title('Distribuição da Variável V14: Legítimo (0) vs Fraude (1)')
plt.show()


"""
Resumo----------------------- 
~ precision/precisão = quantas vezes ele acertou a fraaude 
~ recall/revocacao = de todas as fraudes que realmente aconteceram quantas o modelo conseguiu pegar, e pode ser que ele nao pegou algumas
  ** o recall é a métrica maiis importante em detecçao de fraude
~ f1--score = médida enre a precisao e o recall, como os 2 estao altos o f1 é bom. Serve para comparar com outros modelos no futuro
~ Acurácia = Aqui está o maior perigo para quem estuda ML. O seu modelo diz que tem 100% de acurácia.
  ** nunca use apenas a acurácia olhe sempre para o recall

Modelo Random Forest/Árvore teve um deempenho excelente
Ele é conservador: prefere deixar passar uma fraude do que bloquear o cartão de um cliente honesto.
Se o seu Recall for de 0.95, você terá a satisfação de saber que sua IA pegaria 95% dos bandidos. 
Mas se sua Precisão for de 0.30, você verá que está bloqueando muita gente inocente e precisaria ajustar o modelo.

* A "Armadilha" da Accuracy (Acurácia)
Aqui está o maior perigo para quem estuda ML. O seu modelo diz que tem 100% de acurácia.
Por que isso engana? Se o seu modelo fosse "burro" e simplesmente dissesse que toda e qualquer transação é legítima, ele teria 99,8% de acurácia, porque ele acertaria todos os 56.864 casos normais.
Lição: Nunca use apenas a Acurácia em dados desequilibrados (como fraudes ou resultados de corridas de elite). Olhe sempre para o Recall da classe minoritária.

### Qual das duas você deve olhar?
Para o seu estudo de **Machine Learning**, a regra de ouro é:
1. **Em dados desequilibrados, este caso:** Olhe sempre para o **Macro Avg**.
    Ele é o "juiz rigoroso". 
    Se ele estiver baixo, seu modelo não está aprendendo a classe minoritária (a fraude), mesmo que o Weighted Avg pareça lindo.
2. **Em dados equilibrados (50% cada classe):** As duas médias serão iguais.

"""