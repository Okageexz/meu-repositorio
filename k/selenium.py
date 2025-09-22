from selenium import webdriver
#from selenium.webdriver.common.by import By
import time


# abra o navegador
navegador = webdriver.Chrome()



#entre no site
navegador.get("https://saladofuturo.educacao.sp.gov.br/escolha-de-perfil")

time.sleep(10)