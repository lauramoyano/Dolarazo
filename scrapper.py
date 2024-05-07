from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 

import time

# Devuelve el driver de Chrome
def get_driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.page_load_strategy = 'none' 
    driver = webdriver.Chrome(service=service, options=options)
    driver.implicitly_wait(5)

    return driver


def scrap_dollar(driver):
    url = "https://www.larepublica.co/indicadores-economicos/mercado-cambiario/dolar"
    driver.get(url)
    #time.sleep(5)

    content = driver.find_elements(By.CLASS_NAME, "price")

    # prices = [dolar, apertura, promedio, maximo, minimo, nro_operaciones, trm, trm_dia_sig, compra_casa_cambio, venta_casa_cambio]
    prices = [data.text for data in content]

    return prices


def scrap_trm_prices(driver, days=5):
    url = "https://www.datos.gov.co/Econom-a-y-Finanzas/Tasa-de-Cambio-Representativa-del-Mercado-Historic/mcec-87by/data_preview"
    driver.get(url)
    time.sleep(10)

    prices_table = driver.find_elements(By.CLASS_NAME, "ag-center-cols-container")
    rows = prices_table[0].find_elements(By.XPATH, "./*")[:days]

    prices_and_dates = [get_price_and_date_from_row(row) for row in rows]

    return prices_and_dates


def get_price_and_date_from_row(row):
    childs = row.find_elements(By.TAG_NAME, "div")
    price, date = childs[1].text, childs[5].text

    return (price, date)


if __name__ == '__main__':
    driver = get_driver()
    prices = scrap_dollar(driver)
    history = scrap_trm_prices(driver)
    print(prices)
    print(history)