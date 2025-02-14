### aulas Python Numpay - parte1

import numpy as np

### array lista
l = [1,2,3,4]
arr1 = np.array(1)
print ('########')

print(arr1)
print(type(arr1))


### array de zeros 3 linhas 2 2 colunas
print(np.zeros((3,2)))

### array intervalo, lista
print(list(range(0, 3)))
print(np.arange(6,11))

print(np.arange(1,11))

## array numa variavel
arr_range = np.arange(1,11)
print(arr_range)
print(type(arr_range))

## array numeros aleatórios
print(np.random.random((2,3))) # 2 linhas, 3 colunas

##### Exercícios

## 1 crie um array com 4 linhas e 3 colunas com valores aleatórios
arra1 = np.random.random((4,3))
print (f'exe1 - array com 4 linhas e 3 colunas = ')
print (arra1)


## 2 crie um array zeros com 5 colunas e 10 linhas inicializados com zeros
arra2 = np.zeros((10,5))
print (f'exe2 - array zeros com 5 colunas e 10 linhas = ')
print (arra2)


## 3 crie um array com valores INTERIOS (RANDINT) 3 linhas e 5 colunas valores aleatóriso
arra3 = np.random.randint(30, size=(3,5))  # randint(limite inferior(se for Zero nao precisa por), limite superior, size=(linhas,colunas))
print (f'exe3 - array 3 linhas e 5 colunas = ')
print (arra3)

### Aulas Python Numpy Parte 2

arra1_2d = np.array([[1,2],[3,4]])
arra2_2d = np.array([[5,6],[7,8]])
arra3_2d = np.array([[9,2],[3,4]])

print(arra1_2d)
print(arra2_2d)
print(arra3_2d)

arra_3d = np.array([arra1_2d, arra2_2d, arra3_2d])
print(arra_3d)

arr1 = np.array([arra_3d, arra_3d])
print(arr1)  

## array de zeros

print(np.zeros([2,3,4]))        


arrcubo=np.zeros([3,4,2])   # dimensoes cubo (  x do 3d do cubo ,linhas, colunas)
print(arrcubo)

print(arrcubo.shape) # mostra dimensao, atributo


## metodo flatten, tudo numa 1 dimensao
print(arrcubo.flatten())

arr1 = np.array([arra_3d, arra_3d])
print(arr1)  
print(arr1.flatten())


## metodo reshaping, muda as dimensoes

arra_3d = np.array([arra1_2d, arra2_2d, arra3_2d])
print(arra_3d)
print(arra_3d.reshape(4,3))  # linha,coluna
# este da erro porque nao e dimensao da matriz=print(arra_3d.reshape(2,5))


#### Exercicio parte 2
# reduza o array (5,7) apenas 1 dimensao
exe1 = np.zeros([5,7])
exe1random = np.random.randint(12,size=(5,7)) # 5 linhas, 7 colunas, 0 até maximo numero 12
print(exe1)
print(exe1.flatten())
print(exe1random)
print(exe1random.flatten())

## exe2 -bingo de cartilhas 1 a 30, 10 participantes, cada cartela tem 12 numeros (4,3)
## crie um array que represente esse jogo

bingo = np.random.randint(1,31,size=(10,4,3)) # 4 linhas, 3 colunas, 0 até maximo numero 30
print(bingo)

## reshape das cartelas, 5 cartelas de 4 linhas e 6 colunas

cartelas = bingo.reshape(5,4,6) # 5 cartelas de 4 linhas e 6 colunas
print(cartelas)

##############
### Numpy - parte 3 

##dtype: tipo default, alteração tipo de dados, conversão e coerção

a = np.array([5.4,6.7,2.1]).dtype
print(a)

a = np.array([5,4,2,1]).dtype
print(a)

a = np.array(["Hello","öi","gl"]).dtype
print(a)

a = np.array([5,4,6.7,2.1]).dtype
print(a)

x = np.array([3,4,2.1])
print(x[0])


## boolean
a = np.array([True, 3, False]).dtype
print(a)

b = np.array([True, 3, False])
print(b) # sera [1,3,0]

## converter

x = np.array([3,4,2.1])
print(x)
print(x.dtype)

a = x.astype(np.int32)
print(a)
print(a.dtype)

b = np.array([True, 3, False])
print(b) # sera [1,3,0]
c = b.astype(np.float32)
print(c)
print(c.dtype)

d = b.astype(np.bool8)
print(d)
print(d.dtype)

### Parte 4
## index, order

arr= np.array([2,4,6,7,8])
print(arr)
print(arr[1])
print(arr[4])

#cartela bingo
cart= np.random.randint(30, size=(4,4))  # randint(limite inferior(se for Zero nao precisa por), limite superior, size=(linhas,colunas))
print (cart)

cartela = np.array([[16,10,3,15],[14,23,17,27],[6,19,3,1],[10,4,18,19]])

# slicing fatiar
cartelafatiar = cartela[:,1]
print(cartelafatiar)


# reshape
print(cartela.shape)  # cartela original
print(cartelafatiar.shape)  # cartela fatiada

print(cartelafatiar.reshape((4,1)))  # cartela fatiada

## so 1 linha da cartela
print(cartela)
print(cartela[0])

## sort considerou eixo vertical, axis 1, coluna
s = np.sort(cartela) 
print(s)

## sort considerou eixo horizontal, linha
s = np.sort(cartela, axis=0) 
print(s)


### Exercício
# 1 coluna id especie
# 2 coluna quantidade de esppecies
# 3 coluna profudenza
# 4 coluna tamanho medio de cada especie
esp = np.array([[747,89,33,5],
                [623,123,32,13],
                [501,22,49,2],
                [116,101,42,10],
                [297,56,69,22],
                [613,64,27,7],
                [295,84,29,14],
                [692,105,72,16],
                [229,103,35,5],
                [374,124,70,1]])
print(esp)

qtde = esp[:,1] ## somente 2ª coluna
print(qtde)


primeiras3 = qtde[:3] ## somente as primeiras 3 dessa 2ª coluna
print(primeiras3)

quantas = esp.shape # 1º linha, 2º coluna
print(quantas)

primeiras5 = qtde[:-5] ## somente as 5 primeiras
print(primeiras5)
ultimas5 = qtde[-5:] ## somente as 5 ultimas
print(ultimas5)

## quando nao sei a quantidade
ultimas5 = qtde[-5:] ## somente as 5 ultimas
print(ultimas5)

## crie array apenas com tamanho especies e ordenar crescente

tamanho = esp[:,3]  # tamanho esta na ultima coluna
print(tamanho)
ordenar = np.sort(tamanho)  # ordenar crescente
print(ordenar)
ordenar = np.sort(tamanho)[::-1] # ordenar decrescente
print(ordenar)

## parte 5
# filtrando arrays: mask, fancing indexing, np.where

# mask vai armazenar o numero que é dividido por 2
arr = np.array ([1,2,3,4,5])
print(arr)
mask = arr % 2 == 0 
print(mask)

# mask vai armazenar o numero que é dividido por 3
arr = np.array ([1,2,3,4,5])
print(arr)
mask = arr % 3 == 0 
print(mask)

pessoas_idade = np.array([[1,22],[2,21],[3,27],[4,26]])
print(pessoas_idade)
maioridade = pessoas_idade[:,1] > 21
print(maioridade)

commask = pessoas_idade[maioridade]
print(commask)  # nao imprimi o [2,21]

# where passa o numero da posiçao
teste1Where = np.where(maioridade)
print(teste1Where)
# igual ao de cima
teste1Where = np.where(pessoas_idade[:,1] > 21)
print(teste1Where)

# substituiçao de um numero dividio por 3 por "div3", ai array virou string
cartela = np.array([[16,10,3,15],
                    [14,23,17,27],
                    [6,19,3,1],
                    [10,4,18,19]])
bingo = np.where(cartela %3 == 0, "div3", cartela)
print(bingo)

# idade mair que 21 vou substituir "maior idade"
maior = np.where(pessoas_idade > 21, "maior idade", pessoas_idade)
print(maior)
print(type(maior[0,0]))
#

pessoas_idade = np.array([[1,22],[2,21],[3,27],[4,26]])
print(pessoas_idade)
maioridade = pessoas_idade[:,1] > 21
print(maioridade) # imprimi booleano
commask = pessoas_idade[maioridade]
print(commask)  # nao imprimi o [2,21]
print(type(commask[0,0]))

### Exercício
# 1 coluna id especie
# 2 coluna quantidade de esppecies
# 3 coluna profudenza
# 4 coluna tamanho medio de cada especie
esp = np.array([[747,89,33,5],
                [623,123,32,13],
                [501,22,49,2],
                [116,101,42,10],
                [297,56,69,22],
                [613,64,27,7],
                [295,84,29,14],
                [692,105,72,16],
                [229,103,35,5],
                [374,124,70,1]])
print(esp)

# qual linha com a maior especie = 22, é a de indice/coluna nº 3 da 4ª linha
maior = esp[:,3] == 22 # resultado booleano
print(maior) 
maiornumeros = esp[esp[:,3] == 22] # resultado com os numeros dentro da matriz
print(maiornumeros)

## array especie 297 = toda linha
esp297 = esp[:,0] == 297 # resultado booleano
print(esp297) 
esp297numeros = esp[esp[:,0] == 297] # resultado com os numeros dentro da matriz
print(esp297numeros)

# 105 representantes = 2ª coluna
repre = np.where(esp[:,1] == 105) # [:= (todas linhas), 1(2ª coluna)]
print(repre) # posicao = 7, é a 7linha, contando de 0
repre = esp[esp[:,1] == 105] # desta forma mostra todos os numeros na linha que esta o 105
print(repre)
### igual a
repre = esp[np.where(esp[:,1] == 105)] # desta forma mostra coloca o numero 7 como posicao de esp
print(repre)


### profundezas substitua > 60 "profundo"
## 3ª coluna, indice 2

prof = esp[:,2] # coluna toda com os valores
print(prof)
prof = esp[:,2] > 60 # coluna com booleano nos valores > 60 TRUE
print(prof)
prof = np.where(esp[:,2]) # posicao/indice de cada valor na coluna
print(prof)
prof = np.where(esp[:,2]>60) # posicao/indice de cada valor que for > 60 
print(prof)
prof = np.where(esp[:,2] > 60, 'profundo', esp[:,2])
print(prof)

#### Parte 6
## adicionando ou removendo dados array
## concatenar linhas, arrays

#concatenar
print("##############")
cartela = np.array([[16,10,3,15],
                    [14,23,17,27],
                    [6,19,3,1],
                    [10,4,18,19]])

bingo1 = cartela[:3] # pega todas as 3 primeiras linhas
print(bingo1)

bingo2 = cartela[-1:] # pedou só a ultima linha
print(bingo2)

concaten = np.concatenate((bingo1,bingo2))
print(concaten)

print(cartela==np.concatenate((bingo1,bingo2)))

concaten = np.concatenate((bingo2,bingo1))
print(concaten)

sala = np.array([['5','30','1','Alice'],
['6','29','1','Bob'],
['7','35','3','Cristina'],
['8','54','3','Luiz']])
print(sala)

sala = np.concatenate((bingo1,bingo2))
print(sala)

### Luiz foi chamado e saiu da sala de espera
## tirar  Luiz
delluiz = np.delete(sala,3, axis=0) # exclui toda linha 3
print(delluiz)


### Exercício
# 1 coluna id especie
# 2 coluna quantidade de esppecies
# 3 coluna profudenza
# 4 coluna tamanho medio de cada especie
esp = np.array([[747,89,33,5],
                [623,123,32,13],
                [501,22,49,2],
                [116,101,42,10],
                [297,56,69,22],
                [613,64,27,7],
                [295,84,29,14],
                [692,105,72,16],
                [229,103,35,5],
                [374,124,70,1]])
print(esp)

# adicione mais 2 especies
# # [204,10,40,12]  [392,11,81,11]
# # adicionar estas 2 especies acima na especies já existente

#  adicionar 2 linhas

print("##############")
espadic = np.array([[204,10,40,12],[392,11,81,11]])
print(espadic) 
print("##############")
adic = np.concatenate((esp, espadic))
print(adic) 
print("##############")
testeadic = np.concatenate((esp,[[204,10,40,12],[392,11,81,11]]))
print(testeadic) 


#  adicionar 1 coluna tem que indicar axis=1
# coluna [0,1,0,0,0,0,1,0,1,1,0]
# essa coluna diz se o animal enxerga ou não
print("##############")
enxerga = np.array([0,1,0,0,0,0,1,0,1,1,0])
print(enxerga.shape) 
print(esp.shape)
### temos dimensoes diferentes

## excluir o ultimo item que é zero 0, para dar mesmo shape
enxerga = np.delete(enxerga,-1) # exclui toda linha 3
print(enxerga)

# colocar na mesma dimensao, vertical
vertical_enxerga = enxerga.reshape((10,1))
print(vertical_enxerga)
# mesmo que o de baixo, igul so outra forma
vertical_enxerga = np.array([0,1,0,0,0,0,1,0,1,1]).reshape((10,1))
print(vertical_enxerga)

####
## agora adicionar a coluna enxerga a matriz esp
novaesp = np.concatenate((esp,vertical_enxerga),axis=1)
print(novaesp)


#adic = np.concatenate((esp, enxerga))
#print(adic) 
print("##############")


## Numpy parte 7
# salvando .npy arquivo numpy python
arr2d = np.array([[1,2,3,], [4,5,6]])
print(arr2d)
print('#')
arr3d = np.array([[[1,2,3,], [4,5,6]],[[1,2,3,], [4,5,6]]])
print(arr3d)
print('#')
print(arr3d.shape)

## salvando 2d
np.savetxt('arr2d', arr2d, delimiter=',')
## ou como csv np.savetxt('arr2d.csv',arr2d, delimiter=',')

## salvando 3d
np.save('arr3d',arr3d) # so save e nome array
## 3d nao posso salvar como txt nem csv só como save

### carregar arquivo 3D
arr_saved_3d = np.load('arr3d.npy')
print(arr_saved_3d)
print('3#')
print(arr_saved_3d.shape)

# carregar arquvivo 2D
arr_saved_2d = np.loadtxt('arr2d', delimiter=',')
print(arr_saved_2d)
print('2#')
print(arr_saved_2d.shape)


# outro exemplo salvando 4D dimensões
arr4d = np.array([[[[1,2,3,], [4,5,6]],[[1,2,3,], [4,5,6]]],[[[1,2,3,], [4,5,6]],[[1,2,3,], [4,5,6]]]])
print(arr4d)
print('##4D###')
print(arr4d.shape)

## salvando 4d
np.save('arr4d',arr4d) # so save e nome array
## 3d nao posso salvar como txt nem csv só como save

### carregar
arr_saved_4d = np.load('arr4d.npy')#
print(arr_saved_4d)
print('##4D#')
print(arr_saved_4d.shape)



