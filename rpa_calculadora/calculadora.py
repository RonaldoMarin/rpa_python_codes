'''
RPA para utilização da calculadora windows - v0.1
'''

import pyautogui

pyautogui.press('win', interval=0.25)
pyautogui.write('calculadora')
pyautogui.press('enter', interval=2)


pyautogui.hotkey('5', '5', '5', interval=0.25)
pyautogui.press('+', interval=0.25)
pyautogui.press('5', interval=0.25)
pyautogui.press('enter')




