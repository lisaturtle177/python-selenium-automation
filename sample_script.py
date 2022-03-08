from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

SEARCH_BTN=(By.NAME, 'btnK')

# init driver
driver = webdriver.Chrome(executable_path='/Users/reneeherscovici/Desktop/Automation/python-selenium-automation/chromedriver')
driver.maximize_window()

# open the url
driver.get('https://www.google.com/')
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('Dress')

# wait for 4 sec
#sleep(4)
WebDriverWait(driver, 4).until(EC.element_to_be_clickable(SEARCH_BTN), message='Btn not clickable')
#driver.wait.until(EC.element_to_be_clickable(SEARCH_BTN), message= 'Btn not clickable')
# click search
driver.find_element(*SEARCH_BTN).click()

# verify
assert 'dress' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
