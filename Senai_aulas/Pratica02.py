# aula de Python no Senai, 20 de fevereiro de 2024
# saída tipo floot
print(1.1) # imprime 1.1
# saida numero inteiro
print(11)  # imprime 11
print(-11) # imprime -11
print() # pula uma linha
# type mostra tipo de saida
print(  type("Marcos'Paulo'")   )   # imprime <class 'str'>
print(  type(-11)               )   # imprime <class 'int'>
print(  type(1.1)               )   # imprime <class 'float'>
print(  type("1.1")             )   # imprime <class 'str'>
# bool / bolean, true ou false, sim ou não, verdadeiro ou falso
print(10==10)   # imprime True
print(10==11)   # imprime False
print(10>11)    # imprime False
print(10<11)    # imprime True
print(10>=10)   # imprime True
print(10<=10)   # imrpime True
print(10>=11)   # imprime false
print(10<=11)   # imprime true
print(10!=11)   # imprimi True   (este != significa diferente)
print(10!=10)   # imprime False
print(11,1.1,True)  # imprime 11  1.1  True
# sinal + em numeros faz soma e em string/letras apenas junta/concateno
print(1+1)      # imprimi 2
print(1 +1)     # imprimi 2
print('a'+'b')  # imprimi ab
# print('a'+1) dá erro, só consigo somar mesmo tipo de tipo, Ptython é de tipagem forte mas Java faz soma mas tipagem fraca
# print(int('A'), type(int('1'))) erro nao soma, porque aqui só mostra tipo, n"ao transforma
print(type(float('1'+'1')))
print(bool(''))         # imprime  class 'float
print(str(11) + 'b')    # imprime 11b
print('')               # pula 1 linha

# execício valores booleanos
print("Exercício")
a=3
b=4
c=a<b
d=a>b
e=a==b 
print("Valor de c: ",c)     # imprime Valor de c: True
print("Valor de d: ",d)     # imprime valor de d: False
print("Valor de e: ",e)     # imprime valor de e: False

print(bool())       # imprime False
print(bool(""))     # imprime False
print(bool('limão'=='limão'))   # imprime True
print(bool('limão'=="limão"))   # imprime True
