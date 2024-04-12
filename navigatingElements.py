import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains


def is_element_present(driver, *args):
    try:
        driver.find_element(*args)
        return True
    except NoSuchElementException:
        return False


@pytest.fixture
def driver (request):
    wd = webdriver.Chrome()

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

    countEleents=len(driver.find_elements(By.XPATH, '//li[@id=\"app-\"]'))



    for i in range(countEleents):
        menu = driver.find_element(By.XPATH, '//li[@id=\"app-\"]')
        elements = menu.find_elements(By.XPATH, '//li[@id=\"app-\"]')
        elements[i].click()
        lenVn=len(driver.find_elements(By.XPATH, '//ul[@class=\"docs\"]/li'))

        for j in range(lenVn):
            menu = driver.find_element(By.XPATH, '//li[@id=\"app-\"]')
            subMenu=menu.find_element(By.XPATH, '//ul[@class=\"docs\"]/li')
            subEl=subMenu.find_elements(By.XPATH, '//ul[@class=\"docs\"]/li')
            subEl[j].click()
            time.sleep(1)
            is_element_present(driver, By.TAG_NAME, "h1")





