from selenium.webdriver.common.by import By
from behave import given, when, then

CART=(By.ID, 'nav-cart-count-container')
RESULT=(By.CSS_SELECTOR, "div [class*='your-amazon-cart-is-empty']")

@given('Open Amazon home page')
def open_help(context):
    #context.driver.get('https://www.amazon.com')
    context.app.main_page.open_main()

@when('Clicks on the cart icon')
def search_cancel_order(context):
        # cart_locate=context.driver.find_element(*CART)
        # cart_locate.click()
        context.app.header.click_cart()

@then('Verify that Your Amazon Cart is empty')
def verification(context, expected_result):
    context.app.search_results_page.verify_empty_cart(expected_result)
