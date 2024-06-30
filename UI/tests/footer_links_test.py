import pytest
from base.base_test import BaseTest

class TestLinks(BaseTest):

    @pytest.mark.smoke
    def test_link_to_ready_programm_work(self):
        self.main_page.open()
        self.main_page.click_link_to_ready_program()
        self.ready_program_page.is_opened()

    @pytest.mark.smoke
    def test_link_to_dishmethod_work(self):
        self.main_page.open()
        self.main_page.click_link_to_dishmethod()
        self.dish_method_page.is_opened()