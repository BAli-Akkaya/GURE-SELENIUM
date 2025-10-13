from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pytest

def test_google_open():
    service = Service(ChromeDriverManager().install()) # ChromeDriverManager ile otomatik olarak ChromeDriver'ı indirir ve kurar.
    driver = webdriver.Chrome(service=service)
    driver.get("https://www.google.com")
    assert "Google" in driver.title
    driver.quit()
