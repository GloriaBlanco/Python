""" 
Aula 01/09/25

"""
import csv

with open("dados.csv", "r") as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    for linha in leitor:
        print(linha)


with open("dados.csv", "w") as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(["nome", "idade", "cidade"])
    escritor.writerow(["Maria", "30", "Salvador"])
    escritor.writerow(["José", "51", "Rio de Janeiro"])

