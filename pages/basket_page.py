from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.should_be_basket_url()
        self.should_be_basket_header()

    def should_be_basket_url(self):
        assert "basket" in self.browser.current_url, "Invalid basket page url"

    def should_be_basket_header(self):
        assert self.browser.find_element(*BasketPageLocators.BASKET_HEADER).text == "Basket", 'Header is not "Basket"'

    def should_not_be_products_in_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.BASKET_ITEMS), \
            "The basket is not empty, but should be"

    def should_be_basket_empty_text(self):
        basket_empty_text = self.browser.find_element(*BasketPageLocators.BASKET_EMPTY_TEXT).text
        assert basket_empty_text == "Your basket is empty. Continue shopping", \
            f'The text "Your basket is empty. Continue shopping" was expected, but the text "{basket_empty_text}"'
