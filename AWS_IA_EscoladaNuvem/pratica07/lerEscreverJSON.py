"""
Crie um script em Python que leia e escreva dados 
em um arquivo JSON. O arquivo JSON deve conter 
informações de uma pessoa, com campos nome, idade e cidade.

"""

import json

def lerjson(nomedoarquivo):
    try:
        with open(nomedoarquivo, "r") as arquivo_json:
            dados = json.load(arquivo_json)
            print(dados)
    
    except FileNotFoundError:
        print("Erro !! Arquivo não encontrado !!")

def escreverjson(nomedoarquivo, dados):
    try:
        with open(nomedoarquivo, "w") as arquivo_json:
            json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
            print(f"Dados foram salvos em {nomedoarquivo}")
    
    except Exception as erro:
        print("Erro {erro} !! Arquivo não encontrado !!")

dados = {
    'Nome': 'João',
    'Idade': 25,
    "Cidade": 'Rio de Janeiro'
}

if __name__ == "__main__":
    nomearquivo = input('Digite o nome do arquivo JSON: ')
    escreverjson(nomearquivo, dados)
    lerjson(nomearquivo)



    