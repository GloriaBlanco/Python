"""
Aula 21/08/25

3- Calculadora de IMC
Desenvolva um programa que calcule o Índice de Massa Corporal (IMC) de uma pessoa.
O programa deve solicitar o peso (em kg) e a altura (em metros) do usuário,
calcular o IMC e fornecer a classificação de acordo com a tabela padrão de IMC.

IMC = peso (em quilogramas) / (altura x altura) (em metros)

< 18.5: classificacao = "Abaixo do peso" 
< 25: classificacao = "Peso normal"
 < 30: classificacao = "Sobrepeso"
 Para os demais cenários: classificacao = "Obeso"

"""

print("-------------- Calculadora IMC ------------------")
peso = float(input("Qual seu peso em Kg?"))
altura = float(input("Qual sua altura em metros?"))
imc = peso / (altura*altura)

print(f"Você tem {peso} kg, e {altura} cm e seu IMC é de {imc:.2f}")

