from selenium import webdriver
import pytest

@pytest.mark.parametrize("browser", ["chrome", "firefox"])

def test_title(browser):
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser}")

    link = 'https://EPAM.com'
    expected_title = 'EPAM | Software Engineering & Product Development Services'

    driver.get(link)
    actual_title = driver.title
    assert actual_title == expected_title, f'Test failed: The title is incorrrect. Expected {expected_title}'

    driver.quit()