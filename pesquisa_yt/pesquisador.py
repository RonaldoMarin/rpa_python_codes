'''
Algorítmo para pesquisa de vídeos no youtube
'''

import pyautogui

#Bloco para abrir o Navegador (google)
pyautogui.press('win', interval=0.5)
pyautogui.write('google')
pyautogui.press('enter', interval=1.5)

#Bloco abrir youtube
pyautogui.write('Youtube.com')
pyautogui.press('enter', interval=2)

#Bloco fazer pesquisa
#pyautogui.moveTo(568, 131)
pyautogui.click(568, 131, interval=1)
pyautogui.write('War on Babylon - Izrael Howls (Legendado)')
pyautogui.press('enter', interval=2)

#Bloco entrar no vídeo
pyautogui.click(425, 336, interval=1)

