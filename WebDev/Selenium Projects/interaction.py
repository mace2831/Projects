from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#set up driver and keep window open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True) #Keeps the window open

#create and configure the chrome webdriver
driver = webdriver.Chrome(options = chrome_options)

#get the webpage
driver.get('https://en.wikipedia.org/wiki/Main_Page')

#find the element
total_articles = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
print(total_articles.text)

#click the link
total_articles.click()

#all_portals = driver.find_element(By.LINK_TEXT, value = "Content portals") # click on the link using the text inside the link

#select the search bar
search = driver.find_element(By.NAME, value = "search")
#type in the search bar
search.send_keys("Python")
#hit enter key
search.send_keys(Keys.ENTER)