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

driver = webdriver.Chrome(options=chromeOptions)
driver.get("https://www.pluralsight.com/buy?requestId=1a4d368d-ffd9-4cef-b9b5-85748089216d&priceOptionId=eeb41487-0e8a-46f1-b5c7-0ce91f36e5bd&legacyTrackingId=IND-M-PLUS&time=1565766834152&planId=Individual+plan&quantity=1&analyticsStep=1")

#web driver wait
element = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.NAME, "firstName")))

#first name
first_name = driver.find_element_by_name("firstName")
first_name.clear()
first_name.send_keys("John")

#last name
last_name = driver.find_element_by_name("lastName")
last_name.clear()
last_name.send_keys("Doe")

#email
email = driver.find_element_by_name("email")
email.clear()
email.send_keys("john_is_a_doe@gmail.com")

#confirmation email
conf_email = driver.find_element_by_name("email")
conf_email.clear()
conf_email.send_keys("john_is_a_doe@gmail.com")

#country of residence
time.sleep(2)
country_element = driver.find_element_by_xpath("//select[@data-test='country']")
all_options = country_element.find_elements_by_tag_name("option")

for options in all_options:
    if option.get_attribute("value") =="US":
        options.click()
        
#checkboxes
time.sleep(1)
checkbox = driver.find_element_by_xpath("//div[@role='checkbox']")
checkbox.click()

#submit button
submit_ele = driver.find_element_by_xpath("//button[@data-test='submitButton']")
time.sleep(2)
submit_ele.click()

#switch to iframe by name
driver.switch_to_frame("frameName")

#switch to parent frame
driver.switch_to_default_content()

popup = driver.switch_to_alert()