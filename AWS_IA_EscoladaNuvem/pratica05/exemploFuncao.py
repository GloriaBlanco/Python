"""
Aula 27/08/25
Função

"""
print("---------- Função ----------")
def saudacao():
    print("Olá, bem vindo ao curso de Python!")

saudacao()


def cumprimentar(nome):
    mensagem = f"Olá, {nome}! Bem-vindo ao Python."
    return mensagem

# usando a função
saudacao = cumprimentar("Glória")
print(saudacao)

print("---------- Soma ----------")
def soma(a, b):
    resultado = a+b
    return resultado

total = soma(5,3)
print(f"O total = {total}")

print("---------Funções anônimas Lambda ----------")
multiplicar = lambda x, y: x * y
resultado = multiplicar(4,5)
print(f"O resultado = {resultado}")

print("--------- Exemplo Lambda ----------")
numero = int(input("Digite um número : "))
quadrado = lambda x: x ** 2
resultado = quadrado(numero)
print(f"O quadrado de {numero} = {resultado}")
print(f"Outra forma: O quadrado de {numero} = {quadrado(numero)}")

print("--------- + Exemplo Lambda ----------")
produto = lambda x, y: x * y
print(f"O produto {produto(3,3)}")

print("--------- Função do exemplo Lambda --------")
def multiplicacao(num1, num2):
    resultadof = num1 * num2
    return resultadof

multi = multiplicacao(3,3)
print(f"Resultado função = {multiplicacao(3,3)}")
print(f"resultado variavel multi = {multi}")

print("--------- Função Aônima com Lambda --------")
multiplicar2 = lambda x, y: x * y
resultado2 = multiplicar2(4,5)
print(f"O resultado é = {multiplicar2(4,5)}")
print(f"O resultado variavel = {resultado2}")

