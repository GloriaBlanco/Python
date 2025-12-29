"""
Crie um programa que consulte a cotação atual de uma
 moeda estrangeira em relação ao Real Brasileiro (BRL).
 O usuário deve informar o código da moeda desejada 
 (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
 máximo e mínimo da cotação, além da data e hora da última 
 atualização. Utilize a API da AwesomeAPI para obter 
os dados de cotação.

https://docs.awesomeapi.com.br/api-de-moedas

{
    "USDBRL": {
        "code": "USD",
        "codein": "BRL",
        "name": "Dólar Americano/Real Brasileiro",
        "high": "5.734",
        "low": "5.7279",
        "varBid": "-0.0054",
        "pctChange": "-0.09",
        "bid": "5.7276",
        "ask": "5.7282",
        "timestamp": "1618315045",
        "create_date": "2021-04-13 08:57:27"
    },
    "EURBRL": {
        "code": "EUR",
        "codein": "BRL",
        "name": "Euro/Real Brasileiro",
        "high": "6.8327",
        "low": "6.8129",
        "varBid": "-0.0069",
        "pctChange": "-0.1",
        "bid": "6.8195",
        "ask": "6.822",
        "timestamp": "1618315093",
        "create_date": "2021-04-13 08:58:15"
    },
    "BTCBRL": {
        "code": "BTC",
        "codein": "BRL",
        "name": "Bitcoin/Real Brasileiro",
        "high": "360000",
        "low": "340500",
        "varBid": "17072.9",
        "pctChange": "4.98",
        "bid": "359973.9",
        "ask": "359974",
        "timestamp": "1618315092",
        "create_date": "2021-04-13 08:58:12"
    }
}
"""

import requests

def cotacao(moeda):
    url = f'https://economia.awesomeapi.com.br/json/last/{moeda}-BRL'
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        dados = response.json()
        valorconversao = dados[f'{moeda}BRL']
        return f"""
        Moeda: {moeda} para BRL
        Valor atual: {float(valorconversao["bid"]):.2f}
        Máximo: {float(valorconversao["high"]):.2f}
        Mínimo: {float(valorconversao["low"]):.2f}
        Data/Hora: {valorconversao["create_date"]}
        """
        #return valorconversao
    except  requests.RequestException as erro:
        return f"Erro ao obter a cotação: {erro}"
    except KeyError:
        return f"Moeda não suportada ou não encontrada"

def main():

    print("----------- Cotação moeda ----------")
    try:

        moedaconverter = input("Para qual moeda deseja converter USD, EUR, GBP, JPY : ").upper().strip()
        print("\nObtendo cotação ...........")
        print("-----------------------------")
        valormoeda = cotacao(moedaconverter)
        print(valormoeda)

    except ValueError:
        print(f"\nValor inválido!! digite um valor numérico")

if __name__ == "__main__":
    main()
