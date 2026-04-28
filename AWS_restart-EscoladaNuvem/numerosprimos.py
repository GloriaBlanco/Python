# Laboratório 141
# Abre o arquivo results.txt no modo de escrita
# Se o arquivo nao existir, ele sera criado. Se ja existir, sera sobrescrito.
results = open("results.txt", "w")

for x in range(2, 251):
    # Loop principal para testar cada número de 2 a 250
    primo = True
    
    # Verifica possiveis divisores
    for i in range(2, x):
        # Loop para testar se numero é divisível por algum 'i' (de 2 até 251-1)
        if (x % i) == 0: # verifica o resto = 0, então não é primo
            primo = False
            break

    # Se o numero for primo, escreve ele no arquivo
    if primo:
        # Se numero passou por todos os testes e primo ainda é True
        results.write(str(x) + "\n")
        # escreve o número no arquivo 'results.txt', seguido de uma quebra de linha

results.close() # fecha o arquivo

print("Tudo OK, os números primos entre 1 e 250 foram salvos no arquivo results.txt")

# imprime o arquivo texto results.txt

# Reabre o arquivo em modo de leitura
arquivo_leitura = open("results.txt", "r")

# Lê todo o conteúdo do arquivo
arquivo = arquivo_leitura.read()

# Imprime o conteúdo no console
print("\nConteúdo de results.txt:")
print(arquivo)

# Fecha o arquivo de leitura
arquivo_leitura.close()               
