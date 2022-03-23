from pages.base_page import Page
from selenium.webdriver.common.by import By

class Header(Page):

    SEARCH_WORD = (By.ID, 'twotabsearchtextbox')
    SEARCH_BTN = (By.ID, 'nav-search-submit-button')
    CLICK_ORDERS = (By.CSS_SELECTOR, "a[href*='order-history'] .nav-line-2")
    CART = (By.ID, 'nav-cart-count-container')


    def search_product(self):
        self.input_text('coffee', *self.SEARCH_WORD)

    def click_search(self):
        self.click(*self.SEARCH_BTN)

    def click_orders(self):
        self.click(*self.CLICK_ORDERS)

    def click_cart(self):
        self.click(*self.CART)
