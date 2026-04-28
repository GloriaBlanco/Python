"""
5- Verificador de Ano Bissexto
Faça um programa que determine se um ano inserido pelo 
usuário é bissexto ou não.
Um ano é bissexto se for divisível por 4, exceto anos
centenários (divisíveis por 100) que não são divisíveis por 400.
Para saber se um ano é bissexto, você precisa seguir 
três regras. 

Um ano é bissexto se:
Ele for divisível por 4.
E não for divisível por 100, exceto se...
Ele for divisível por 400.
Em outras palavras, se um ano for divisível por 4, ele é bissexto. 
A única exceção a essa regra é para os anos de século (aqueles que terminam em 00).
Nesses casos, o ano só é bissexto se for divisível por 400.

Exemplos práticos
2024 é bissexto?
Sim, porque é div
1900 é bissexto?
Não, porque, apesar de ser divisível por 4, é divisível por 100 e não é divisível por 400.
2000 é bissexto?
Sim, porque, apesar de ser divisível por 100, também é divisível por 400.

"""
print("-----------  Verifica se o Ano é bissexto ----------")

def ano(msg):
    while True:
        try:
            entradaano = int(input(msg))
            if entradaano > 10000:
                print(f"Ano {entradaano} inválido! digite novamente")
            else:
                # ok retorna
                return entradaano
                #break

        except ValueError:
            print("Valor Inválido! Digite um ano")

anodigitado=ano("Digite o ano que deseja verificar se é bissexto: ")

if ((anodigitado % 4) == 0 and (anodigitado % 100) != 0 ) or ((anodigitado % 4) == 0 and (anodigitado % 100) == 0 and (anodigitado % 400) == 0):
    print(f"Simm, {anodigitado} é um ano Bissexto !!")
else:
    print(f"Não, {anodigitado} não é um ano bissexto")
