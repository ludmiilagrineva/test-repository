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
    driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")
    listZones = []
    zonesElement = driver.find_elements(By.XPATH, '//table[@class=\"dataTable\"]/tbody/tr')
    for i in range(1, len(zonesElement) - 1):
        driver.find_element(By.XPATH, f'//table[@class=\"dataTable\"]/tbody/tr[{i + 1}]/td[3]/a').click()
        time.sleep(1)

        zonesElementsName = driver.find_elements(By.XPATH, '//table[@class=\"dataTable\"]/tbody/tr/td[3]/select/option[@selected=\"selected\"]')
        namesZone = []
        for i in range(len(zonesElementsName)):
            namesZone.append(zonesElementsName[i].text)
        sortedzonesList = sorted(namesZone)
        if namesZone != sortedzonesList:
            pytest.fail("еверная сортировка зон")
        driver.get("http://localhost/litecart/admin/?app=geo_zones&doc=geo_zones")