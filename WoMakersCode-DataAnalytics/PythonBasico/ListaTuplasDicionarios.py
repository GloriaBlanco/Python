"""
Listas --------
lista = []
lista.append('Maça')

tupla nao podem ter valores alterados

Tuplas -------
tupla = ()
tuplas = ('Maça', 'uva','banana')

Dicionários -------
dicionario = {}
dicionario = {'Chave': 'Valor'}
dicionario['Carro'] = 'é um veículo'

Exercícios

Tuplas,Listas e Dicionários
1.Utilizandolistasfaçaumprogramaquefaça5perguntasparaumapessoasobreumcrime.Asperguntassão:
""Telefonouparaavítima?
""Estevenolocaldocrime?
""Morapertodavítima?
""Deviaparaavítima?
""Játrabalhoucomavítima?""Oprogramadevenofinalemitirumaclassificaçãosobreaparticipaçãodapessoanocrime.
Seapessoaresponderpositivamentea2questõeseladeveserclassificadacomo""Suspeita"",entre3e4como""Cúmplice""e5como""Assassino"".Casocontrário,eleseráclassificadocomo""Inocente"".

2.FaçaumProgramaquepeçaasquatronotasde5alunos,calculeearmazenenumalistaamédiadecadaaluno,imprimaonúmerodealunoscommédiamaiorouiguala7.0.

3.Crieumdicionáriorepresentandoumcarrinhodecompras.Adicioneprodutos(chaves)equantidades(valores)aocarrinho.Calculeototaldocarrinhodecompra.

4.Crieumdicionáriorepresentandocontatos(nome,telefone).Permitaaousuárioprocurarporumcontatopelonome.

5.Crieduastuplas.Concatene-asparaformarumanovatupla.

6.Faça um programa que permita ao usuário digitar os seu nome e em seguida mostre o nome do usuário de trás para frente utilizandosomenteletrasmaiúsculas.

Dica:lembre−sequeaoinformaronomeousuáriopodedigitarletrasmaiúsculasouminúsculas. 
"""

lista = []
lista.append('Maça')
lista.append('Uva')
print(lista)

nova_fruta = input('Qual fruta : ')
lista.append(nova_fruta)
print(lista)

###########

tupla = ('Maça', 'banana')
print(tupla)

###########

dicionario = {}
dicionario['Maça'] = 'E uma fruta'
dicionario['Carro'] = 'é um veículo'
dicionario['Gato'] = 'é um animal'
print(dicionario)
