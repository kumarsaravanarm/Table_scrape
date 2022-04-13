from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from pandas import DataFrame as df

import time

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()))

web = "https://www.geeksforgeeks.org/web-driver-methods-in-selenium-python/"
# web = "https://www.geeksforgeeks.org/element-methods-in-selenium-python/"

driver.get(web)
tabel_values = []

# tabels = WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.XPATH,".//table[@class='math-table']//tr")))
tabels = driver.find_elements(By.XPATH,".//table[@class='math-table']//tr")
# print(tabels.text)

for values in tabels:
    tabel_values.append(values.text.split(" ",1))
# print(tabel_values)

table_dataframe = df(tabel_values)
# print(table_dataframe)
table_dataframe.to_csv("Selenium_methods.csv",encoding='utf-8',index=False)