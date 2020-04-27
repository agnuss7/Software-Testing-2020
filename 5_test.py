from selenium import webdriver
import pytest
import random
register=[""]
class Testing():
	#jei scope butu 'function', kiekvienam testavimui atsidarytu ir uzsidarytu naujas skirtukas
	#su 'class','session' ir 'module' testavimas ivyksta vienam skirtuke, baigus jis uzsidaro
	@pytest.fixture(scope="class")
	def browser(self):
		bowser=webdriver.Firefox()
		yield bowser
		bowser.quit()
	#kiekviename teste bus skirtingo ilgio masyvas 'register'
	@pytest.fixture(autouse=True)
	def auto(self):
		global register
		register=["a"]
		for i in range(random.randint(1,6)):
			register.append("a")
	#testavimas vyks 6 kartus
	@pytest.mark.parametrize("link",["http://suninjuly.github.io/registration2.html","http://suninjuly.github.io/registration1.html","http://suninjuly.github.io/registration2.html","http://suninjuly.github.io/registration1.html","http://suninjuly.github.io/registration2.html","http://suninjuly.github.io/registration1.html"])
	def test(self,browser,link):
		browser.get(link)
		inputs=browser.find_elements_by_class_name("form-control")
		assert len(inputs)<=len(register), "reikia maziausiai {} langeliu".format(len(inputs))
		for index,x in enumerate(inputs):
			x.send_keys(register[index])
		butt1=browser.find_element_by_css_selector(".btn-default")
		butt1.click()


