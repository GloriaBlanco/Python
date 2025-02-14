# Aula sobre while 27 de fevereiro de 2024
qtde_linhas = 5
qtde_colunas = 5

linha = 1

# em cada impressão de linha imprimi a quantidade de x da coluna, 
# exemplo para linha 1, imprimi 5x a linha 1 com coluna de 1 a 5, 
# será lin 1 col 1, lin 1 col 2, lin 1 col 3, lin 1 col 4, lin 1 col 5, lin 2 col 1 etc
 
while linha <= qtde_linhas:
    coluna = 1
    while coluna <=qtde_colunas:
        print(f"{linha= } {coluna= }")
        coluna += 1
    linha +=1

