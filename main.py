import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from auth_data import vk_password, vk_login, token, playlist_id
import time
from bs4 import BeautifulSoup
import json


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

# Enter and open a playlist

driver.get(f"{playlist_id}")
time.sleep(2)
url = playlist_id



# Parser audio
req = requests.get(url=url)
result = req.content

soup = BeautifulSoup(result, "lxml")
hrefs = soup.find(class_="AudioPlaylistRoot")



audio_data = []
count = 0
for item in hrefs:
    href_audio = item.get("data-audio")
    # print(href_audio)

    count += 1
    audio_data.append(href_audio)

with open("audio_data.json", "w", encoding="utf8") as file:
    json.dump(audio_data, file, indent=4, ensure_ascii=False)


driver.close()
driver.quit()
