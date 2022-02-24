from selenium.webdriver.common.by import By
from behave import given, when, then

CART=(By.ID, 'nav-cart-count-container')
RESULT=(By.CSS_SELECTOR, "div [class*='your-amazon-cart-is-empty']")

@given('Open Amazon home page')
def open_help(context):
    context.driver.get('https://www.amazon.com')

@when('Clicks on the cart icon')
def search_cancel_order(context):
        cart_locate=context.driver.find_element(*CART)
        cart_locate.click()

@then('Verify that Your Amazon Cart is empty')
def verification(context):
        expected_result = "Your Amazon Cart is empty"
        actual_result = context.driver.find_element(*RESULT).text
        assert expected_result == actual_result, f"Expected search text {expected_result} did not match actual search text {actual_result}"
