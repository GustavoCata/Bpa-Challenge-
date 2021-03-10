from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import pandas as pd


def writer(lista=None, columns=None, file=''):
    df = pd.DataFrame(lista, columns=columns)
    wrt = pd.ExcelWriter(f'{file}.xlsx', engine='xlsxwriter')
    df.to_excel(wrt, sheet_name='result', startcol=0, startrow=0, index=False)
    wrt.save()


chrome_options = Options()
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
driver.maximize_window()

driver.get("https://www.amazon.com.br")
driver.find_element_by_id('twotabsearchtextbox').send_keys('IPHONE')
driver.find_element_by_id('twotabsearchtextbox').send_keys(Keys.ENTER)

data = driver.find_elements_by_xpath("//*[@id=\"search\"]/div[1]/div[2]/div/span[3]/div[2]")
data = [t.text for t in data][0].split('\n')

grupos = []

grupo = [data.pop(0)]
while data:
    line = data.pop(0)
    if 'iphone' in line.lower():
        grupos.append(grupo)
        grupo = [line]
    else:
        grupo.append(line)

dftemp = []
for grupo in grupos:
    for g in grupo:
        if 'R$' in g:
            valor = g[2:].split(' ')[0]
            dftemp.append([grupo[0], valor])
            break
driver.close()
writer(dftemp, columns=['PRODUTO', 'VALOR'], file='SAIDA')
