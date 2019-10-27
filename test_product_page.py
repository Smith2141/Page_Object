import pytest
from .pages.links import ProductPageLinks
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        self.page = ProductPage()

    def test_user_cant_see_success_message(self, browser):
        link = ProductPageLinks.PRODUCT_PAGE_LINK_2
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = ProductPageLinks.PRODUCT_PAGE_LINK_2
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        page.should_be_name_added_product_correct()
        page.should_be_price_added_product_correct()


def test_guest_cant_see_success_message(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_2
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_can_add_product_to_basket(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_2
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_be_name_added_product_correct()
    page.should_be_price_added_product_correct()

@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_2
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_2
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_1
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_1
    page = ProductPage(browser, link)
    page.open()
    # page.should_be_login_link()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = ProductPageLinks.PRODUCT_PAGE_LINK_1
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_be_basket_page()
    basket_page.should_not_be_products_in_basket()
    basket_page.should_be_basket_empty_text()

# pytest -vs --tb=line --language=en test_product_page.py
