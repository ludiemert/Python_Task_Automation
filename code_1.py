"""
Este módulo automatiza tarefas usando o PyAutoGUI.
"""

import time
import pandas as pd  # Renomeando pandas para 'pd', que é uma convenção comum
import pyautogui
import keyboard

# Configuração do PyAutoGUI
pyautogui.PAUSE = 1  # Define um delay padrão entre as ações para evitar erros

try:
    # === Início do programa ===
    print("Pressione 'Esc' para interromper o programa a qualquer momento.")

    # Passo 1: Abrir o sistema da empresa
    print("Abrindo o sistema...")
    pyautogui.press("win")  # Abrir o menu iniciar
    pyautogui.write("chrome")  # Digitar 'chrome'
    pyautogui.press("enter")  # Pressionar Enter para abrir o navegador
    time.sleep(2)

    # Abrir a URL do sistema
    pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
    pyautogui.press("enter")
    time.sleep(5)  # Aguardar o carregamento do site

    # Passo 2: Fazer login
    print("Realizando login...")
    pyautogui.click(x=466, y=374)  # Clicar no campo de e-mail
    pyautogui.write("lua@gmail.com")  # Digitar o e-mail
    pyautogui.press("tab")  # Ir para o campo de senha
    pyautogui.write("123")  # Digitar a senha
    pyautogui.press("tab")  # Ir para o botão de login
    pyautogui.press("enter")  # Fazer login
    time.sleep(3)  # Aguardar o carregamento do sistema

    # Passo 3: Importar a base de dados dos produtos
    print("Importando base de dados...")
    tabela = pd.read_csv("produtos.csv")
    print(tabela)
    time.sleep(2)

    # Passo 4: Cadastrar produtos
    print("Cadastrando produtos...")
    for linha in tabela.index:
        # Preencher campos com base na tabela
        pyautogui.click(x=463, y=257)  # Clicar no campo 'Código'

        # Código do produto
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(str(codigo))
        pyautogui.press("tab")

        # Marca
        marca = tabela.loc[linha, "marca"]
        pyautogui.write(str(marca))
        pyautogui.press("tab")

        # Tipo
        tipo = tabela.loc[linha, "tipo"]
        pyautogui.write(str(tipo))
        pyautogui.press("tab")

        # Categoria
        categoria = tabela.loc[linha, "categoria"]
        pyautogui.write(str(categoria))
        pyautogui.press("tab")

        # Preço unitário
        preco_unitario = tabela.loc[linha, "preco_unitario"]
        pyautogui.write(str(preco_unitario))
        pyautogui.press("tab")

        # Custo
        custo = tabela.loc[linha, "custo"]
        pyautogui.write(str(custo))
        pyautogui.press("tab")

        # Observações
        obs = str(tabela.loc[linha, "obs"])
        if obs != "nan":  # Verifica se o campo não está vazio
            pyautogui.write(obs)
        pyautogui.press("tab")

        # Enviar o formulário
        pyautogui.press("enter")

        # Scroll para ajustar a visualização
        pyautogui.scroll(10000)  # Subir para o topo da tela

        # Verificar interrupção
        if keyboard.is_pressed('esc'):
            print("Programa interrompido pelo usuário.")
            break

#Captura especificamente o erro FileNotFoundError, que ocorre quando o programa tenta acessar um arquivo inexistente (no caso, o arquivo produtos.csv).
except FileNotFoundError:
    print("Erro: Arquivo 'produtos.csv' não encontrado.")
except Exception as e: # Captura qualquer outro tipo de erro que não seja o FileNotFoundError.
    print(f"Erro inesperado: {e}") #Mostra uma mensagem indicando que ocorreu um erro inesperado, junto com os detalhes desse erro.

finally:
    print("Encerrando o programa. Obrigado por usar o PyAutoGUI!")
