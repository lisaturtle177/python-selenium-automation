from selenium.webdriver.common.by import By
from behave import given, when, then

CLICK_ORDERS=(By.CSS_SELECTOR, "a[href*='order-history'] .nav-line-2")

@given('Open Amazon homepage')
def open_amazon(context):
    context.driver.get('https://www.amazon.com')


@when('Click Orders')
def click_on_orders(context):
    context.driver.find_element(*CLICK_ORDERS).click()