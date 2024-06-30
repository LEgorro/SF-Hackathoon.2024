import pytest
from base.base_test import BaseTest

class TestDishMethod(BaseTest):

    @pytest.mark.now
    def test_add_half_plate_id4(self):
        self.dish_method_page.open()
        self.dish_method_page.click_on_half_plate_with_id4()
        self.dish_method_page.current_half_plate_id4_is_visible()