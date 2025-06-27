# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager  # EKLENDİ
import time
import datetime
import sys
import io


sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
# -*- coding: utf-8 -*-
# Bu kod, Selenium WebDriver kullanarak bir web uygulamasına giriş yapmayı, belirli bir modülü açmayı ve form doldurmayı otomatikleştirir.
# WebDriver ayarları
service = Service(ChromeDriverManager().install())  # ChromeDriverManager ile otomatik olarak ChromeDriver'ı indirir ve kurar.
driver = webdriver.Chrome(service=service)
driver.maximize_window()
driver.get("https://stage.gurerp.com/login")
driver.implicitly_wait(10)  # Sayfanın yüklenmesi için bekler.
# Sayfanın Türkçe karakterlerle düzgün yüklendiğinden emin olmak için:
driver.page_source.encode('iso-8859-9').decode('utf-8')
today = datetime.date.today().strftime("%d-%m-%Y")  # Bugünün tarihi formatlanır.

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

# "Satın Alma Talebi" başlığına tıklamak için:
driver.find_element(By.XPATH, "//*[contains(text(), 'Satın Alma Talebi')]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Satın alma talebi sayfasının yüklenmesi için bekler.

# "Talep Listesi" başlığına tıklamak için:
driver.find_element(By.XPATH, "//*[contains(text(), 'Talep Listesi')]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Talep listesi sayfasının yüklenmesi için bekler.

# "Yeni Ekle" butonuna tıklamak için:
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Yeni Ekle')]]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Yeni talep formunun açılması için bekler.

# "Talep Tipi" dropdown menüsünden "Hizmet" seçeneğini seçmek için:
driver.find_element(By.XPATH, "//*[contains(text(), 'Hizmet') and @role='menuitem']").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Dropdown'un açılması için bekler.

# "Açıklama" inputuna metin yazmak için:
driver.find_element(By.XPATH, "//input[@name='aciklama']").send_keys("Bu talep otomasyonla oluşturulmuştur.")  # Açıklama olarak "Bu talep otomasyonla oluşturulmuştur." yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.

# Kod Search (arama) ikonunu seçmek için:
driver.find_element(By.XPATH, "//input[@name='malzemeler[0].ortakNo']/following-sibling::*[name()='svg' and contains(@class, 'lucide-search')]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Arama sonuçlarının yüklenmesi için bekler.

# Stok satırındaki checkbox'ı seçmek için:
driver.find_element(By.XPATH, "//div[@role='row' and @data-rowindex='0']//input[@type='checkbox']").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Seçimin yapılması için bekler.

# "Seç ve Ekle" butonuna tıklamak için:
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Seç ve Ekle')]]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Seçimin yapılması için bekler.

# Stok Açıklama alanına metin yazmak için:
wait = WebDriverWait(driver, 10)
input_aciklama = wait.until(EC.presence_of_element_located((By.NAME, "malzemeler[0].detayAciklama")))
input_aciklama.send_keys("Hizmet açıklaması")
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.

# "Miktar" inputuna metin yazmak için:
input_miktar = driver.find_element(By.NAME, "malzemeler[0].miktar")
input_miktar.clear()  # Önceki değeri temizler.
input_miktar.send_keys("0")  # Miktar olarak 0 yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.

# Dropdown'u aç
dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-6-input']")))
dropdown_input.click()
# İstersen bir şey yazabilirsin, boş bırakıp sadece açabilirsin
dropdown_input.send_keys("01.17.170.9320")  # veya bir şey yaz
time.sleep(1)  # Değerin yazılması için bekler.
# İlk seçeneği seçmek için Enter tuşuna bas
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)  # Seçimin yapılması için bekler.

# "Birim Yaklaşık Maliyet" inputuna metin yazmak için:
input_birim_fiyat = driver.find_element(By.NAME, "malzemeler[0].birimFiyat")
input_birim_fiyat.clear()  # Önceki değeri temizler.
input_birim_fiyat.send_keys("1000000")  # Birim fiyat olarak 1000000 yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.

# "Para Birimi seçiniz" dropdown'unu açmak için:
dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-7-input']")))
dropdown_input.click()
# İstersen bir şey yazabilirsin, boş bırakıp sadece açabilirsin
dropdown_input.send_keys("TRY")  # veya bir şey yaz
# İlk seçeneği seçmek için Enter tuşuna bas
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)  # Seçimin yapılması için bekler.

# "İl seçiniz" dropdown'unu açmak için:
dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-8-input']")))
dropdown_input.click()
# İstersen bir şey yazabilirsin, boş bırakıp sadece açabilirsin
dropdown_input.send_keys("Konya")  # veya bir şey yaz
# İlk seçeneği seçmek için Enter tuşuna bas
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)  # Seçimin yapılması için bekler.

# "İlçe seçiniz" dropdown'unu açmak için:
dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-9-input']")))
dropdown_input.click()
# İstersen bir şey yazabilirsin, boş bırakıp sadece açabilirsin
dropdown_input.send_keys("Meram")  # veya bir şey yaz
# İlk seçeneği seçmek için Enter tuşuna bas
dropdown_input.send_keys(Keys.ENTER)
time.sleep(1)  # Seçimin yapılması için bekler.

# "Telefon" inputuna metin yazmak için:
input_telefon = driver.find_element(By.CLASS_NAME, "form-control")  # Telefon inputunu bulur.
input_telefon.send_keys("5555555555")  # Telefon numarası olarak 5555555555 yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.

# "Adres" inputuna metin yazmak için:
input_adres = driver.find_element(By.NAME, "malzemeler[0].adres")
input_adres.send_keys("Konya/Meram")  # Adres bilgisi olarak "Konya/Meram" yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.


# "Posta Kodu" inputuna metin yazmak için:
input_posta_kodu = driver.find_element(By.NAME, "malzemeler[0].postaKodu")
input_posta_kodu.send_keys("42123")  # Posta kodu olarak "42123" yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Değerin yazılması için bekler.

# Doğrudan Temin dropdown'unu açmak için:
dropdown_input = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='react-select-11-input']")))
dropdown_input.click()
# İsterseniz bir şey yazabilir veya Enter ile seçim yapabilirsiniz
dropdown_input.send_keys("Hayır")  # veya bir şey yaz
dropdown_input.send_keys(Keys.ENTER)
time.sleep(2)

# Ekranı sağa kaydırmak için:
driver.execute_script("window.scrollBy(200, 0);")  # 200 px sağa kaydırır
time.sleep(1)  # Ekranın kaydırılması için bekler.

# Dropdown input alanını bekle ve tıklanabilir olunca tıkla
dropdown_input = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'css-yxkkaz-control')]//input[@id='react-select-14-input']"))
)
dropdown_input.click()
time.sleep(0.5)  # Menü açılması için bekle
# Arama metni gir (opsiyonel)
dropdown_input.send_keys("İşletme")  # Veya başka bir metin, veya boş
time.sleep(0.5)  # Önerilerin yüklenmesini bekle
# Enter ile ilk öneriyi seç
dropdown_input.send_keys(Keys.ENTER)
time.sleep(2)  # Seçimin yapılması için bekler.

# Başlangıç tarihi inputunu seçmek için:
start_date_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//td[contains(@class, 'MuiTableCell-root')]//input[@type='date'])[1]")))
start_date_input.send_keys(today)  # Bugünün tarihi yazılır.
time.sleep(2)  # Başlangıç tarihinin seçilmesi için bekler.

# Bitiş tarihi inputunu seçmek için:
next_year = (datetime.date.today().replace(year=datetime.date.today().year + 1)).strftime("%d-%m-%Y")
end_date_input = wait.until(EC.presence_of_element_located((By.XPATH, "(//td[contains(@class, 'MuiTableCell-root')]//input[@type='date'])[2]")))
end_date_input.send_keys(next_year)  # Gelecek yılın tarihi yazılır.
time.sleep(2)  # Bitiş tarihinin seçilmesi için bekler.

# "Gerekçe" inputuna metin yazmak için:
input_gerekce = driver.find_element(By.NAME, "malzemeler[0].gerekce")
input_gerekce.send_keys("Bu talep otomasyonla oluşturulmuştur.")  # Gerekçe olarak "Bu talep otomasyonla oluşturulmuştur." yazılır.
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(2)  # Değerin yazılması için bekler.

# "Şablon Kaydet" butonuna tıklamak için:
button = driver.find_element(By.XPATH, "//button[.//span[text()='Şablon Kaydet']]")
button.click()
time.sleep(2)  # Şablon kaydetme işleminin tamamlanması için bekler.

# "Confirm" butonuna tıklamak için:
button = driver.find_element(By.XPATH, "//button[@type='button' and .//span[text()='Evet']]")
button.click()
time.sleep(1)  # Onaylama işleminin tamamlanması için bekler.
print("Şablon başarıyla oluşturuldu.")  # Başarılı bir şekilde talep oluşturulduğunu bildirir.
time.sleep(2)  # Onaylama işleminin tamamlanması için bekler.

# "Yeni Ekle" butonuna tıklamak için:
driver.find_element(By.XPATH, "//button[.//text()[contains(., 'Yeni Ekle')]]").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Yeni talep formunun açılması için bekler.

# "Talep Tipi" dropdown menüsünden "Şablon Seç" seçeneğini seçmek için:
driver.find_element(By.XPATH, "//*[contains(text(), 'Şablon Seç') and @role='menuitem']").click()
driver.implicitly_wait(10)  # Değerin yazılması için bekler.
time.sleep(1)  # Dropdown'un açılması için bekler.

# "Seçim yapınız" dropdown'unun bulunduğu alanı bekle
wait.until(EC.visibility_of_element_located(
    (By.XPATH, "//div[contains(@class, 'css-ju9thq-control')]")
))
time.sleep(0.5)  # Stil animasyonları için kısa bekleme

# Dropdown input alanını bekle ve tıkla
dropdown_input = wait.until(EC.element_to_be_clickable(
    (By.XPATH, "//input[contains(@id,'react-select') and @type='text']")
))
dropdown_input.click()
time.sleep(0.5)  # Tıklamadan sonra input aktifleşsin
# İlgili değeri yaz
dropdown_input.send_keys(Keys.ARROW_DOWN)  # İlk öneriyi seçmek için aşağı ok tuşuna bas
time.sleep(1)  # Önerilerin gelmesi için bekle
dropdown_input.send_keys(Keys.ENTER)
time.sleep(2)

# "Seç" butonunu bul ve tıkla
sec_buton = wait.until(EC.element_to_be_clickable((By.XPATH, "//button[normalize-space()='Seç']")))
sec_buton.click()
time.sleep(3)  # Menü açılmasını bekle

# Tarayıcıyı kapat
driver.quit()  # Tarayıcıyı kapatır.
# Not: Bu kod, Selenium WebDriver ile bir web uygulamasına giriş yapmayı, belirli bir modülü açmayı ve form doldurmayı otomatikleştirir.