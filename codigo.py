# pip install pyautogui (biblioteca que permite controlar o mouse e teclado do computador)

import pyautogui
import time

# Comandos básicos do Pyautogui
# pyautogui.press (pressiona tecla)
# pyautogui.write (escreve/digita)
# pyautogui.click (clica o botão do mouse mas esse comando depende da posição X e Y para saber onde clicar)

# define o tempo de espera entre os comandos do Pyautogui
pyautogui.PAUSE = 0.5

# abrir o sistema de cadastro usando chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#esperar carregar
time.sleep(3)

# fazer login (pode usar qualquer dado)
pyautogui.click(x=386, y=412)
pyautogui.write("lemarto@gmail.com")
pyautogui.press("tab")
pyautogui.write("123123")
pyautogui.press("tab")
pyautogui.press("enter")

#Importar a base dados de produtos que serão cadastrados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
# print (tabela)

# iremos percorrer as linhas da tabela
# para cada linha iremos cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código (primeiro campo)
    pyautogui.click(x=391, y=292)
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")
    # agora repete para os outros campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    #verifica se existe informação no campo obs
    if not pd.isna(tabela.loc[linha, "obs"]):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter")
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim