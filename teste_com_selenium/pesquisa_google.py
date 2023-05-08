from selenium import webdriver
from selenium.webdriver.common.by import By

nav = webdriver.Chrome()

nav.get('https://www.google.com.br/')

nav.find_element(By.NAME, 'q').send_keys('temperatura natal')
nav.find_element(By.NAME, 'btnK').click()
nav.find_element(By.ID, 'wob_tm').text
nav.quit()