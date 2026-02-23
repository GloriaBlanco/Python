###############
# Libertadores = armazenamento dos 20 primeiros colocados do Brasileirão 2024

import os
os.system('cls')

times = (
        "Palmeiras",
        "Grêmio",
        "Atletico-MG",
        "Flamengo",        
        "Botafogo",
        "Bragantino",
        "Fluminense",
        "Athletico-PR",
        "Internacional",
        "Fortaleza",
        "São Paulo",
        "Cuiba",
        "Corinthians",
        "Cruzeiro",
        "Vasco",
        "Bahia",
        "Santos",
        "Goias",
        "Coritiba",
        "America-MG"
)

pontuacao  = (
        70,
        68,
        66,
        66,
        64,
        62,
        56,
        56,
        55,
        54,
        53,
        51,
        50,
        47,
        45,
        44,
        43,
        38,
        30,
        24       
)

consulta = str(input('\nDigite o time ou posição que deseja consultar: '.title()))

try:
     consulta=int(consulta)
     print(f'O time que está na {consulta} posição é o {times[consulta-1]}')

except ValueError:
     if consulta in times:
        print(f'O time {consulta} está???? na {times.index(consulta)+1}ª posição')

     else:
         print(f'O time {consulta} não participou da competição')

   

