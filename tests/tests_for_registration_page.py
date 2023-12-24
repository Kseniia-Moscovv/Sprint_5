from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants.constants import Constants
from locators.locators import Locators


class TestRegistrationPage:
    def test_user_registration_with_correct_parameters(self, go_to_registration_page, user):
        driver = go_to_registration_page

        driver.find_element(*Locators.name_input_registration_form).send_keys(user.name)
        driver.find_element(*Locators.email_input_registration_form).send_keys(user.email)
        driver.find_element(*Locators.password_input_registration_form).send_keys(user.password)
        driver.find_element(*Locators.registration_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        current_login_url = driver.current_url
        assert Constants.LOGIN_PAGE_URL == current_login_url

    def test_user_registration_with_correct_password(self, go_to_registration_page, user):
        driver = go_to_registration_page

        driver.find_element(*Locators.name_input_registration_form).send_keys(user.name)
        driver.find_element(*Locators.email_input_registration_form).send_keys(user.email)
        driver.find_element(*Locators.password_input_registration_form).send_keys(123)
        driver.find_element(*Locators.registration_button).click()
        error_message = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.error_input_pass)).text
        assert error_message == Constants.ERROR_MESSAGE_FOR_INCORRECT_PASS
