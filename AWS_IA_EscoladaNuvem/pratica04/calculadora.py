"""
Aula 25/08/25
Prática 04

Desenvolva uma calculadora em Python que realize as quatro operações básicas 
(adição, subtração, multiplicação e divisão) entre dois números. A calculadora 
deve ser capaz de lidar com diversos tipos de erros de entrada e operação. 
Siga as especificações abaixo:
A calculadora deve solicitar ao usuário que insira dois números e uma operação.
As operações válidas são: + (adição), - (subtração), * (multiplicação) e / (divisão).
O programa deve continuar solicitando entradas até que uma operação válida seja concluída.
Trate os seguintes erros:
Entrada inválida (não numérica) para os números
Divisão por zero
Operação inválida
Use try/except para capturar e tratar os erros apropriadamente.
Após cada erro, o programa deve informar o usuário sobre o erro e solicitar nova entrada.
Quando uma operação é concluída com sucesso, exiba o resultado e encerre o programa.
"""

print('---------- Calculadora --------------')

while True:
    try: 
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número:"))
        operacao = input("Qual operação deseja (+, -, X, /) ? ")

        if operacao == "+":
            resultado = n1+n2
        elif operacao == "-":
            resultado = n1-n2
        elif operacao == "x":
            resultado = n1*n2
        elif operacao == "/":
            resultado = n1/n2
        elif operacao == "@":
            # testado raise com @
            raise ValueError("Estou testanto RAISE, digitei @")
        else:
            # resultado = "Operação inválida"
            raise ValueError("Operação inválida")

        print(f"Resultado da operação de {n1} {operacao} {n2} = {resultado}")
        break

    except ZeroDivisionError:
        # se for / Zero 
        print("Erro de divisão por zero não permitira. \nPor favor, tente novamente.")
    except ValueError as erro:
        #
        print(f"Erro {erro}. \nPor favor, tente novamente.")


