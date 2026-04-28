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

#############################################
# NULOS   IDADE    E SALÁRIO
#############################################

######## NULOS ############ SALARIO ############
# pegar os valores salários nulos e susbtituir pela mediana
salariomediana = dados['SALARIO'].median()
# substitua pela SALARIOMEDIANA
dados.loc[(dados['SALARIO'].isnull()),'SALARIO'] = salariomediana
#################################
### outro metodos de calculo, calculando desvio padrao para ver quanto esta distante da média
# entao vamos ver qual a média
media =dados['SALARIO'].mean()
desvio=dados['SALARIO'].std()
#############
# media= 10517.53 e desvio = 18.096,21, então 
#############
######### agora #######
# limite superior, é media x um cert numer de desvio padrao
# temos que analisar  contexto, vamos fazer 3x, já que os OUTLIERS estao MUITO acima
limitesuperior3x = media + (3*desvio)
# RESPOSTA  64.806,00
######### conclusão ##########
## PELO BOXPLOT analisando esse valor de 64.806,00 podemos ver que sim, então
# É UM VALOR BOM para limite superior, então acima desse valor podemos considerar OUTLIER
# será que os salarios muitos altos foram erro de preenchimento, ou faz sentido esses salários estão OK?
###########################################
## tratando os valores discrepantes
##########################################
## remover, nao é indicado
## podemos substituir como nos NaNs/Faltantes
## ou substituir plos valores máximos
## ou ainda o caso de manter caso ejam necessários
################# entre 30 e 40 mil ###############
# vamos fazer a media dos salários entre 30 a 40mil 
mediaentre30e40mil = dados[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']<limitesuperior3x)]['SALARIO'].mean()
# ENTAO A MEDIA dos valores abaixxo do limitesuperior entre 30 e 40 mil = 39mil
# agra substituir a media de 30 a 40 mil nesses 3 valores
(dados.loc[(dados['FAIXA SALARIAL'] == 'de R$ 30.001/mês a R$ 40.000/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO']) = mediaentre30e40mil
################# acima de 40 mil ###############
# vamos fazer a media dos salários acima de 40mil mas que nao sejam outliers, e substituir os outliers por esse valor
mediaacima40mil = dados[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']<limitesuperior3x)]['SALARIO'].mean()
#RESPOSTA = 53.127,84
# ENTAO A MEDIA dos valores abaixxo do limitesuperior acima de 40 mil = 53.127,84 mil
# agora substituir a media de acima de 40 mil nesses 19 valores de salarios
(dados.loc[(dados['FAIXA SALARIAL'] == 'Acima de R$ 40.001/mês') & (dados['SALARIO']>limitesuperior3x),'SALARIO']) = mediaacima40mil


######### NULOS ############ I D A D E ########################
# vamos ver se aas pessoas preencheram a faixa etária de idade
# vou ter a faixa etaria das pessoas que preencheram NaNs e quantas dessas preencheram a faixa etária
# todas preencheram a faixa etaria
# agora faremos a media da faixa de idade
#############################################
### faixa etaria = de 17-21 anos
media1721=dados[dados['FAIXA IDADE']=='17-21']['IDADE'].mean()
# MÉDIA DEU 20,20
# agora vamoslocalizar com filtro das linhas de faixa etaria entre 17-21 e idade estej vazia=NaNs
# O LOC SÓ LOCALIZA 
# AGORA VAMOS SUSBSTITUIR esses que foram encontrados com a media da faixa idade de 17-21
dados.loc[(dados['FAIXA IDADE']=='17-21') & (dados['IDADE'].isnull()),'IDADE'] = media1721
print ("-----------------------------------")
#########################
## agora para faixa de idade +55
media55=dados[dados['FAIXA IDADE']=='55+']['IDADE'].mean()
## deu resultado nan 
## vamos visualizar o que tem sem o mean()
# vimos que NENHUMA da faixa 55+ marcou idade, entao nao consigo fazer media
# vamos ver a coluna de nivel já que a de idade esta vazia
# a resposta não deu pra resolver
## vou preencher com a media geral ja que nao consigo ela faixa idade
mediageral = dados['IDADE'].mean()
##### media geral foi de 31.15
# agora vamoslocalizar com filtro das linhas de faixa etaria 55+ e idade estej vazia=NaNs
# O LOC SÓ LOCALIZA 
# se no final nao colocar a ,IDADE, vai mostrar todas as colunas
# AGORA VAMOS SUSBSTITUIR esses que foram encontrados com a media da faixa idade de 17-21
dados.loc[(dados['FAIXA IDADE']=='55+') & (dados['IDADE'].isnull()),'IDADE'] = mediageral

"""
 AGORA vamos ver a correlação, variaveis CONTINUAS
Vamos analisar se existe alguma relacao entre a idade das pessoas e o salário que elas recebem
tipo se a idade aumenta os salarios aumentam também?
"""
correlacaocontinua = dados['IDADE'].corr(dados['SALARIO'])
print ("------CORRELACAO entre IDADE e SALARIO-----------------------------")
print(correlacaocontinua)
# RESULTADO = 0,288744  da professora= 0.2902
print ("-----------------------------------")
"""
resultado, 0,29 entao a correlaçao é baixa, mais proxima de zero
apesar de ser positiva nao é tao forte
entao, a idade maior nao significa salario maior
vamos fazer um mapa de calor para ver quais estao mais correlacionadas
"""

############ CORRELACAO ###############
#  VARIAVEIS categóricas
#########  método CRAMER ##############

# calcular tabela cruzada 
tabelacruzada=pd.crosstab(dados['COR/RACA/ETNIA'], dados['NIVEL DE ENSINO'])
print(tabelacruzada)
print ("-----------------------------------")
# tabela cruzada como matriz utilizo NP, só numeros
tabelacruzada2=np.array(tabelacruzada)
print(tabelacruzada2)
print ("-----------------------------------")

# biblioteca stats usar funçao chi2-contigency
from scipy.stats import chi2_contingency
# comente

from scipy.stats import chi2_contingency 
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

"""
Chama a função 'cramercoeficiente' passando as colunas 'COR/RACA/ETNIA' e 
'NIVEL DE ENSINO' do DataFrame 'dados' e imprime o resultado (o coeficiente de Cramer) na tela.
""" 
print ("--------coeficiente cramer---------------------------")
print ("--------CORRELACAO entre COR/RACA/ETNIA e NIVEL DE ENSINO-------")
print(cramercoeficiente(dados['COR/RACA/ETNIA'], dados['NIVEL DE ENSINO'])) 
# resultado = 0.04503 Professora deu 0.04499
# nao tem correlacao
print('')



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
