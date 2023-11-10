from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_logo_main_page(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    services_url = "https://www.epam.com/about/"
    main_page_url = "https://www.epam.com/"

    driver.get(services_url)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-banner-sdk"))).click() 
    accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_button.click()

    company_logo = driver.find_element(By.CSS_SELECTOR, "a[class*=header__logo-container]")
    company_logo.click()
    
    driver.implicitly_wait(2)
   
    assert driver.current_url == main_page_url, f"Test Failed: Clicking the company logo does not lead to the main page."
    
    driver.quit()