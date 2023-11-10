import os
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Constants
BASE_URL = "https://www.epam.com/about"
DOWNLOAD_DIR = "C:\\random"  # The desired download directory
expected_extension = ".pdf"

@pytest.mark.parametrize("report_name", ["EPAM_Corporate_Overview_Q3_october.pdf"])
def test_download_report(report_name):
    chrome_options = Options()
    chrome_options.add_experimental_option("prefs", {
        "download.default_directory": DOWNLOAD_DIR,
    })

    driver = webdriver.Chrome(options=chrome_options)
    driver.get(BASE_URL)
    driver.maximize_window()

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-banner-sdk"))).click() 
    accept_button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler")))
    accept_button.click()
    
    # Locate the "EPAM at a Glance" block and click the download link
    glance_block = driver.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[5]/section')
    download_link = glance_block.find_element(By.XPATH, '//*[@id="main"]/div[1]/div[5]/section/div[2]/div/div/div[1]/div/div[3]/div/a')
    download_link.click()

    # Wait for the download to complete (you can implement a more robust waiting strategy)
    downloaded_file = os.path.join(DOWNLOAD_DIR, report_name)
    time.sleep(2)

    assert os.path.exists(downloaded_file), f"File '{report_name}' was not downloaded."

    # Check the file extension
    actual_extension = os.path.splitext(downloaded_file)[1]
    assert actual_extension == expected_extension, f"Downloaded file has an unexpected extension: {actual_extension}"

    driver.quit()
