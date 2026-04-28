"""
Desenvolva um programa que consulte informações de endereço
 a partir de um CEP fornecido pelo usuário, utilizando a API ViaCEP.
 O programa deve exibir o logradouro, bairro, cidade e estado 
 correspondentes ao CEP consultado.

 get - recupera dados de um servidor
 post - envia dados para serem processados por um servidor
 put - atualiza dados existentes no servidor
 delete - remove dados no servidor
  
 Documentaçao webservice do site
 
"""

import requests
print("---------  Busca CEP ----------")

def obtercep(cep):
    url = f'https://viacep.com.br/ws/{cep}/json/'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        if "erro" in dados:
            return "Cep não encontrado"
        return f"""
        Cep: {cep}
        Logradourocep: {dados['logradouro']}
        Complementocep: {dados['complemento']}
        Bairro: {dados['bairro']}
        Localidade: {dados['localidade']}
        UF: {dados['uf']}
        Estado: {dados['estado']}
        Regiao: {dados['regiao']}
        """
        #return f"\nLogradouro: {logradourocep}\nComplemento: {complementocep}\nBairro: {bairro}\nLocalidade: {localidade}\nUF: {uf}\nEstado: {estado}\nRegião: {regiao}"

    except  requests.RequestException as erro:
        return f"Erro ao obter cep: {erro}"
    
def main():
    cepconsultar= input("Digite o cep que deseja consultar: ")
    dadoscep = obtercep(cepconsultar)
    print(f"\n{dadoscep}\n")

if __name__ =="__main__":
    main()