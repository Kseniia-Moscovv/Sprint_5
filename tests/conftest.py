import random
import string

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

from constants.constants import Constants
from locators.locators import Locators
from utils.utils import UserData


@pytest.fixture
def driver():
    service = Service(ChromeDriverManager().install())
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--headless')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get(Constants.MAIN_PAGE_URL)
    yield driver
    driver.quit()


@pytest.fixture
def go_to_registration_page(driver):
    user_profile_button_in_header = driver.find_element(*Locators.user_profile_button_in_header)
    user_profile_button_in_header.click()

    WebDriverWait(driver, 3).until(
        expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Вход"]')))

    registration_link = driver.find_element(*Locators.registration_link)
    registration_link.click()

    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/h2[text()="Регистрация"]')))

    return driver


@pytest.fixture
def user_login(driver):
    driver.get(Constants.LOGIN_PAGE_URL)
    email_input_login_form = driver.find_element(*Locators.email_input_login_form)
    email_input_login_form.click()
    email_input_login_form.send_keys(Constants.USER_EMAIL)

    pass_input_login_form = driver.find_element(*Locators.pass_input_login_form)
    pass_input_login_form.click()
    pass_input_login_form.send_keys(Constants.USER_PASS)

    login_button = driver.find_element(*Locators.login_button)
    login_button.click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.XPATH, './/button[text()="Оформить заказ"]')))

    return driver


@pytest.fixture
def user():
    name = ''.join(random.choice(string.ascii_lowercase) for i in range(10))
    email = 'kseniya_moskovkina_4_' + str(random.randint(100, 999)) + '@ya.ru'
    password = random.randint(100000, 999999)

    user = UserData(name, email, password)

    return user
