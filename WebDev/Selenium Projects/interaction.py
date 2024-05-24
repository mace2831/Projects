from selenium import webdriver
from selenium.webdriver.common.by import By

#set up driver and keep window open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('deta  ch', True)
driver = webdriver.Chrome(options = chrome_options)

#get the webpage
driver.get('https://en.wikipedia.org/wiki/Main_Page')

#find the element
total_articles = driver.find_element(By.ID, value="articlecount")
print(total_articles.text)

driver.quit()