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
driver.find_element(By.XPATH, "//button[normalize-space(text())='İş Emri']").click()
time.sleep(1)
driver.find_element(By.XPATH, "//button[normalize-space(text())='Onay Tanımı']").click()
time.sleep(1)

# Yeni Ekle
driver.find_element(By.XPATH, "//button[.//span[normalize-space(text())='Yeni Ekle']]").click()
time.sleep(1)

# Grup numarası
def get_next_group_number(file_path="grup_sayac.txt"):
    try:
        with open(file_path, "r") as file:
            sayac = int(file.read())
    except FileNotFoundError:
        sayac = 1
    with open(file_path, "w") as file:
        file.write(str(sayac + 1))
    return sayac

grup_numarasi = get_next_group_number()
grup_adi = f"Test Onay Tanımı {grup_numarasi}"
driver.find_element(By.XPATH, "//input[@id='input-Onay Tanımı Adı']").send_keys(grup_adi)

# Süreç Seçimi
dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-5rvhb9')]//input[@type='text']")))
dropdown_input.click()
dropdown_input.send_keys("Yeni Malzeme Talebi")
time.sleep(1)
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)

# Süreç Türü
surec_dropdown = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
surec_dropdown.click()
surec_dropdown.send_keys("Malzeme")
surec_dropdown.send_keys(Keys.ENTER)
time.sleep(1)

# Açıklama
aciklama_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//textarea[@id='input-Açıklama']")))
aciklama_input.send_keys(f"Bu, {grup_adi} için oluşturulan bir test iş emridir.")

# Kaydet
kaydet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']")))
kaydet_btn.click()
time.sleep(2)

# Menü → Düzenle
menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Open menu']]")))
menu_button.click()
time.sleep(1)
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and text()='Düzenle']")))
edit_button.click()
time.sleep(1)

# İş Emri adı değiştir
input_grup_adi = driver.find_element(By.XPATH, "//input[@id='input-İş Emri Adı']")
input_grup_adi.clear()
input_grup_adi.send_keys(f"Yeni İş Emri Adı {grup_numarasi}")

# Kaydet
kaydet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']")))
kaydet_btn.click()
time.sleep(2)

print("İş Emri başarıyla oluşturuldu") # Sonuç mesajı


driver.quit()
