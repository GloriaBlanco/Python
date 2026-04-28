""" 
1- Conversor de Moeda 
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:
Valor em reais: R$ 100.00
Taxa do dólar: R$ 5.60
Taxa do euro: R$ 6.60 
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais.

"""
# variáveis
valor = 100.00
txdolar = 5.60
txeuro = 6.60

# cálculos
valordolar = valor*txdolar
valoreuro = valor*txeuro

# exibir resultados
print("-------------- Conversor moedas -----------")
print(f"Valor R$ {valor:.2f}")
print(f"Taxa do dólar = {txdolar:.2f} corresponde a R$ {valordolar:.2f}")
print(f"Taxa do euro = {txeuro:.2f} corresponde a R$ {valoreuro:.2f}")
