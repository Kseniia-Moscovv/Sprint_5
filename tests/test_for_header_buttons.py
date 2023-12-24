from constants.constants import Constants
from locators.locators import Locators


class TestForHeaderButtons:
    def test_click_on_constructor_button_from_profile(self, user_login):
        driver = user_login

        driver.find_element(*Locators.user_profile_button_in_header).click()
        driver.find_element(*Locators.constructor_button).click()
        current_url = driver.current_url
        assert Constants.MAIN_PAGE_URL == current_url

    def test_click_on_logo_from_profile(self, user_login):
        driver = user_login

        driver.find_element(*Locators.user_profile_button_in_header).click()
        driver.find_element(*Locators.logo_stellar_burgers).click()
        current_url = driver.current_url
        assert Constants.MAIN_PAGE_URL == current_url
