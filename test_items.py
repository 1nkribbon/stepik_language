import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_add_to_cart_button_existance(browser):
	browser.get(link)
	time.sleep(30)
	add_to_cart_button = []
	add_to_cart_button = browser.find_elements_by_css_selector(".btn-add-to-basket")
	assert len(add_to_cart_button) == 1
