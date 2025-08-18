from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # EKLENDİ
import time
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# -*- coding: utf-8 -*-
# Bu kod, Selenium WebDriver kullanarak bir web uygulamasına giriş yapmayı, belirli bir modülü açmayı ve form doldurmayı otomatikleştirir.

service = Service(ChromeDriverManager().install())  # ChromeDriverManager ile otomatik olarak ChromeDriver'ı indirir ve kurar.
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://stage.gurerp.com/login")
driver.implicitly_wait(10)  # Sayfanın yüklenmesi için bekler.

wait = WebDriverWait(driver, 10)  # 10 saniye bekleme süresi
# Giriş sayfasında gerekli elementlerin yüklenmesini bekler
# Giriş bilgilerini doldur
driver.find_element(By.NAME, "userName").send_keys("ali.akkaya")  # Kullanıcı adını yazar.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
driver.find_element(By.NAME, "password").send_keys("123")  # Şifreyi yazar.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
driver.find_element(By.NAME, "privacyPolicy").click()  # Gizlilik politikasını kabul eder.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
driver.find_element(By.CLASS_NAME, "MuiButtonBase-root").click()  # Giriş butonuna tıklar.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Giriş işleminin tamamlanması için bekler.

# "Tema Değiştir" butonuna tıklamak için:
driver.find_element(By.XPATH, "//button[@title='Karanlık Mod']").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Tema değişikliğinin uygulanması için bekler.

# "Satın Alma, İhale ve Malzeme Yönetimi" kartına tıklamak için:
driver.find_element(By.XPATH, "//h3[contains(text(), 'Satın Alma, İhale ve Malzeme Yönetimi')]/ancestor::a").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Satın alma modülünün yüklenmesi için bekler.

# Sol menüdeki "Satın Alma, Malzeme ve İhale Yönetimi" butonuna tıkla
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Satın Alma, Malzeme ve İhale Yönetimi')]]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Satın alma modülünün yüklenmesi için bekler.

# Sol menüdeki "Tanımlamalar" butonuna tıkla
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Tanımlamalar')]]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Tanımlamalar modülünün yüklenmesi için bekler.

# "Tanımlamalar" modülünde "İş Emri" başlığına tıkla
buton = driver.find_element(By.XPATH, "//button[normalize-space(text())='İş Emri']")
buton.click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # İş Emri sekmesinin yüklenmesi için bekler.

# "Tanımlamalar" modülünde "Grup" başlığına tıkla
driver.find_element(By.XPATH, "//button[normalize-space(text())='Onay Seviyeleri']").click()
time.sleep(1)  # Değerin yazılması için bekler.


# Eğer bir seçim yapıldıysa, "İşlemler" butonuna tıkla
wait = WebDriverWait(driver, 10)
# Daha stabil bir XPATH veya CSS seçici kullanın
menu_button = wait.until(EC.element_to_be_clickable((
    By.XPATH,
    "//button[.//span[text()='Open menu']]"
)))
menu_button.click()
time.sleep(1)  # Menü açılmasını bekler.

# 'Düzenle' menü öğesini bekle ve tıkla
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and text()='Pasif Yap']")))
edit_button.click()
time.sleep(2)  # Kaydetme işleminin tamamlanması için bekler.

# "Evet" butonunu bekle ve tıkla
evet_button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//button[text()='Evet']"))
)
evet_button.click()
time.sleep(2)  # Evet butonunun tıklanması için bekler.

print("Onay Seviyesi başarıyla pasif yapıldı")  # Sonuç mesajı

driver.quit()  # Tarayıcıyı kapatır.