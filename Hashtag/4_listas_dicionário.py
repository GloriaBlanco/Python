
# lista, sempre com colchetes
# lista vazia = lista = []
lista_nomes = ["lira", "jorge", "gi", "renan"]
print(lista_nomes)
lista_nomes.append("julia") # adiciona informação ao final de uma lista
print(lista_nomes)

primeiro_item = lista_nomes[0]
print(primeiro_item)    # primeiro é 0 zero
print(lista_nomes[4])   # este é o ultimo


# dicionario python
# dicionario voce armazena varias informaçoes para cada item e a lista apenas 1 informação
# dicionario =  {nome0: valor, nome1:valor}
# dicionario = dicionario[nome1]
dicionario = {'Lira':31, 'Thalia':23, 'Gi': 51}
print(dicionario)
print(dicionario['Lira'])
dicionario["Michely"] = 25
dicionario["Lira"] = 26  
print(dicionario)

# no código vou precisar de um dicionario das mensagens
# no main (streamlit) vou precisar guardar o usuário e o texto dessa mensagem
# guardar a lista de mensagens1, 2, etc 
mensagem1 = {"usuario":"IA", "texto": "Bora aprender Python"}
mensagem2 = {"usuario":"Lira", "texto": "Sim, me ensine Python"}
mensagem3 = {"usuario":"IA", "texto": "Entao vou começar a aula"}
# uma lista com várias mensagens 
listamensagens = [mensagem1, mensagem2, mensagem3]
print(listamensagens)



# role = quem enviou a mensagem = "função" = usuário que escreveu mensagem
# content = texto da mensagem = "conteudo"
mensagem = {"role": "user", "content": "Coe galera"}
# dicionario = {chave: valor, chave: valor}
# 1 elemento -> dicionario[chave] -> valor

texto_mensagem = mensagem["role"]
print(texto_mensagem)

# lista + dicionario
lista_mensagens = [
    {"role": "user", "content": "Coe galera"}, 
    {"role": "assistant", "content": "Resposta da IA"}, 
    {"role": "user", "content": "Tamo junto"}
    ]

lista_mensagens.append(
    {"role": "assistant", "content": "Eu desisto de você"}
)

print(lista_mensagens)

# exibir todos os itens de uma lista
for nome in lista_nomes:
    print(nome)

for mensagem in lista_mensagens:
    print(mensagem)