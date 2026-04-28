"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, realizando o cálculo do preço final após a aplicação do desconto. Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).

"""
print("------------- Cálculo desconto --------------")

def calculadesconto(preco, percentualdesconto):
    desconto = preco * (percentualdesconto/100)
    precofinal = preco - desconto
    return precofinal

while True:
    try:
        preco = float(input("Digite o preço R$ "))
        percentualdesconto = float(input("Digite o percentual de desconto (%) "))
        break

    except ValueError:
        print("Entrada inválida!! Insira valor numérico.")

    

precofinal = calculadesconto(preco, percentualdesconto)
print(f"Preço original R$ {preco:.2f}")
print(f"Desconto de {percentualdesconto}%")
print(f"O preço final com desconto é de R$ {precofinal:.2f}")
