# ##############
# buscar cep quantas vezes quiser ate informar que nao quer
# se o cep for correto informa o nome da rua, bairro, cidade e estado
# Awesome API -  http:/docs.awesomeapi.com.br/api-cep
##############

import requests
import json

while True:
    cep = str(input('Digite o cep a ser consultado: ').replace('-',''))
    res = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
    endereco = res.json()

    if 'code' in endereco:
        if endereco['code'] == 'invalid':
            print('Por favor digite um cep válido')
              
        elif endereco['code'] == 'not_found':
             print(f'O cep {cep} que você digitou, não foi encontrado')
    else: # caso encontre o cep
        print(f'O cep {endereco["cep"]} está localizado na {endereco["address"]} no Bairro {endereco["district"]} em {endereco["city"]} - {endereco["state"]}')
        
    opcao = input("Deseja refazer a pesquisa cep? (S/N): ")
    if opcao.lower() == 'n':
       break  # sai do loop / while
              