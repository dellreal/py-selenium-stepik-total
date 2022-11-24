from pages.product_page import ProductPage
import pytest

# url_list = ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
#             pytest.param("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7", marks=pytest.mark.xfail),
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
#             "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"]


# @pytest.mark.parametrize('url', url_list)
# def test_add_to_cart(browser, url):
#     link = url
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_add_to_cart_button()
#     page.add_to_cart()
#     page.should_be_correct_adding_product_price()
#     page.should_be_correct_adding_product_name()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/'
    page = ProductPage(browser, link)
    page.open()
    page.add_to_cart()
    page.should_see_as_disppearing_message()

# Command to start
# pytest -s test_product_page.py
