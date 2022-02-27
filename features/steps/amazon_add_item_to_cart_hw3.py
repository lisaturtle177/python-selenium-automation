from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys


SEARCH_WORD=(By.ID, 'twotabsearchtextbox')
ITEM = (By.XPATH, "//div[@data-component-type='s-search-result']//a[.//span[@class='a-price']]")
ADD=(By.ID, "add-to-cart-button")
CART=(By.ID, 'nav-cart-count-container')



@when('Click on the first product')
def click_item(context):
    searched_item=context.driver.find_element(*ITEM)
    searched_item.click()

@when('Click on Add to cart button')
def add_to_cart(context):
    add_to_cart=context.driver.find_element(*ADD)
    add_to_cart.click()

@when('Open cart page')
def click_cart(context):
    click_on_cart=context.driver.find_element(*CART)

@then('Verify cart has {expected_count} item')
def verification(context, expected_count):
    actual_result=context.driver.find_element(*CART).text
    assert expected_count == actual_result, f'Expected {expected_count} but got {actual_result}'