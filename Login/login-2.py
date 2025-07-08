from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager  # EKLENDİ
import time

def login(driver, username, password, accept_policy=True):
    # Giriş işlemini otomatikleştirir.
    user_input = driver.find_element(By.NAME, "userName")  # Kullanıcı adı input'unu bulur.
    pass_input = driver.find_element(By.NAME, "password")  # Şifre input'unu bulur.
    user_input.send_keys(username)  # Kullanıcı adını yazar.
    time.sleep(1)
    pass_input.send_keys(password)  # Şifreyi yazar.
    time.sleep(1)
    if accept_policy:
        # Eğer gizlilik politikasını kabul etmesi gerekiyorsa, kutucuğu işaretler.
        try:
            driver.find_element(By.NAME, "privacyPolicy").click()
            time.sleep(1)
        except:
            pass  # Eğer kutucuk yoksa hata vermez, devam eder.
    driver.find_element(By.CLASS_NAME, "MuiButtonBase-root").click()  # Giriş butonuna tıklar.
    time.sleep(2)  # Sonraki işlemler için kısa bir bekleme.

def main():
    service = Service(ChromeDriverManager().install())  # ChromeDriverManager ile otomatik olarak ChromeDriver'ı indirir ve kurar.
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()
    driver.get("https://stage.gurerp.com/login")
    time.sleep(2)

    # Başarılı Login
    login(driver, "ali.akkaya", "123", accept_policy=True)
    time.sleep(3)

    # SatınAlma modülüne geçiş
    driver.find_element(By.CLASS_NAME, "rounded-xl").click()  # Satın alma modülüne geçiş yapar.
    time.sleep(2)  # Satın alma modülünün yüklenmesi için bekler.

    driver.quit()

if __name__ == "__main__":
    main()
# Bu kod, Selenium kullanarak bir web sitesine giriş yapmayı ve belirli bir modüle geçiş yapmayı otomatikleştirir.
# Giriş işlemi sırasında kullanıcı adı, şifre ve gizlilik politikası onayı gibi bilgileri kullanır.
# Ayrıca, ChromeDriver'ı otomatik olarak indirip kurmak için `webdriver_manager` kütüphanesini kullanır.
# Bu sayede, ChromeDriver'ın doğru sürümünü manuel olarak indirme ihtiyacını ortadan kaldırır.
# Kod, giriş işlemi başarılı olduktan sonra "Satın Alma" modülüne geçiş yapar ve ardından tarayıcıyı kapatır.
# Bu, web otomasyonu için yaygın bir kullanım senaryosudur ve test otomasyonu   i veya web uygulamalarının etkileşimli testleri için kullanılabilir.
# Kodun sonunda, `main()` fonksiyonu çağrılarak tüm işlemler başlatılır.
# Bu, kodun modüler ve okunabilir olmasını sağlar.