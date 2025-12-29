"""
Aula 25/08/25
Prática 04

Crie um programa que verifique se uma senha é forte. 
Uma senha forte deve ter pelo menos 8 caracteres e conter 
pelo menos um número. 
O programa deve continuar pedindo senhas 
até que uma válida seja inserida ou o usuário digite 'sair'.

"""

print('---------- Controla Senhas ------------')
print("Sua senha deve ter 8 caracteres e pelo menos 1 deles deve ser número")

for i in range(1,9):
    print(i)
    while True:
        try:
            senha = input("Digite o primeiro caracter/numero da senha (total 8 caracteres e pelo menos 1 numero) ou SAIR para fim: ")
    
            #if senha.upper() == "SAIR":
            #    break
            #elif 0 <= len(senha) < 9:
            #    if nota = nota + float(notadigitada)
            #    n+=1
            #else: 
            #    print("Nota inválida. \nDigite novamente uma nota de 0 até 10: ")
            #    continue
        except ValueError:
            print(f"Entrada inválida !!. \nPor favor, tente novamente.")

"""
if n > 0:
    print(f"Foram digitadas notas de {n} alunos")
    print(f"A soma de todas as notas = {nota}")
    media = nota/n
    print(f"Média de nota dos alunos é de {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")
"""

      



