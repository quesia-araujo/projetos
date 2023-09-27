from selenium import webdriver
import time
import requests
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.instagram.com/')
time.sleep(3)


### VARIÁVEIS
campoLogin = '//*[@id="loginForm"]/div/div[1]/div/label/input'
campoSenha = '//*[@id="loginForm"]/div/div[2]/div/label/input'
notificacaoClass ='_a9--._a9_1'
bolaNotificacao = 'xzolkzo'
msgPadraoClass = 'xjp7ctv'
contatoCliente = 'xuxw1ft' 
mensagem = 'x1g8br2z'



######## COMEÇAR  LOGIN
login = driver.find_element(By.XPATH, campoLogin)
login.click
login.send_keys('https.olamundo')
time.sleep(1)
senha = driver.find_element(By.XPATH, campoSenha)
senha.click
senha.send_keys('84093350')
time.sleep(1)
senha.send_keys(Keys.ENTER)

#######
####### ENTRANDO NA ÁREA DE CHAT
time.sleep(5)
driver.get('https://www.instagram.com/direct/inbox/')
time.sleep(5)
notificacao = driver.find_element(By.CLASS_NAME, notificacaoClass)
time.sleep(3)
notificacao.click()

def bot():
    try:
        ####apertar a bolinha
        bola = driver.find_element(By.CLASS_NAME, bolaNotificacao)
        bola = driver.find_elements(By.CLASS_NAME, bolaNotificacao)
        clicaBola = bola[-1]
        acaoBola = webdriver.common.action_chains.ActionChains(driver)
        acaoBola.move_to_element_with_offset(clicaBola, 0, -20)
        acaoBola.click()
        acaoBola.perform()
        time.sleep(3)

        #### Voltar para msg padrão  
        #msgPadrão = driver.find_element(By.CLASS_NAME, msgPadraoClass)
        #time.sleep(1)
        #msgPadrão.click

        # Pegar o contato do cliente
        contato = driver.find_elements(By.CLASS_NAME, contatoCliente)
        contatoFinal = contato[2]
        contato2 = contatoFinal.text
        print(contato2)
        print('Peguei o contato')
        


        ############## Pegando a msg do cliente
        todasMensagens = driver.find_elements(By.CLASS_NAME, mensagem)
        todasMensagensTexto = [e.text for e in todasMensagens]
        msg = todasMensagensTexto[-1]
        print(msg)
        time.sleep(2)
        print('Peguei a mensagem')

        ####################
        ### Respondendo a msg
        element = driver.find_element(By.CSS_SELECTOR, "[role='textbox']")
        element.send_keys('Olá me  chamo Quesia', Keys.ENTER)
        time.sleep(3)
        print('MSG RESPONDODA')
    

    except:
        print('Aguarde')
        time.sleep(1)

while True:
    bot()

