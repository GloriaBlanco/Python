"""
Módulo IA - Escola da Nuvem
4- Calculadora de Preço Total
Desenvolva um programa que calcule o preço total de uma compra. Use as seguintes informações:
Nome do produto: "Cadeira Infantil"
Preço unitário: R$ 12.40
Quantidade: 3 
O programa deve calcular o preço total e exibir todas as informações, incluindo o resultado final.
"""
produto="Cadeira Infantil"
qtde=3
precounit=12.40
total = qtde*precounit
print(f"Produto -- {produto} ")
print(f"Preço unitário = R$ {precounit:.2f}")
print(f"comprei {qtde} unidades ")
print(f"Preço total da compra = R$ {total:.2f}")
