# Para importar todo o conteúdo do módulo "funcoes_do_log" sem precisar
# utilizar o namespace para usá-lo, podemos utilizar a palavra chave "from".
# O conteúdo do módulo vai ser todo importado para o namespace corrente.
# O asterisco indica que queremos importar todo o conteúdo deste módulo.
from funcoes_do_log import *
# utilizei o from para importar *=tudo da função funcoes_do_log
# todas as funcoes e variaveis verão para cá
# cuidado porque o * traz tudo e isso pode gerar conflitos e trazer muita coisa
# não é uma boa prática
imprimir_no_log(f'Bem vinda, {nome_de_usuario}!')