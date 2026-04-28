################
## Exemplo 2
## usuario entra com nome e valor da media, codigo informa se foi aprovado, reprovado ou recuperacao
#################

while True:
   
    aluno={} # variavel aluno vazia
    aluno['nome'] = str(input('Nome: '))
    aluno['media'] = float(input(f'Media de {aluno['nome']} '))
    if aluno['media'] >=7:
        aluno['situacao']='Aprovado'
    elif aluno['media'] >=5:
        aluno['situacao']='Recuperação'
    else:
        aluno['situacao']='Reprovado'

    print('=='*30)
    for k, v in aluno.items():
        print({k}) # k e a variavel nome, media, situacao - 1x cada um no for, sao itens da lista
        print({v}) # v e o que esta armazenado na variavel  nome digitado, media digitada, situacaodamedia - 1x cada um no for, sao itens da lista
    
        print(f' - {k} é igual a {v}')

    opcao = input("Deseja verificar outro aluno? (S/N): ")
    if opcao.lower() =='n':  # maisculo e minusculo tanto faz
       break
   
