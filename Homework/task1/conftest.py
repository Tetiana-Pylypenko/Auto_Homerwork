import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.epam.com")
    driver.maximize_window()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-banner-sdk"))).click() 
    accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_button.click()

    yield driver
    driver.quit()

@pytest.fixture
def wait():
    return WebDriverWait(driver, 10)