""" 
2- Calculadora de Desconto 
Desenvolva um programa que calcula o desconto em uma loja. 
Use as seguintes informações:
Nome do produto: "Camiseta"
Preço original: R$ 50.00
Porcentagem de desconto: 20% 
O programa deve calcular o valor do desconto e o 
preço final, exibindo todos os detalhes.

"""
# variáveis
nomeproduto = "Camiseta"
precooriginal=50.00
desconto=20

#calculo desconto
valorfinal = precooriginal - (precooriginal*desconto)/100

# exibir resultado
print("---------- Valor a pagar -----------")
print(f'Nome do produto : {nomeproduto}')
print(f'Valor produto = R$ {precooriginal:.2f}')
print(f'Desconto = {desconto}%')
print(f'Total a pagar = R$ {valorfinal:.2f}')


