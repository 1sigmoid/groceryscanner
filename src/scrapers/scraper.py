from selenium import webdriver
from bs4 import BeautifulSoup
import time

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome('/usr/lib/chromium/chromedriver', options = options)
url = 'https://grofers.com/prn/grofers-mothers-choice-american-almonds/prid/391676'
driver.get(url)
time.sleep(5)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')
js_test = soup.find('div', class_ = 'pdp-product__price--new')
print(js_test.text)
