from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
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
    service = Service(executable_path="chromedriver.exe")
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