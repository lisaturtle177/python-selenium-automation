from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

PRVCY_NTC_LNK=(By.CSS_SELECTOR, "a[href='https://www.amazon.com/privacy']")
PRVCY_VERIF=(By.XPATH, "//h1[contains(text(),'Amazon.com Privacy Notice')]")

@given('Open Amazon T&C page')
def open_terms_and_conditions(context):
    context.driver.get('https://www.amazon.com/gp/help/customer/display.html/ref=ap_register_notification_condition_of_use?ie=UTF8&nodeId=508088')

@given('Store original windows')
def store_window(context):
    context.original_window=context.driver.current_window_handle
    print(context.original_window)

@when('Click on Amazon Privacy Notice link')
def click_privy_ntc_link(context):
    context.driver.find_element(*PRVCY_NTC_LNK).click()

@when('Switch to the newly opened window')
def switch_new_window(context):
    context.driver.wait.until(EC.new_window_is_opened)
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(current_windows[1])

@then('Verify Amazon Privacy Notice page is opened')
def verify_prv_page(context):
    expected_result = "Amazon.com Privacy Notice"
    actual_result = context.driver.find_element(*PRVCY_VERIF).text
    assert expected_result == actual_result, f"Expected search text {expected_result} did not match actual search text {actual_result}"


@then('User can close new window and switch back to original')
def close_blog(context):
    context.driver.close()
    current_windows = context.driver.window_handles
    print('\nCurrent:', current_windows)
    context.driver.switch_to.window(context.original_window)