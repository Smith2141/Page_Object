from .pages.product_page import ProductPage
import time


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_added_product_correct()
    page.should_be_price_added_product_correct()
    time.sleep(5)


"""
<div class="alertinner ">
    <strong>The shellcoder's handbook</strong> has been added to your basket.
            </div>

==
<div class="alertinner ">
Your basket now qualifies for the 
<strong>Deferred benefit offer</strong> offer.
            </div>

===
<p>
            Your basket total is now <strong>£9.99</strong>
</p>
"""
