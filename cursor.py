from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# Tarayıcı ayarları
options = Options()
options.add_experimental_option("detach", True)  # Tarayıcı açık kalsın

# Tarayıcı başlat
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Hedef siteye git
driver.get("https://stage.gurerp.com/login")

# Kırmızı imleci ekle
cursor_script = """
var cursor = document.createElement('div');
cursor.id = 'selenium-cursor';
cursor.style.width = '15px';
cursor.style.height = '15px';
cursor.style.background = 'red';
cursor.style.borderRadius = '50%';
cursor.style.position = 'fixed';
cursor.style.zIndex = '9999';
cursor.style.top = '0px';
cursor.style.left = '0px';
cursor.style.pointerEvents = 'none';
document.body.appendChild(cursor);

document.addEventListener('mousemove', function(e) {
    var c = document.getElementById('selenium-cursor');
    if (c) {
        c.style.left = e.clientX + 'px';
        c.style.top = e.clientY + 'px';
    }
});
"""

driver.execute_script(cursor_script)

# İmleç görünür kalsın diye bekletme
time.sleep(10)

driver.quit()