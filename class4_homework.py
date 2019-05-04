#1
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
driver = os.path.join("/home/nadav/Desktop/chromedriver")
browser = webdriver.Chrome(executable_path=driver,chrome_options=chrome_options)
browser.get("http://google.com")
driver = os.path.join("/home/nadav/Desktop/geckodriver")
#browser.get("http://ynet.co.il")
print(browser.title)
#2
title = driver.title
driver.refresh()
if title == driver.title():
    print("Equal")
#3

#yES
#4


#
# # driver.get("https://translate.google.com/")
# # driver.find_element_by_id("source").send_keys("חתול")
# # driver.find_element_by_id("gt-submit").click()

#5
browser.get("https://www.youtube.com/")
browser.find_element_by_id("search").send_keys("cats")
browser.find_element_by_id("search-icon-legacy").click()

#6
browser.get("https://www.translte.google.com/")
browser.find_element_by_id("search").send_keys("cats")
browser.find_element_by_id("search-icon-legacy").click()

#7

browser.get("https://www.facebook.com/")
browser.find_element_by_id("email").send_keys("nadav.daniel")
browser.find_element_by_id("pass").send_keys("asasas")
browser.find_element_by_id("loginbutton").click()

#8

browser.get("https://www.google.com")
browser.get_cookies()
browser.delete_all_cookies()
print("all cookies has been deleted")

