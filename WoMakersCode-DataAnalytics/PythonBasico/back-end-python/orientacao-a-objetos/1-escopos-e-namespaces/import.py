# A função "imprimir no log" está no módulo "funcoes_do_log" (nome do arquivo .py).
# Precisamos importar o módulo para poder reutilizar seu conteúdo aqui.

# A palavra chave import disponibiliza o conteúdo do módulo através do
# namespace "funcoes_do_log".
import funcoes_do_log
# preciso colocar o name space da funcao para o import reconhecer

funcoes_do_log.imprimir_no_log(f'Bem vinda, {funcoes_do_log.nome_de_usuario}!')