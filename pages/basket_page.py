from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_not_be_quantity_field(self):
        assert self.is_not_element_present(*BasketPageLocators.QUANTITY_FIELD), "Сart is not empty"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_MESSAGE), "There is not message 'Your cart is empty'"
