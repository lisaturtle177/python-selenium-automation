from selenium.webdriver.common.by import By
from behave import given, when, then
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS=(By.CSS_SELECTOR, '#variation_color_name li')
CURRENT_COLOR=(By.CSS_SELECTOR, '#variation_color_name .selection')

@given('Open product {product_id} page')
def open_product_page(context, product_id):
    context.driver.get(f'https://www.amazon.com/dp/{product_id}/')

@then('Verify user can click through options')
def verify_colors(context):
    expected_colors = ()
    color_options = context.driver.find_elements(*COLOR_OPTIONS)

#option 1
    actual_colors = []
    for color in color_options:

        color.click()
        current_color_name = context.driver.find_element(*CURRENT_COLOR).text
        actual_colors+=[current_color_name]
        print(actual_colors)
        assert expected_colors == actual_colors, f' Actual {actual_colors} do not match expected {expected_colors}'

# #option 2
#     for i in range(len(color_options)):
#         print('i:',i)
#         color_options[i].click()
#         current_color=context.driver.find_element(*CURRENT_COLOR).text
#         print('current_color:', current_color)
#         assert current_color == expected_colors[i]
