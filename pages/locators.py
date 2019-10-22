from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOG_IN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, ".btn-primary.btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".col-sm-6.product_main .price_color")

# http://selenium1py.pythonanywhere.com/ru/accounts/login/

