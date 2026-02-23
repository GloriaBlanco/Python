# ############ 
# fazer lista supermercado
# usuario digita um item a ser incluido na lista
# usuario digita um nome para verificar se esta na lista
# e fala qual posicao do item na lista
# ##############
 
print('\n') # uma linha

mercado = ["café","açúcar","leite","água","suco","queijo","atum","gelatina","pimenta","ovos"]
print(mercado)  #  variavel mercado com lista 

print(f'tamanho da lista: {len(mercado)}')          # tamanho da lista: 4
print(f'endereço da palavra suco: {mercado.index('suco')}') # endereço da letra ovos:

i = 0
# Append adicionar um item ao final da lista
adicionar = str(input("Digite o item que falta na lista: ")) # imprimi na tela
while i < len(mercado):
        if mercado[i] == (adicionar):
            print(f'O item {mercado[i]} ja esta na lista , te achei na  {i+1} posição da lista)')
            break
        i +=1
        if i >= len(mercado): 
                mercado.append(adicionar)    # aguarda usuário digitar uma nova marca e inclui no final da lista
                print('\n')  # imprimi uma linha
                print(mercado) # imprimi a lista com novo item incluido
                break
        
print('\n')  # imprimi uma linha
print(mercado) # imprimi a lista com novo item incluido                

# verificar a existencia de um nome na lista
i=0

print('*********************************************')
print('\n')

# verificar a existencia de um nome na lista, se nao tiver inclui

var = input('Informe um item : ')
if var.lower() in mercado:
    print(f"O item '{var.lower()}' está na lista")
    while i < len(mercado):
        if mercado[i] == (var):
            print(f'OIeee {mercado[i]} , te achei na  {i+1} posição da lista)')
            break
        else:
            if i ==len(mercado): 
                print(f'OIeee {var} , não te achei na lista')   
        i +=1
else:
    print(f"O item '{var.lower()}' não está na lista")
    
# verificar a existencia de um nome na lista que usuário incluiu e fala qual posicao

print('*********************************************')
print('\n')

var1 = input('Informe MAIS um item : ')
ii=0
while ii < len(mercado):
    if mercado[ii] == (var1):
       print(f'OIeee {var1} , te achei na  {ii+1} posição da lista)')
       break
    elif (ii+1) == len(mercado): 
         print(f'OIeee {var1} , não te achei na lista')   
    ii +=1
