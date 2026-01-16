### Criação do arquivo de vendas para análise

import pandas as pd

# 1. CRIAR OS DADOS (Os ingredientes do nosso exemplo)
dados = {
    'Investimento_Marketing': [100, 200, 300, 400, 500, 600, 700, 800],
    'Vendas': [1100, 2300, 2900, 4100, 4800, 6200, 6900, 8100]
}

# 2. TRANSFORMAR EM DATAFRAME (A estrutura de tabela do Pandas)
df = pd.DataFrame(dados)

# 3. SALVAR COMO .CSV (Criar o ficheiro no teu computador)
# sep=';' é o melhor para abrir diretamente no Excel em Português
# index=False evita que o Python salve a coluna de contagem (0, 1, 2...)
df.to_csv('exemplovendas.csv', index=False, sep=';', encoding='utf-8-sig')

print("Arquivo 'exemplovendas.csv' criado com sucesso na tua pasta!")