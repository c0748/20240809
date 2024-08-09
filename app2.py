from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from dotenv import load_dotenv
import os
load_dotenv()

driver = webdriver.Chrome()
url = os.getenv('URL')
email = os.getenv('email')
password = os.getenv('password')

try:
    driver.get(url)
    time.sleep(5)
    email_input = driver.find_element(By.NAME, "email")
    password_input = driver.find_element(By.NAME, "password")

    email_input.send_keys(email)
    password_input.send_keys(password)
    time.sleep(5)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    login_button.click()
    time.sleep(5)

    download_link = driver.find_element(By.LINK_TEXT,'ファイルをダウンロード')
    download_link.click()
    time.sleep(10)





finally:
    driver.quit()
