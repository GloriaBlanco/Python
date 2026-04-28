"""
Aula 20/08/25
4- Calculadora de Consumo de Combustível
Desenvolva um programa que calcula o consumo médio de combustível de um veículo. Use os seguintes dados:
Distância percorrida: 300 km
Combustível gasto: 25 litros 
O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem, incluindo o resultado final arredondado para duas casas decimais.

"""
# variáveis
distancia = 300
combustivel = 25

# cálculo
valorgasto = distancia/combustivel

# exibir
print("---------- Calculadora Consumo de combustível ---------------")
print(f"Distância percorrida = {distancia}Km")
print(f"Combustível gasto = {combustivel} litros")
print(f"Total consumo Km por litro {valorgasto:.2f} Km/l")

# outra forma de exibição
# obs a função, neste caso o round nao vai dar 2 casas decimais
print("---------- Calculadora Consumo de combustível ---------------")
print("Distância percorrida =", distancia, "Km")
print("Combustível gasto =", combustivel, "litros")
print("Total consumo Km por litro", round(valorgasto, 2), "Km/l")

