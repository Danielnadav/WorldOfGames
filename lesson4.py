import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("no-sandbox")
chrome_options.add_argument("--disable-extensions")
#chrome_options.add_argument("--headless")
driver = os.path.join("/home/nadav/Desktop/chromedriver")
browser = webdriver.Chrome(executable_path=driver,chrome_options=chrome_options)
browser.get("file:///home/nadav/Desktop/tip_calc/index.html")
#browser

print(browser.title)