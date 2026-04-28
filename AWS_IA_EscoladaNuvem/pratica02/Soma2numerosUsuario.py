"""
Aula 20/08/25
5- Calculadora de Soma com Entrada do Usuário
Leia 2 valores inteiros e armazene-os nas variáveis A e B. 
Efetue a soma de A e B, atribuindo o seu resultado à 
variável X. 
Entrada: A entrada contém 2 valores inteiros informados 
pelo usuário. 
Saída: Imprima a mensagem "X = " (letra X maiúscula) seguido
pelo valor da variável X e pelo final de linha.

"""
# variáveis

# entrada usuário
print("-------- Calculadora soma -------")
A = int(input("Digite um número : "))
B = int(input("Digite mais um número : "))

# cálculo
X = A+B

# exibir
print("--------- Soma -----------")
print(f"X = {A} + {B} ")
print(f"X = {X}")


### outra forma com controle que o numero seja inteiro
print("/n----------------------------------------------")
print("---- Controle para garantir numero inteiro ----")

# entrada usuário
print("-------- Calculadora soma ---------")

def entrada(msg):
    while True:
        try: 
            numero = int(input(msg))
            return numero
        except ValueError:
            print("Entrada inválida!! \nPor favor, digite um numero inteiro.")

A = entrada("Digite um número : ")
B = entrada("Digite mais um número : ")

# cálculo
X = A + B

# exibir
print("--------- Soma -----------")
print(f"X = {A} + {B}")
print(f"X = {X}\n")
