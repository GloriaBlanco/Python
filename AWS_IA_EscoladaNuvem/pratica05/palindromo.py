""" 
Crie uma função que verifique se uma palavra ou 
frase é um palíndromo (lê-se igual de trás para frente, 
ignorando espaços e pontuação). Se o resultado é True,
responda “Sim”, se o resultado for False, responda “Não”.
escrever de trás pra frente é a mesma coisa
Arara
ana
a cara rajada da jararaca
lembrar de tirar espaços em branco
"""

print("--------- Função do exemplo Lambda --------")
def palindromo(textodigitado):
    # remover espeços em branco e converter para minusculo
    textolimpo = ''.join(char.lower() for char in textodigitado if char.isalnum())
    # aqui pergunta se o texto limpo é igual ao invertido, Verdadeiro ou falso
    return textolimpo == textolimpo[::-1]
    
texto = input('Entre com frase ou palavra palíndromo: ')
resultado = palindromo(texto)

print(f"O texto {texto} é palindromo ? {palindromo(texto)}")
print(f"O texto {texto} é palindromo ? {resultado}")

# outra forma de exibir
if resultado == True:
    resposta = "sim"
else:
    resposta = "não"

print(f"O texto {texto}, {resposta} é um palindromo")



