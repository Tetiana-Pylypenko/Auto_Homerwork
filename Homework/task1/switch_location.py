import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_find_regions(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get("https://www.epam.com")
    driver.maximize_window()
    
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-banner-sdk"))).click() 
    accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_button.click()

    expected_regions = ["AMERICAS", "EMEA", "APAC"]
    region_elements = driver.find_elements(By.CSS_SELECTOR, "div[class*=js-tabs-title]")
    actual_regions = [region.text for region in region_elements]
    
    assert expected_regions == actual_regions, "Expected regions are not presented."

@pytest.mark.parametrize("region_name", ["AMERICAS", "EMEA", "APAC"])
def test_switch_region(driver, region_name):
    region = driver.find_element(By.LINK_TEXT, region_name)
    region.click()
    
    assert region.get_attribute('aria-selected') == 'true' , f"Failed to switch to {region_name}."
