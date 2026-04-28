# Jogo da advinhação
# programa python atraves do random seleciona um numero aleatoriamente entre 1 e 10
# o usuário entra com numero tentando acertar o numero escolhido pelo python
# quando usuário acerta ele interronpe o while e imprimi as tentativas do usuário

print(' ********************************************* ')

import random

def jogo_advinhacao():
    numero_secreto = random.randint(1,10)
    tentativas = 0

    print("Bem-vindo ao jogo de advinhação! ")
    print("Eu escolhi um número entre 1 e 10.")
    print("Tente Advinhar!")
    
    while  True: # while funciona ate voce acertar
        tentativa = int(input("Digite o seu palpite: "))
        tentativas += 1
        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns !!! Você acertou em {tentativas}  tentativas.")
            break # interrompe o while assim que acerta numero
# inicia jogo
jogo_advinhacao()
                

