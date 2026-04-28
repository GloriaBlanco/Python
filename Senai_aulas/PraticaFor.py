# Aula Senai 26/02/2024
# Aula for  -----------------------------------------------------------
nomes ='Glória' 
for n in nomes: # imprimi 1 letra em cada linha até terminar o nome
    print(n)

for i in range(6): # imprimi 6 numeros iniciando em 0, sendo, 0,1,2,3,4,5
    print(i)

for i in range(0,9,2): # imprimi desde 0 até o 9, pulando de 2 em 2, será impresso 0,2,4,6,8
    print(i)

for i in range(0,8,2): # imprimi desde 0 até o 8, pulando de 2 em 2, será impresso 0,2,4,6 OBS aqui nao vai imprimir o 8
    print(i)

def tabuada(numero):
    for i in range(1, 11):  
        resultado = numero*i
        print(f"{numero} x {i} = {resultado}")
# exemplo: Tabuada do 7
tabuada(7)





# abaixo temos uma entrada do usuário de 8 numeros inteiros e no final a soma será de todos os numeros pares digitados
print(' **************************************************************** ')
print('Soma somente numeros pares digitados')
soma = 0
contar = 0
for i in range(1,8):
    num = int(input(f'Digite o  {i}º número:  '))

    if num % 2 == 0:
        soma +=num
        contar += 1

print(f'A soma dos {contar} numero PARES foi igual a {soma}')




# usurário que digita até que numero quer imprimir e quantos quer pular na impressao
print(' **************************************************************** ')
print('Usuário escolhe até que numero vai imprimir e quantos vai pular')
num1 = int(input('Digite até qual número você quer chegar:  '))
num2 = int(input('Digite de quantos em quantos números você quer pular:  '))

for i in range(0,num1+1,num2):
    print(i)



# Aula while -----------------------------------------------------------

# Jogo da advinhação
print(' **************************************************************** ')
import random

def jogo_advinhacao():
    numero_secreto = random.randit(1,10)
    tentativas = 0

    print("Bem-vindo ao jogo de advinhação! ")
    print("Eu escolhi um número entre 1 e 10.")
    print("Tente Advinhar!")
    
    while  True:
        tentativa = int(input("Digite o seu palpite: "))

        tentativas += 1

        if tentativa < numero_secreto:
            print("Tente um número maior.")
        elif tentativa > numero_secreto:
            print("Tente um número menor.")
        else:
            print(f"Parabéns !!! Você acertou em {tentativas}  tentativas.")
            break
# inicia jogo
        jogo_advinhacao()
                



