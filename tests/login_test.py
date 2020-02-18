import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import os

class TestLogin():

    @pytest.fixture
    def driver(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
        driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self, driver):
        driver.get("https://the-internet.herokuapp.com/login")
        driver.find_element(By.ID, "username").send_keys("tomsmith")
        driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
        driver.find_element(By.CSS_SELECTOR, "button").click()
