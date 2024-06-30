import pytest

from pages.account_page import AccountPage
from pages.main_page import MainPage
from pages.ready_program_page import ReadyProgramPage
from pages.dish_method_page import DishMethodPage


class BaseTest:

    account_page: AccountPage
    main_page: MainPage
    ready_program_page: ReadyProgramPage
    dish_method_page: DishMethodPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.account_page = AccountPage(driver)
        request.cls.main_page = MainPage(driver)
        request.cls.ready_program_page = ReadyProgramPage(driver)
        request.cls.dish_method_page = DishMethodPage(driver)