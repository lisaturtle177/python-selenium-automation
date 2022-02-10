from selenium import webdriver
from selenium.webdriver.common.by import By

# init driver
driver = webdriver.Chrome()

#Amazon logo by XPATH using attribute
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

#Email field by ID
driver.find_element(By.ID, "ap_email")

#Continue button by ID
driver.find_element(By.ID, "continue")

#Need help link by XPATH using attribute
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

#Forgot your password link by ID
driver.find_element(By.ID, "auth-fpp-link-bottom")

#Other issues with Sign-In link by ID
driver.find_element(By.ID, "ap-other-signin-issues-link")

#Create your Amazon account button by ID
driver.find_element(By.ID, "createAccountSubmit")

#*Conditions of use link by XPATH using text
driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

#*Privacy Notice link by partial text using contains and attribute
driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Not') and @class='a-link-normal']")
