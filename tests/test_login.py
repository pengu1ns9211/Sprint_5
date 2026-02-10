from data import Data, UrlList
from locators import Locators
from conftest import driver
import helper_functions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_from_main_page(self, driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.login_button_main).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()

    # Вход через кнопку «Личный кабинет»
    def test_login_from_account(self, driver):
        driver.get(UrlList.page_main_url)
        driver.find_element(*Locators.personal_account_button).click()
        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 6).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()

    # Вход через кнопку в форме регистрации
    def test_login_after_registration(self, driver):
        driver.get(UrlList.page_registration_url)
        driver.find_element(*Locators.input_name_field).send_keys(helper_functions.random_name())
        driver.find_element(*Locators.input_email_field).send_keys(helper_functions.random_email())
        driver.find_element(*Locators.input_password_field).send_keys(helper_functions.random_password())
        driver.find_element(*Locators.registration_button).click()

        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.login_button_login_page))

        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()

    # Вход через кнопку в форме восстановления пароля
    def test_login_from_recovery_pass(self, driver):
        driver.get(UrlList.page_login_url)
        driver.find_element(*Locators.recovery_pass_link).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.recovery_pass_button))

        driver.find_element(*Locators.login_link_from_recovery_pass).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.login_button_login_page))

        driver.find_element(*Locators.input_email_field).send_keys(Data.email)
        driver.find_element(*Locators.input_password_field).send_keys(Data.password)
        driver.find_element(*Locators.login_button_login_page).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(Locators.order_button))

        assert driver.find_element(*Locators.order_button).is_displayed()
    
