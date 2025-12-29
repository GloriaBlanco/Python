"""
Aula 25/08/25
Prática 04

Crie um programa que permita a um professor registrar as notas de 
uma turma. O programa deve continuar solicitando notas até que o 
professor digite 'fim'. Notas válidas são de 0 a 10. O programa 
deve ignorar notas inválidas e continuar solicitando. No final, 
deve exibir a média da turma.

"""

print('--------- Média de Notas dos alunos da turma ------------')
n = 0
nota = 0

while True:
    try: 
        notadigitada = input("Digite a nota do aluno (0 até 10) ou FIM para sair: ")
    
        if notadigitada.upper() == "FIM":
            break
        elif 0 <= float(notadigitada) < 11:
            nota = nota + float(notadigitada)
            n+=1
        else: 
            print("Nota inválida. \nDigite novamente uma nota de 0 até 10: ")
            continue
    except ValueError:
        print(f"Entrada inválida !!. \nPor favor, tente novamente.")
# if notas: Aqui
if n > 0:
    print(f"Foram digitadas notas de {n} alunos")
    print(f"A soma de todas as notas = {nota}")
    media = nota/n
    print(f"Média de nota dos alunos é de {media:.2f}")
else:
    print("Nenhuma nota foi digitada.")


      



