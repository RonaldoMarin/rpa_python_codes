from selenium import webdriver
from selenium.webdriver.common.by import By

nav = webdriver.Chrome()

nav.get('https://www.youtube.com.br/')

#Pesquisar essa música -> War on Babylon - Izrael Howls (Legendado
nav.find_element(By.NAME, 'search_query').send_keys('War on Babylon - Izrael Howls (Legendado)')
nav.find_element(By.ID, 'search-icon-legacy').click()

nav.find_element(By.CLASS_NAME, 'style-scope ytd-video-renderer').click()


nav.quit()