from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from auth_data import vk_password, vk_login, token, playlist_id
import time


# options
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=https://") # ссылка личной страницы
options.add_argument("user-agent=VKAndroidApp/4.38-849 (Android 6.0; SDK 23; x86; Google Nexus 5X; ru")
s = Service("/Users/valiev/code/python/vkbot_playlist/chromedriver/chromedriver")
driver = webdriver.Chrome(service=s, options=options)

'''
# Authorization

driver.get("https://vk.com/")
time.sleep(5)

# login
email_input = driver.find_element("id", "index_email")
email_input.clear()
email_input.send_keys(vk_login)
time.sleep(5)

login_button = driver.find_element(By.XPATH, "//*[@id='index_login']/div[1]/form/button[1]").click()
time.sleep(5)

# password
password_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input")
password_input.clear()
password_input.send_keys(vk_password)
time.sleep(5)

password_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div[2]/div/div/div/form/div[2]/button").click()
time.sleep(50)
'''

# Вход и открытие плейлиста

driver.get(f"{playlist_id}")
time.sleep(2)
url = playlist_id


# Цикл
amount = driver.find_element(By.XPATH, f'//*[@id="mcont"]/div/div/div[4]').text
new_amount = amount[:-30]   # 30 # 32 # 34
new_thing = int(new_amount) + 1
print(new_thing)


for i in range(1, new_thing):
    driver.find_element(By.XPATH, f'//*[@id="mcont"]/div/div/div[3]/div/div[{i}]').click()
    time.sleep(36)


driver.close()
driver.quit()
