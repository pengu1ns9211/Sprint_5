from selenium.webdriver.common.by import By
from data import UrlList
from locators import Locators
from conftest import driver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestTabsSwitching:
    # Переход во вкладку "Соусы"
    def test_go_to_sauces(self, driver):
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.sauces_span))
        driver.find_element(*Locators.sauces_span).click()
        
        # Ждем, пока активный таб изменится на "Соусы"
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.select_tab_constructor, 'Соусы'))
        
        assert driver.find_element(*Locators.select_tab_constructor).text == 'Соусы'

    # Переход во вкладку "Начинки"
    def test_go_to_filling(self, driver):
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.filling_span))
        driver.find_element(*Locators.filling_span).click()
        
        # Ждем, пока активный таб изменится на "Начинки"
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.select_tab_constructor, 'Начинки'))
        
        assert driver.find_element(*Locators.select_tab_constructor).text == 'Начинки'

    # Переход во вкладку "Булки" через "Начинки"
    def test_go_to_buns(self, driver):
        driver.get(UrlList.page_main_url)
        
        # Сначала переходим во вкладку "Начинки", чтобы потом вернуться к "Булкам"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.filling_span))
        driver.find_element(*Locators.filling_span).click()
        
        # Ждем, пока активный таб изменится на "Начинки"
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.select_tab_constructor, 'Начинки'))
        
        # Теперь переходим во вкладку "Булки"
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.buns_span))
        driver.find_element(*Locators.buns_span).click()
        
        # Ждем, пока активный таб изменится на "Булки"
        WebDriverWait(driver, 5).until(
            expected_conditions.text_to_be_present_in_element(Locators.select_tab_constructor, 'Булки'))
        
        assert driver.find_element(*Locators.select_tab_constructor).text == 'Булки'
