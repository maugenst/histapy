import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from getpass import getpass

print("HIS - TestDriver at Python")
username = input("Username: ")
password = getpass("Password: ")

chrome_options = Options()

chrome_options.add_argument("disable-infobars")
chrome_options.add_argument("--disable-extensions")
chrome_driver = os.getcwd() +"\\bin\\chromedriver.exe"

print("Using chromedriver at {}".format(chrome_driver))
driver = webdriver.Chrome(chrome_options=chrome_options, executable_path=chrome_driver)

driver.get("http://www.foodsharing.de")
assert "foodsharing" in driver.title
elem = driver.find_element_by_id("login-email")
elem.clear()
elem.send_keys(username)
elem = driver.find_element_by_id("login-password")
elem.clear()
elem.send_keys(password)
elem.send_keys(Keys.RETURN)
#driver.implicitly_wait(10)
#driver.get("https://foodsharing.de/?page=fsbetrieb&id=32625")
#driver.close()