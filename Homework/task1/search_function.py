from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_search_function(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    driver.get('https://EPAM.com')

    search_icon = driver.find_element(By.CSS_SELECTOR, '.header-search__button').click()
    search_field = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'input[type=search]')))
    search_field.send_keys('AI')
    search_field.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    page_source = driver.page_source
    search_word = 'AI'
    assert search_word in page_source, f'Test failed: The search word {search_word} is not found'

    driver.quit()

