""" Aula 20/08/25
3- Calculadora de Média Escolar 
Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:
Nota 1: 7.5
Nota 2: 8.0
Nota 3: 6.5 
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.

"""
# notas do aluno
nota1 = 7.5
nota2 = 8.0
nota3 = 6.5

# cálculo da média
media = (nota1+nota2+nota3)/3

# exibe o resultado
print('---------- Notas do aluno --------------')
print(f'Nota 1 = {nota1}')
print(f'Nota 2 = {nota2}')
print(f'Nota 3 = {nota3}')
print(f'A Média do aluno = {media:.2f}')
print(f'A Média do aluno =', round(media, 2))


