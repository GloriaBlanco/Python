# bloco while padrão para opção S-sim ou N-não

# enquanto verdade, ate opcao 'n' onde o comando break interrompe o while

while True:
    opcao = input("Deseja refazer a senha? (S/N): ")
    if opcao.lower() =='s':  # maisculo e minusculo tanto faz
        tamanho = int(input("Digite a quantidade de caracteresque deseja: "))
        print("A quantidade de senha terá ", tamanho, "numeros")
    elif opcao.lower() == 'n':
         break        