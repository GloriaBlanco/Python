#programa gereador de senha
import random
import string

def gerar_senha(tamanho): # funcao gerar senha
    caracteres = string.ascii_letters + string.digits + string.digits + "!@#?&" *2 # seleciona quais caracteres especiais pode ter
    senha = ' '.join(random.choice(caracteres) for _ in range(tamanho))
    return senha

i = 0
# tamanho_senha = int(input("Digite a quantidade de caracteresque deseja: ")) # usuario informa/digita quantos caracteres pode ter
#senha_gerada = gerar_senha(tamanho_senha) # chama funcao para gerar senha
#print("A senha gerada é:", senha_gerada)  # imprimi senha gerada

while True: # enquanto quiser refazer senha fica no loop
    tamanho_senha = int(input("Digite a quantidade de caracteres que deseja: "))
    senha_gerada = gerar_senha(tamanho_senha)
    print("A senha gerada é: ", senha_gerada)
    opcao = input("Deseja refazer a senha? (S/N): ")
    if opcao.lower() == 'n': #opcao digitada for n sai do while e encerra, se for outra ler
         break        
    