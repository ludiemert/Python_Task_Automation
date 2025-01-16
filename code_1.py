"""
Este módulo automatiza tarefas usando o PyAutoGUI.

Exemplo:
- Interações com a interface do usuário
- Captura de eventos do teclado e mouse
"""

import pyautogui

import time # ja eh um pacote do py

pyautogui.PAUSE = 1 #o pyautogui vai esperar 1 seg p algum delay sera em todo programa esse tempo, ele faz em todo o comando do projeto

# print(pyautogui.size())  # Exibe a resolução da tela
# pyautogui.click => clicar
# pyautogui.press => pressionar uma tecla de cada vez
# pyautogui.write => escrever um texto


# Passo 1: Abrir o sistema da empresa
  #sistema :  https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win")
# abrir o chome
pyautogui.write("chrome")
#de enter
pyautogui.press("enter")
#adicionar sistema emp
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
#de enter
pyautogui.press("enter")

#pedir p o comp esperar 3 seg, porq a net pode estar com dalay, ele faz somente nessa linha
time.sleep(3) # seu comp vai ficar "dormindo" qto tempo vc quiser, depois vai p prox etapa


# Passo 2:   Fazer login
# tem que clicar no campo de email e selecionar, p isso vc precisa dar click com mouse na tela, o lugar da tela??



# Passo 3: Importar a base de dados dos produtos

# Passo 4 : Cadastrar 1 produto

# Passo 5: Repetir o passo 4 ate acabar todos os produtos