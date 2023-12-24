from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants.constants import Constants
from locators.locators import Locators


class TestLoginPage:
    def test_login_button_on_main_page(self, driver):
        driver.find_element(*Locators.user_profile_button_under_order_form).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        current_login_url = driver.current_url
        assert Constants.LOGIN_PAGE_URL == current_login_url

    def test_login_button_in_header(self, driver):
        driver.find_element(*Locators.user_profile_button_in_header).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        current_login_url = driver.current_url
        assert Constants.LOGIN_PAGE_URL == current_login_url

    def test_login_button_in_registration_form(self, driver):
        driver.find_element(*Locators.user_profile_button_under_order_form).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        driver.find_element(*Locators.registration_link).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.registration_header))
        login_link = driver.find_element(*Locators.login_link)
        driver.execute_script("arguments[0].scrollIntoView();", login_link)
        login_link.click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        current_login_url = driver.current_url
        assert Constants.LOGIN_PAGE_URL == current_login_url

    def test_login_button_in_reset_pass_form(self, driver):
        driver.find_element(*Locators.user_profile_button_in_header).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        driver.find_element(*Locators.reset_pass_link).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.reset_pass_header))
        driver.find_element(*Locators.login_link).click()
        current_login_url = driver.current_url
        assert Constants.LOGIN_PAGE_URL == current_login_url

    def test_logout_user(self, user_login):
        driver = user_login

        driver.find_element(*Locators.user_profile_button_in_header).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.exit_button))
        driver.find_element(*Locators.exit_button).click()
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.login_header))
        current_login_url = driver.current_url
        assert Constants.LOGIN_PAGE_URL == current_login_url
