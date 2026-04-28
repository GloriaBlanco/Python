# Primeira aula de Python no Senai, 19 de fevereiro de 2024
''' isto é Docstring mas NÃO é UM comentário 
    desde as 3 aspas iniciais até as 3 aspas abaixo
    Python lê mas nao compila
    no comentário com # o Python nem lê
'''
print('Hello World')
print(123)
print(1,2,34)
print("Glória","Glo","G")
# 1º programa solicitado pelo Professor
#print("Hello world")
#print("Hello world")
# me permite fazer meus comentários
# "Estou adorando Python"

print('Agora sou dev')
# sep='-' é separador do print, da um espaço em branco entre os itens do print
# end='\r\n muda de linha
# end='\r\n\r\n muda de linha e mais uma linha em branco
print(12, 34, 1011, sep='-', end='\r\n\r\n') # imprimi  12-34-1011
print(56, 78, sep='-', end='\r\n')           # imprimi 56-78
print(9, 10, sep='-', end='\r\n')            # imprimi 9-10
# escape
print("Marcos \"Paulo") # imprimi Marcos "Paulo
print("Marcos'Paulo'")  # imprimi Marcos 'Paulo'
print('Python')         # imprimi Python
# sep='-' muda de linha no final da print da tela
print('Explicito', 'é','melhor-que-implicito.',sep='-')
print('Simples', 'é','melhor-que-complexo.',sep='-')

# end='-' coloca - no final do print, e nao muda de linha
print('Explicito', 'é','melhor-que-implicito.', end='-')
print('Simples', 'é','melhor-que-complexo.', end='-')

# print sem nada, mesmo assim cada print ja muda de linha
print('Explicito', 'é','melhor-que-implicito.')
print('Simples', 'é','melhor-que-complexo.')
