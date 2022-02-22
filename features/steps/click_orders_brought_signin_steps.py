from selenium.webdriver.common.by import By
from behave import given, when, then

SIGNIN=(By.CSS_SELECTOR, 'h1.a-spacing-small')
SIGNIN2=(By.XPATH, "//h1[@class='a-spacing-small']")

@then('Verify user is brought to signin page')
def verify_result(context):
    expected_result = "Sign-In"
    actual_result = context.driver.find_element(*SIGNIN).text
    assert expected_result == actual_result, f"Expected text {expected_result} did not match actual {actual_result}"


