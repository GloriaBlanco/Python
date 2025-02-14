# Pandas objeto dataFrame conjunto de dados numa tabela

import pandas as pd
dicionario = {'Autores':['Rick','JRR','Rick','Riordan'], 'Titulo': ['Ladrao','Sociedade','Policia', 'Memorias'], 'Preco': [41.2,35.7,77.77,40.5]}
df= pd.DataFrame(dicionario)
print(df['Autores'][1])
print(df['Autores'])
print(df['Preco'])

print('###############  Encontra item especific ###########')

mascara =(df['Autores'] == 'Rick')
print(df[mascara])

print('###############  Encontra item especific ###########')

mask_corr = df['Titulo'] == "Ladrao"
print(mask_corr)

# substitui todos os titulos ---- mask_corr = df['Titulo'] = 'Ladrão'
print('############### Correção nomr especific ###########')

mask = df.loc[mask_corr, 'Titulo'] = "Ladrão"

print(mask)
print(df)

print('###############  df2 ###########')
new = {'Autores':['Jordan'], 'Titulo':['Titã'], 'Preco':[4.20]}
df2 = pd.DataFrame(new)
print(df2)
df = pd.concat([df, df2])
print(df)

#result = df.append(new_row, ignore_index=True)



print(df[df['Autores']=='Rick']['Titulo'])

df = df.append('glo','python','40')
print(df)

