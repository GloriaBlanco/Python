###################
## Cotaçao moeda, dolar, euro, peso chileno, libra
###################

import json
import requests

# este site awesomeapi é uma biblioteca com várias informações
res = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL,CLP-BRL,GBP-BRL')
moeda = res.json()

print(f'O dolar está R${float(moeda["USDBRL"]["bid"]):.2f}')
print(f'O euro está R${float(moeda["EURBRL"]["bid"]):.2f}')
print(f'O bitcoin está R${float(moeda["BTCBRL"]["bid"]):.2f}')
print(f'O peso chileno está R${float(moeda["CLPBRL"]["bid"]):.2f}')
print(f'A libra esterlina está R${float(moeda["GBPBRL"]["bid"]):.2f}')

