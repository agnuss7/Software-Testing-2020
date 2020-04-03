from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import math
from selenium.webdriver.support.ui import WebDriverWait


link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Firefox()

browser.get(link)
butt=browser.find_element_by_css_selector(".btn-primary")
butt.click()
alert=browser.switch_to.alert
alert.accept()
wait = WebDriverWait(browser, 10)
wait.until(lambda browser: browser.current_url != link)
x=browser.find_element_by_id('input_value').get_attribute("innerHTML")
an=math.log(abs(12*math.sin(float(x))))
a=browser.find_element_by_id("answer")
a.send_keys(str(an))
butt2=browser.find_element_by_css_selector(".btn-primary")
butt2.click()
