import pytest

from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC

class DishMethodPage(BasePage):

    PAGE_URL = Links.DISHMETHOD_PAGE

    HALF_PLATE_ID4 = ('xpath', '//img[@src="/api/v1/images/7?half_dish_id=4"]')
    CURRENT_HALF_PLATE_ID4 = ('xpath', '//div[@class="DishMethod_currentDish__fCXPv"]//img[@src="/api/v1/images/7?half_dish_id=4"]')

    def click_on_half_plate_with_id4(self):
        self.wait.until(EC.element_to_be_clickable(self.HALF_PLATE_ID4)).click()

    def current_half_plate_id4_is_visible(self):
        self.wait.until(EC.element_to_be_clickable(self.CURRENT_HALF_PLATE_ID4))