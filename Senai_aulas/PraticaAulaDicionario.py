###########
# Aula Dicionario, 01 de março de 2024
# listas (), dic {:}
###########

dic = {"Curso":"Python","Aula":"Aula7","Professor":"Marcos Paulo"}
print(f'Professor {dic["Professor"]} que ministra o curso {dic["Curso"]}')
print("\n")
            
dic["aula"] = "Aula07 - Dicionarios"
dic.clear()
print(dic)
del dic

####################
# Dicionário = obtendo itens, chaves e valores
####################

carros = {'marca':'VM','modelo':'Gol','ano_modelo':2016}
print(f'Itens do dicionário carros : {carros.items()}')
print(f'Chaves do dicionário carros : {carros.keys()}')
print(f'Valores do dicionário carros : {carros.values()}')

#################
## exemplos
#################

produtos ={'Mouse': 98.75,
           'Teclado':125.65,
           'Monitor':134.78,
           'Gabinete':170.00,
           'HD Externo':510.50,
           'Headset':125.45 }
print("\n")
print("produtos disponiveis:")
for i, k in produtos.items():
    print(f' - {i}')
print("\n")
while True:
    produto = input('Informe o produto a pesquisar o preço ou fim para sair: ')
    if produto =='fim':
        break
    if produto in produtos:
        print("\n")
        print(f'Produto {produto} custa {produtos[produto]}.')
    else:
        print(f'Produto {produto} não encontrado.')


#################
## Outra funções
#################

dic ={'Nome': 'Fulano','Sobrenome':'de Tal'}
local ={'UF':'SP','cidade':'São Carlos' }

dic2 = dic.copy()   # copiou a lista/dicionario do dic
dic.update(local)   # a lista/dicionario dic incorpora/adiciona a lista/dicionario Local
a=(len(dic))     # tamanho dic
print(f"tamanho da lista e {a}")
print(f'dic:{dic}')     #{'Nome': 'Fulano', 'Sobrenome': 'de Tal', 'UF': 'SP', 'cidade': 'São Carlos'}
print(f'dic2:{dic2}')   #{'Nome': 'Fulano', 'Sobrenome': 'de Tal'} 


#################
## Exemplo 2
#################

aluno={}
aluno['nome'] = str(input('Nome: '))
aluno['media'] = float(input(f'Media de {aluno['nome']} '))
if aluno['media'] >=7:
    aluno['situacao']='Aprovado'
elif aluno['media'] >=5:
    aluno['situacao']='Recuperação'
else:
    aluno['situacao']='Reprovado'

print('=='*30)
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')

