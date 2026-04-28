"""Prática Aula gratuita Hashtag dia 12/01/2026"""

import time      # Importa a biblioteca de tempo (para pausas)
import pyautogui  # Importa a biblioteca que controla mouse e teclado
2
# 1. Pausa o programa por 5 segundos
# Isso serve para dar tempo de você mudar de janela, para o navegador
time.sleep(5)

# 2. Captura e imprime no terminal a posição atual do mouse (X e Y)
# Útil para descobrir as coordenadas de onde você quer clicar depois
print(pyautogui.position())

# 3. Rola a página/tela para cima
# O número 300 indica a "quantidade" de scroll. 
# Valores positivos (300) sobem, valores negativos (-200) descem.
pyautogui.scroll(300)
