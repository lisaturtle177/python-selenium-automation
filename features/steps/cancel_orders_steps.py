from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

SEARCH_HELP=(By.ID, 'helpsearch')


@given('Open Amazon help page')
def open_help(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html')

@when('Search for "Cancel order"')
def search_cancel_order(context):
        search_bar= context.driver.find_element(*SEARCH_HELP)
        search_bar.send_keys("Cancel order")
        search_bar.send_keys(Keys.ENTER)