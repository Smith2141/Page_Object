import pytest
from .pages.product_page import ProductPage


# xfile = 7
# mask = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer'
# links = [mask+str(i) for i in range(10) if i != xfile]
# xlink = pytest.param(mask+str(xfile), marks=pytest.mark.xfail(reason="mistake on page"))
# links.insert((xfile, xlink))

# marked_num = 7
# short_link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer"
# links = [f"{short_link}{num}" for num in range(10) if num != marked_num]
# marked_link = pytest.param(f"{short_link}{marked_num}", marks=pytest.mark.xfail(reason="product names are different"))
# links.insert(marked_num, marked_link)
# @pytest.mark.parametrize('link', links)
@pytest.mark.parametrize('link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                  pytest.param
                                      ("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                               marks=pytest.mark.xfail),
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                  "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
def test_guest_can_add_product_to_basket(browser, link):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_name_added_product_correct()
    page.should_be_price_added_product_correct()

# pytest -vs --tb=line --language=en test_product_page.py
