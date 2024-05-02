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
    driver.find_element(By.LINK_TEXT, "Catalog").click()
    driver.find_element(By.LINK_TEXT, "Rubber Ducks").click()
    elements = driver.find_elements(By.XPATH, "//table[@class=\"dataTable\"]/tbody/tr[@class=\"row\"]/td[3]/a")
    logs=[]
    for i in range(1, len(elements)):
        elements = driver.find_elements(By.XPATH, "//table[@class=\"dataTable\"]/tbody/tr[@class=\"row\"]/td[3]/a")
        elements[i].click()


        for l in driver.get_log("browser"):
            logs.append(l)
            print(l)
        driver.back()
    if len(logs)>0:
        pytest.fail("Найдены логи")