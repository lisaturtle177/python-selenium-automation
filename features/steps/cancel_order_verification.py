from selenium.webdriver.common.by import By
from behave import given, when, then

RESULT=(By.XPATH, "//div[@class='help-content']/h1")


@then('Verify that ‘Cancel Items or Orders’ text is present')
def verification(context):
        expected_result = "Cancel Items or Orders"
        actual_result = context.driver.find_element(*RESULT).text
        assert expected_result == actual_result, f"Expected search text {expected_result} did not match actual search text {actual_result}"



