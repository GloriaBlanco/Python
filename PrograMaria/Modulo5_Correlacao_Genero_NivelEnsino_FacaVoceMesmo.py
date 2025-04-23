#######################################################
#### CORRELAÇAO
#######################################################
"""
CORRELAÇAO É importante para entender a relaçao entre variaveis 
para identificar padrões e fazer previsões
Vamos analisar se existe alguma relacao entre a idade das pessoas e o salário que elas recebem
tipo se a idade aumenta os salarios aumentam também?
vamos ver a relacao entre as variaveis através da correlação
2 variaveis CONTINUAS
2 tipos de correlaçao, positiva (as 2 variaveis aumentam) e negativa(em 1 aumenta e outra diminue)
Correlacao e representada pela correlacao de pearson, varia entre -1 e 1
valor proximo de 1 indica forte correlacao positiva
valor proximo de -1 indica forte correlacao negativa
ZERO indica que nao á relacao linear/não tem relaçao
"""
import pandas as pd
import numpy as np
# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')
print(dados.columns)
print ("-----------------------------------")

"""
Vamos analisar se existe alguma relacao entre oo genero e o nivel ensino
############ CORRELACAO ###############
#  VARIAVEIS categóricas
#########  método CRAMER ##############
"""

# calcular tabela cruzada 
tabelacruzada=pd.crosstab(dados['GENERO'], dados['NIVEL DE ENSINO'])
print(tabelacruzada)
print ("-----------------------------------")
# tabela cruzada como matriz utilizo NP, só numeros
tabelacruzada2=np.array(tabelacruzada)
print(tabelacruzada2)
print ("-----------------------------------")
# biblioteca stats usar funçao chi2-contigency
from scipy.stats import chi2_contingency
# comente
"""
 Importa a função chi2_contingency do módulo stats da biblioteca scipy, utilizada para realizar o teste qui-quadrado de independência entre variáveis categóricas.
 A função 'cramercoeficiente' recebe duas colunas de dados (séries do pandas) como entrada,
 calcula o coeficiente de Cramer, que é uma medida de associação entre duas variáveis categóricas nominais,
 e retorna esse coeficiente.
"""
def cramercoeficiente(coluna1, coluna2):
    # calcular tabela cruzada
    tabelacruzada2=np.array(pd.crosstab(coluna1, coluna2)) # usa a função pd.crosstab para criar uma tabela de contingência (frequência) entre as duas colunas fornecidas e, em seguida, converte essa tabela para um array NumPy.
    chi2 = chi2_contingency(tabelacruzada2)[0]  # faz o teste qui-quadrado de independência na tabela cruzada. A função retorna uma tupla, e o índice [0] acessa o valor estatístico do qui-quadrado.
    soma = np.sum(tabelacruzada2) # calcula a soma de todas as frequências na tabela cruzada, que representa o número total de observações.
    mini = min(tabelacruzada2.shape)-1 # aqui determina o número de graus de liberdade para o coeficiente de Cramer, que é o mínimo entre o número de linhas menos 1 e o número de colunas menos 1 da tabela cruzada.
    cramer = np.sqrt(chi2/(soma*mini)) # Calcula o coeficiente de Cramer utilizando a fórmula: raiz quadrada de (qui-quadrado dividido pelo produto da soma total e o número mínimo de graus de liberdade).
    return cramer # Retorna o valor calculado do coeficiente de Cramer.

print(cramercoeficiente(dados['GENERO'], dados['NIVEL DE ENSINO'])) 

"""
Chama a função 'cramercoeficiente' passando as colunas 'GENERO' e 
'NIVEL DE ENSINO' do DataFrame 'dados' e imprime o resultado (o coeficiente de Cramer) na tela.
""" 
print ("--------coeficiente cramer---------------------------")
# resultado = 0.084
# tem uma correlaço mais proximo de 1, então sim podemos ter correlaçao entre o genero e nivel de ensino


"""
CRAMER ----------------------------------
O Coeficiente de Cramer (V de Cramer) é uma medida estatística que quantifica a força de associação entre duas ou mais variáveis categóricas nominais.
Cramer e o valor do QUI-QUADRADO normalizado entre 0 e 1
Para que serve? Indica o grau de relacionamento entre categorias.
Permite comparar a intensidade da associação em diferentes tabelas de contingência, mesmo com dimensões distintas.

Como funciona? Baseia-se no resultado do teste qui-quadrado de independência.
Normaliza o valor do qui-quadrado pela dimensão da tabela e pelo número total de observações.
O valor varia de 0 a 1:
0: Nenhuma associação entre as variáveis.
1: Associação perfeita entre as variáveis.
Valores intermediários indicam associações de diferentes intensidades.

Parábola: Imagine duas cestas de frutas (variáveis categóricas). O Coeficiente de Cramer diria o quão "relacionada" é a presença de um tipo de fruta em uma cesta com a presença de outro tipo na mesma cesta, independentemente do tamanho das cestas ou da quantidade total de frutas.
"""
