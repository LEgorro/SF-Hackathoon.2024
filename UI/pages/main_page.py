from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class MainPage(BasePage):

    PAGE_URL = Links.HOST

    LINK_TO_READY_PROGRAM = ('xpath', '//a[@href="/readyprogram"]')
    LINK_TO_DISHMETHOD = ('xpath', '//a[@href="/dishmethod"]')
    LINK_TO_ACCOUNT = ('xpath', '//button/a[@href="/account"]')

    def click_link_to_ready_program(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_TO_READY_PROGRAM)).click()

    def click_link_to_dishmethod(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_TO_DISHMETHOD)).click()

    def click_link_to_account(self):
        self.wait.until(EC.element_to_be_clickable(self.LINK_TO_ACCOUNT)).click()

