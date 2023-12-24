from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from constants.constants import Constants
from locators.locators import Locators


class TestMenuList:
    def test_click_to_sauces_section_from_buns_section(self, driver):
        sauces_tab = driver.find_element(*Locators.sauces_section)
        sauces_tab.click()
        sauces_tab_class_list = sauces_tab.get_attribute('class')
        assert Constants.ACTIVE_SECTION_CLASS_NAME in sauces_tab_class_list

    def test_click_to_fillings_section_from_buns_section(self, driver):
        fillings_tab = driver.find_element(*Locators.fillings_section)
        fillings_tab.click()
        fillings_tab_class_list = fillings_tab.get_attribute('class')
        assert Constants.ACTIVE_SECTION_CLASS_NAME in fillings_tab_class_list

    def test_click_to_buns_section_from_sauces_section(self, driver):
        driver.find_element(*Locators.sauces_section).click()
        buns_tab = driver.find_element(*Locators.buns_section)
        buns_tab.click()
        buns_tab_class_list = buns_tab.get_attribute('class')
        assert Constants.ACTIVE_SECTION_CLASS_NAME in buns_tab_class_list

    def test_scroll_to_fillings_section(self, driver):
        fillings_section_name = driver.find_element(*Locators.fillings_section_name)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_section_name)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.fillings_section_name))
        assert fillings_section_name.is_displayed() == True

    def test_scroll_to_sauces_section_from_fillings_section(self, driver):
        fillings_section_name = driver.find_element(*Locators.fillings_section_name)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_section_name)
        sauces_section_name = driver.find_element(*Locators.sauces_section_name)
        driver.execute_script("arguments[0].scrollIntoView();", sauces_section_name)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.sauces_section_name))
        assert sauces_section_name.is_displayed() == True

    def test_scroll_to_buns_section_from_fillings_section(self, driver):
        fillings_section_name = driver.find_element(*Locators.fillings_section_name)
        driver.execute_script("arguments[0].scrollIntoView();", fillings_section_name)
        buns_section_name = driver.find_element(*Locators.buns_section_name)
        driver.execute_script("arguments[0].scrollIntoView();", buns_section_name)
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.buns_section_name))
        assert buns_section_name.is_displayed() == True
