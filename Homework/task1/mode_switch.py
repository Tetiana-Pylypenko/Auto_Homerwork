from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_mode_switch(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")
    
    driver.get('https://EPAM.com')
    driver.maximize_window()
    
    theme_toggle = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//*[@id="wrapper"]/div[2]/div[1]/header/div/div/section/div')))

    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
   
    initial_theme_state = driver.find_elements(By.CSS_SELECTOR, "body[class*=dark-mode]")

    theme_toggle.click()
    driver.implicitly_wait(5)

    oposit_theme_state = driver.find_elements(By.CSS_SELECTOR, "body[class*=dark-mode]")

    assert initial_theme_state != oposit_theme_state,"Test Failed: The theme has not been changed to the opposite state."

    driver.quit()