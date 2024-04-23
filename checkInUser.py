import random
import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import string


@pytest.fixture
def driver (request):
    wd=webdriver.Chrome()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    def generate_email():
        username = ''.join(random.choice(string.ascii_lowercase) for i in range(7))
        email = f"{username}@mail.ru"
        return email

    def logOut():
        driver.find_element(By.XPATH, "//div[@id=\"box-account\"]/div/ul/li[4]/a").click()

    # check in
    driver.get("http://localhost/litecart/en/")
    driver.find_element(By.XPATH, "//form[@name=\"login_form\"]/table/tbody/tr[5]/td/a").click()
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"tax_id\"]").send_keys("user")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"company\"]").send_keys("company")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"firstname\"]").send_keys("Luda")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"lastname\"]").send_keys("Grineva")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"address1\"]").send_keys("address1")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"address2\"]").send_keys("address2")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"postcode\"]").send_keys("11111")
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"city\"]").send_keys("city")
    select = driver.find_element(By.CSS_SELECTOR, "select")
    driver.execute_script("arguments[0].selectedIndex=224; arguments[0].dispatchEvent(new Event('change'))", select)
    email = generate_email()
    print(email)
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"email\"]").send_keys(email)
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"phone\"]").send_keys("+79999999999")
    password = "password"
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"password\"]").send_keys(password)
    driver.find_element(By.XPATH, "//tbody/tr/td/input[@name=\"confirmed_password\"]").send_keys(password)
    driver.find_element(By.XPATH, "//button[@name=\"create_account\"]").click()
    time.sleep(1)

    # log out
    logOut()

    # log in
    driver.find_element(By.XPATH, "//input[@name=\"email\"]").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name=\"password\"]").send_keys(password)
    driver.find_element(By.XPATH, "//button[@name=\"login\"]").click()

    # log out
    logOut()
