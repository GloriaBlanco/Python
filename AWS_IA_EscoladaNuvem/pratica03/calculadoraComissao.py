"""
Aula 22/08/25

6- Calculadora de Comissão
Faça um programa que leia o nome de um vendedor, o seu salário
 fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). 
Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber 
no final do mês, com duas casas decimais. 
Entrada: O arquivo de entrada contém um texto (primeiro
 nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando
 o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, 
respectivamente. 
Saída: Imprima o total que o funcionário deverá receber, 
conforme exemplo fornecido.

"""

print("-----------  Cálculo Comissão -------------")
nome=input("Digite o nome do vendedor: ")
salariofixo= float(input("Qual valor do salário fixo: "))
totalvendas =int(input("Qual total de vendas: "))
print("------------------------------------------")

percentual = 0.15
comissao = totalvendas * percentual
salario = salariofixo+comissao

print(f"Vendedor ........... {nome}")
print(f"Salário fixo ....... {salariofixo:.2f}")
print(f"Total de vendas .... {totalvendas}")
print(f"Comissão de ........ {percentual}%")
print(f"Valor da comissão .. R$ {comissao:.2f}")
print(f"Salário total ====== R${salario:.2f}")