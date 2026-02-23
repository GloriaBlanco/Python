"""
O arquivo original do kaglle creditcard.csv era muito grande para baixar para o github
Usei este código para diminuir o numero de registros e assim diminuir arquivo
"""

import pandas as pd

# 1. Carregar o arquivo gigante
print("Lendo o arquivo original .............")

df = pd.read_csv("creditcard.csv")

# 2. separar quem e fraude Class=1 e quem nao é class=0
fraude = df[df['Class']==1]
naofraude = df[df['Class']==0]


# 3. Criar uma amostra equilibrada de 10.000 registros aleatórios
# vou pegar proporcional ao arquivo original fraude e nao fraude
# original tenho 56.864 = 0 = 99.828% e 98 = 1 = 1.172%
# novo arquivo deve ter 9983 = 0 e 17 = 1
# O sample aceita o random_state
# poderia usar o head() mas nao aceita o random_state
df_amostrafraude = fraude.sample(n=17, random_state=42)
df_amostranaofraude = naofraude.sample(n=9983, random_state=42)

# 4. juntar os 2 arquivos
# frac=1: Significa "fração de 100%". Ou seja, eu quero que o Python pegue todos os dados existentes, mas em uma ordem aleatória. Se eu usasse frac=0.5, ele pegaria apenas metade.
#  reset_index(drop=True) = Quando você embaralha ou junta tabelas, os números das linhas (os índices na esquerda) ficam todos bagunçados (ex: a linha 500 vira a primeira, a linha 10 vira a segunda)
#  drop=True: Diz ao Python: "Apague os números de linha antigos e crie uma nova sequência começando do 0, 1, 2...". Se você não colocar isso, o Python cria uma coluna extra chamada "index" com os números velhos, o que só suja o seu arquivo.

df_amostrafinal = pd.concat([df_amostrafraude, df_amostranaofraude])
df_amostrafinal = df_amostrafinal.sample(frac=1, random_state=42).reset_index(drop=True)

# 5. Salvar o novo arquivo,  criando um novo .csv

df_amostrafinal.to_csv('creditcard_reduzido.csv', index=False)

print(f"Arquivo reduzido salvo com sucesso! Novo tamanho: {len(df_amostrafinal)} registros.")

# 6. verificando arquivo
df = pd.read_csv("creditcard_reduzido.csv")

print(df.info())