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
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.sauces_span)))
        driver.find_element(By.XPATH, Locators.sauces_span).click()
        assert driver.find_element(By.XPATH, Locators.select_tab_constructor).text == 'Соусы'

    # Переход во вкладку "Начинки"
    def test_go_to_filling(self, driver):
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.filling_span)))
        driver.find_element(By.XPATH, Locators.filling_span).click()
        assert driver.find_element(By.XPATH, Locators.select_tab_constructor).text == 'Начинки'

    # Переход во вкладку "Булки" через "Начинки", так как раздел «Булки» при заходе на сайт выбраны по дефолту
    def test_go_to_buns(self, driver):
        driver.get(UrlList.page_main_url)
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located((By.XPATH, Locators.buns_span)))
        driver.find_element(By.XPATH, Locators.buns_span)
        assert driver.find_element(By.XPATH, Locators.select_tab_constructor).text == 'Булки'
