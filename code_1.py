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
pyautogui.click(x=466, y=374)
# se quiser dar mais comandos na mesma linha pyautogui.click(x=466, y=374, clicks=2)
#digitar o email
pyautogui.write("lua@gmail.com")
#passar para prox linha senha (tem 2 formas ou pega posicao do mouse ou tecla TAB ele vai p prox linha)
pyautogui.press("tab")
#senha
pyautogui.write("123")
#prox tecla e depois de enter p entrar no sistema
pyautogui.press("tab")
#tecla login
#prox tecla e depois de enter p entrar no sistema
pyautogui.press("enter")

# Passo 3: Importar a base de dados dos produtos
#instal  pip install pandas openpyxl
import pandas

# precisa armazenar essa base de dados, preciso criar uma variavel
# vai ler e armazenar na variavel tabela

tabela = pandas.read_csv("produtos.csv")

print(tabela)

time.sleep(2)
# trazer a base de dados para o pandas
#ler um arquivo csv
# pandas.read_csv("produtos.csv") #passa o produto que quer ler
# se quiser ver a tabela print(tabela)
# se quiser copiar tabela tabela.copy()

# Passo 4 : Cadastrar 1 produto
#pegar posicao x,y do cod produto
pyautogui.click(x=463, y=257)

#cadastrar o texto na primeira linha, o primeiro produto
#fazer 1 produto primeiro
# MOLO000251,Logitech,Mouse,1,25.95,6.50,
# nome das colunas => codigo,marca,tipo,categoria,preco_unitario,custo,obs

#codigo
pyautogui.write("MOLO000251")
pyautogui.press("tab")

#marca
pyautogui.write("Logitech")
pyautogui.press("tab")

#tipo
pyautogui.write("Mouse")
pyautogui.press("tab")

#categoria
pyautogui.write("1")
pyautogui.press("tab")

#preco_unitario
pyautogui.write("25.95")
pyautogui.press("tab")

#custo
pyautogui.write("6.50")
pyautogui.press("tab")

#obs
pyautogui.write("")
pyautogui.press("tab")


#Enviar




# Passo 5: Repetir o passo 4 ate acabar todos os produtos