from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

#amazon by CSS Selector using multiple classes
driver.find_element(By.CSS_SELECTOR,'.a-icon.a-icon-logo')

#create account by CSS selector using class and tag
driver.find_element(By.CSS_SELECTOR, 'h1.a-spacing-small')

#yourname by CSS Selector using ID
driver.find_element(By.CSS_SELECTOR, '#ap_customer_name')

#email by CSS Selector using ID and tag
driver.find_element(By.CSS_SELECTOR, 'input#ap_email')

#password by CSS Selector using ID
driver.find_element(By.CSS_SELECTOR, '#ap_password')

#re-enter password by CSS Selector using ID
driver.find_element(By.CSS_SELECTOR, '#ap_password_check')

#create your account - mine is called "Continue" or "verify email" - by CSS selector using ID
driver.find_element(By.CSS_SELECTOR, '#continue')

#conditions of use by CSS selector using partial attribute
driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']")

#privacy Notice by CSS selector using partial attribute and tag
driver.find_element(By.CSS_SELECTOR, "a[href*='register_notification_privacy_notice']")

#Sign in by CSS Selector through nodes
driver.find_element(By.CSS_SELECTOR,"div a[href*='signin']" )