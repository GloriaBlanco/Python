### Pandas
import pandas as pd
dados = {'Nome':['Max', 'Bella'],
         'Raca' :['Labrador', 'Poodle'],
         'Cor' :['Amarelo', 'branco']}
df_cacho = pd.DataFrame(dados)
print(df_cacho)

df = pd.read_csv('carros.csv')
df.head()
print(df.head())
print(df.head(2))
print(df.columns)
print(df.index)

# sort couna
print(df.sort_values('Quant Carros', ascending=False))

# quantidade carros polulação do estado
proporcao=(df['Quant Carros']/df['População do Estado'])
print(proporcao)

df['Carros por habitantes'] = proporcao      
print(df.head())

df_estado_hab = df[['Estado', 'Carros por habitantes']]
print(df_estado_hab)

####  Atividade 2
df_concurso = pd.read_csv('concurso.csv')
print(df_concurso.head())

# quantas pessoas sao do estado PI, usar count()
contando = df_concurso[df_concurso['Estado'] == "PI"].count()
print(contando)

# quantas pessoas sao do estado PI, selecionar tamebm o numero de inscrico
contandoinscricao = df_concurso[df_concurso['Estado'] == "PI"]['Número de Inscrição'].count()
print(contandoinscricao)

contandogrupo = df_concurso[['Número de Inscrição', 'Estado']].groupby([df_concurso['Estado']=="PI"]).count()
print(contandogrupo)


## grupo novo
contandogrupo = df_concurso[['Estado', 'Escolaridade', 'Número de Inscrição']].groupby(['Estado', 'Escolaridade']).count()
print(contandogrupo)

## grupo novo com escolaridade superior
contandogrupo = df_concurso[['Estado', 'Escolaridade', 'Número de Inscrição']].groupby([df_concurso['Escolaridade']=="Ensino Superior"]).count()
print(contandogrupo)


## qual a porcentagem de pessoas com deficiencia
contaporcent = df_concurso['Deficiência'].value_counts(normalize=True)
print(contaporcent)
print(df_concurso)

## qual a porcentagem de pessoas com deficiencia e vezes 100 para aparecer porcetagem
contaporcent = df_concurso['Deficiência'].value_counts(normalize=True)*100
print(contaporcent)

