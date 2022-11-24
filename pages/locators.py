from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.CSS_SELECTOR, "[href='/en-gb/basket/']")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIELD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_FIELD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "[name='registration_submit']")


class ProductPageLocators():
    ADD_TO_CART_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    PRODUCT_NAME = (By.CSS_SELECTOR, ".product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "p.price_color")
    PRODUCT_NAME_IN_CART = (By.CSS_SELECTOR, "#messages strong")
    PRODUCT_PRICE_IN_CART = (By.CSS_SELECTOR, "p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, '#messages .alertinner strong')
    BASKET_LINK = (By.CSS_SELECTOR, "[href='/en-gb/basket/']")


class BasketPageLocators():
    QUANTITY_FIELD = (By.CSS_SELECTOR, '#id_form-0-quantity')
    EMPTY_MESSAGE = (By.CSS_SELECTOR, '#content_inner p')
