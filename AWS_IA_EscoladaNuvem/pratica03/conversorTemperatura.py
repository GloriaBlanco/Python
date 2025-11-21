"""
Aula 22/08/25

4- Conversor de Temperatura 
Crie um programa que converta temperaturas entre Celsius,
 Fahrenheit e Kelvin. 
O usuário deve informar a temperatura, a unidade de 
origem e a unidade para qual deseja converter.
Com certeza! A seguir, você encontra uma tabela que pode ser 
facilmente copiada e colada. 
Ela contém as fórmulas para a conversão entre as três principais
 escalas termométricas: **Celsius**, **Fahrenheit** e **Kelvin**.

### Fórmulas de Conversão de Temperatura
| De | Para | Fórmula |
| Celsius       | Fahrenheit =  (9/5)*C + 32
                | Kelvin (K) =  C + 273.15

| Fahrenheit    | Celsius = (F-32) * 5/9
                | Kelvin (K) = (F-32) * 5/9 + 273.15
                
| Kelvin (K)    | Celsius  = K - 273.15
                | Fahrenheit = 9/5*(K - 273.15)+ 32

"""
print("---------------  Conversão de temperaturas ---------------")
temperatura = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (ex. C, F ou K) : ").upper()
destino = input("Digite a unidade de destino (ex. C, F ou K) : ").upper()

if origem == destino:
    # não preciso converter
    resultado = temperatura
elif origem == "C":
    # escolhido = Celsius e converter para Fahrenheit ou Kelvin
    if destino == "F":
        # converter Celsius para Fahrenheit = C*(9/5) + 32
        resultado = (temperatura * 9/5) + 32
    else:
        # converter Celsius para Kelvin = C + 273.15
        resultado = temperatura+ 273.15
elif origem == "F":
        # escolhido = Fahrenheit então converter para Celsius ou Kelvin
        if destino == "C":
            # converter Fahrenheit para Celsius =  (F-32) * 5/9
            resultado = (temperatura-32)* 5/9
        else:
            # converter Fahrenheit para Kevin = (F-32) * 5/9 + 273.15
            resultado = (temperatura-32) * 5/9 + 273.15
else:
    # se nao for Celsius nem Fahrenheit entao é Kelvin
    if destino == "C":
        # converter de Kelvin para Celsius = K - 273.15
        resultado =  temperatura -273.15
    else: 
        # converter de Kelvin para Fahrenheit = (K - 273.15) * 9/5+ 32 
        resultado = (temperatura - 273.15) * 9/5 + 32


print("-------------------------------------")
print(f"Temos que {round(temperatura)} {origem} corresponde a {round(resultado)} {destino}")               
