""" 
Aula 21/08/25

2- Classificador de Idade
Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:
Criança (0-12 anos),
Adolescente (13-17 anos),
Adulto (18-59 anos)
Idoso (60 anos ou mais).

"""
print("---------- Calsssifcador Idade -----------")
idade = int(input("Qual sua idade? "))

if idade < 13:
    print(f"Você tem {idade} anos, é uma criança")
elif idade < 18:
    print(f"Você tem {idade} anos, é um adolescente")
elif idade < 60:
    print(f"Você tem {idade} anos, é um adulto")
else:
    print(f"Você tem {idade} anos, é um idoso")
