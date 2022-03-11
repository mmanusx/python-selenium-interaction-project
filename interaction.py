
web_url = "https://en.wikipedia.org/wiki/Main_Page"

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_driver_path = "C:/Users/hudayis/Documents/Development/chromedriver.exe"

ser = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=ser)
driver.get(web_url)
number_of_articles = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
#number_of_articles.click()

all_portals = driver.find_element(By.LINK_TEXT, "All portals") # yeni bir nesne oluşturma
# all_portals.click()
#print(number_of_articles.text)

search = driver.find_element(By.NAME, "search")
search.send_keys("Python")                                      # search butonuna kelime yazma
search.send_keys(Keys.ENTER)                                    # enter tuşuna basar



#driver.quit()
