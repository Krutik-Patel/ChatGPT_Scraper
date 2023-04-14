from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from fake_useragent import UserAgent
from dotenv import load_dotenv
import undetected_chromedriver as uc
import time
import os


def open():
    driver.get("https://chat.openai.com/auth/login")
    time.sleep(10)

def login(emailID, password):
    open()
    loginBtn = driver.find_elements(By.CSS_SELECTOR, ".btn.relative.btn-primary")[0]
    loginBtn.click()
    time.sleep(3)
    userNm = driver.find_element(By.ID, 'username')
    userNm.send_keys(emailID)
    userNm.send_keys(Keys.RETURN)
    time.sleep(2)
    passwd = driver.find_element(By.ID, 'password')
    passwd.send_keys(password)
    passwd.send_keys(Keys.RETURN)

def skip_popups():
    nxtBtn = driver.find_element(By.CSS_SELECTOR, '.btn.relative.btn-neutral.ml-auto')
    nxtBtn.click()
    nxtBtn.click()
    dnBtn = driver.find_element(By.CSS_SELECTOR, '.btn.relative.btn-primary.ml-auto')
    dnBtn.click()
    
def enter_gpt(emailID, password):
    login(emailID, password)
    skip_popups()

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={UserAgent.random}")
    options.add_argument("user-data-dir=./")
    options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = uc.Chrome(chrome_options=options)

    load_dotenv()
    EMAIL_ID = os.getenv("EMAIL_ID")
    PASS = os.getenv("PASSWORD")
    enter_gpt(EMAIL_ID, PASS)
    time.sleep(15)