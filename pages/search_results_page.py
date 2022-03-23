from pages.base_page import Page
from selenium.webdriver.common.by import By

class SearchResultsPage(Page):
    RESULT = (By.CSS_SELECTOR, '.a-color-state.a-text-bold')
    PRODUCT_PRICE = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
    SIGNIN = (By.CSS_SELECTOR, 'h1.a-spacing-small')
    EMPTY_CART = (By.CSS_SELECTOR, "div [class*='your-amazon-cart-is-empty']")

    def verify_search_result(self, expected_result):
        self.verify_text(expected_result, *self.RESULT)

    def verify_signin_page(self, expected_result):
        self.verify_text(expected_result, *self.SIGNIN)

    def verify_empty_cart(self, expected_result):
        self.verify_text(expected_result, *self.EMPTY_CART)