""" 
Problema : "Quem vai querer sorvete?" Carrinho de Sorvete
Dor: Desperdício de tempo e estoque com quem não quer comprar
Solução: IA que identifica os clientes certos com base no clima e dinheiro.

O Problema - O Carrinho de Sorvete
Imagine que você tem um carrinho de sorvete. 
Você quer prever se uma criança vai comprar um sorvete (Sim ou Não) baseada em duas coisas:
. O tempo: Está Sol ou está Chovendo?
. O dinheiro: A criança tem moedas ou o cofrinho está vazio

Resumo
. Data Ingestion: Cria e carrega arquivos .csv para simular uma base de dados histórica e uma base de novos dados (inferência).
. Feature Engineering: Utiliza variáveis numéricas binárias (esta_sol, tem_moeda) como preditores para facilitar o processamento do modelo.
. Model Training: Instancia e treina um algoritmo de Aprendizado Supervisionado (RandomForestClassifier) para encontrar padrões entre as features e o target (comprou).
. Inference: Aplica o modelo treinado sobre dados inéditos para realizar a predição de classe.
. Output: Exibe os resultados das predições para tomada de decisão.

 A ordem lógica: Criação dos Dados + EDA + Treinamento + Inferência + Comparação = Resultado/Conclusão.

"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression # Novo modelo importado
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split # Faltava para uma análise real

# ------- PASSO 1: CRIAR OS ARQUIVOS -------------

# Dados, histórico do que já aconteceu
dados_sorvete = {
    'esta_sol':  [1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 0, 1], # 16 dados agora
    'tem_moeda': [1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1],
    'comprou':   ['Sim','Não','Não','Não','Sim','Não','Sim','Não','Sim','Sim','Não','Não','Não','Sim','Não','Não'] 
    # O último cliente acima (1, 1) disse NÃO. Isso confunde a IA!
}

#tabela_sorvete = pd.DataFrame(dados_sorvete)
#tabela_sorvete.to_csv("sorvete.csv", index=False) # Cria o arquivo CSV
pd.DataFrame(dados_sorvete).to_csv("sorvete.csv", index=False)

dados_novos = {
    'esta_sol': [1, 0], 
    'tem_moeda': [1, 1]
}
tabela_previsao = pd.DataFrame(dados_novos)
tabela_previsao.to_csv("novos_clientes_sorvete.csv", index=False) # Cria o arquivo CSV
# outra forma = pd.DataFrame({'esta_sol': [1, 0], 'tem_moeda': [1, 1]}).to_csv("novos_clientes_sorvete.csv", index=False)

print("-" * 100)
print("Arquivos CSV criados com sucesso!!! ")
print("-" * 100)


# ------ PASSO 2: ANÁLISE EXPLORATÓRIA DE DADOS EDA ---------

# 1. Carregar o arquivo
tabela = pd.read_csv("sorvete.csv")

# 2. Explorar os DADOS (Visualizar as primeiras linhas)
print("--- Primeiras 5 linhas do arquivo ------------------------")
print(tabela.head())

# 3. Mostra média, desvio padrão, valor mínimo e máximo
print("\n--- Describe -------------------------------------------")
print(tabela.describe())

# 4. Ver INFO e TIPOS das colunas (Dtype)
print("\n--- Informações Gerais e Tipos de Dados ----------------")
tabela.info() 
# No terminal, o Dtype mostrará 'int64' para números e 'object' para texto

# 5. Identificar a COLUNA TARGET (Alvo y)
# Aqui exibimos a contagem de valores para entender o equilíbrio da classe alvo
y = tabela["comprou"]
print("\n--- Distribuição da Coluna Alvo (y) --------------------")
print(y.value_counts())

# 6. Ver apenas os nomes das colunas (Features + Target)
print("\n--- Lista de todas as colunas -------------------------")
print(tabela.columns)

# 7. Verificar QUANTOS valores nulos existem em cada coluna
print("\n--- Quantidade de valores nulos por coluna ---")
print(tabela.isnull().sum())

# 8. Verificar a PORCENTAGEM de valores nulos (bom para bases grandes)
print("\n--- Porcentagem de valores nulos ---")
print(tabela.isnull().mean() * 100)


# ------ PASSO 3: O PROCESSO DA INTELIGÊNCIA ARTIFICIAL ---
# ------ PREPARAÇAO E DIVISÃO ------------------------------

# 1. Separar X (características) e Y (resultado que queremos aprender)
# X = Está sol? Tem moeda?
# Y = Comprou?
X = tabela.drop(columns="comprou")
y = tabela["comprou"]

# 2. AJUSTE: Separar dados para validar se a IA aprendeu de verdade
# x_treino/y_treino (estudo) | x_teste/y_teste (prova)
X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)

"""  
O Pandas e o Scikit-Learn sempre entregam nessa ordem exata:
. x_treino: Perguntas para o robô estudar/praticar.
. x_teste: Perguntas para o exame surpresa.
. y_treino: Respostas para o robô estudar.
. y_teste: Gabarito para conferir a nota do exame surpresa/robo nao sabe resposta, vai testar ele.

Estou usando dados que ja aconteceram e sei a resposta de tudo, uso o train_test_split e ele separa em 4 partes oos dados que ja aconteceram, x_treino 80% dados o x_teste  20% dos dados, o y_treino resposta dos  80% do x_treino e  y_teste resposta dos 20% do x_teste mas estes ficam esperando a resposta da IA para conferir se acertou 

O fechamento do ciclo:
. O Estudo: A IA usa o x_treino e o y_treino para criar as regras na cabeça dela.
. O Desafio: Você entrega o x_teste (20%) para a IA. Ela não sabe o que tem no y_teste.
. A Aposta: A IA gera os "chutes" dela (as previsões).
. A Correção: Você pega os chutes da IA e compara com o y_teste (que estava ali guardadinho esperando).

"""
# 3. Criar o "Robô" IA/MODELO
# modelo_a = RandomForestClassifier(random_state=42)  # modelo arvore - o lógico
modelo_a = RandomForestClassifier()  # modelo arvore - o lógico
modelo_rlog = LogisticRegression()   # modelo regressao - o probabilistico

# 4. TREINAMENTO do "Robô" IA/MODELOS ------- fit
modelo_a.fit(X_treino, y_treino)    # modelo arvore, o robô estuda o arquivo - lógico
modelo_rlog.fit(X_treino, y_treino) # modelo regressao, o robô estuda o arquivo - Probabilistico

# 5. O Robô faz a previsão ----------- predict  
# Cada modelo tenta prever os 20% que foram escondidos
predicao_a = modelo_a.predict(X_teste)
predicao_rlog = modelo_rlog.predict(X_teste)

# 6. Acurácia  - é a nota/% para cada modelo dos dados que ele treinou e fez previsao -------- accuracy_score
acc_a = accuracy_score(y_teste, predicao_a)         # arvore
acc_rlog = accuracy_score(y_teste, predicao_rlog)   # regressao logistica

# 7. Resultados
print("-" * 70)
print(f"\nResultado Acurácia da Árvore de decisão/RandomForest : {acc_a*100:.2f}%")
print(f"\nResultado Acurácia da Regressão Logística/Logistica  : {acc_rlog*100:.2f}%")
print("\n")
print("-" * 70)


# --- PASSO 4: PREVISÃO PARA NOVOS CLIENTES (Futuro Real) -----------

# 1. Carregar os novos dados para prever o futuro
# Dados de novos clientes - meu alvo o que queremos descobrir
novos_clientes = pd.read_csv("novos_clientes_sorvete.csv")

# 2. Análise exploratória EDA
print("--- Arquivo novos Clientes ------------------------")
print(novos_clientes)
print("--- Primeiras 5 linhas do arquivo ------------------------")
print(novos_clientes.head())

# 3. Previsões finais
final_a = modelo_a.predict(novos_clientes)
final_rlog = modelo_rlog.predict(novos_clientes)

# 4. Probabilidades (Nível de Certeza)
prob_a = modelo_a.predict_proba(novos_clientes)
prob_rlog = modelo_rlog.predict_proba(novos_clientes)

 
# --- PASSO 5: MOSTRAR OS RESULTADOS ---
print("\n")
print("-" * 70)
print("\nPrevisão para Novos clientes :")
print("\nO robô acha que:")
for i in range(len(novos_clientes)):
    print(f"\nCliente {i+1}:")
    print(f"  RandomForest/Árvore: {final_a[i]} (Certeza: {prob_a[i].max()*100:.2f}%)")
    print(f"  RegressãoLogística: {final_rlog[i]} (Certeza: {prob_rlog[i].max()*100:.2f}%)")

"""
Enquanto o Random Forest cria regras de "Sim ou Não" (como um fluxograma), a Regressão Logística calcula uma curva de probabilidade. Ela é o padrão ouro para problemas binários simples porque é extremamente rápida e menos propensa a "decorar" (overfitting) dados pequenos.

"""


# --- PASSO 6: GRAVAR UM ARQUIVO CSV COM A PREVISAO ---
# E se quiser salvar isso em um arquivo para enviar para seu chefe:
# Precisamos criar as colunas ANTES de salvar o arquivo
novos_clientes['Comprou_Previsao_Arvore'] = final_a
novos_clientes['Comprou_Previsao_Logistica'] = final_rlog
novos_clientes.to_csv("resultado_final_novos_clientes.csv", index=False)

previsao_novos_clientes = pd.read_csv("resultado_final_novos_clientes.csv")
print("\n--- Arquivo Resultado PREVISÃO novos Clientes ------------------------")
print(previsao_novos_clientes)



# --- PASSO 7: GRÁFICOS DE COMPARAÇÃO ---

# 1. Gráfico de Acurácia 
modelos = ['Random Forest', 'Regressão Logística']
notas = [acc_a, acc_rlog]

plt.figure(figsize=(10, 5))

# Subplot 1: Acurácia
plt.subplot(1, 2, 1) # 1 linha, 2 colunas, posição 1
plt.bar(modelos, notas, color=['skyblue', 'salmon'])
plt.ylabel('Acurácia (0 a 1)')
plt.title('Qual modelo tirou nota maior?')
plt.ylim(0, 1) # Define o limite do gráfico de 0 a 100%

# Subplot 2: Certeza para o Cliente 1
plt.subplot(1, 2, 2) # 1 linha, 2 colunas, posição 2
certezas = [prob_a[0].max(), prob_rlog[0].max()]
plt.bar(modelos, certezas, color=['blue', 'red'])
plt.ylabel('Certeza (0 a 1)')
plt.title('Confiança no Cliente 1')
plt.ylim(0, 1)

plt.tight_layout()
plt.show()