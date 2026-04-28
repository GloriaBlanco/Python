"""
Sistema=Aplicativo

Passo a passo do Sistema = Aplicativo:
. Escolher o framework/ferramentas: streamlit, flask, Django, FastAPI. Cada um tem regras diferentes
    Escolhemos o streamlit porque ele permite apenas com python criar o front-end (visual) e o back-end (lógica)
. Escolher qual IA vamos usar: OpenAI(chatGPT), Gemini, Claude, Grok
    Escolhemos a OpenAI
. Escolher um Título 
. Campo de mensagem = input do chat para usuário
. A cada mensagem que o usuário enviar:
    # mostrar a mensagem que o usuario enviou no chat
    # enviar essa mensagem para a IA responder
    # exibir a resposta da IA na tela

OBSERVAÇAO
Execuçao deve ser pelo terminal:  streamlit run main.py
 
"""

# streamlit - frontend e backend
# pip install openia streamlit

import streamlit as st  # Importa a biblioteca Streamlit para criar a interface web
from openai import OpenAI  # Importa a classe OpenAI da biblioteca oficial para conectar com a API

# Cria uma instância do cliente OpenAI utilizando a sua chave de API para autenticação
#########################################################################
### esta chave API_KEY  NAO DEVE SER PUBLICADO É como uma SENHA
## para obter senha/api_key  =abrir site no google do OpneIA api, direita botao fazer login, engrenagem/apikeys/createnewsecret/colocarnome 
#########################################################################

modelo = OpenAI("SUA CHAVE API_KEY")

# Escreve um título no formato Markdown (H3) na página, tipo # letra pequena e ### letra maior
st.write("### ChatBot com IA") 

# session_state = memoria do streamlit
# Verifica se a chave "lista_mensagens" já existe na memória da sessão; se não existir, cria uma lista vazia
if not "lista_mensagens" in st.session_state:
    # crio a lista vazia
    st.session_state["lista_mensagens"] = []

# exibir o histórico de mensagens
# Percorre a lista de mensagens salva no session_state para redesenhar o chat a cada interação
for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]  # Identifica quem enviou (user ou assistant)
    content = mensagem["content"]  # Pega o conteúdo do texto
    st.chat_message(role).write(content)  # Renderiza a bolha de chat correspondente na tela

# Cria o campo de entrada de texto no rodapé da página para o usuário digitar
mensagem_usuario = st.chat_input("Escreva sua mensagem aqui")

# Verifica se o usuário pressionou Enter ou enviou uma mensagem
# para nao correr o risco de nao seguir sem o usuario ter digitado nada 
if mensagem_usuario:
    print(mensagem_usuario)
    #4 TIPOS DE informacao st.chat_message("tipo")
    #.nome do usuário - nome "Lira" = st.chat_message("Lira").write(mensagem_usuario) --- vai mostrar 1a. letra nome
    #.user -> ser humano =  st.chat_message("user").write(mensagem_usuario) --- vai mostrar icone usuario
    #.assistant -> inteligencia artificial = st.chat_message("assistant").write(mensagem_usuario) --- vai mostrar o icone do robo/IA
    #.Mostra imediatamente a mensagem que o usuário acabou de digitar na interface
    st.chat_message("user").write(mensagem_usuario)
    # abaixo tipo de resposta da IA respondendo, aqui nao esta usando a busca e respondendo, apenas usando o básico do streamlit
    # Cria um dicionário representando a mensagem do usuário e adiciona ao histórico (memória)
    mensagem = {"role": "user", "content": mensagem_usuario}
    st.session_state["lista_mensagens"].append(mensagem)

    # resposta da IA
    # Faz a chamada para a API da OpenAI enviando todo o histórico de mensagens para dar contexto0
    resposta_modelo = modelo.chat.completions.create(
        messages=st.session_state["lista_mensagens"], # Envia a lista completa de mensagens
        model="gpt-4o" # Define o modelo de linguagem a ser utilizado
    )

    # resposta da IA
    resposta_ia = "Você perguntou : " + mensagem_usuario

    # Extrai apenas o texto da resposta gerada pelo modelo
    resposta_ia = resposta_modelo.choices[0].message.content
    # exibir a resposta da IA na tela
    # Renderiza a bolha de chat do assistente com a resposta da IA
    st.chat_message("assistant").write(resposta_ia)
    # Cria o dicionário da resposta da IA e o salva no histórico para as próximas perguntas
    mensagem_ia = {"role": "assistant", "content": resposta_ia}
    # adicionar uma mensagem
    # st.session_state["lista_mensagens"].append(mensagem)
    st.session_state["lista_mensagens"].append(mensagem_ia)

print(st.session_state["lista_mensagens"])


