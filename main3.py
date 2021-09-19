# ------------ Imports ---------------
import react as react
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, ElementNotVisibleException
from selenium.webdriver.common.keys import Keys
import time
import random

# ------------ Def Random --------------
def sleepTime(start):
    _sleep = (random.randint(start, 10))
    time.sleep(_sleep)

#  ---------------- WebDriver -----------------
driverpth = "C:\webdrivers\chromedriver.exe"
# driver = webdriver.Chrome(executable_path=driverpth,options=options)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")
driver = webdriver.Chrome(executable_path=driverpth)
driver.get('https://www.instagram.com/accounts/login/')
driver.email = ''
driver.password = ''
driver.username = 'khloekardashian'
sleepTime(1)
try:
    emailInput=driver.find_element_by_xpath("//input[@name = 'username']")
    passwordInput=driver.find_element_by_xpath("//input[@name = 'password']")
except (NoSuchElementException, ElementNotVisibleException) as exceptions:
    pass
emailInput.send_keys(driver.email)
passwordInput.send_keys(driver.password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(3)
# sleepTime(7)

# ---pop up handle---
NotNow=driver.find_element_by_xpath("//button[text() = 'Not Now']").click()
# sleepTime(1)
time.sleep(2)
# ---------- Going to folower list ----------
driver.get('https://www.instagram.com/' + driver.username + '/')

# follow = driver.find_element_by_xpath("//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/div/span/span[1]/button").click()
Follow_Button = driver.find_element_by_xpath("//*[text()='Follow']").click()

# sleepTime(7)
# driver.get('https://www.instagram.com/' + driver.username + '/followers/')
# Followers=driver.find_element_by_xpath("//a[@class='-nal3 ']").click()
# sleepTime(1)
# # -------------------------------------------
# #find all li elements in list
# fBody  = driver.find_element_by_xpath("//div[@class='isgrP']")
# scroll = 0
# for j in (1,(random.randint(4, 20))):
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#     sleepTime(7)
# # for k in (1,4):
# #     driver.execute_script('arguments[0].scrollDown = arguments[0].scrollDown + arguments[0].offsetHeight;', fBody)
# #     time.sleep(10)
#
# count = 0
# while scroll < 500: # scroll 500 times
#     sleepTime(7)
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#     for i in (0,(random.randint(5, 20))):
#         try:
#             Follow=driver.find_element_by_xpath("//button[text() = 'Follow']")
#             Follow.click()
#             print(count)
#             count = count + 1
#             driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#             time.sleep(10)
#         except NoSuchElementException:
#             pass
#     sleepTime(8)
#     # driver.executeScript("window.scrollBy(0,100)")
#     scroll += 1
#     driver.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', fBody)
#     sleepTime(4)
sleepTime(7)
driver.close()

