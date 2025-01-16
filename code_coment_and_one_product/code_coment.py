"""
Este módulo automatiza tarefas usando o PyAutoGUI.

Exemplo:
- Interações com a interface do usuário
- Captura de eventos do teclado e mouse
"""


"para pausar o projeto qdo estiver executando so colocar o mouse acima do monitor o programa para"

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

# Passo 4 : Cadastrar 1 produto
# poderia usar o while, mas o while tem que falar qdo comeca e qdo termina, eh outra regra o for eh faz ate o fim

#fazer uma identacao apos o for (um tab) ele executa esse bloco de comandos
# para o py cada linha eh um index (indice) => tabela.index sao as linhas ta tab
#para cada linha dentro da minha tabela execute tudo isso:
for linha in tabela.index:

  # tem que ser o mesmo campo da tabela "da base de dados" (codigo,marca,tipo,categoria,preco_unitario,custo,obs)
  #pegar posicao x,y do cod produto
  pyautogui.click(x=463, y=257) # a partir daqui eu quero que ele repita no campo 5, vamos fazer um for

  #codigo
  codigo = tabela.loc[linha, "codigo"] # variavel codigo => "loc"localiza na minha tabela linha codigo. o [] porque toda lista de valores do py eh essa regra.
  pyautogui.write(str(codigo)) # pyautogui.write("MOLO000251") . sempre relacionar algo na tabela usa []
  pyautogui.press("tab")

  #marca
  marca = tabela.loc[linha, "marca"]
  pyautogui.write(str(marca)) # str => string = texto
  pyautogui.press("tab")

  #tipo
  tipo = tabela.loc[linha, "tipo"]
  pyautogui.write(str(tipo))
  pyautogui.press("tab")

  #categoria
  categoria = tabela.loc[linha, "categoria"]
  pyautogui.write(str(categoria))
  pyautogui.press("tab")

  #preco_unitario
  preco_unitario = tabela.loc[linha, "preco_unitario"]
  pyautogui.write(str(preco_unitario))
  pyautogui.press("tab")

  #custo
  custo = tabela.loc[linha, "custo"]
  pyautogui.write(str(custo))
  pyautogui.press("tab")
  #obs
  #qdo o campo obs estiver vazio oq fazer?
  #obs ele pode vir vazio prec trab ele
  obs = str(tabela.loc[linha, "obs"])
  if obs != "nan" : # se obs for diferente "!=" de nan entao cadastra o obs aqui
    pyautogui.write(obs)
  pyautogui.press("tab")

  #apertar botao de Enviar
  pyautogui.press("enter")


  #dar um scroll p cima da tela, numero positivo scroll sobe numero negativo desce scroll
  pyautogui.scroll(10000) # numero alto em pixel ele vai p cima da tela,
  #pode ser colocar a press na  tecla pg up e pg dn

# Passo 5: Repetir o passo 4 ate acabar todos os produtos

# nan qdo aparecer no py ele eh um valor vazio em uma base de dados, o pandas coloca nan em valores vazios
# nan vem de NOT A NUMBER um valor que nao esta preenchido, precisa trab ele no codig, ex o obs da tab