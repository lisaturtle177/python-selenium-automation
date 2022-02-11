from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# init driver
driver = webdriver.Chrome(executable_path='/Users/reneeherscovici/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

driver.get('https://www.amazon.com/gp/help/customer/display.html')

elem=driver.find_element(By.ID, 'helpsearch')
elem.send_keys("Cancel order")
elem.send_keys(Keys.RETURN)

expected_result = "Cancel Items or Orders"
actual_result = driver.find_element(By.XPATH, "//div[@class='help-content']/h1").text
print(actual_result)

assert expected_result == actual_result, f"Expected search text {expected_result} did not match actual search text {actual_result}"
print("Test case passed")
driver.quit()