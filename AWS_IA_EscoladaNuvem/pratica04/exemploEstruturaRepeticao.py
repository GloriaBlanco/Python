"""
Aula 25/08/25
Estruturras de Repetição
For
Break
Continue
Try e Except


""" 
# lista
frutas = {"maca", "banana","laranja", }

# usando FOR para iterar sobre uma lista o laço de repetição
print("------ FOR ------")
for fruta in frutas:
        print(fruta)

# range para contar
for i in range(1,6):
     print(i)


# usando break para interromper o laço de repetição
print("------ BREAK ------")
for i in range(1,11):
    if i ==5:
        print(f"O loop chegou no numero i = {5}")
    print(i)


# usando o CONTINUE para pular uma iteracao
print("------ CONTINUE ------")
for i in range(1,6):
    if i == 3:
        continue # pula a impressao do numero 3
        print("continue")
    print(f"valor do i = {i}") 


# TRY e EXCEPT
# tratar o controle de erros que pode acontecer
print("------ TRY e EXCEPT ------")
try:
    # código que quero controlar erro
    numero = int(input("Digite um numero: "))
except ValueError:
    # significa que deu ERRO, e posso mostrar mensagem usuário
    print("Valor inválido!! Por favor, insira um número.")
