from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pandas as pd

opt = Options()
opt.add_argument("--headless")
opt.add_argument("--no-sandbox")
opt.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(service= Service(ChromeDriverManager().install()),options=opt)

web = "https://www.simplilearn.com/tutorials/python-tutorial/selenium-with-python"

driver.get(web)

html = driver.page_source
data = pd.read_html(html)

for i in range(len(data)):
    filename = "Selenium_useful_methods_file_" + str(i) +'.csv'
    data[i].to_csv(filename,index=False,encoding='utf-8')




