""" 
Aula dia 02/09/25
Crie um script en Python que leia um arquivo 
CSV e exiba os dados na tela. 
O arquivo CSV deve conter informações 
de pessoas, com colunas Nome, Idade e 
Cidade.

"""
import csv

def lercsv(nomearquivo):
    try:
        with open(nomearquivo, 'r')as arquivocsv:
            ler = csv.reader(arquivocsv)
            for linha in ler:
                print(linha)

            print(f"Arquivo lido com sucesso !!!")

    except FileNotFoundError as erro:
        print(f"Erro {erro} Arquivo não encontrado.")
    except Exception as erro:
        print(f"Erro {erro}!!!")

if __name__ == "__main__":
    nomearquivo =input('Digite o nome do arquivo CSV: ').strip()
    lercsv(nomearquivo)


