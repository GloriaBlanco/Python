import pandas as pd
import numpy  as np

vida = pd.read_csv('saude_do_sono_estilo_vida.csv')
vida.head()
print(vida.head(375))
print(vida.columns)
print(vida.index)

## Atividade 1
vida = vida.rename(columns={'ID': 'Identificador'})
print(vida.columns)

vida = vida.rename(columns={'Pressão sanguíneaaaa': 'Pressão sanguínea'})
print(vida.columns)

vida = vida.rename(columns={'Ocupação': 'Profissão'})
print(vida.columns)

vida = vida.rename(columns={'Categoria BMI': 'Categoria IMC'})
print(vida.columns)

# Atividade 2
med = vida[['Duração do sono']].groupby([vida['Profissão']]).mean()
print(f'Média',med)

mediana = vida[['Duração do sono']].groupby([vida['Profissão']]).median()
print(f'Mediana', mediana)

#mod = vida[['Duração do sono']].groupby([vida['Profissão']]).mode()
#print(mod)

geral = vida[['Duração do sono']].groupby([vida['Profissão']]).describe()
print(geral)


# Atividade 3
# porcentagem obesos em Engenharia de Software
obesos = ((vida[vida['Profissão']=="Eng. de Software"])['Categoria IMC'].value_counts()['Obesidade'] / (vida[vida['Profissão']=="Eng. de Software"]).shape[0]) * 100
print(f"OBESOS em Engenharia de Software são ",obesos, '%')

#Atividade 4
#quem faz dormir menos advogar ou repsent vendas, isin media

#sonoadv = (vida[vida['Profissão'].isin(["Advogado(a)"])])
#sonorepr = (vida[vida['Profissão'].isin(["Representante de Vendas"])])
#sonoadv = sonoadv['Duração do sono'].mean()
#sonorepr = sonorepr['Duração do sono'].mean()
##  outra forma
print("##Atividade 4 #####")
sonoadv = (vida[vida['Profissão'].isin(["Advogado(a)"])])['Duração do sono'].mean()
sonorepr = (vida[vida['Profissão'].isin(["Representante de Vendas"])])['Duração do sono'].mean()
print(f'média sono advogado',sonoadv)
print(f'média sono representante de vendas', sonorepr)

if sonoadv > sonorepr:
    print('Representantes de vendas dormem menos')
else:
    print('Advogados(as) dormem menos')

# Atividade 5
# Enfermagem ou medicina quem dorme menos
print("##Atividade 5 #############")

sonomed = (vida[vida['Profissão'].isin(["Médico(a)"])])['Duração do sono'].mean()
sonoenf = (vida[vida['Profissão'].isin(["Enfermeiro(a)"])])['Duração do sono'].mean()
print(f'média sono Médico ',sonomed)
print(f'média sono Enfermeiro ', sonoenf)
if sonomed> sonoenf:
    print('Enfermeiros(as) dormem menos')
else:
    print('Médicos(as) dormem menos')

# Atividade 6
# criar subconjunto do dataframe vida com apenas colunas Idade e Gênero
print("######## Atividade 6 #############")
subconj = vida[['Identificador', 'Gênero', 'Idade','Pressão sanguínea','Frequência cardíaca']]
print(subconj)
print('##################')

#Atividade 7
# como saber a profissao que  menos aparece no dataframe vida
print("####### 7 ###############")
print(vida['Profissão'].value_counts())
print(f'Gerente menos aparece')


# Atividade 8 
# quem tem maior pressao sanguínea homens ou mulheres, pela média

print("######   Atividade 8 #############")

vida[['Sistolica','Asistolica']] = vida['Pressão sanguínea'].str.split('/', expand=True).astype(int)
print(vida.head())
pressao = vida.groupby('Gênero').agg({'Sistolica':'mean','Asistolica':'mean'})
print(pressao)
#agora como comparar a pressao de homem e mulheres
homens = (pressao.loc['Homem','Sistolica'])
mulheres = (pressao.loc['Mulher','Sistolica']) 
print(f'pressão homens =', homens)
print(f'pressão mulheres =', mulheres)

if homens > mulheres:
    print('Homens têm maior pressão sanguínea')
else:
    print('Mulheres têm maior pressão sanguínea')

# Atividade 9
print(vida['Duração do sono'].mode())
print('Não, é predominante dormirem 8 horas por dia')

# Atividade 10
#Pessoas com frequências cardíacas acima de 70 dão mais passos que
#pessoas com frequência cardíaca menor ou igual a 70? (Use a média)
print("########## 10 ##############")

freq70 = vida[vida['Frequência cardíaca'] > 70]['Passos diários'].mean()
freqmenor70 = vida[vida['Frequência cardíaca'] <= 70]['Passos diários'].mean()

print(f'freq > 70 = ',freq70,'média de passos')
print(f'freq <= 70 = ',freqmenor70,'média de passos')
if freq70 > freqmenor70:
    print('Pessoas dão mais passos com frequencia cardiaca maior que 70')
else:
    print('Pessoas dão menos passos com frequencia cardiaca > que 70')
    print('ou seja, pessoas com frequencia cardiaca < = a 70 dão mais passos')

print(vida[vida['Frequência cardíaca'] > 70]['Passos diários'].sum())

print(vida[vida['Frequência cardíaca'] <= 70]['Passos diários'].sum())
