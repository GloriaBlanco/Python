""" 

Biblioteca Requests Python
https://www.digitalocean.com/community/tutorials/how-to-get-started-with-the-requests-library-in-python-pt

Documentação Randomuser
https://randomuser.me/documentation


Crie um programa que gera um perfil de usuário aleatório 
usando a API 'Random User Generator'. O programa deve 
exibir o nome, email e país do usuário gerado.

"""

import requests

def obterusuarioaleatorio():
    url ='https://randomuser.me/api/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()['results'][0]
        nome = f"{dados['name']['title']} {dados['name']['first']} {dados['name']['last']}"
        email = dados['email']
        genero = dados['gender']
        celular = dados['cell']
        pais = dados['location']['country']
        return f"\nNome: {nome}\nEmail: {email}\nGênero: {genero}\nCelular: {celular}\nPaís: {pais}"
    except  requests.RequestExcepption as e:
        return f"Erro ao obter usuário aleatório: {e}"
    
print("Gerando um usuário aleatório: ")
usuario = obterusuarioaleatorio()
print(usuario)