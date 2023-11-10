from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()  
driver.get("https://www.epam.com/about/who-we-are/contact")
driver.maximize_window()
banner = driver.find_element(By.ID, "onetrust-accept-btn-handler").click()

def test_validation():
    contact_form = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type=submit]"))).click()

    empty_fields = driver.find_elements(By.CSS_SELECTOR, "[aria-invalid='true']")

    for e in empty_fields:
        parent_element = e.find_element(By.XPATH, "../../..")
        validation_block = parent_element.find_element(By.CLASS_NAME, 'validation-tooltip')
        try:
            validation_text = validation_block.find_element(By.CLASS_NAME, 'validation-text')
            error_message = validation_text.get_attribute('innerText')
        except NoSuchElementException:
            error_message = validation_block.get_attribute('innerText')

        assert error_message, "Error message is empty"

        