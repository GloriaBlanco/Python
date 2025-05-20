"""
📌Faça a mesma análise utilizando o índice de educação. Existe alguma correlação com salário?

Quando chegar aqui, mostre no grupo da turma que concluiu a atividade do 

Faça Você Mesme | Conectando SQL com o pandas ✅

Nosso código será a hashtag: #SQLePandasCheck

"""

import sqlite3
import pandas as pd

# carregar o banco de Dados do Dbeaver
conexao = sqlite3.connect('status_brasil')

# carregar o arquivo planilha_modulo3.xlsx
dados = pd.read_excel('planilha_modulo3.xlsx')
print(dados.columns)
print ("-----------------------------------")
"""
ID', 'IDADE', 'FAIXA IDADE', 'GENERO', 'COR/RACA/ETNIA',
'PCD', 'EXPERIENCIA_PROFISSIONAL_PREJUDICADA', 'ASPECTOS_PREJUDICADOS',
'VIVE_NO_BRASIL', 'ESTADO ONDE MORA', 'UF ONDE MORA',
'REGIAO ONDE MORA', 'MUDOU DE ESTADO?', 'REGIAO DE ORIGEM',        
'NIVEL DE ENSINO', 'ÁREA DE FORMAÇÃO',
'QUAL SUA SITUAÇÃO ATUAL DE TRABALHO?', 'SETOR',
'NUMERO DE FUNCIONARIOS', 'GESTOR?', 'CARGO COMO GESTOR', 'CARGO ATUAL',
'NIVEL', 'FAIXA SALARIAL',
'QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE DADOS VOCÊ TEM?',
'QUANTO TEMPO DE EXPERIÊNCIA NA ÁREA DE TI/ENGENHARIA DE SOFTWARE VOCÊ TEVE ANTES DE COMEÇAR A TRABALHAR NA ÁREA DE DADOS?',
'SALARIO'],
"""
###### TRATAMENTO SALÁRIO ####################3
#### anteriormente tratamos os nulos na coluna salario
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

print(dados.head())
# o list = cria uma lista com os estados da planilha do modulo3.csv
lista_estados=list(dados['UF ONDE MORA'].unique())
print(lista_estados)
""" 
Para o SQL entender que estamos passando valores vindos de fora, 
precisamos concatenar interrogações (?) no lugar onde ficariam os nossos estados. 
Entendida essa parte, a consulta SQL foi armazenada em uma string e, em seguida, 
executada no banco de dados usando o método read_sql() do pandas e, a cláusula WHERE com o operador IN foi utilizada para filtrar os registros. Algo mais ou menos assim:

"""
query = ''' SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.educacao) FROM 
        Municipios_Brasileiros 
        INNER JOIN Municipio_Status 
        ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID
        WHERE Municipios_Brasileiros.Estado IN ({}) 
        GROUP BY Municipios_Brasileiros.Estado'''.format(','.join(['?' for _ in lista_estados]))

estados_educa=pd.read_sql(query,con=conexao, params=lista_estados)
print(estados_educa)

"""
Depois do merge com a nossa tabela original. Lembrando que o how 
do merge precisa respeitar as mesmas regras de left, right, inner 
que o JOIN em SQL.  
"""
dados =dados.merge(estados_educa, left_on='UF ONDE MORA', right_on='Estado',how='left')
print((dados))
print('_______________________________________________')
""" 
Faça a mesma análise utilizando o índice de educação. 
Existe alguma correlação com salário?

"""
# calcular a correlacao da variavel continua indice de educacao e salario
correlacao = dados['SALARIO'].corr(dados['AVG(Municipio_Status.educacao)'])
print(f'A correlação entre o índice de educação com salário é de ', correlacao)
print(f'este resultado não indice uma correlação porque é muito próximo de Zero')
# resultado 0,15
print('_______________________________________________')



