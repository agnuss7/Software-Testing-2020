from selenium import webdriver
import pytest

register=["agne","burokaite","aggie@mail.com","86977887","gatve"]

class Testing():
	@pytest.fixture(scope="function")
	def browser(self):
		bowser=webdriver.Firefox()
		yield bowser
		bowser.quit()
	@pytest.mark.parametrize("link",["http://suninjuly.github.io/registration1.html","http://suninjuly.github.io/registration2.html"])
	def test(self,browser,link):
		browser.get(link)
		inputs=browser.find_elements_by_class_name("form-control")
		assert len(inputs)==5, "reikia 5 langeliu"
		for index,x in enumerate(inputs):
			x.send_keys(register[index])
		butt1=browser.find_element_by_css_selector(".btn-default")
		butt1.click()


