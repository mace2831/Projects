from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#set up options and driver
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)
driver = webdriver.Chrome(options = chrome_options)

#get webpage
driver.get('https://secure-retreat-92358.herokuapp.com/')

#variables for user information
first_name = 'Buppleup'
last_name = 'Buntupplepup'
email = f"{first_name}.{last_name}@doodatoo.org"

#set up fields to enter
enter_first = driver.find_element(By.NAME, value='fName')
enter_first.send_keys(first_name)

enter_last = driver.find_element(By.NAME, value='lName')
enter_last.send_keys(last_name)

enter_email = driver.find_element(By.NAME, value = 'email')
enter_email.send_keys(email)
#press the submit button
enter_email.send_keys(Keys.ENTER)