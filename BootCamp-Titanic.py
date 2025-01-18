### Desafio 3

from pydataset import data
import pandas as pd


df_navio = data('titanic')
print(df_navio.head(1316))


# 2. Quantas pessoas sobreviveram e quantas morreram?
sobreviventes = df_navio[df_navio['survived'] == 'yes'].shape[0]
mortos = df_navio[df_navio['survived'] == 'no'].shape[0]


# soobreviventes
tabela = pd.DataFrame({'Descrição': ['Pessoas que sobreviveram', 'Pessoas que morreram'], 'Qtde': [sobreviventes, mortos] })
print(tabela)

dataTitanic = data('titanic')
classe1 = dataTitanic[dataTitanic['class'] == '1st class'].shape[0]
classe2 = dataTitanic[dataTitanic['class'] == '2nd class'].shape[0]
classe3 = dataTitanic[dataTitanic['class'] == '3rd class'].shape[0]

# por classe
classe = pd.DataFrame({ 'Descrição': ['Pessoas 1ª classe', 'Pessoas 2ª classe', 'Pessoas 3ª classe'], 'Qtde': [classe1, classe2, classe3] })

print(classe)

# 1ª classe
# sobreviventes
sobreviventes_1classe = dataTitanic[(dataTitanic['class'] == '1st class') & (dataTitanic['survived'] == 'yes')].shape[0]
# porcentagem
porcentagem_sobreviventes_1classe = (sobreviventes_1classe / classe1) * 100 if classe1 > 0 else 0
# mortos
mortos_1classe = dataTitanic[(dataTitanic['class'] == '1st class') & (dataTitanic['survived'] == 'no')].shape[0]
# porcentagem
porcentagem_mortos_1classe = (mortos_1classe / classe1) * 100 if classe1 > 0 else 0

# 2ª classe
# sobreviventes
sobreviventes_2classe = dataTitanic[(dataTitanic['class'] == '2nd class') & (dataTitanic['survived'] == 'yes')].shape[0]
# porcentagem
porcentagem_sobreviventes_2classe = (sobreviventes_2classe / classe2) * 100 if classe2 > 0 else 0
# mortos
mortos_2classe = dataTitanic[(dataTitanic['class'] == '2nd class') & (dataTitanic['survived'] == 'no')].shape[0]
# porcentagem
porcentagem_mortos_2classe = (mortos_2classe / classe2) * 100 if classe2 > 0 else 0

# 3ª classe
# sobreviventes
sobreviventes_3classe = dataTitanic[(dataTitanic['class'] == '3rd class') & (dataTitanic['survived'] == 'yes')].shape[0]
# porcentagem
porcentagem_sobreviventes_3classe = (sobreviventes_3classe / classe3) * 100 if classe3 > 0 else 0
# mortos
mortos_3classe = dataTitanic[(dataTitanic['class'] == '3rd class') & (dataTitanic['survived'] == 'no')].shape[0]
# porcentagem
porcentagem_mortos_3classe = (mortos_3classe / classe3) * 100 if classe3 > 0 else 0

# imprimindo
print("____________________________________________________")
print("____________________________________________________")
print("Sobreviventes e Mortos por Classe:")
print("____________________________________________________")

tabela = pd.DataFrame({
    "Classe": ["1ª classe", "1ª classe", "2ª classe", "2ª classe", "3ª classe", "3ª classe"],
    "Descrição": ["Sobreviventes", "Mortos", "Sobreviventes", "Mortos", "Sobreviventes", "Mortos"],
    "Quantidade": [sobreviventes_1classe, mortos_1classe, sobreviventes_2classe, mortos_2classe, sobreviventes_3classe, mortos_3classe],
    "Porcentagem": [f"{porcentagem_sobreviventes_1classe:.2f}%", f"{porcentagem_mortos_1classe:.2f}%", f"{porcentagem_sobreviventes_2classe:.2f}%", f"{porcentagem_mortos_2classe:.2f}%", f"{porcentagem_sobreviventes_3classe:.2f}%", f"{porcentagem_mortos_3classe:.2f}%"]
})
print(tabela)


# outra forma de tabela
print("____________________________________________________")
print("____________________________________________________")
tabela = pd.DataFrame({
    "Descrição": ["Sobreviventes", "Mortos", "% Sobreviventes", "% Mortos"],
    "1ª classe": [sobreviventes_1classe, mortos_1classe, f"{porcentagem_sobreviventes_1classe:.2f}%", f"{porcentagem_mortos_1classe:.2f}%"],
    "2ª classe": [sobreviventes_2classe, mortos_2classe, f"{porcentagem_sobreviventes_2classe:.2f}%", f"{porcentagem_mortos_2classe:.2f}%"],
    "3ª classe": [sobreviventes_3classe, mortos_3classe, f"{porcentagem_sobreviventes_3classe:.2f}%", f"{porcentagem_mortos_3classe:.2f}%"]
})
print(tabela)


# SOBREVIVENTES
print("____________________________________________________")

tabela_sobreviventes = pd.DataFrame({
    "Descrição": ["Quantidade", "Porcentagem"],
    "1ª classe": [sobreviventes_1classe, f"{porcentagem_sobreviventes_1classe:.2f}%"],
    "2ª classe": [sobreviventes_2classe, f"{porcentagem_sobreviventes_2classe:.2f}%"],
    "3ª classe": [sobreviventes_3classe, f"{porcentagem_sobreviventes_3classe:.2f}%"]
})

# MORTOS
print("____________________________________________________")
print("____________________________________________________")
tabela_mortos = pd.DataFrame({
    "Descrição": ["Quantidade", "Porcentagem"],
    "1ª classe": [mortos_1classe, f"{porcentagem_mortos_1classe:.2f}%"],
    "2ª classe": [mortos_2classe, f"{porcentagem_mortos_2classe:.2f}%"],
    "3ª classe": [mortos_3classe, f"{porcentagem_mortos_3classe:.2f}%"]
})


# Exibir as tabelas
print("____________________________________________________")
print("SOBREVIVENTES___________________________________")
print(tabela_sobreviventes)
print("____________________________________________________")
print("MORTOS__________________________________________")
print(tabela_mortos)



