from selenium import webdriver
import unittest
browser = webdriver.Firefox()

link1="http://suninjuly.github.io/registration1.html"
link2="http://suninjuly.github.io/registration2.html"

register=["agne","burokaite","aggie@mail.com","86977887","gatve"]


class TestAbs(unittest.TestCase):
    def test_abs1(self):
	browser.get(link1)
	inputs=browser.find_elements_by_class_name("form-control")
	self.assertEqual(len(inputs), 5, "reikia 5 langeliu")
	for index,x in enumerate(inputs):
		x.send_keys(register[index])
	butt1=browser.find_element_by_css_selector(".btn-default")
	butt1.click()
        
    def test_abs2(self):
	browser.get(link2)
	inputs=browser.find_elements_by_class_name("form-control")
        self.assertEqual(len(inputs), 5, "reikia 5 langeliu")
	for index,x in enumerate(inputs):
		x.send_keys(register[index])
	butt1=browser.find_element_by_css_selector(".btn-default")
	butt1.click()

unittest.main()
