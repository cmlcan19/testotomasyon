from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

# WebDriver başlatılıyor (otomatik driver ayarı ile)
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# Login sayfasına git
driver.get("https://the-internet.herokuapp.com/login")

# Yanlış kullanıcı adı ve şifre gir
driver.find_element(By.ID, "username").send_keys("wrongUser")
driver.find_element(By.ID, "password").send_keys("wrongPass")
driver.find_element(By.CSS_SELECTOR, "button.radius").click()

# Hata mesajını kontrol et
error_message = driver.find_element(By.ID, "flash").text
assert "Your username is invalid!" in error_message

# Sonuçları görmek için bekle ve tarayıcıyı kapat
time.sleep(3)
driver.quit()
