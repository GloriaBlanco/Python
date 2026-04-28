

def soma():
    calculo = 10+2
    print(f"O resultado da soma é : {calculo}")

def subtracao():
    calculo = 10-2
    print(f"o resultado da substraçao é : {calculo}")
    multiplicacao() # chamando uma funcao dentro de outra funçao
    print('Chamei a função multiplicação dentro da subtraçao')

def multiplicacao():
    calculo = 10*2
    print(f"o resultado da multiplicação é : {calculo}")


# chama função
soma() 
subtracao()
multiplicacao()

### função com entrada do usuário

def soma():
    numero1 = int(input('Digite o primeiro numero = '))
    numero2 = int(input('Digite o segundo numero = '))
    calculo = numero1+numero2
    print(f"Usuário = O resultado da soma é : {calculo}")

def subtracao():
    numero1 = int(input('Digite o primeiro numero = '))
    numero2 = int(input('Digite o segundo numero = '))
    calculo = numero1-numero2
    print(f"Usuário = o resultado da substraçao é : {calculo}")
    multiplicacao() # chamando uma funcao dentro de outra funçao
    print('Chamei a função multiplicação dentro da subtraçao')

def multiplicacao():
    numero1 = int(input('Digite o primeiro numero = '))
    numero2 = int(input('Digite o segundo numero = '))
    calculo = numero1*numero2
    print(f"Usuário = o resultado da multiplicação é : {calculo}")

# chama função
soma() 
subtracao()
multiplicacao()

### função com parametros

def soma(numero1,numero2):
    calculo = numero1+numero2
    print(f"Parametros == O resultado da soma é : {calculo}")

def subtracao(numero1,numero2):
    calculo = numero1-numero2
    print(f"Parametros ==o resultado da substraçao é : {calculo}")
    multiplicacao(numero1,numero2) # chamando uma funcao dentro de outra funçao
    print('Chamei a função multiplicação dentro da subtraçao')

def multiplicacao(numero1,numero2):
    calculo = numero1*numero2
    print(f"Parametros==o resultado da multiplicação é : {calculo}")


numero1 = int(input('Digite o primeiro numero = '))
numero2 = int(input('Digite o segundo numero = '))

# chama função
soma(numero1,numero2) 
subtracao(numero1,numero2)
multiplicacao(numero1,numero2)


