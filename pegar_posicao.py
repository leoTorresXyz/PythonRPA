import pyautogui
import time

# pega a posição do mouse depois de 5 segundos para saber onde clicar
time.sleep(5)
print(pyautogui.position())
# testa quanto de scroll para rolar a página
pyautogui.scroll(-200)