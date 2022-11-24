from pages.product_page import ProductPage

def test_add_to_cart(browser):
    link = 'https://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser, link)
    page.open()
    page.should_be_add_to_cart_button()
    page.add_to_cart()
    page.should_be_correct_adding_product_price()
    page.should_be_correct_adding_product_name()



# Command to start
# pytest -s test_product_page.py