"""
Crie um programa que gera uma senha aleatória com o módulo random,
 utilizando caracteres especiais, possibilitando o usuário a 
 informar a quantidade de caracteres dessa senha aleatória.
"""

import random  # gera numeros aleatorios
import string  # trabalha com caracteres

print("----------- Gera senha aleatório -----------")
def gerarsenha(tamanho):
    # caracteres variavel vai armazenar  todas as maisculas e minusculas e numeros
    caracteres = string.ascii_letters + string.digits + "!@#$%^&?/"
    # escolhendo de maneira aleatoria dentro do caracteres
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

tamanho_senha = int(input("Digite o tamanho da senha desejada: "))
nova_senha = gerarsenha(tamanho_senha)

print(f"Sua senha gerada é : {nova_senha}")

