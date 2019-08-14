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
search_ele.send_keys("Rolando Aarons")
search_ele.send_keys(Keys.RETURN)

#clicking on wayne rooney
driver.implicitly_wait(3)
click_wayne = driver.find_element_by_xpath("//img[@data-player='p155513']").click()

page_source_overview = driver.page_source

from bs4 import BeautifulSoup

#loading page source info
soup = BeautifulSoup(page_source_overview, 'lxml')

#locating the titles
title_finder = soup.find_all("span", class_="title")

title_finder

print(10*"-" + "These are the latest news headlines about wayne rooney" + 10*"-" + "\n")
for title in title_finder:
	print(title.string)
	
#stats button element
time.sleep(1)
wayne_stats = driver.find_element_by_xpath("//a[@href='stats']").click()

page_source_stats = driver.page_source

soup = beautifulSoup(page_source_stats, "lxml")

#locating all the stats
stat_finder = soup.find_all("span", class_="allStatContainer")

print(stat_finder)

print(10*"-" + "Wayne Rooney Stats" + 10*"-" + "\n")
for title in stat_finder:
	print(stat["data-stat"] + " - " + stat.string) 