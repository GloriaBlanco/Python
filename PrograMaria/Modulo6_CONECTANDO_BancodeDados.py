"""
CONECTANDO Banco de Dados criado no DBeaver

###########
Scripts de manipulação
###########
-- ALTER, alterações , aqui cria mais uma coluna na tabela com o nome da coluna
-- ALTER  TABLE Municipios_Brasileiros ADD COLUMN pais;

-- UPDATE atualizaçoes, Inclui dados na coluna criada
-- UPDATE Municipios_Brasileiros SET pais='Brasil';

-- DROP, excluir, exclui a coluna pais
-- ALTER  TABLE Municipios_Brasileiros DROP COLUMN pais;

-- SELECT, consulta
-- SELECT Regiao FROM Municipios_Brasileiros;
-- SELECT * FROM Municipios_Brasileiros;
-- SELECT * FROM Municipios_Brasileiros WHERE Cidade="Itaquaquecetuba";
-- SELECT * FROM Municipios_Brasileiros WHERE Cidade LIKE "Itaquaquecetuba";
-- SELECT * FROM Municipios_Brasileiros WHERE Cidade LIKE "Itaqua%";
-- SELECT * FROM  Municipio_Status WHERE populacao_residente>50000;
-- SELECT * FROM  Municipio_Status WHERE populacao_residente>500000;
-- SELECT * FROM Municipio_Status WHERE renda<1;
-- SELECT renda, sum(educacao) FROM Municipio_Status WHERE renda="0.584" and educacao="0.466";


-- Combinar os dados de 2 tabelas
-- Abaixo vou obter informacoes sobre a população residente de cada cidade, combinando os dados das 2 tabelas com base no ID do Municipio
-- queremos a Cidade da tabela Municipios_Brasileiros e a populacao-residente da Tabela Municipio_Status(aqui nao tem nome cidade)
-- fazemos INNER JOIN da tabela Municipio_Status onde a coluna Municipio_ID da tabela Municipios_Brasileiros for IGUAL a coluna Municipio_ID da tabela Municipio_Status
-- SELECT Municipios_Brasileiros.Cidade, Municipio_Status.populacao_residente FROM Municipios_Brasileiros INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID

-- Estados com mais cidades
-- SELECT Estado, COUNT(Cidade) FROM municipios_brasileiros GROUP BY Estado ORDER BY 2 DESC ;

-- Explore os diferentes tipos de JOIN para escolher o ideal para sua necessidade.
-- SELECT Municipios_Brasileiros.Cidade, Municipio_Status.populacao_residente FROM Municipios_Brasileiros INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID

-- Use funções de agregação como COUNT(), SUM(), AVG() e MAX() para resumir dados agrupados.
-- COUNT conta quantidade
-- SUM soma valores
-- SELECT SUM(pessoas_brancas), SUM(pessoas_pretas_pardas) FROM Gerencia_Regiao ;
-- SELECT Regiao, MAX(pessoas_pretas_pardas) FROM Gerencia_Regiao ;
-- SELECT Regiao, MIN(pessoas_pretas_pardas) FROM Gerencia_Regiao ;

-- SELECT Regiao FROM Gerencia_Regiao WHERE gerencia_branca>gerencia_preta_parda ;

-- Combine ORDER BY com funções de agregação para visualizar os maiores ou menores valores em cada grupo.
-- SELECT Regiao, MAX(pessoas_pretas_pardas) FROM Gerencia_Regiao ;

"""

import sqlite3
import pandas as pd

conexao = sqlite3.connect('status_brasil')
query = "SELECT * FROM Municipios_Brasileiros WHERE Cidade='Itaquaquecetuba';"
print(pd.read_sql(query,con=conexao))

# Populacao residente de cada Cidade
query = ''' SELECT Municipios_Brasileiros.Cidade, Municipio_Status.populacao_residente
        FROM Municipios_Brasileiros INNER JOIN Municipio_Status ON 
        Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID '''
print(pd.read_sql(query,con=conexao))


# MÉDIA de cada renda por Estados
query = ''' SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.renda) FROM 
        Municipios_Brasileiros INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID 
        = Municipio_Status.municipio_ID GROUP BY Municipios_Brasileiros.Estado '''
print(pd.read_sql(query,con=conexao))

# MÉDIA de cada renda por Estados ORDER BY
query = ''' SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.renda) FROM 
        Municipios_Brasileiros INNER JOIN Municipio_Status ON Municipios_Brasileiros.municipio_ID 
        = Municipio_Status.municipio_ID GROUP BY Municipios_Brasileiros.Estado  ORDER BY 2 DESC'''
print(pd.read_sql(query,con=conexao))

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
'SALARIO'],"""

# o list = cria uma lista com os estados da planilha do modulo3.csv
lista_estados=list(dados['UF ONDE MORA'].unique())
print(lista_estados)

# trabalhando com format e join
a= "batata"
print('eu gosto de '+a)
print('eu gosto de {} '.format(a))

a =['batata', 'tomate', 'alface']
print('Eu gosto de {}, {} e {}'.format(a[0],a[1],a[2]))

print('Eu gosto de {}'.format(', '.join(a)))
""" 
Para o SQL entender que estamos passando valores vindos de fora, 
precisamos concatenar interrogações (?) no lugar onde ficariam os nossos estados. 
Entendida essa parte, a consulta SQL foi armazenada em uma string e, em seguida, 
executada no banco de dados usando o método read_sql() do pandas e, a cláusula WHERE com o operador IN foi utilizada para filtrar os registros. Algo mais ou menos assim:

"""
query = ''' SELECT Municipios_Brasileiros.Estado, AVG(Municipio_Status.renda) FROM 
        Municipios_Brasileiros 
        INNER JOIN Municipio_Status 
        ON Municipios_Brasileiros.municipio_ID = Municipio_Status.municipio_ID
        WHERE Municipios_Brasileiros.Estado IN ({}) 
        GROUP BY Municipios_Brasileiros.Estado'''.format(','.join(['?' for _ in lista_estados]))

estados_renda=pd.read_sql(query,con=conexao, params=lista_estados)
print(estados_renda)


"""Depois disso fizemos o merge com a nossa tabela original. Lembrando que o how do merge precisa
 respeitar as mesmas regras de left, right, inner que o JOIN em SQL. Nosso merge ficou assim """
# se quiser posso renomear == dados.rename(columns={'UF ONDE MORA': 'Estado'}, inplace=True)

dados =dados.merge(estados_renda, left_on='UF ONDE MORA', right_on='Estado',how='left')
print((dados))

""" Por fim, analisamos a correlação entre o salário e o índice de renda média do Estado utilizando
 a função corr(). Descobrimos que a correlação é positiva, quando maior o índice, maior o salário, porém baixa, mostrando que só esse índice não causa um impacto tão grande para o salário, precisamos analisar juntando outras variáveis de importância.

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

# calcular a correlacao da variavel continua renda e salario

correlacao = dados['SALARIO'].corr(dados['AVG(Municipio_Status.renda)'])
print(correlacao)
# resultado  IGUAL = prof 0.12


