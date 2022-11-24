from .base_page import BasePage
from .locators import ProductPageLocators
import time

class ProductPage(BasePage):

    def should_be_add_to_cart_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_CART_BUTTON), "Button 'Add to cart' is not presented"

    def add_to_cart(self):
        button_add_to_cart = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        button_add_to_cart.click()
        self.solve_quiz_and_get_code()
        # time.sleep(300)

    def should_be_correct_adding_product_price(self):
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        product_price_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE_IN_CART).text
        print(f'Product price {product_price}, product price in cart {product_price_in_cart}')
        assert product_price == product_price_in_cart, "Price in the cart does not match the price of the product"

    def should_be_correct_adding_product_name(self):
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_in_cart = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_CART).text
        print(f'Product name "{product_name}", product name in cart "{product_name_in_cart}"')
        assert product_name == product_name_in_cart, "Price in the cart does not match the price of the product"