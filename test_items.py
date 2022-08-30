from selenium.webdriver.common.by import By


class TestMainPage1():
    def test_check_basket_button(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        browser.get(link)
        assert browser.find_elements(By.CSS_SELECTOR,"[type = 'submit']"), 'basket button not found'
