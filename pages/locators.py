from selenium.webdriver.common.by import By


class MainPageLocators(object):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)

class LoginPageLocator(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTRATION_EMAIL = (By.ID, "id_registration-email")
    REGISTRATION_PASSWORD_1 = (By.ID, "id_registration-password1")
    REGISTRATION_PASSWORD_2 = (By.ID, "id_registration-password2")
    REGISTER_BUTTON = (By.NAME, "registration_submit")

class ProductPageLocators(object):
    ADD_TO_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main > h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main > .price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '.alert-success')

class BasePageLocators(object):
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CLASS_NAME, "icon-user")