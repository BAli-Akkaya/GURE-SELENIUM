# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
import time
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# WebDriver kurulumu
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://stage.gurerp.com/login")
driver.implicitly_wait(10)

wait = WebDriverWait(driver, 10)

# Giriş
driver.find_element(By.NAME, "userName").send_keys("ali.akkaya")
driver.find_element(By.NAME, "password").send_keys("123")
driver.find_element(By.NAME, "privacyPolicy").click()
driver.find_element(By.CLASS_NAME, "MuiButtonBase-root").click()
time.sleep(1)

# Tema Değiştir
driver.find_element(By.XPATH, "//button[@title='Karanlık Mod']").click()
time.sleep(1)

# Modüllere geçiş
driver.find_element(By.XPATH, "//h3[contains(text(), 'Satın Alma, İhale ve Malzeme Yönetimi')]/ancestor::a").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Satın Alma, Malzeme ve İhale Yönetimi')]]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Tanımlamalar')]]").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[normalize-space(text())='Stok Süreçleri']").click()
time.sleep(1)

# Yeni Ekle
driver.find_element(By.XPATH, "//button[.//span[normalize-space(text())='Yeni Ekle']]").click()
time.sleep(1)

# Stok Kategorisi Seçimi (React Select)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-2-input")))
dropdown_input.click()
dropdown_input.send_keys("1 AKUMULATOR")
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)

# Stok Alt Kategorisi Seçimi (React Select)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
dropdown_input.click()
dropdown_input.send_keys("AKUMULATOR BATARYASI")
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)

# Stok Adı Seçimi (React Select)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
dropdown_input.click()
dropdown_input.send_keys("deneme")
time.sleep(1)  # Dropdown menüsünün açılması için bekle
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)

# Onay Tanımı Seçimi (React Select)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-5-input")))
dropdown_input.click()
dropdown_input.send_keys("Test Onay Tanımı 63")
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)

# Kaydet
kaydet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']")))
kaydet_btn.click()
time.sleep(2)

print("Onay Tanımı başarıyla oluşturuldu") # Sonuç mesajı
driver.quit()
