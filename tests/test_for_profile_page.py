from selenium.webdriver.support.wait import WebDriverWait
from locators.locators import Locators
from selenium.webdriver.support import expected_conditions as EC


class TestProfilePage:
    def test_show_user_profile_on_profile_header_button_click(self, user_login):
        driver = user_login

        driver.find_element(*Locators.user_profile_button_in_header).click()
        profile_section = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.profile_section_link)).text
        assert profile_section == 'Профиль'





