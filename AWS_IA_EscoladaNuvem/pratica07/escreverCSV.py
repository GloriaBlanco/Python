"""
Aula dia 02/09/25
Leia um arquivo que contenha dados de log de
 treinamento de modelos de Machine Learning. 
 Calcule a média e o desvio padrão do tempo 
 de exercução constantes

"""
import csv
def escrevercsv(nomearquivo, dados):
    try:
        with open(nomearquivo, 'w')as arquivocsv:
            escritor = csv.writer(arquivocsv)
            escritor.writerow(['Nome', 'idade', 'Cidade'])
            for linha in dados:
                escritor.writerow(linha)

            print(f"Arquivo saldo com sucesso em {nomearquivo}")
    except Exception as erro:
        print(f"Erro {erro} ao salvar o arquivo.")

dados = [
    {'Ana', 28, 'Rio de janeiro'},
    {"Bernardo", 51, 'Sao Paulo'},
    {'Claudio', 29, 'Rio de janeiro'},
    {'Beto', 81, 'Salvador'},
]

if __name__ == "__main__":
    nomearquivo =input('Digite o nome do arquivo CSV: ').strip()
    escrevercsv(nomearquivo, dados)

