from pages.base_page import Page
from selenium.webdriver.common.by import By

class BestSellersPage(Page):
    # BEST_SELLERS_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    TOP_LINKS = (By.CSS_SELECTOR, '#zg_header a')
    HEADER = (By.ID, 'zg_banner_text')

    def open_best_sellers(self):
        self.open_url(end_url='gp/bestsellers/')

    def click_thru_top(self):
        top_links = self.driver.find_elements(*self.TOP_LINKS)

        for x in range(len(top_links)):
            link_to_click = self.driver.find_elements(*self.TOP_LINKS)[x]
            link_text = link_to_click.text
            link_to_click.click()
            self.verify_partial_text(link_text, *self.HEADER)