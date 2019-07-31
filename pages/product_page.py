from .base_page import BasePage
from .locators import ProductPageLocators

class ProductPage(BasePage):

    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET).click()
        assert True

    def check_success_message(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text in self.browser.find_elements_by_css_selector('.alertinner > strong')[0].text
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text in self.browser.find_element_by_css_selector('.alertinner > p > strong').text