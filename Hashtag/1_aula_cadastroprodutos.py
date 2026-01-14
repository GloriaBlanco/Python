""" 
Projeto Hashtag aulas do dia 12/01/2026
Este é um excelente exemplo de um script para realizar 
uma tarefa várias vezes.

"""
#### Monitor notebook lenovo em 90%

# Passo 1: Entrar no sistema da empresa 
site = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"


import pyautogui # Importa a biblioteca para controle do mouse e teclado
import time      # Importa a biblioteca para controle de tempo e pausas

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclas
pyautogui.PAUSE = 0.3 # Define uma pausa de 0.3 segundos entre cada comando do pyautogui

# abrir o navegador (chrome)
pyautogui.press("win")      # Aperta a tecla Windows do teclado
time.sleep(1) 
pyautogui.write("google chrome")   # Digita a palavra "chrome"
time.sleep(1) 
pyautogui.press("enter")    # Aperta a tecla Enter para abrir o navegador

# entrar no link MOLO000192 
pyautogui.write(site) # Digita o endereço do site
time.sleep(1) 
pyautogui.press("enter")    # Aperta Enter para acessar o site
time.sleep(3)               # Pausa o programa por 3 segundos para a página carregar


# Passo 2: Fazer login
# selecionar o campo de email
# pyautogui.click(x=685, y=451) # Clica na coordenada X e Y onde fica o campo de email
pyautogui.click(x=779, y=414)
# escrever o seu email
time.sleep(2) 
pyautogui.write("pythonimpressionador@gmail.com") # Digita o email de login
time.sleep(1) 
pyautogui.press("tab") # passando pro próximo campo (senha)
pyautogui.write("sua senha") # Digita a senha no campo 
time.sleep(1)      
#pyautogui.press("tab") # Vai para o botão de enviar
#pyautogui.press("logar") # cad
# astra o produto (botao enviar)
    
# pyautogui.click(x=955, y=638) # clique no botao de login através das coordenadas
pyautogui.click(x=673, y=574) # clique no botao de login através das coordenadas
time.sleep(4) # Espera 3 segundos para o sistema carregar após o login

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd # Importa a biblioteca Pandas para ler a base de dados
tabela = pd.read_csv("produtos.csv") # Carrega o arquivo "produtos.csv" para a variável tabela

print(tabela) # Exibe o conteúdo da tabela no terminalpythonimpressionador@gmail.com    sua senha

# Passo 4: Cadastrar um produto
for linha in tabela.index: # Inicia um loop para repetir o processo para cada linha da tabela
    # clicar no campo de código
    pyautogui.click(x=653, y=294) # Clica no primeiro campo do formulário de cadastro
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"] # Localiza a informação na coluna "codigo" da linha atual
    # preencher o campo
    pyautogui.write(str(codigo)) # Escreve o código convertido em texto (string)
    # passar para o proximo campo
    pyautogui.press("tab") # Aperta Tab para ir ao campo seguinte
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"])) # Localiza e escreve a marca
    pyautogui.press("tab") # Vai para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "tipo"])) # Localiza e escreve o tipo
    pyautogui.press("tab") # Vai para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "categoria"])) # Localiza e escreve a categoria
    pyautogui.press("tab") # Vai para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"])) # Localiza e escreve o preço
    pyautogui.press("tab") # Vai para o próximo campo
    pyautogui.write(str(tabela.loc[linha, "custo"])) # Localiza e escreve o custo
    pyautogui.press("tab") # Vai para o próximo campo
    obs = tabela.loc[linha, "obs"] # Armazena o que está na coluna "obs"
    if not pd.isna(obs): # Verifica se a informação de observação não está vazia
        pyautogui.write(str(tabela.loc[linha, "obs"])) # Escreve a observação caso ela exista
    pyautogui.press("tab") # Vai para o botão de enviar
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000) # Rola a página para o topo para recomeçar o processo
    # Passo 5: Repetir o processo de cadastro até o fim
