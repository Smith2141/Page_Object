from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()

    def should_be_name_added_product_correct(self):
        product_name_page = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_basket = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        assert product_name_page == product_name_basket,\
            f'The name of the product "{product_name_page}", and added to cart as "{product_name_basket}"'
        
    def should_be_price_added_product_correct(self):
        product_price_page = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_basket = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        assert product_price_page == product_price_basket,\
            f'The product cost by {product_price_page}, and added to cart by {product_price_basket}'

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "The add message is present, but should not be"

    def message_disappeared_after_adding_product_to_basket(self):
        assert self.is_disappeared(*ProductPageLocators.ADDED_PRODUCT_NAME), \
            "The add message did not disappear, but it should not be"
