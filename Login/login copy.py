from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager    
import time

class LoginAutomation:
    def __init__(self):
        self.service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=self.service)
        self.driver.maximize_window()
        self.driver.get("https://stage.gurerp.com/login")
        time.sleep(2)

    def clear_input(self, element):
        element.click()
        element.send_keys(Keys.CONTROL + "a")
        element.send_keys(Keys.DELETE)
        time.sleep(0.2)

    def login(self, username, password, accept_policy=True):
        user_input = self.driver.find_element(By.NAME, "userName")
        pass_input = self.driver.find_element(By.NAME, "password")
        self.clear_input(user_input)
        self.clear_input(pass_input)
        user_input.send_keys(username)
        time.sleep(1)
        pass_input.send_keys(password)
        time.sleep(1)
        
        if accept_policy:
            try:
                self.driver.find_element(By.NAME, "privacyPolicy").click()
                time.sleep(1)
            except:
                pass
        
        self.driver.find_element(By.CLASS_NAME, "MuiButtonBase-root").click()
        time.sleep(2)

    def run_tests(self):
        # Hatalı Login
        self.login("test", "asdf", accept_policy=True)
        time.sleep(2)

        # Hatalı Kullanıcı Adı
        self.login("test", "123", accept_policy=False)
        time.sleep(2)

        # Hatalı Şifre
        self.login("ali.akkaya", "asdf", accept_policy=False)
        time.sleep(2)

        # Başarılı Login
        self.login("ali.akkaya", "123", accept_policy=False)
        time.sleep(3)

    def close(self):
        self.driver.quit()

