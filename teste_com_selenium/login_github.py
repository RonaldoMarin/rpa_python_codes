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

#Criação de um novo repositório
navegador.find_element('xpath', '/html/body/div[1]/div[6]/div/div/aside/div/loading-context/div/div[1]/div/h2/a').click()

#Nomeação do novo repositório e Create
navegador.find_element('xpath', '//*[@id="react-aria-2"]').send_keys('aa')
sleep(5)
navegador.find_element('xpath', '//*[@id="react-aria-8"]').click()
sleep(5)
navegador.find_element('xpath', '/html/body/div[1]/div[6]/main/react-app/div/div/form/div[5]/button').click()
sleep(5)


navegador.find_element('xpath', '//*[@id="repo-content-pjax-container"]/div/div/div[2]/div[1]/div[2]').click()
navegador.quit()



