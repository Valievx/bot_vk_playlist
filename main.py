from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import json
import os
import sys
import threading


'''options'''
# options.add_argument("--headless")


'''Authorization'''
playlist_url = input("Введите URl playlist: ")

working_dir = os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1])

with open(os.path.join(working_dir, "accounts.json"), "r", encoding="utf-8") as file:
    data = json.loads(file.read())
    accounts = data["accounts"]


def auth_user(t):
    for k in range(0 + t, len(accounts) + t, 2):
        if k >= len(accounts):  # проверяем к , чтоб не вылететь за пределы списка.
            continue
        account = accounts[k]

        try:
            options = webdriver.ChromeOptions()
            options.add_argument(f"user-data-dir={account['id']}")
            options.add_argument("user-agent=VKAndroidApp/4.38-849 (Android 6.0; SDK 23; x86; Google Nexus 5X; ru")
            options.add_argument("--disable-blink-features=AutomationControlled")
            s = Service("/Users/valiev/code/python/vkbot_playlist/chromedriver/chromedriver")
            driver = webdriver.Chrome(service=s, options=options)

            try:
                ''' Save session'''
                driver.get("https://m.vk.com/")
                time.sleep(2)

                '''btn-open'''
                btn_open = driver.find_element(By.XPATH, "//*[@id='vkidform__signin']/a").click()
                time.sleep(2)

                '''login'''
                email_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div[2]/div/div/div/form/div[1]/section/div[1]/div/div/input")
                email_input.clear()
                email_input.send_keys(account['phone'])
                time.sleep(2)

                login_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div/div/div/div/form/div[2]/div[1]/button/span[1]").click()
                time.sleep(10)

                '''password'''
                password_input = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div[2]/div/div/div/form/div[1]/div[3]/div[1]/div/input")
                password_input.clear()
                password_input.send_keys(account['password'])
                time.sleep(2)

                password_button = driver.find_element(By.XPATH, "//*[@id='root']/div/div/div/div/div[2]/div/div/div/form/div[2]/button").click()
                time.sleep(2)

            except Exception as ex:
                pass

            driver.get(f"{playlist_url}")
            time.sleep(2)

            amount = driver.find_element(By.XPATH, f'//*[@id="mcont"]/div/div/div[4]').text
            new_amount = amount[:2]   # 2(1-99) 3(100-999)
            new_thing = int(new_amount) + 1

            for i in range(1, new_thing):
                driver.find_element(By.XPATH, f'//*[@id="mcont"]/div/div/div[3]/div/div[{i}]').click()
                time.sleep(36)
                driver.find_element(By.XPATH, f'//*[@id="mcont"]/div/div/div[1]/div[1]/div[2]/div/div/div[1]/a').click()
                time.sleep(2)
        except Exception as ex:
            print(ex)
        finally:
            driver.close()
            driver.quit()


if __name__ == '__main__':
    threads = []
    for i in range(2):
        t = threading.Thread(target=auth_user, args=(i,))
        threads.append(t)
        t.start()

