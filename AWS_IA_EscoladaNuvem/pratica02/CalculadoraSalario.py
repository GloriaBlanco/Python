"""
Aula 20/08/25

6- Calculadora de salário por horas trabalhadas
Leia o número de um funcionário, seu número de horas trabalhadas
e o valor que recebe por hora. Calcule o salário do funcionário e 
exiba o resultado formatado corretamente.

Entrada:
O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando:
Número do funcionário (numero_funcionario).
Quantidade de horas trabalhadas (horas_trabalhadas).
Valor recebido por hora (valor_por_hora).
Saída:
Imprima o número do funcionário e o salário calculado com 
duas casas decimais. Deve haver um espaço em branco antes 
e depois do sinal de igualdade, e no caso do salário, 
também um espaço em branco após o R$

"""

#variáveis

#entrada usuário
nfuncionario = int(input('Digite o número do funcionário: '))
qtdehoras = int(input('Digite a quantidade de horas trabalhadas: '))
valorhora = float(input('Digite o valor/hora:'))

# cálculo
salario = qtdehoras * valorhora

# exibir
print("----------- Cálculo salário -----------")
print(f'Número do funcionárioo : {nfuncionario}')
print(f'Quantidade de horas trabalhadas = {qtdehoras} horas')
print(f'Valor por hora = R$ {valorhora:.2f}/hora')
print(f'Total salário = R$ {salario:.2f}')

