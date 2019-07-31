from .base_page import BasePage
from .locators import LoginPageLocator

class LoginPage(BasePage):

    def should_be_login_page(self):
        self.should_be_login_form()
        self.should_be_register_form()
        self.should_be_login_url()

    def should_be_login_url(self):
        assert "/login/" in str(self.browser.current_url), "Url is not correct!"

    def should_be_login_form(self):
        self.browser.find_element(*LoginPageLocator.LOGIN_FORM)
        assert True, "No login form!"

    def should_be_register_form(self):
        self.browser.find_element(*LoginPageLocator.REGISTER_FORM)
        assert True, "No register form!"
