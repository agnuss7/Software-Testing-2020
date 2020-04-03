from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep
link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Firefox()

browser.get(link)
butt=browser.find_element_by_css_selector(".btn-primary")
butt.click()
sleep(1)
browser.switch_to_window(browser.window_handles[-1])

x=browser.find_element_by_id('input_value').get_attribute("innerHTML")
an=math.log(abs(12*math.sin(float(x))))
a=browser.find_element_by_id("answer")
a.send_keys(str(an))
butt2=browser.find_element_by_css_selector(".btn-primary")
butt2.click()
