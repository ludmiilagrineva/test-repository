import time
import pytest
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

def convert_to_absolute_path():
    relative_path = "Черная уточка.jpg"
    directory = os.getcwd()
    absolute_path = os.path.join(directory, relative_path)
    return absolute_path
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
    driver.find_element(By.XPATH, "//ul[@id=\"box-apps-menu\"]/li[2]/a").click()
    driver.find_element(By.XPATH, "//td[@id=\"content\"]/div/a[2]").click()

    # general
    driver.find_element(By.XPATH, "//input[@type=\"radio\"][1]").click()
    driver.find_element(By.XPATH, "//input[@name=\"name[en]\"]").send_keys("black duck")
    driver.find_element(By.XPATH, "//input[@name=\"code\"]").send_keys("000000")
    driver.find_element(By.XPATH, "//input[@name=\"categories[]\"] [@data-name=\"Root\"]").click()
    driver.find_element(By.XPATH, "//input[@name=\"categories[]\"] [@data-name=\"Rubber Ducks\"]").click()
    driver.find_element(By.XPATH, "//input[@name=\"product_groups[]\"] [@value=\"1-1\"]").click()
    driver.find_element(By.XPATH, "//input[@name=\"quantity\"]").clear()
    driver.find_element(By.XPATH, "//input[@name=\"quantity\"]").send_keys("100")
    driver.find_element(By.XPATH, "//input[@name=\"new_images[]\"]").send_keys(f"{convert_to_absolute_path()}")
    driver.find_element(By.XPATH, "//input[@name=\"date_valid_from\"]").send_keys("01052024")
    driver.find_element(By.XPATH, "//input[@name=\"date_valid_to\"]").send_keys("31052024")

    # information
    driver.find_element(By.XPATH, "//ul[@class=\"index\"]/li[2]").click()
    selectManufacturer = driver.find_element(By.XPATH, "//select[@name=\"manufacturer_id\"]")
    driver.execute_script("arguments[0].selectedIndex=1; arguments[0].dispatchEvent(new Event('change'))",selectManufacturer)
    driver.find_element(By.XPATH, "//input[@name=\"short_description[en]\"]").send_keys("dark duck")
    driver.find_element(By.XPATH, "//div[@class=\"trumbowyg-editor\"]").send_keys("black duck")
    driver.find_element(By.XPATH, "//input[@name=\"head_title[en]\"]").send_keys("black duck")
    driver.find_element(By.XPATH, "//input[@name=\"meta_description[en]\"]").send_keys("black duck")

    # prices
    driver.find_element(By.XPATH, "//ul[@class=\"index\"]/li[4]").click()
    driver.find_element(By.XPATH, "//input[@name=\"purchase_price\"]").send_keys("10")
    selectCode = driver.find_element(By.XPATH, "//select[@name=\"purchase_price_currency_code\"]")
    driver.execute_script("arguments[0].selectedIndex=1; arguments[0].dispatchEvent(new Event('change'))", selectCode)
    driver.find_element(By.XPATH, "//input[@name=\"gross_prices[USD]\"]").clear()
    driver.find_element(By.XPATH, "//input[@name=\"gross_prices[USD]\"]").send_keys("12")
    driver.find_element(By.XPATH, "//input[@name=\"gross_prices[EUR]\"]").clear()
    driver.find_element(By.XPATH, "//input[@name=\"gross_prices[EUR]\"]").send_keys("13")
    driver.find_element(By.XPATH, "//button[@name=\"save\"]").click()

    driver.find_element(By.XPATH, "//ul[@id=\"box-apps-menu\"]/li[2]/a").click()
    driver.find_element(By.XPATH, "//table[@class=\"dataTable\"]/tbody/tr[3]/td[3]/a").click()
    isPresent = False
    ducksElements = driver.find_elements(By.XPATH, "//table[@class=\"dataTable\"]/tbody/tr/td/a")
    for i in range(1, len(ducksElements) - 1):
        if ducksElements[i].text == "black duck":
            isPresent = True
    if not isPresent:
        pytest.fail("Товар не добавлен")
