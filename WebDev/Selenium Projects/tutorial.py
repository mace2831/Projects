from selenium import webdriver
from selenium.webdriver.common.by import By

#keep browser open, have to pass chrome_options into driver variable instantiation
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
#get past captcha
chrome_options.add_argument("--user-agent={Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36}")

driver = webdriver.Chrome(options=chrome_options)

#Meta Quest 3
#driver.get("https://www.amazon.com/Meta-Quest-512GB-Breakthrough-Reality-3/dp/B0CD1JTBSC/ref=sr_1_1_sspa?crid=23IWI71W5FE9R&dib=eyJ2IjoiMSJ9.BNL0XshPOuZ3lobU5yu3cCziH0rMF3MqkgI5OZmFfI3nyq1ojxQzlPV4bhtl78deXY1d7xb0NmqxDqZVeEzs8D-_lppuQU0HrynYDR6-zM943IomwiLiad8aAjaJpKPYJETsLUodQGzyzDmhflNPFJUBl8lxQPPuOm3kKl8NdCbmVPq55-beJdFB7cM5i_4hfah1l2MNV1zHnDJusQc4Mbu4BlHbGU1oMtrcyiKRBrE.3f0nBZBaX5HDCEptPLbw8td8YD-JGLG1qUkf3CnserA&dib_tag=se&keywords=meta%2Bquest%2B3&qid=1716247620&sprefix=meta%2Bquest%2B3%2Caps%2C154&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&th=1")

#Python.org
driver.get("https://www.python.org")

#get html element value
#price_dollars = driver.find_element(By.CLASS_NAME, value ="a-price-whole")
#price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
""" 
#python.org
search_bar = driver.find_element(By.NAME, value="q")
button = driver.find_element(By.ID, value="submit")

#print(f"The Meta Quest 3 512GB is currently ${price_dollars.text}.{price_cents.text}")

print(search_bar.tag_name)
print(button.size)
#get ahold of elements with css using anchor
print(driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a").text) """

""" #search by XPath
buglink = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(buglink.text) """

#get event dates and names
event_dates = driver.find_elements(By.CSS_SELECTOR, value = '.event-widget time')
event_names = driver.find_elements(By.CSS_SELECTOR, value = '.event-widget a')

"""
for index, item in enumerate(events_list):
    events_dict[index] = item.text
"""
#save event dates and names into a new dictionary
events_dict = {}
for index in range(len(event_dates)):
   events_dict[index] = {
      "time": event_dates[index].text,
      "name": event_names[index].text
   }

print(events_dict) 


driver.quit()