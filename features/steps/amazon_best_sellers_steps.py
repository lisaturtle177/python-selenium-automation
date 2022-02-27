from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys

BEST_SELLERS_LINKS=(By.CSS_SELECTOR, '._p13n-zg-nav-tab-all_style_zg-tabs-li-div__1YdPR')

@given('Open Amazon Best Sellers page')
def open_best_sellers(context):
    context.driver.get('https://www.amazon.com/gp/bestsellers/?ref_=nav_cs_bestsellers')

@then('Verify user can see {expected_amount} links')
def verify_links(context, expected_amount):
    links_amount =len(context.driver.find_elements(*BEST_SELLERS_LINKS))
    assert links_amount == int(expected_amount), f'Expected 5 benefits, but got {links_amount}'