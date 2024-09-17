# Aula Python ao vivo Nara Gumarães 01/08/24  #

# tipos variáveis
var_string = 'nome'
print(type(var_string))

var_bool = True
print(type[var_bool])


print(1+2)
print(5-3)
print(10/4)
print(10//4)
print(10%4)    # resto divisoa
print(5/3)     # resultado  1.6666 float
print(5//3)    # resultado 1 inteiro
print(5 %3)    # resultado 2 resto
print(10% 2)   # resto 0 entao par
print(5% 2)    # resto 1 nao par

print(4 ** 2) # = 16 # exponenciao

#raiz quadrada tem que importar biblioteca
print(4 ** 1/2) # é 2.0 isto é = raiz quadrada de 4 sem importar = 2.0 da resultado como float

# operadores comparação
# variável sempre ocupa espaço na memória
a = 14 
b = 15
print(id(a)) # posiçao na memória da variável a
print(id(b)) # posição na memória da variável b

print(a != b) # diferente
print(a == b)  # igual
print (a==b-1)  
print(a > b)  # maior que
print(a >= b)  # maior igual que
print(a < b)  # menor que
print(a <= b)  # menor igual que


# Comparações e|and, ou|or, não|not

print(not (a>b))
print(a > b)
c = 12
print(a < b) and (c<a) # true
print(a < b) and (c<a) # false

#   COMP1    COMP2   AND     OR     NOT|COMP1
#   false   false   false   false   true
#   false   true    false   true    true
#   true    false   false   true    false
#   true    true    true    true    false


##############################
## Listas: conjunto expresso dentro de colchetes
## lista pode ser chamada de vetor ou array
## sempre inicia posição|índice 0(zero)

lista1 = [] # lista vazia, tipo list
lista2 = list() #lista vazia, tipo list
#lista homogenia: todos elementos mesmo tipo, inteiros
#lista heterogenea: tipos diferentes
lista_homogenea=[1,2,3,4,5,6,7]
lista_heterogenea=[1,'nome',4.5, True]
# lista_heterogenea: o 1=indice 0, nome=indice1, 4.5=indice2, true=indice3
# tamanho é diferente de indice, é a quantidade de elementos, aqui 4


print(lista_homogenea)
print(lista_heterogenea)

#lista é mutável, pode mudar os elementos
lista1 = [1,2,3,4,5,6.7]
# mudar o item 6.7
lista1[5] = 6 # mudamos o 5º elemento de 6.7 para 6
print(lista1)
print(lista1[-1]) # vai de tras pra frente, aqui indice inicial e 1
print(lista1[-3]) # retorna o numero 4 


##############################
## Tuplas: náo consigo alterar valor de uma tupla
## usa () colchete

tupla1 =()
tupla2 = tuple()

print(type(tupla1))
print(type(tupla2))

tupla_homogenea=[1,2,3,4,5,6,7]
tupla_heterogenea=[1,'nome',4.5, True]

print(tupla_homogenea)
print(tupla_heterogenea)

tupla_heterogenea[2] = 'teste'
print(tupla_heterogenea)


##############################
## Dicionário: consigo alterar valor de uma tupla
## usa {} chaves
## mutável como a lista

dic1= {
    'nome': 'Maria',
    'idade':25,
    'cidade': 'SãoPaulo'
}

dic2= {
     'nome': 'Joao',
    'idade': 5,
    'cidade': 'Rio'
}

dic2['nome'] = 'Glo'

print(dic1)
print(dic2)


########################
### conjuntos: tem valores únicos, nao tem valores iguais
## usa colchetes {}

conjunto = set()
print(type(conjunto))
numeros = {1,2,3,4,5}
numeros.add(6)
print(numeros)
numeros.add(6)
print(numeros)

valores = {1,2,2,2,2,2,2,2,2,2,2}
set(valores) # excluir os valores repetidos
print(valores)

#########################
## estruturas de controle
## IF = se .... ELIF= se .... ELse = senao
## el

if (1 == '1'):  # são diferentes
    print('são iguais')
else:
    print('São diferentes')


if (1 == 1.0):  # são iguais
    print('são iguais')
else:
    print('São diferentes')

if (1 == '1') and (1 == 1.0):  # são diferentes
    print('são iguais')
else:
    print('São diferentes')

if (1 == '1') or (1 == 1.0):  # são iguais
    print('são iguais')
else:
    print('São diferentes')

if not(1 == '1'):  # são iguais
    print('são iguais')
else:
    print('São diferentes')


if not(1 == 1.0):  # são diferentes
    print('são iguais')
else:
    print('São diferentes')

a=2
b=16
c=21
d=50

if a>b:  # sim
    print(f'A variável a {a} é maior que a variável b {b}')
else: 
     print(f'A variável a {a} é MENOR que a variável b {b}')
     print(f'A variável b {b} é maior que a variável a {a}')


if a>b:  # nao
    print(f'A variável a {a} é maior que a variável b {b}')
elif c> d: # nao
    print(f'A variável c {c} é maior que a variável d {d}')
elif b> d: #nao
    print(f'A variável b {b} é maior que a variável d {d}')
elif b> c: # não
    print(f'A variável b {b} é maior que a variável c {c}')
else:
     print(f'A maior variável é a d {d}')

var_idade = input('Digite sua idade: ')

var_idade = int(input('Digite sua idade: '))
print(type(var_idade))

var_sal = float(input('Digite seu salário: '))
print(type(var_sal))

idade = int(input('Digite sua idade: '))

print(idade)

if idade >= 18:
    print('Maior de idade')
else:
    print("Menor idade")


################
##  FOR: loop a ser exetutado ate o limite

print(range(10))

for i in range(10):
# range já existe no Python, inicio 0(zero), até o 9(nove) nao inclui o 10
    print(i, end='---')    

for i in range(idade, 21, 1): # se idade foor maior que 22 nao vai entrar
     print(i, end='---') 

for i in range(0, 10, 3): # aqui pula de 3 em 3 = 0 3 6 9
     print(i, end='---') 

for valores in lista_heterogenea:
    print(valores)

for valores in tupla_heterogenea:
    print(valores)


for cristiane in tupla_heterogenea:
    print(cristiane)


###################
## while: sempre ter que ter uma saída, cuidado

j = 0
while j <= 10:  # sempre
    print(j, end='--')
    j +=2

while True:
    salario = float(input('Digite seu salário; '))
    if salario >=1412:
        print('Salario valido')
        break
    else:
        print('Salário inválido')
        continue
                    


















