from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options
from data import UrlList


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--window-size=1920,1080")
    driver = webdriver.Chrome(options=options)
    driver.get(UrlList.page_main_url)
    yield driver
    driver.quit()
