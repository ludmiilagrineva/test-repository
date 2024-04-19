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
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")

    listCountries=[]
    listCountZones=[]

    countriesElements = driver.find_elements(By.XPATH, '//table[@class=\"dataTable\"]/tbody/tr[@class=\"row\"]/td[5]')
    for i in range(len(countriesElements)):
        listCountries.append(countriesElements[i].text)

    zonesElements = driver.find_elements(By.XPATH, '//table[@class=\"dataTable\"]/tbody/tr[@class=\"row\"]/td[6]')
    for i in range(len(zonesElements)):
        listCountZones.append(zonesElements[i].text)

    sortedListCountries = sorted(listCountries)
    if sortedListCountries != listCountries:
        pytest.fail("Неверная сортировка стран")

    for i in range(len(listCountZones)):
        if listCountZones[i] != '0':
            driver.find_element(By.XPATH, f'//table[@class=\"dataTable\"]/tbody/tr[{i + 2}]/td[5]/a').click()
            zonesElements = driver.find_elements(By.XPATH, '//table[@class=\"dataTable\"]/tbody/tr/td[3]')
            listZones = []
            for j in range(len(zonesElements) - 1):
                listZones.append(zonesElements[j].text)
            sorterZones = sorted(listZones)
            if listZones != sorterZones:
                pytest.fail("Неверная сортировка зон")

            driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")


