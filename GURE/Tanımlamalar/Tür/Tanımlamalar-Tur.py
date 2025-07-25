from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager  # EKLENDİ
import time
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# -*- coding: utf-8 -*-
# Bu kod, Selenium WebDriver kullanarak bir web uygulamasına giriş yapmayı, belirli bir modülü açmayı ve form doldurmayı otomatikleştirir.

service = Service(ChromeDriverManager().install()) # ChromeDriverManager ile otomatik olarak ChromeDriver'ı indirir ve kurar.
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

# "Tanımlamalar" modülünde "Tür" başlığına tıkla
buton = driver.find_element(By.XPATH, "//button[normalize-space(text())='Tür']")
buton.click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Tür sekmesinin yüklenmesi için bekler.

# "Tür" sayfasında "Yeni Ekle" başlığına tıkla
yeni_ekle_buton = driver.find_element(By.XPATH, "//button[.//span[normalize-space(text())='Yeni Ekle']]")
yeni_ekle_buton.click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Yeni Ekle sekmesinin yüklenmesi için bekler.

# Grup sayacını al ve bir sonraki grup numarasını oluştur
def get_next_group_number(file_path="grup_sayac.txt"):
    try:
        with open(file_path, "r") as file:
            sayac = int(file.read())
    except FileNotFoundError:
        sayac = 1  # Dosya yoksa 1 ile başla

    with open(file_path, "w") as file:
        file.write(str(sayac + 1))

    return sayac


# Grup numarasını al ve grup adını oluştur
grup_numarasi = get_next_group_number()
grup_adi = f"Test Türü {grup_numarasi}"

# "Grup Adı" alanına metin gir
input_grup_adi = driver.find_element(By.XPATH, "//input[@id='input-Tür Adı']")
input_grup_adi.send_keys(grup_adi)

# 1. Dropdown input'a tıkla
dropdown_input = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-5rvhb9')]//input[@type='text']"))
)
dropdown_input.click()
time.sleep(0.5)

# 2. Metni yaz (örneğin: "Düzenleme")
dropdown_input.send_keys("Malzeme Talep Grubu")
time.sleep(1)  # Önerilerin yüklenmesini bekle

# 3. İlk çıkan sonucu ENTER ile seç
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)

wait = WebDriverWait(driver, 10)  # 10 saniye bekleme süresi

# Eğer bir seçim yapıldıysa, "Kaydet" butonuna tıkla
kaydet_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']"))
)
kaydet_btn.click()
time.sleep(2)  # Kaydetme işleminin tamamlanması için bekler.
# Eğer "Kaydet" butonu tıklanırsa, başarılı bir şekilde kaydedildi mesajını gösterir.

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
edit_button = wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@role='menuitem' and text()='Düzenle']")))
edit_button.click()
time.sleep(1)  # Düzenleme sayfasının yüklenmesi için bekler.

# "Tür Adı" alanını düzenle
input_grup_adi = driver.find_element(By.XPATH, "//input[@id='input-Tür Adı']")
input_grup_adi.clear()
input_grup_adi.send_keys("Yeni Tür Adı"+ f" {grup_numarasi}")  # Yeni tür adını girer.
# "Kaydet" butonuna tıkla
kaydet_btn = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//button[normalize-space(text())='Kaydet']"))
)
kaydet_btn.click()
time.sleep(2)  # Kaydetme işleminin tamamlanması için bekler.
# Eğer "Kaydet" butonu tıklanırsa, başarılı bir şekilde kaydedildi mesajını gösterir.
# "Grup" sayfasını kapat

driver.quit()  # Tarayıcıyı kapatır.