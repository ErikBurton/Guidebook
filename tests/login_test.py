import pytest
from selenium import webdriver
from pages import login_page
import os

class TestLogin():

    @pytest.fixture
    def login(self, request):
        _chromedriver = os.path.join(os.getcwd(), 'vendor', 'chromedriver')
        driver_ = webdriver.Chrome()

        def quit():
            driver_.quit()

        request.addfinalizer(quit)
        return driver_

    def test_valid_credentials(self, login):
        login.with_("tomsmith", "SuperSecretPassword!")
        assert login.success_message_present()
