from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
#from webdriver_manager.chrome import ChromeDriverManager #as part of the possible fix for the webdriver issue

start = time.time()
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')

driver = webdriver.Chrome('/usr/lib/chromium/chromedriver', options = options)
#driver = webdriver.Chrome(ChromeDriverManager().install(), options=options) #part of a possible fix



query = input('Enter what you want to search for\n')

url = 'https://www.bigbasket.com/ps/?q=' + query

print('Random print statement')

driver.get(url)

print('Page loaded')

# //product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]/span
# //product-template/div/div[4]/div[1]/a

time.sleep(3)
items = driver.find_elements_by_xpath('//product-template/div/div[4]/div[3]/div/div[1]/h4/span[2]/span')
item_names = driver.find_elements_by_xpath('//product-template/div/div[4]/div[1]/a')

print(len(items))

for i in range(len(items)):
	print(item_names[i].text, '-', items[i].text)

end = time.time()
print(end-start)
