"""
Crie uma função que calcule a gorjeta a ser deixada 
em um restaurante, baseada no valor total da conta e 
na porcentagem de gorjeta desejada. Calcule o valor 
da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: 
valor_conta (float): O valor total da conta
 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada

"""
def calculagorjeta(valorconta, porcentagem):
    gorjeta = (valorconta * porcentagem)/100
    return gorjeta

valorconta = float(input("Digite o valor da conta R$ "))
porcentagem = float(input("Digite o percentual de desconto "))

gorjeta = calculagorjeta(valorconta, porcentagem)
print(f"Para a conta de R$ {valorconta}, a gorjeta de {porcentagem}% é de R$ {gorjeta:.2f}")