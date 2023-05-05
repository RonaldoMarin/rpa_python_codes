'''
RPA para utilização da calculadora windows - v0.1
'''

import pyautogui

pyautogui.press('win')
pyautogui.write('calculadora')
pyautogui.press('enter', interval=1)


pyautogui.hotkey('1', '1', '1', interval=0.25)
pyautogui.press('*', interval=0.25)
pyautogui.press('2', interval=0.25)
pyautogui.press('enter')




