""" Estruturas de condições
condição = if : else: 
repetição enquanto = while :
repetição para cada item = for  i in lista:  = loop infinito numero vezes

Exercícios
TomadadeDecisão
1.FaçaumProgramaquepeçadoisnúmeroseimprimaomaiordeles.
2.FaçaumProgramaquepergunteemqueturnovocêestuda.PeçaparadigitarM-matutinoouV-VespertinoouN-Noturno.Imprimaamensagem"BomDia!","BoaTarde!"ou"BoaNoite!"ou"ValorInválido!",conformeocaso.3.Façaumprogramaquepeçaumanota,entrezeroedez.Mostreumamensagemcasoovalorsejainválidoecontinuepedindoatéqueousuárioinformeumvalorválido.4.Implementeumprogramaqueclassifiqueumalunocombaseemsuapontuaçãoemumexame.Oprogramadeverásolicitarumanotade0a10.Seapontuaçãoformaiorouiguala7,oalunoéaprovado;casocontrário,éreprovado.5.Desenvolvaumprogramaquesoliciteaousuáriooscomprimentosdostrêsladosdeumtriânguloeclassifique-ocomoequilátero,isóscelesouescaleno.equilátero:todososladoscomomesmovalorisósceles:doisladoscomomesmovalorescaleno:todososladoscommedidasdistintas.6.Crieumprogramaquesoliciteaousuárioumlogineumasenha.Oprogramadevepermitiroacessoapenasseousuáriofor"admin"easenhafor"admin123",casocontrárioimprimaumamensagemdeerro.7.Desenvolverumprogramaquesoliciteaidadedousuárioeidentifiqueseeleéumacriança,umadolescente,adultoouidoso.8.CriarumprogramaemPythonquesolicitetrêsnúmerosaousuário,utilizeestruturascondicionaisparadeterminaromaiorentreeleseapresenteoresultado.
9.Oprogramadevecalculareapresentaraquantidadedenúmerospareseímparesinseridos.Oprocessodeleituradeveserencerradoquandoousuárioinformarovalorzero.Certifique-sedeincluirvalidaçõesparagarantirqueapenasnúmerospositivossejamconsideradosnacontagemecálculos.10.Façaumprogramaquelêtrêsnúmerosinteiroseosmostraemordemcrescente.11.Escrevaumprogramaquecalculeosaláriolíquido.LembrandodedeclararosaláriobrutoeopercentualdedescontodoImpostodeRenda.●RendaatéR$1.903,98:isentodeimpostoderenda;●RendaentreR$1.903,99eR$2.826,65:alíquotade7,5%;●RendaentreR$2.826,66eR$3.751,05:alíquotade15%;●RendaentreR$3.751,06eR$4.664,68:alíquotade22,5%;●RendaacimadeR$4.664,68:alíquotamáximade27,5%.

"""

idade = 0

while idade < 18:
    idade = int(input('Qual sua idade : '))
    if idade > 17:
        print('Maior de idade.................')
    else:
        print('Menor de idade')


frutas = ['Maça', 'Banana','Uva']
# para cada fruta
for fruta in frutas:  # fruta = i = qualquer nome
    print(fruta)

for i in frutas:
    print(i)
