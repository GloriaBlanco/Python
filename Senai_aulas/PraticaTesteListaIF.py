# aula sobre listas 27 de fevereiro de 2024
# toda lista começa no 0
# procura um nome numa determinada lista

nome = ['Gloria', 'Glo','G','Celo','Francisco']
print(nome) # imprimi ['Gloria', 'Glo','G','Celo','Francisco']

i = 0

while i < len(nome): # enquanto i  for menor que tamanho da lista nome e nao encontra nome, i inicia em 0 zero
    print(i)
    n = nome[i]
    print(n)
    if n == 'G': # o nome da lista da posicao i 'e igual a `G` entra no if, senao volta while
       print(f'OIeee {nome[i]} , te achei no {i+1} nome da lista e na {i} vez do loop')
       break
    i +=1
