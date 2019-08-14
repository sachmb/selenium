#importing required packages
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

#adding options on chrome
chromeOptions = Options()
chromeOptions.add_argument("--kiosk")

#navigating to the premiew league site
driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.premierleague.com/")

#clicking on the players tab
players_ele = driver.find_element_by_link_text("Players").click()

#searching for wayne rooney
#web driver wait
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "search-input")))
	
search_ele = driver.find_element_by_id("search-input")
search_ele.send_keys("Wayne Rooney")
search_ele.send_keys(Keys.RETURN)

#clicking on wayne rooney
driver.implicitly_wait(3)
click_wayne = driver.find_element_by_xpath("//img[@data-player='p13017']")
click_wayne.click()
#page_source_overview = driver.page_source