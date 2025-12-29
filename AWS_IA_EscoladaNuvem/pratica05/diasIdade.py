"""
Crie uma função que calcule a idade de uma
 pessoa em dias, baseada no ano de nascimento.

"""
import datetime

print("------------- Calculo Idade em dias -------------")

def calculardias(anonascimento):
    anoatual = datetime.datetime.now().year
    idadeanos =  anoatual - anonascimento
    idadedias = idadeanos * 365
    return idadedias

anonascimento = int(input("Digite o ano de nascimento: "))
qtdedias = calculardias(anonascimento)
print(f"Você nasceu em {anonascimento} e já viveu {qtdedias} dias")
