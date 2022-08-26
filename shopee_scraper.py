from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from winotify import Notification

chrome_options = Options()
chrome_options.add_argument("--headless")

url = input('Enter your Shopee URL: ')

driver = webdriver.Edge(service = Service('msedgedriver.exe'))

driver.get(url)

while True:
    sleep(4)
    # stock reading count on the product detail section
    read_stock = "/html/body/div[1]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[3]/div/div[4]/div/div[2]/div/div[2]/div[2]/div[2]"
    out = driver.find_element(By.XPATH, read_stock).text

    if out[0] != "0":
        print("Product is available to purchase!")
        print(out)

        toast = Notification("Product available", out)
        toast.add_actions(label="Click here", launch=url)
        toast.show()
        break

    driver.refresh()

driver.quit()
