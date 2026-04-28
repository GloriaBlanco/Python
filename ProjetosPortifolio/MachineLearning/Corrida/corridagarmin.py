"""
Garmin Connect
Arquivo com corridas de rua
28 colunas/columns
Passos:
0. Importar Bibliotecas
1. Carregar o arquivo e visualizar: 
    . abrir arquivo
    . visualizar os tipos de dados e os 1ºs registros
2. Dicionário padrão snake_case
    . renomear as colunas
3. ETL-Extract, Transform, Load  
   Limpeza de dados
   Data Cleaning 
   Wrangling 
    . problemas a resolver 
    . verificar erros como -- 
    . remover vírgulas e/ou trocar por vazio ''
    . converter tipos de texto para números : int, float, datatime.
    . criar novas colunas com tempo em minutos
4. Análise EAD - Exploratory Data Analysis | Análise exploratória
    . Estatistica descritiva : describe(), médias, desvio padrao, correlação
    . Análise Outliers : identificar picos
    . Matriz Correlacao : e Heatmap
5. Análise visual - gráficos | DataViz
    . Histogramas, boxploots, scatter plots
    . Interpretacao graficos
6. Machine Learnig - seleção variáveis
    . separar X e y : features=variavel= X e target=alvo=y=PREVER 
7. Machine Learning - dividir treino
    . dividir treino e teste = 70/30 ou 80/20
8. Machine Learning - escolher  modelo
    . escolher tipo modelo: Classificação ou Regressão
9. Machine Learning - treinar modelo
    . treinar modelo com fit
10. Machine Learning - previsao avaliar modelo
    . predict
11. Machine Learning - avaliação
    . Classificacaoo = verificar quantos acertou - acuracia, f1-score
    . Classificacao = matriz de confusão
    ou
    . Regressao = avaliar métrica de numero
    . Regressão = mean_squared_error, mean_absolute, r2_score
    . Regressão = MSE, MAE = perto de zero melhor=menos erro

"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### 0. Importar dados
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import matplotlib.ticker as ticker # gráfico mostrar hora em vezde segundos

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#### 1. Carregar o arquivo e visualizar
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

df = pd.read_csv('Activities24e25.csv')

# Ver as primeiras linhas e os nomes das colunas originais
print('\n~~~~~~~~~~~~~~~~ Arquivo ')
print(df.head())
print('\n~~~~~~~~~~~~~~~~ Colunas|Columns ')
print(df.columns)
print('\n~~~~~~~~~~~~~~~~ Info ')
print(df.info())


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
####  2. Dicionário para renomear colunas do Garmin, padrao snake_case
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

renomear_colunas = {
    'Tipo de atividade': 'tipo',
    'Data': 'data',
    'Título': 'titulo',
    'Distância': 'distancia_km',
    'Calorias': 'calorias',
    'Tempo': 'tempo',
    'FC Média': 'fc_media',
    'FC máxima': 'fc_max',
    'Cadência de corrida média': 'cadencia_media',
    'Cadência de corrida máxima': 'cadencia_max',
    'Ritmo médio': 'pace',
    'Melhor ritmo': 'melhor_ritmo',
    'Subida total': 'subida_total',
    'Descida total': 'descida_total',
    'Comprimento médio da passada': 'comp_medio_passada',
    'Training Stress Score®': 'training_stress_score',
    'Total de braçadas': 'total_bracadas',
    'Média de Swolf': 'media_swolf',
    'Taxa média de braçadas': 'tx_media_bracadas',
    'Passos': 'passos',
    'Descompressão': 'descompressao',
    'Tempo da melhor volta': 'tempo_melhor_volta',
    'Número de voltas': 'n_voltas',
    'Tempo em movimento': 'tempo_movimento',
    'Duração': 'duracao',
    'Elevação mínima': 'elevacao_min',
    'Elevação máxima': 'elevacao_max'
}
df = df.rename(columns=renomear_colunas)  # apenas no df, original está intacto

# Verificar quais os dados internos de cada coluna
print('\n~~~~~~~~~~~~ Dados do 1º registro ~~~~~~~~~~~~' )
print(df.iloc[0]) # pega a primeira linha completa e a exibe verticalmente


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
##### 3. ETL-Extract, Transform, Load |Limpeza de dados| Data Cleaning| Wrangling 
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Problemas a resolver verificar erros
# Tenho colunas que estão como string que preciso que sejam numéricas para fazer calculos estatisticos
# listei conteudo das colunas para ver qual tipo/forma
# print(df['tipo'].unique())
""" 
11 tipos = Corrida, Caminhada, 'Outros', 'Corrida em esteira', 
'Esportes aquáticos', 'Ciclismo', 'Natação em piscina', 'Cardiovascular', 
'Ioga', 'Ciclismo em local fechado', 'Academia e equipamentos de fitness'
"""
# print(df['comp_medio_passada'].unique())
"""
43 tipos = tem float 0.95 e '--' 
"""

#### Estta funçao vai buscar colunas/dados com "--", ou seja, sem informaçao
# depois resolvo como vou trata-los
# Dataframe ORIGINAL
def analise_geral(df):
    print("\n~~~~~~~~~~~~~~~~ Original -- Verificando erros = '--' \n")
    # Percorre todas as colunas do DataFrame automaticamente
    for col in df.columns:
        # Conta as ocorrências de '--' na coluna
        qtd_erros = (df[col] == '--').sum()
        # Imprime a qtde erros 
        if qtd_erros > 0:
            print(f"{col:25} | {qtd_erros}= Erros '--'")
        else:
            print(f"{col:25} | Limpa sem erros")
    print("\n" + "~"*50)
    print(f"Total de colunas analisadas = {len(df.columns)}")
# Chamando a função
analise_geral(df)
"""
Resultado das Colunas com erros
# Análises para trocas
~~~~~~~~~~~~~~~~ Verificando erros = '--'
----- Coluna -------------- Original (qtde=360)-- Só Corrida/Esteira (qtde=322)-----
pace                      | 5= Erros '--'           LIMPA SEM ERROS
# Posso excluir, nao vou usar para avalição de corridas
total_bracadas            | 349= Erros '--'         322= Erros '--'
media_swolf               | 349= Erros '--'         322= Erros '--'
tx_media_bracadas         | 349= Erros '--'         322= Erros '--'

# trocar pela mediana, tem , e transformar numeros
elevacao_min              | 32= Erros '--'          9= Erros '--'
elevacao_max              | 20= Erros '--'          4= Erros '--'
passos                    | 19= Erros '--'          1= Erros '--'
fc_media                  | 3= Erros '--'           1= Erros '--' 
fc_max                    | 3= Erros '--'           1= Erros '--'
cadencia_media            | 19= Erros '--'          1= Erros '--'
cadencia_max              | 19= Erros '--'          1= Erros '--'
comp_medio_passada        | 19= Erros '--'          1= Erros '--'

# trocar pela mediana ???? estao em horas
melhor_ritmo              | 6= Erros '--'           1= Erros '--'

# Posso susbtituir por 0 , sao corridas em esteira, e nao vao alterar resultados futuros sem subida/descida
subida_total              | 20= Erros '--'          4= Erros '--'
descida_total             | 21= Erros '--'          4= Erros '--'

Ou seja, se eu ficar apenas com Corridas rua e esteira já resolvo a grande maioria dos erros

"""
## Selecionar e criar um novo dataframe so com coorridas
# Lista com tipo que quero manter
corrida = ['Corrida', 'Corrida em esteira']
# Criei um novo DataFrame df_corrida apenas com esses 2 tipos
df_corrida = df[df['tipo'].isin(corrida)].copy()
# O axis=1 indica que você quer apagar uma COLUNA e não uma linha
# O inplace=True faz a alteração direto no seu DataFrame  corrida
df_corrida.drop('descompressao', axis=1, inplace=True)
# TSS - tirei esta coluna porque neste arquivo a coluna nao tem nenhum dado
# antes do drop em outro arquivo verificar se tem valores
df_corrida.drop('training_stress_score', axis=1, inplace=True)

# Conferência
print('\n~~~~~~~~~~~~~~~~ Atividades do novo Dataframe ')
print(df_corrida['tipo'].unique())
print(f"\nTotal de treinos de corrida = {len(df_corrida)}")

## verificar NULOS NanS
print('\n~~~~~~~~~~~~~~~~ Nulos - NaNs ')
print(df_corrida.isna().sum())
print(df_corrida[df_corrida.isna().any(axis=1)])

# excluir as 3 colunas que não fazem parte das estatísticas de corrida
# colunas de natação que não fazem sentido para corrida
# total_bracadas, media_swolf, tx_media_bracadas
colunas_natacao = ['total_bracadas', 'media_swolf', 'tx_media_bracadas']
# Excluindo as colunas do dataframe df_corrida
df_corrida = df_corrida.drop(columns=colunas_natacao)

## Focar nas demais colunas com erro
# Filtra apenas as linhas onde as colunas que tem erros  possuem '--'
# 11 colunas = elevacao_min, elevacao_max, passos, fc_media, fc_max, cadencia_media, cadencia_max, comp_medio_passada,melhor_ritmo, subida_total,descida_total
colunas_erros = [
    'elevacao_min', 'elevacao_max', 
    'passos', 'fc_media', 'fc_max', 
    'cadencia_media', 'cadencia_max',
    'comp_medio_passada', 'melhor_ritmo', 
    'subida_total','descida_total'
]
erros_ = df_corrida[(df_corrida[colunas_erros] == '--').any(axis=1)]
# Exibe os resultados de erros das colunas
print("\n~~~~~~~~~~~~~~~~ Registros com '--' das colunas com erro")
print(erros_[['distancia_km','tipo','titulo']+ colunas_erros])

""" 
Resultados
~~~~~~~~~~~~~ Registros com '--' das colunas com erro
    distancia_km                tipo                          titulo elevacao_min elevacao_max  passos fc_media fc_max cadencia_media cadencia_max comp_medio_passada melhor_ritmo subida_total descida_total
69         10.01  Corrida em esteira                         Rodagem           --           --  10,496      147    163            179          250               0.95         4:17           --            --
70          9.01  Corrida em esteira                         Rodagem           --           --   9,226      147    163            177          190               0.97         5:03           --            --
76          6.00             Corrida  Cancun - Benito Juárez Corrida           --           19   7,140      132    157            172          215               0.85         4:59           43            42
87         28.02  Corrida em esteira                   Longo Esteira           --           --  29,672      144    162            172          240               0.94         4:19           --            --
137        10.01             Corrida         Porto Seguro - Potência           --           14  10,372      148    167            168          194               0.99         4:50           58            59
138        10.00             Corrida    Porto Seguro - Forte x Fraco           --           17  10,456      149    165            180          194               0.96         4:55           29            32
203         6.00  Corrida em esteira                         Esteira           --           --      --       --     --             --           --                 --           --           --            --
244        12.01             Corrida                New York Corrida           --           36  18,228      111    155            121          249               0.64         4:57           79            61
245        30.04             Corrida                New York Corrida           --           36  34,632      160    190            164          244               0.87         4:50          118           146

"""

## Caso especial 5 registros - Tratar erros e limpeza
# tenho 5 registros que tenho elevacao_max e vou substituir "--"da elevacao_min pelo mesmo valor da max 
# Filtrei apenas onde a mínima é '--' e atribuí o valor da máxima
# Trocar pela mediana e transf em numeros
# Usei .loc para garantir que estou alterando o DataFrame corrida
df_corrida.loc[df_corrida['elevacao_min'] == '--', 'elevacao_min'] = df_corrida['elevacao_max']
# Conferência= se ainda houver '--' na mínima, é porque a máxima também era '--'
erro = (df_corrida['elevacao_min'] == '--').sum()
print(f"/n ~~~~~~~~~~~~ Erros restantes após a substituição= {erro}")

## Tratar erros e limpeza geral
# agora os outros 4 registros de corrida em esteira sem elevacao_min nem elevacao_max e demais colunas com erros
# colunas: elevacao_min, elevacao_max, passos, fc_media, fc_max, cadencia_media, cadencia_max, comp_medio_passada, subida_total,descida_total
# vou substituir ambos pela Mediana, porque se colocar 0 pode alterar muito meus resultados
# mas antes tenho que: excluir a ,| substituir os '--' por nulos=NaNs | converter em float | calcular mediana | susbtituir
# aqui vou incluir as outras colunas com erro
# obs: inclui as colunas que preciso trasnformar em FLOAT: distancia_km, calorias, n_voltas
cols = [
    'elevacao_min', 'elevacao_max', 
    'passos', 'fc_media', 'fc_max', 
    'cadencia_media', 'cadencia_max',
    'comp_medio_passada', 
    'subida_total','descida_total', 'distancia_km',
    'calorias', 'n_voltas'
]
for col in cols:
    # Transformar em texto e REMOVER a vírgula (milhar)
    # "1,183" vira "1183"
    df_corrida[col] = df_corrida[col].astype(str).str.replace(',', '')
    # Trocar o erro "--" pelo nulos NaN
    df_corrida[col] = df_corrida[col].replace('--', np.nan)
    # Converter para número float
    df_corrida[col] = df_corrida[col].astype(float)

    """
    # Calcular as medianas separadas
    m_rua = df_corrida[df_corrida['tipo'] == 'Corrida'][col].median()
    m_esteira = df_corrida[df_corrida['tipo'] == 'Corrida em esteira'][col].median()

    # IF de controle: se for Corrida, preenche os vazios desta coluna com m_rua
    df_corrida.loc[df_corrida['tipo'] == 'Corrida', col] = df_corrida.loc[df_corrida['tipo'] == 'Corrida', col].fillna(m_rua)

    # IF de controle: se for Esteira, preenche os vazios desta coluna com m_esteira
    df_corrida.loc[df_corrida['tipo'] == 'Corrida em esteira', col] = df_corrida.loc[df_corrida['tipo'] == 'Corrida em esteira', col].fillna(m_esteira)
    
    """

    # Calcular a Mediana e preencher os vazios (os das esteiras)
    mediana = df_corrida[col].median()
    df_corrida[col] = df_corrida[col].fillna(mediana)

    # excessão as colunas n_voltas e passos tem que ser inteiro
    if col in ['n_voltas', 'passos']:
        # converte em inteiro "Int64" aceitas Nans
        df_corrida[col]= df_corrida[col].astype("Int64") 

print("/n ~~~~~~~~~~~~~ Dados OK ")

print('\n~~~~~~~~~~~~ Dados do registro 203 ~~~~~~~~~~~~' )
print(df_corrida.iloc[203]) 

#### tratamento da hora
# 6 Colunas: pace, tempo, melhor_ritmo, tempo_melhor_volta, tempo_movimento, duracao = "05:30" ou "00:59:34
# Tranformar em segundos|float = gráficos, machine learning, calculos
# Transformar em  Timedelta  - ainda ficará com formato data mas nao como texto str
# print(df['pace'].unique())
# print(df['tempo'].unique())
# lista o conteudo de todos os registros dessa coluna
# print(df['tipo'].tolist())
# 'def' define uma nova função. 'txt' é o nome que damos ao dado que entra nela.
cols_tempo = ['pace', 'tempo', 'melhor_ritmo', 'tempo_melhor_volta', 'tempo_movimento', 'duracao']
def segundos(hora):
    # 'pd.isna(hora)' checa se o valor é nulo =NaN 
    # 'or hora == '--'' checa se o valor é "--"
    if pd.isna(hora) or hora == '--':
        # verifica os erros conhecidos
        #  não interrompe o código porque ele vai preencher com a mediana
        print(f'erro no 1º if NaNs {hora}')
        return np.nan # retorna sem travar    
    try:
        # 'str(hora)' garante que o dado é um texto. 
        # '.split(':')' corta o texto nos dois pontos. "05:30" vira a lista ="05", "30"
        partes = str(hora).split(':')
        # 'len(partes)' conta quantos pedaços o split criou
        if len(partes) == 3: # Se tem 3 pedaços, é = HH:MM:SS
            # 'map(float, partes)' transforma cada pedaço, que era texto, em número decimal
            h, m, s = map(float, partes)
            # Faz a conta matemática para converter tudo em segundos totais.
            return h * 3600 + m * 60 + s
        elif len(partes) == 2: # Se tem 2 pedaços, é MM:SS
            m, s = map(float, partes)
            return m * 60 + s
        
        # Se não cair em 2 ou 3 partes, o formato está errado
        print(f'erro no else do if {hora}')
        return np.nan # retorna vazio
    except:
        # Se qualquer outro erro ocorrer, tipo texto onde deveria ser número
        print(f'erro no except {hora}')
        print('\n~~~~~~~~~~~~ Dados do registro 203 ~~~~~~~~~~~~' )
        print(df_corrida.iloc[203]) 
        return np.nan
    
# 'for col in cols_tempo= repete os passos abaixo para cada coluna da lista
for col in cols_tempo:
    # susbstitui os ultimos "--" por NaNs
    # esta linha serve exatamente para 1 caso de erro de melhor_ritmo em corrida esteira
    # se tiver outros erros melhor analisar antes de usar esta linha
    df_corrida[col] = df_corrida[col].replace('--', np.nan)

    # 'df_corrida['seg_'+ col]' cria uma COLUNA NOVA com nome = seg_tempo
    # '.apply(p_segundos)' pega a coluna original e "passa" cada linha pela função lá de cima.
    nome = 'seg_'+col
    df_corrida[nome] = df_corrida[col].apply(segundos)

    # '.median()' calcula o valor central da coluna nova (segundos). 
    # O Pandas ignora automaticamente os NaNs (erros) ao calcular a mediana.
    mediana_val = df_corrida[nome].median()
  
    # '.fillna(mediana_val)' procura todos os buracos (NaNs) e "carimba" a mediana neles.
    # Aqui é onde o seu erro '--' (que virou NaN) finalmente recebe um valor real.
    df_corrida[nome] = df_corrida[nome].fillna(mediana_val)
    
    # 'pd.to_timedelta()' converte a coluna ORIGINAL para o tipo "Duração de Tempo".
    # 'errors='coerce'' é o comando que força o '--' ou qualquer erro a virar NaT (vazio de tempo).
    # df_corrida[col] = pd.to_timedelta(df_corrida[col], errors='coerce')
# a coluna melhor ritmo é um texto e nao foi possivel preencher o erro faltante com a mediana
# mas posso preencher com a mediana dos segundos e transformar em texto e preencher
# Calcula a mediana dos segundos
mediana_segundos = df_corrida['seg_melhor_ritmo'].median()
# Função para transformar segundos de volta para o formato M:SS
def segundos_melhorritmo(segundos):
    minutos = int(segundos // 60)
    segs = int(segundos % 60)
    return f"{minutos}:{segs:02d}"
# agora preenche o nulo na coluna de texto usando a mediana convertida
valor_formatado = segundos_melhorritmo(mediana_segundos)
df_corrida['melhor_ritmo'] = df_corrida['melhor_ritmo'].fillna(valor_formatado)

####  Conferência FINAL Erros 
erros_ = df_corrida[(df_corrida[colunas_erros] == '--').any(axis=1)]
# Exibe os resultados de erros das colunas
print("\n~~~~~~~~~~~~~~~~ Registros com '--' das colunas com erro")
print(erros_[['distancia_km','tipo','titulo']+ colunas_erros])

def analise_geral(df_corrida):
    print("\n~~~~~~~~~~~~~~~~ Verificando erros = '--' \n")
    # Percorre todas as colunas do DataFrame automaticamente
    for col in df_corrida.columns:
        # Conta as ocorrências de '--' na coluna
        qtd_erros = (df_corrida[col] == '--').sum()
        # Imprime a qtde erros 
        if qtd_erros > 0:
            print(f"{col:25} | {qtd_erros}= Erros '--'")
        else:
            print(f"{col:25} | Limpa sem erros")
    print("\n" + "~"*50)
    print(f"Total de colunas analisadas = {len(df_corrida.columns)}")
# Chamando a função
analise_geral(df_corrida)

#### tratamento data
# as datas estão como str e trasnformei em data
df_corrida['data'] = pd.to_datetime(df_corrida['data'])
print(f'\n~~~~~~~~~~~~~~~~~~~ Tipo data = ',df_corrida['data'].dtypes)
data_min = df_corrida['data'].min()
data_max = df_corrida['data'].max()
print(f'\n~~~~~~~~~~~~~~~~~~~ Arquivo do período de {df_corrida['data'].min()} até {data_max}')

#### Conferência no 1º registro 
print('\n~~~~~~~~~~~~~~~~~~~ Dados do 1º registro ~~~~~~~~~~~~~~~' )
print(df_corrida.iloc[0]) # pega a primeira linha completa e a exibe verticalmente
print('\n~~~~~~~~~~~~~~~~~~~ Info do Arquivo ~~~~~~~~~~~~~~~' )
print(df_corrida.info())

print('\n~~~~~~~~~~~~ Dados do registro 203 ~~~~~~~~~~~~' )
print(df_corrida.iloc[203])


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 4 - Análise EAD - Exploratory Data Analysis | Análise exploratória
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Estatistica descritiva : describe(), médias, desvio padrao, correlação
# Análise Outliers : identificar picos
# Matriz Correlacao : e Heatmap

# Estatística descritiva : médias, desvio padrao, correlação
print(df_corrida.info())
pd.set_option('display.max_columns', None)  # Mostra todas as colunas
print(df_corrida.describe())

# No describe percebi que 2 colunas não são boas para treinar um modelo e nem como comparação e análise
# colunas n_voltas e seg_tempo_melhor_volta = os treinos nao tem padrão de voltas
# TSS - tirei esta coluna porque neste arquivo a coluna nao tem nenhum dado
# antes do drop em outro arquivo verificar se tem valores
df_corrida.drop(['n_voltas', 'seg_tempo_melhor_volta'], axis=1, inplace=True)

# Análise Outliers : identificar picos
# agora quero ver quais treinos estão causando o STD|desvio padrão
# Lista das colunas que queremos investigar
colunas = ['fc_media', 'fc_max', 'cadencia_media', 'cadencia_max', 'comp_medio_passada']

print("\n")
print("INVESTIGAÇÃO ERROS STD|OUTLIERS)")
for col in colunas:
    print(f"\n Coluna: {col.upper()} ------------------------")
    # aqui vai pegar os 3 menores valores 
    print(f"--- Menores valores encontrados  {col}:")
    print(df_corrida.nsmallest(3, col)[['data', 'distancia_km', 'tipo', col]])
    # aqui os 3 maiores valores
    print(f"\n--- Maiores valores encontrados  {col}:")
    print(df_corrida.nlargest(3, col)[['data', 'distancia_km', 'tipo', col]])
    print("-" *30)
    
# identifiquei 2 registros o 291 e o 32 que estão com dados incorretos e vou excluir
# axis=0 indica que estamos removendo linhas, se fosse coluna seria axis=1
# inplace=True aplica a alteração diretamente no df_corrida
df_corrida.drop([291, 32], axis=0, inplace=True)
# abaixo comando para reordenar a numeração
df_corrida.reset_index(drop=True, inplace=True)

# describe() novamente
pd.set_option('display.max_columns', None)  # Mostra todas as colunas
print(df_corrida.describe())

# Matriz Correlacao : e Heatmap
## Heatmap (Mapa de Calor) =  A Visão Geral
# preferido dos gestores. 
# Ele mostra a correlação entre todas as colunas de uma vez só, usando cores.
# usar apenas as  colunas numéricas
df_numeric = df_corrida.select_dtypes(include=[np.number])
# remove colunas de ID ou que não fazem sentido para correlação (se houverem)
# Exemplo: se tiver uma coluna 'id' ou 'index', removemos aqui
colunas_excluir = ['id', 'Unnamed: 0', 'datetime64'] 
df_numeric = df_numeric.drop(columns=[c for c in colunas_excluir if c in df_numeric.columns])
# calcula a matriz
corr = df_numeric.corr()
plt.figure(figsize=(12, 10))
# Calculamos a correlação de todas as colunas numéricas
corr = df_numeric.corr()
sns.heatmap(corr, annot=True, fmt=".2f", cmap='coolwarm', center=0)
plt.title('Mapa de Calor: Correlação entre Métricas do Garmin')
plt.show()
""" O que observar: > * Perto de 1.0 (Vermelho): Forte ligação positiva (ex: quanto mais distância, mais calorias).
Perto de -1.0 (Azul): Forte ligação negativa (ex: quanto mais cadência, menor o pace - você fica mais rápida).
Perto de 0: Nenhuma ligação.
"""


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 5 - Análise visual - gráficos | DataViz
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Histogramas, boxploots, scatter plots
# Interpretacao graficos
##### b ~ Análise visual: gráficos
## Histograma= mostra distribuição dos dados
# SEGUNDOS
plt.figure(figsize=(10, 6))
sns.histplot(df_corrida['seg_pace'], kde=True, color='teal', bins=20)
plt.title('Distribuição do Pace -SEGUNDOS')
plt.xlabel('Pace - SEGUNDOS')
plt.ylabel('Frequência/Qtde de Treinos')
plt.show()

## Histograma= mostra distribuição dos dados
# HORA
plt.figure(figsize=(10, 6))
ax = sns.histplot(df_corrida['seg_pace'], kde=True, color='teal', bins=40)
# transformaçao segundos hora
def transforma_pace(x,pos):
    min = int(x //60)
    seg = int(x % 60)
    return f"{min}:{seg:02d}"
ax.xaxis.set_major_locator(ticker.MultipleLocator(10.0))
# applicar formato x pace
ax.xaxis.set_major_formatter(ticker.FuncFormatter(transforma_pace))
plt.xticks(rotation=90, fontsize=7)
plt.title('Distribuição do Pace',fontsize=12)
plt.xlabel('Pace min/km')
plt.ylabel('Frequência/Qtde de Treinos')
plt.grid(axis='y', linestyle='--', alpha=0.3)
plt.show()


# Histograma com line data
# Vamos criar uma coluna de "Mês/Ano" para agrupar os treinos
df_corrida['mes_ano'] = df_corrida['data'].dt.to_period('M').astype(str)
# DATAVIZ (O Gráfico de Linha de Frequência por Data) ---
# Criar o FacetGrid: Um gráfico para cada Mês/Ano
# Usamos 'hue' para dar cores diferentes e 'aspect' para deixar largo
g = sns.FacetGrid(df_corrida, hue='mes_ano', palette='viridis', height=5, aspect=2)
# 2. Mapear o KDE Plot (A linha de frequência/densidade)
# x='seg_pace' é o que estamos analisando (Pace em segundos)
# fill=True preenche a área sob a linha, fica lindo!
g.map(sns.kdeplot, 'seg_pace', fill=True, alpha=0.3)
# APLICAR A MÁGICA DO TICKER (Em todos os subgráficos)
for ax in g.axes.flat:
    ax.xaxis.set_major_formatter(ticker.FuncFormatter(transforma_pace))
# Títulos e Labels
g.set_axis_labels("Pace (min/km)", "Frequência de Treinos")
g.add_legend(title="Mês/Ano do Treino")
plt.subplots_adjust(top=0.9) # Espaço para o título principal
g.fig.suptitle('Evolução da Distribuição de Pace ao Longo do Tempo', fontsize=14)
plt.show()



## BoxPlot = Caçador de Outliers
# os mínimos, máximos e quartis (25%, 50%, 75%)
plt.figure(figsize=(8, 6))
sns.boxplot(x=df_corrida['fc_max'], color='salmon')
plt.title('Análise de Outliers: Frequência Cardíaca Máxima')
plt.show()

## Scatter Plot (Dispersão)= O Gráfico de Relacionamento
# serve para ver se uma coisa afeta a outra. 
# Por exemplo: Se eu corro mais rápido (Pace menor), meu batimento cardíaco (FC) aumenta?
plt.figure(figsize=(10, 6))
sns.scatterplot(data=df_corrida, x='seg_pace', y='fc_media', hue='distancia_km', palette='viridis')
plt.title('Relacionamento: Pace vs. Frequência Cardíaca Média')
plt.show()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 6 - Machine Learnig - seleção variáveis
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# separar X=dados e y=alvo : features=variavel= X e target=alvo=y=PREVER 

print('\n~~~~~~~~~~~~~~~~ Info ')
print(df_corrida.info())

"""X = df_corrida.drop('coluna_alvo', axis=1)
y = df_corrida['coluna_alvo']

#  separar X (dados) e y (alvo)
# Separar X e y:   Classificação:  y é uma categoria=fraude/naofraude, spam/naospam
# Regressão: y é um número = preço do Imóvel
X = df_corrida.drop('coluna_alvo', axis=1)
y = df_corrida['coluna_alvo']
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 7 - Machine Learnig - dividir treino
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#  dividir treino e teste = 70/30 ou 80/20
#  Dividir Treino = 80% = perguntas e respostas e Teste 20% = perguntas e gabarito com respostas
#X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 8 - Machine Learnig - escolher  modelo
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# escolher tipo modelo: Classificação ou Regressão



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 9 - Machine Learnig - treinar modelo
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# treinar modelo com fit




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 10 - Machine Learnig - previsao avaliar modelo
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# predict



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 11 - Machine Learnig - avaliação
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
""" 
    . Classificacaoo = verificar quantos acertou - acuracia, f1-score
    . Classificacao = matriz de confusão
    ou
    . Regressao = avaliar métrica de numero
    . Regressão = mean_squared_error, mean_absolute, r2_score
    . Regressão = MSE, MAE = perto de zero melhor=menos erro

"""





