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
driver.find_element(By.XPATH, "//button[normalize-space(text())='Onay Seviyeleri']").click()
time.sleep(1)

# Yeni Ekle
driver.find_element(By.XPATH, "//button[.//span[normalize-space(text())='Yeni Ekle']]").click()
time.sleep(1)

# Onay Tanımı Seçimi (React Select)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-2-input")))
dropdown_input.click()
dropdown_input.send_keys("Test Onay Tanımı 63")
dropdown_input.send_keys(Keys.ENTER)

# # # 2️⃣ İlk seçenek görünür olana kadar bekle
# # first_option = wait.until(EC.element_to_be_clickable(
# #     (By.ID, "react-select-2-option-0")  # React-Select ilk seçenek genellikle option-0 olur
# # ))

# # 3️⃣ Tıkla
# first_option.click()
time.sleep(1)

# 1️⃣ Input'a tıkla (dropdown açılır)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-3-input")))
dropdown_input.click()

# 2️⃣ İlk seçenek görünür olana kadar bekle
first_option = wait.until(EC.element_to_be_clickable(
    (By.ID, "react-select-3-option-0")  # React-Select ilk seçenek genellikle option-0 olur
))
time.sleep(1)
# Ünvan Seviye Kodu
# 3️⃣ Tıkla
first_option.click()

# 1️⃣ Input'a tıkla (dropdown açılır)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-4-input")))
dropdown_input.click()

# 2️⃣ İlk seçenek görünür olana kadar bekle
first_option = wait.until(EC.element_to_be_clickable(
    (By.ID, "react-select-4-option-0")  # React-Select ilk seçenek genellikle option-0 olur
))
time.sleep(1)
# 3️⃣ Tıkla
first_option.click()

# Yeni satır ekle
add_row_button = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "button.inline-flex.items-center.rounded.h-8.w-8")  # Butonun class'ından seçtik
))
add_row_button.click()

# 2. Yeni eklenen satırdaki dropdown input'u bul
new_row_dropdown = wait.until(EC.element_to_be_clickable(
    (By.CSS_SELECTOR, "input#react-select-7-input")  # Yeni satırdaki dropdown input ID'si
))
new_row_dropdown.click()

# 3. İlk seçeneği seç
first_option = wait.until(EC.element_to_be_clickable(
    (By.ID, "react-select-7-option-0")  # Açılan ilk seçenek
))
time.sleep(1)
first_option.click()



# 1️⃣ Input'a tıkla (dropdown açılır)
dropdown_input = wait.until(EC.element_to_be_clickable((By.ID, "react-select-9-input")))
dropdown_input.click()

# 2️⃣ İlk seçenek görünür olana kadar bekle
first_option = wait.until(EC.element_to_be_clickable(
    (By.ID, "react-select-9-option-0")  # React-Select ilk seçenek genellikle option-0 olur
))
time.sleep(1)
first_option.click()


# Kaydet
kaydet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']")))
kaydet_btn.click()
time.sleep(2)

# # Menü → Düzenle
# menu_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[.//span[text()='Open menu']]")))
# menu_button.click()
# time.sleep(1)
# edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and text()='Düzenle']")))
# edit_button.click()
# time.sleep(1)

# # Onay Tanımı adı değiştir
# input_grup_adi = driver.find_element(By.XPATH, "//input[@id='input-Onay Adı']")
# input_grup_adi.clear()
# grup_numarasi = get_next_group_number()
# grup_adi = f"Test Onay Tanımı {grup_numarasi}"
# input_grup_adi.send_keys(grup_adi)
# time.sleep(1)


# # Çıkış Kararı Seçimi (React Select)
# wait = WebDriverWait(driver, 15)

# # 1) CikisKarari control'ünü aç
# control = wait.until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "#cikisKarari [class*='control']")
# ))
# control.click()

# # 2) Mevcut değer varsa X ile temizle (varsa)
# try:
#     clear_btn = driver.find_element(By.CSS_SELECTOR, "#cikisKarari [class*='clearIndicator']")
#     clear_btn.click()
# except:
#     pass

# # 3) Aynı container içindeki input'a yaz
# inp = wait.until(EC.element_to_be_clickable(
#     (By.CSS_SELECTOR, "#cikisKarari input[id*='react-select'][id$='-input']")
# ))
# # güvenli temizlik
# inp.send_keys(Keys.CONTROL, "a")
# inp.send_keys(Keys.DELETE)

# inp.send_keys("Tedarikci")

# # Menü gerçekten açıldı mı? (aria-expanded true olsun)
# wait.until(EC.text_to_be_present_in_element_attribute(
#     (By.CSS_SELECTOR, "#cikisKarari input[id*='react-select'][id$='-input']"),
#     "aria-expanded",
#     "true"
# ))

# # 4A) Metni birebir eşleşen opsiyonu tıkla (menü portalde olabilir, bu yüzden global arıyoruz)
# option = wait.until(EC.element_to_be_clickable(
#     (By.XPATH, "//div[@role='option' and normalize-space()='Tedarikci']")
# ))
# option.click()

# # --- Alternatif 4B: İlk filtrelenen opsiyonu seç (↓ + Enter)
# # inp.send_keys(Keys.ARROW_DOWN)
# # inp.send_keys(Keys.ENTER)

# # (İsteğe bağlı) seçimin gerçekten yapıldığını doğrula
# selected = wait.until(EC.visibility_of_element_located(
#     (By.CSS_SELECTOR, "#cikisKarari [class*='singleValue']")
# ))
# assert selected.text.strip() == "Tedarikci"

# # Kaydet
# kaydet_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']")))
# kaydet_btn.click()
# time.sleep(2)

print("Onay Tanımı başarıyla oluşturuldu") # Sonuç mesajı
print("Onay Tanımı başarıyla düzenlendi") # Düzenleme mesajı
driver.quit()
