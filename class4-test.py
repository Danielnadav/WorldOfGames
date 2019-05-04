#1
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
driver = os.path.join("/home/nadav/Desktop/chromedriver")
browser = webdriver.Chrome(executable_path=driver,chrome_options=chrome_options)
#browser.get("http://google.com")
driver = os.path.join("/home/nadav/Desktop/geckodriver")


# browser.get("https://www.facebook.com/")
# browser.find_element_by_id("email").send_keys("nadav.daniel")
# browser.find_element_by_id("pass").send_keys("asasas")
# browser.find_element_by_id("loginbutton").click()
# browser.get("https://www.google.com")
# browser.get_cookies()
# browser.delete_all_cookies()
# print("all cookies has been deleted")


browser.get("https://github.com")
#browser.find_element_by_id("Search").send_keys("Selenium")
#browser.find_element(By.ID,value="search")
#browser.find_element_by_name("search")
# browser.find_element_by_id("Search").is_enabled()
# browser.find_element_by_class_name("Search").send_keys("Selenium")
browser.find_element_by_class_name("form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus").is_enabled()

browser.find_element_by_class_name("form-control input-sm header-search-input jump-to-field js-jump-to-field js-site-search-focus")
