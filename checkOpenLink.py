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
    driver.find_element(By.NAME, "password").send_keys("admin")
    driver.find_element(By.NAME, "login").click()
    driver.find_element(By.LINK_TEXT, "Countries").click()
    driver.find_element(By.XPATH, "//table[@class=\"dataTable\"]/tbody/tr[@class=\"row\"][2]/td/a/i[@class=\"fa fa-pencil\"]").click()
    mainWindowHandle = driver.current_window_handle
    linkElenemts = driver.find_elements(By.XPATH, "//table/tbody/tr/td/a/i[@class=\"fa fa-external-link\"]")

    for i in range(len(linkElenemts)):
        linkElenemts[i].click()
        WebDriverWait(driver, 10).until(EC.number_of_windows_to_be(2))
        openedWindowHandle = driver.window_handles
        driver.switch_to.window(openedWindowHandle[1])
        driver.close()
        driver.switch_to.window(mainWindowHandle)
