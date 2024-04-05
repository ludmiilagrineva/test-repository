import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver (request):
    wd=webdriver.Chrome()

    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://localhost/litecart/admin/")
    driver.find_element(By.NAME, "username").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.NAME, "password").send_keys("admin")
    time.sleep(1)
    driver.find_element(By.NAME, "login").click()
    time.sleep(1)





