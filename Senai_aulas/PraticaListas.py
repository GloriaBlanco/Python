# aula sobre listas 27 de fevereiro de 2024

#############
# toda lista começa no 0
#############

bancos = ['Banco do Brasil', " Caixa", 'Santander']
print(bancos)
# resultado será: ['Banco do Brasil', " Caixa", 'Santander']
bancos[1] = "Itaú"
print(bancos)
# Resultado: ['Banco do Brasil', "Itaú", 'Santander']
bancos[-1] = "C6"
print(bancos)
# resultado: ['Banco do Brasil', " Caixa", 'C6']



#############
# INCREMENTAR O VALOR DE UMA LISTA
#############

bancos = bancos + ['Bradesco', 'Nubank']
print(bancos)
# resultado será: ['Banco do Brasil', "Itaú", C6, Bradesco, Nubank']
bancos += ['Safra']
print(bancos)
# Resultado: ['Banco do Brasil', "Itaú", 'C6', 'Bradesco', 'Nubank', 'Safra']

lista = [4,5,3,5]
print(lista)    #[4,5,3,5]

# append = insere item a uma lista
lista.append(2)
print(lista)    #[4,5,3,5,2]

# insert = adiciona um item à lista definindo um índece especifico
lista.insert(2,-3)
print(lista)    # [4, 5, -3, 3, 5, 2]

# remove = remove 1 elemento da lista
lista.remove(4)
print(lista)    #[5, -3, 3, 5, 2]

# sort  = ordena os itens de uma lista
lista.sort()
print(lista)    #[-3, 2, 3, 5, 5]

# reverse = invete os itens de uma lista
lista.reverse()
print(lista)    #[5, 5, 3, 2, -3]

# qnt = quantidade de x que aparece 1 item
qnt = lista.count(5)
print(qnt)      # 2
print(lista)    # [5, 5, 3, 2, -3]

# exc 
exc = lista.pop()
print(lista)    #[5, 5, 3, 2]
print(exc)      # -3

# del = remove 1 item de uma lista
del lista[2]
print(lista)    # [5,5,2]

del lista[2:5]
print(lista)    # [5,5]

# clear = limpa lista inteira
lista.clear()
print(lista)    # []



#############
# 1 lista dentro de 1 lista
#############

compra = [10.2,3.34,16.3,['tomate','sabonete','arroz']]
print(compra)       #[10.2, 3.34, 16.3, ['tomate', 'sabonete', 'arroz']]
produtos = compra[3]
print(produtos)     #['tomate', 'sabonete', 'arroz']
total = compra[0]+compra[1]+compra[2]
print(total)        # soma 3ºs itens 29.84
letra = ['a','b','c']
num = [2,4,6]
tudo = [letra,num]
print(tudo)         # [['a', 'b', 'c'], [2, 4, 6]]
print(f"Letras: {tudo[0]}")  #Letras: ['a', 'b', 'c']
print(f"Numeros: {tudo[1]}") #Numeros: [2, 4, 6]


#############
# 1 lista  com list()
#############

times = list(('Palmeiras','Santos'))

print('\n')
print(times)    # ['Palmeiras', 'Santos']

marcas = ['Ford',
          'Fiat',
          'Ferrari',
          'MCLaren']

# enumerate = utilizado para trazer indice e o valor do item na lista, sem usar range e len
print('\n')

for pos, valor in enumerate(marcas):
    print(f'O {pos}º item da sua lista é {valor}')
    # tela :    O 0º item da sua lista é Ford
    #           O 1º item da sua lista é Fiat
    #           O 2º item da sua lista é Ferrari
    #           O 3º item da sua lista é MCLaren

print('\n')

# alteramos um item na nossa variavel utilizando o colchetes
# aqui entra Bugatti no lugar da Ford

marcas[0] = 'Bugatti'
print(marcas)       # ['Bugatti','Fiat','Ferrari','MCLaren']
print('\n')

#
for pos, valor in enumerate(marcas):
    print(f'O  {pos}º item da sua lista é  {valor}')
    # tela :    O 0º item da sua lista é Bugatti
    #           O 1º item da sua lista é Fiat
    #           O 2º item da sua lista é Ferrari
    #           O 3º item da sua lista é MCLaren
print('\n')

# Append adicionar um item ao final da lista
adicionar = str(input("Adicione uma nova marca: "))
marcas.append(adicionar)    # aguarda usuário digitar uma nova marca e inclui na lista

# outra opção e colocar nao usar variavel, marcas.append(str(input("Adicione uma nova marca: ")))
print('\n')

for pos, valor in enumerate(marcas):
    print(f'O  {pos}º item da sua lista é  {valor}')
    # tela :    O 0º item da sua lista é Bugatti
    #           O 1º item da sua lista é Fiat
    #           O 2º item da sua lista é Ferrari
    #           O 3º item da sua lista é MCLaren
    #           O 4º item da sua lista é "O NOME QUE FOI DIGITADO PELO USUÁRIO"
print('\n')

# INSERT adicionar um item ao final da lista
# adicionar = str(input("Adicione uma nova marca: "))
marcas.insert(1,  'Tesla')

for pos, valor in enumerate(marcas):
    print(f'O  {pos}º item da sua lista é  {valor}')
    # tela :    O 0º item da sua lista é Bugatti
    #           O 1º item da sua lista é Fiat
    #           O 2º item da sua lista é Tesla
    #           O 3º item da sua lista é Ferrari
    #           O 4º item da sua lista é MCLaren
    #           O 5º item da sua lista é "O NOME QUE FOI DIGITADO PELO USUÁRIO"
print('\n')




