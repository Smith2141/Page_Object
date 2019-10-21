from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#registration_link")


class LoginPageLocators:
    LOG_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "id_registration-email")
    REGISTER_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_CONFIRM_PASSWORD = (By.CSS_SELECTOR, "#id_registration-password2")



# http://selenium1py.pythonanywhere.com/ru/accounts/login/
