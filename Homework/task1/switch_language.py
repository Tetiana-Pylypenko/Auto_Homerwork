from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_login(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
     
    driver.get("https://www.epam.com")
    driver.maximize_window()

    language_selector = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[2]/div/div/button')))
    language_selector.click()

    select = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/ul/li[2]/div/nav/ul/li[6]')))
    select.click()

    driver.implicitly_wait(2)

    assert bool(driver.find_element(By.CSS_SELECTOR, "html[lang=uk-UA]")), "Test Failed: The site's context has not been changed to UA."

    driver.quit()