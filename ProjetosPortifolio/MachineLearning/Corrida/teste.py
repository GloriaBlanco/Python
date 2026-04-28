import pandas as pd
print("--- INICIANDO TESTE ---")

try:
    df = pd.read_csv('ActivitiesOriginal.csv') # Coloque o nome correto do seu CSV aqui
    print("Arquivo carregado com sucesso!")
    print(df.head())
except Exception as e:
    print(f"Erro ao carregar: {e}")

print("--- FIM DO TESTE ---")