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
""" Boxplot de Distribuição (Outliers)
Para entender por que o modelo escolheu certas variáveis, escolha a variável mais importante (geralmente a V17, V14 ou V12 nesse dataset) e veja como ela se comporta em transações normais vs. fraudes."""
"""
plt.figure(figsize=(10, 6))
sns.boxplot(x='Class', y='V14', data=df) # V14 costuma ser muito relevante
plt.title('Distribuição da Variável V14: Legítimo (0) vs Fraude (1)')
plt.show()
"""

"""
#### Interpretaçao resultados: 
Arquivo menor 10.000
Resultados 26/02/2026
Amostra treino teste de 2000
Class
0    9983 / 1997
1    17 / 3
^^^^^^^^^^^ Random Forest ^^^^^^^^^^
              precision    recall  f1-score   support
           0       1.00      1.00      1.00      1997
           1       0.75      1.00      0.86         3
    accuracy                           1.00      2000
   macro avg       0.88      1.00      0.93      2000
weighted avg       1.00      1.00      1.00      2000

 ^^^^^^^^^^^ Logistic Regression ^^^^^^^^^^
              precision    recall  f1-score   support
           0       1.00      1.00      1.00      1997
           1       0.75      1.00      0.86         3
    accuracy                           1.00      2000
   macro avg       0.88      1.00      0.93      2000
weighted avg       1.00      1.00      1.00      2000


#### Interpretaçao resultados: 
Arquivo com 20.000
Resultados 23/02/2026
Amostra treino teste de 4000
Class
0    3993
1    34 / 7
Name: proportion, dtype: float64
              precision    recall  f1-score   support

           0       1.00      1.00      1.00      3993
           1       1.00      0.57      0.73         7
    accuracy                           1.00      4000
   macro avg       1.00      0.79      0.86      4000
weighted avg       1.00      1.00      1.00      4000


#### Interpretaçao resultados
# Com arquivo original do kaggle  

Resultados em 11/02/25 
Resultados 23/02/2026
Amostra treino teste de 56962
Class
0    56864
1    98
sim/não     precision  recall  f1-score    support
0 ok           1         1          1       56864
1 fraude      0.94       0.82       0.87    98
accuracy                            1       56962
macro avg      0.97      0.91      0.94     56962
weighted avg   0.97      0.91      0.94     56962

A precisao apontou as fraudes e 94% acertou mas no geral o modelo nao apontou 18% de todas as fraudes
IA me deu uma analogia: 
"Para fixar de vez, pense no seu modelo como um Investigador de Polícia:
* Precisão (94%): O Investigador é muito criterioso. 
Quando ele coloca alguém na viatura e diz "Este é o ladrão!", ele está certo em 94% das vezes. 
Ele raramente prende um inocente por engano.
* Recall (82%): O Investigador é um pouco "lento". 
De todos os crimes que aconteceram na cidade naquele dia, ele só conseguiu resolver 82% dos casos. 
Os outros 18% dos criminosos fugiram e ele nem ficou sabendo quem eram."

Resumo----------------------- 
precision/precisão = quantas vezes ele acertou a fraaude = 94%
recall/revocacao = de todas as fraudes(1) que realmente aconteceram que foram 98 quantas o modelo conseguiu pegar foram 82%, significa que 18% das fraudes ele nao pegou
** o recall é a métrica maiis importante em detecçao de fraude
f1--score = médida enre a precisao e o recall, como os 2 estao altos o f1 é bom. Serve para comparar com outros modelos no futuro
Acurácia = Aqui está o maior perigo para quem estuda ML. O seu modelo diz que tem 100% de acurácia.
** nunca use apenas a acurácia olhe sempre para o recall

No geral o modelo Random Forest/Árvore teve um deempenho excelente
Ele é conservador: prefere deixar passar uma fraude (Recall de 0.82) do que bloquear o cartão de um cliente honesto (Precisão de 0.94).

Se o seu Recall for de 0.95, você terá a satisfação de saber que sua IA pegaria 95% dos bandidos. 
Mas se sua Precisão for de 0.30, você verá que está bloqueando muita gente inocente e precisaria ajustar o modelo.

#### Interpretaçao resultados:

Resumo----------------------- 
precision/precisão = quantas vezes ele acertou a fraaude = 94%
recall/revocacao = de todas as fraudes(1) que realmente aconteceram que foram 98 quantas o modelo conseguiu pegar foram 82%, significa que 18% das fraudes ele nao pegou
** o recall é a métrica maiis importante em detecçao de fraude
f1--score = médida enre a precisao e o recall, como os 2 estao altos o f1 é bom. Serve para comparar com outros modelos no futuro
Acurácia = Aqui está o maior perigo para quem estuda ML. O seu modelo diz que tem 100% de acurácia.
** nunca use apenas a acurácia olhe sempre para o recall

No geral o modelo Random Forest/Árvore teve um deempenho excelente
Ele é conservador: prefere deixar passar uma fraude (Recall de 0.82) do que bloquear o cartão de um cliente honesto (Precisão de 0.94).


Detalhado ------------------
1. O Desequilíbrio (O campo "Support")
Olhe para a coluna Support. Ela indica quantas transações reais de cada tipo havia no seu teste:
Classe 0 (nao fraude/Legítimo): 56.864 transações.
Classe 1 (Fraude): 98 transações.
Conclusão: É um problema de "agulha no palheiro". 
O modelo tem que ser muito bom para achar 98 fraudes no meio de quase 57 mil casos.

2. O que significam as métricas (Para a Classe 1 - Fraude)
Precision (Precisão): 0.94 (94%)
A pergunta: "De todas as vezes que o modelo disse que era fraude, quantas vezes ele acertou?"
Resposta: Em 94% das vezes que ele deu o alerta, era fraude mesmo. Ele é muito "certeiro", raramente acusa um inocente.
Recall (Revocação): 0.82 (82%)
A pergunta: "De todas as fraudes que realmente aconteceram (as 98), quantas o modelo conseguiu pegar?"
Resposta: Ele pegou 82% das fraudes. Isso significa que 18% das fraudes passaram batidas (o modelo disse que era legítimo, mas era roubo).
Em detecção de fraude, o Recall costuma ser a métrica mais importante.
F1-Score: 0.87
É uma média entre a Precisão e o Recall. Como os dois estão altos, o F1-Score é bom. Ele serve para você ter um único número para comparar com outros modelos no futuro.

3. A "Armadilha" da Accuracy (Acurácia): 1.00 (ou 100%)
Aqui está o maior perigo para quem estuda ML. O seu modelo diz que tem 100% de acurácia.
Por que isso engana? Se o seu modelo fosse "burro" e simplesmente dissesse que toda e qualquer transação é legítima, ele teria 99,8% de acurácia, porque ele acertaria todos os 56.864 casos normais.
Lição: Nunca use apenas a Acurácia em dados desequilibrados (como fraudes ou resultados de corridas de elite). Olhe sempre para o Recall da classe minoritária.

4. Interpretando a Análise Geral
O seu modelo Random Forest teve um desempenho excelente.
Ele é conservador: prefere deixar passar uma fraude (Recall de 0.82) do que bloquear o cartão de um cliente honesto (Precisão de 0.94).

Essas duas linhas no final do relatório servem para te dar uma "visão global" do modelo, já que você tem duas classes (Legítimo e Fraude) com tamanhos completamente diferentes.

Como você está estudando **Machine Learning**, entender a diferença entre elas é fundamental para saber se o seu modelo é bom de verdade ou se ele está apenas sendo carregado pela classe que tem mais dados.
5. Macro Avg (Média Aritmética Simples)
O **Macro Avg** trata as classes como se fossem **iguais em importância**, ignorando quantas vezes cada uma aparece.
* **O cálculo:** Ele soma a métrica da Classe 0 com a da Classe 1 e divide por 2.
* **O que ele te diz:** Ele avalia o quão "justo" o modelo é. Se o seu modelo for excelente em achar transações legítimas (Classe 0), mas péssimo em achar fraudes (Classe 1), o Macro Avg vai cair drasticamente.
* **No seu caso (0.91):** Como a média deu alta, isso prova que seu modelo é bom nas duas tarefas, e não apenas na mais fácil.

6. Weighted Avg (Média Ponderada)
O **Weighted Avg** leva em conta o **peso (Support)** de cada classe.
* **O cálculo:** Ele dá muito mais importância para a Classe 0 (que tem 56.864 exemplos) do que para a Classe 1 (que só tem 98).
* **O que ele te diz:** Ele mostra a performance média considerando a realidade dos dados que você tem.
* **No seu caso (0.94):** Ele é quase igual à acurácia. Note que ele é maior que o Macro Avg porque a performance quase perfeita da Classe 0 "puxa" a média para cima.

---

### Qual das duas você deve olhar?

Para o seu estudo de **Machine Learning**, a regra de ouro é:

1. **Em dados desequilibrados, este caso:** Olhe sempre para o **Macro Avg**.
    Ele é o "juiz rigoroso". 
    Se ele estiver baixo, seu modelo não está aprendendo a classe minoritária (a fraude), mesmo que o Weighted Avg pareça lindo.
2. **Em dados equilibrados (50% cada classe):** As duas médias serão iguais.

---

### Resumo Comparativo

| Métrica | Tratamento das Classes | Para que serve? |
| --- | --- | --- |
| **Macro Avg** | Dá o mesmo peso para Fraude e Legítimo. | Ver se o modelo aprendeu a **Fraude** (o caso difícil). |
| **Weighted Avg** | Dá mais peso para a classe que aparece mais. | Ver a performance geral no **dia a dia** do banco. |

No seu resultado, o **Macro Avg de 0.91** para o Recall é um sinal de que seu modelo Random Forest é muito robusto, pois conseguiu manter uma média alta mesmo tendo pouquíssimos exemplos de fraude para aprender.


"""