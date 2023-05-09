from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
#instala a versão mais recente do Chrome Driver Manager
servico = Service(ChromeDriverManager().install())


navegador = webdriver.Chrome(service=servico)

navegador.get('https://github.com/login')

#email -> testeselenium11@gmail.com
#senha email -> 721091720

#user Name -> SeleniumTEST2
navegador.find_element('xpath', '//*[@id="login_field"]').send_keys('SeleniumTEST2')

#senha -> Bw@721091720
navegador.find_element('xpath', '//*[@id="password"]').send_keys('Bw@721091720')

#Clica em sing in
navegador.find_element('xpath', '//*[@id="login"]/div[4]/form/div/input[12]').click()


#Bloco de código Editar perfil: navBar -> click perfil
navegador.find_element('xpath', '/html/body/div[1]/div[1]/header/div[7]/details/summary').click()
sleep(3)
navegador.find_element('xpath', '/html/body/div[1]/div[1]/header/div[7]/details/details-menu/a[10]').click()

sleep(3)
#trocar nome 
navegador.find_element('xpath', '//*[@id="user_profile_name"]').send_keys('Ronaldo O Marinho')
sleep(2)

#Mudar bio
navegador.find_element('xpath', '//*[@id="user_profile_bio"]').send_keys('Eu sou um robo!')
sleep(2)

#mudar localização
navegador.find_element('xpath', '//*[@id="user_profile_location"]').send_keys('Robolandia')
sleep(2)

#set horário
navegador.find_element('xpath', '//*[@id="user_profile_display_local_time_zone"]').click()
sleep(2)

#Savar
navegador.find_element('xpath', '//*[@id="edit_user_132947495"]/div/p[2]/button').click()
sleep(3)

