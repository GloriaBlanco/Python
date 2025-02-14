# Aula inserir, apagar, listar
# import OS = biblioteca que oferece varias funcionalidade, criar,copiar, renomear e excluir
import os
lista = []  # cria uma lista vazia
while True:  # loop enquanto for verdade
    print('Selecione uma opção') 
    opcao = input('[i]nserir [a]pagar [l]listar [S]sair: ')    #usuário vai escolher i, a, l ou s
    
    if opcao == "i":        # verifica a variavel digitada
        os.system('cls')      # ou clear ? armazena e limpa codigo
        valor = input('valor: ')  # armazena valor digitado
        lista.append(valor)   # adiciona o valor digitado a lista
    elif opcao == 'a':  # verifica se a minha variavel "a" foi digitada
        indice_str = input('Escolha o índice para apagar:  ')
        try:    # para tratar um erro usamos o try
            indice = int(indice_str)    #armazena um nº inteiro
            del lista[indice]   # deleta um numero da minha lista
        except ValueError:      # trata o erro caso o valor não seja o esperado
            print('Por favor digite número int. ')  #digite um numero inteiro
        except IndexError:      # trata o erro no indice_str caso não há
            print('Índice não existe na lista')    
        except Exception:      # trata um erro deconhecido
            print('Erro desconhecido')
    elif opcao == 'l':      # verifica se a variável digitada foi l, ou seja, se existe + de 1 opção
         os.system('cls')  #  limpa o terminal
         if len(lista) == 0: # compara e conta minha lista
             print('Nada para listar')

         for i, valor in enumerate(lista):   #repete e enumera a lista
             print(i, valor)     #imprimi nº contador e valor da lista

    elif opcao == 's':      # verifica se a variável digitada foi s, SAIR
         break

    else:   #caso for falso
        print('Por favor, escolha i, a, l ou s.') 
        
 
