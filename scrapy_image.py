from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
import json
import sys
import urllib.request

homeid = "BD ANGIOCATHÂ™  IV CATHETERS<br>Combines the BD AutoguardÂ™ needle shielding technology with the name you trust in IV catheters"
options = webdriver.ChromeOptions()
options.binary_location = r"C:\Users\dell\AppData\Local\Google\Chrome\Application\chrome.exe"
chrome_driver_path = r"chromedriver.exe"

driver = webdriver.Chrome(chrome_driver_path, chrome_options=options)
driver.get("https://www.google.com/")
search = driver.find_element_by_name('q')
search.send_keys(homeid)
search.send_keys(Keys.RETURN)

source = driver.find_elements_by_css_selector('#rso > div > div > div > div > div > div.r > a')
url = source[0].get_attribute('href')
print(url)
source[0].click();

print("asdfasdfasdfasd")
source = driver.find_elements_by_xpath('//*[@id="slider"]/div/div/div/div/img')

print("asdfasdfasdfasd")
url = source[0].get_attribute('src')
urllib.request.urlretrieve(url, "local-filename.jpg")

#page = driver.page_source

#soup = BeautifulSoup(page, "html.parser")#rso > div > div > div > div > div.rc > div.r > a 
#source = soup.select('#js_2 > div._3-98 > div > div > div._65db > a > div > div._2ph_._2ms_._4-u3 > div._50f4 > div > p')
#text = [];
#for element in source:
	#text.append(element.text)
#print(json.dumps(text))
