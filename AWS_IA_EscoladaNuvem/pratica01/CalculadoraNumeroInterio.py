"""
5- Calculadora de Número Inteiro
Leia quatro valores inteiros A, B, C e D.
A seguir, calcule e mostre a diferença do produto de A e B pelo produto de C e D segundo a fórmula: DIFERENCA = (A * B - C * D).
Entrada: O arquivo de entrada contém 4 valores inteiros. 
Saída: Imprima a mensagem "DIFERENCA = " com todas as letras maiúsculas.
"""

a = int(input("Digite o 1º numero inteiro A = "))
b = int(input("Digite o 2º numero inteiro B = "))
c = int(input("Digite o 3º numero inteiro C = "))
d = int(input("Digite o 4º numero inteiro D = "))
diferenca = (a * b - c * d)
print("DIFERENCA (A*B-C*D) = ", diferenca) 

# com controle para garantir que o numero seja inteiro
def ninteiro(numero):
    while True:
        try:
            return int(input(numero))
        except ValueError:
            print("Por favor, digite um número inteiro.")

a = ninteiro("Digite o 1º numero inteiro A = ")
b = ninteiro("Digite o 2º numero inteiro B = ")
c = ninteiro("Digite o 3º numero inteiro C = ")
d = ninteiro("Digite o 4º numero inteiro D = ")
diferenca = (a * b - c * d)
print("DIFERENCA (A*B-C*D) = ", diferenca)


