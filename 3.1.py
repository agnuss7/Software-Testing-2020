from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
link="http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Firefox()

browser.get(link)
element = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
    )



butt=browser.find_element_by_id("book")
butt.click()

inpt=browser.find_element_by_id("input_value").get_attribute("innerHTML")
an=math.log(abs(12*math.sin(float(inpt))))

a=browser.find_element_by_id("answer")
a.send_keys(str(an))
butt2=browser.find_element_by_id("solve")
butt2.click()
