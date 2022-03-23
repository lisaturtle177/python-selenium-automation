from selenium.webdriver.common.by import By
from behave import given, when, then

SIGNIN=(By.CSS_SELECTOR, 'h1.a-spacing-small')


@then('Verify user is brought to signin page')
def verify_result(context, expected_result):
    context.app.search_results_page.verify_signin_page(expected_result)

