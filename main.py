import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options  
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
chrome_options = Options()

url_main = 'https://educacao.uol.com.br/bancoderedacoes/'


driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(url_main)

contador = 0
while(contador < 10):
    time.sleep(10) 
    driver.find_element(By.XPATH, '//button[text()="ver mais "]').click()   
    time.sleep(10) 


soup = BeautifulSoup(driver.page_source,'html.parser')

temas = [x.text for x in soup.find_all('h3',{'class':'thumb-title title-xsmall title-lg-small'})]
links_temas =[x.find('a')['href'] for x in soup.find_all('div',{'class':'thumbnails-wrapper'})]

df_principal = pd.DataFrame()
df_principal['Temas'] = temas
df_principal['Link temas'] = links_temas

df_principal['Temas'].loc[0]
df_principal['Link temas'].loc[0]

