# Análise de Vendas 
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# ==========================================
# PASSO 1, 2 e 3: INGESTÃO E LIMPEZA
# ==========================================
try:
    # Lendo o arquivo CSV (O separador ';' é comum no Brasil)
    df = pd.read_csv('exemplovendas.csv', sep=';') 
    
    # Removendo linhas que tenham qualquer valor vazio para não confundir o robô
    df = df.dropna() 

    print("Dados carregados e limpos com sucesso!")
except FileNotFoundError:
    print("Erro: O arquivo 'exemplovendas.csv' não foi encontrado na pasta.")

print(df.describe())

# ==========================================
# PASSO 5: PRÉ-PROCESSAMENTO (Preparar Ingredientes)
# ==========================================
# O Scikit-Learn (nosso robô) exige que os dados de entrada (X) 
# estejam em um formato de matriz (linhas e colunas separadas).
# O .values converte a coluna do Pandas em uma lista simples do Numpy.
# O .reshape(-1, 1) organiza essa lista em uma coluna vertical oficial.
X = df['Investimento_Marketing'].values.reshape(-1, 1)

# A saída (y) é o que queremos prever (o resultado do bolo).
y = df['Vendas'].values

# ==========================================
# PASSO 6: MODELAGEM (Treinar o Robô)
# ==========================================
# Criamos uma instância do modelo (compramos um robô de fábrica)
modelo = LinearRegression()

# O comando .fit é o TREINAMENTO. 
# Aqui o robô olha para X e y e descobre a regra matemática entre eles.
modelo.fit(X, y)

# ==========================================
# PREVISÃO E ENTREGA (O Resultado)
# ==========================================
# Queremos saber: "Se eu investir 600, quanto vou vender?"
# Precisamos passar o 600 no mesmo formato de "potinho" (matriz) que o robô aprendeu.
entrada_teste = np.array([[600]])
previsao = modelo.predict(entrada_teste)

print(f"--- RESULTADO DA ANÁLISE ---")
print(f"Se o investimento for 600, a previsão de vendas é: R$ {previsao[0]:.2f}")

# Salvando a tabela final em Excel para mostrar ao chefe
df.to_excel('ResultadoAnaliseVendas_Excel.xlsx', index=False)
print("Relatório salvo em 'ResultadoAnaliseVendas_Excel.xlsx!")
# index=False evita que o Pandas salve aquela coluna de números (0, 1, 2...) lateral

# Salva em CSV usando o ponto e vírgula como separador (padrão do Excel no Brasil)
df.to_csv('ResultadoAnaliseVendas_CSV.csv', sep=';', index=False, encoding='utf-8-sig')
print("Relatório salvo em 'ResultadoAnaliseVendas_CSV.csv!")