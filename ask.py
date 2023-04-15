from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from fake_useragent import UserAgent
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from dotenv import load_dotenv
import loginAuth
import undetected_chromedriver as uc
import time
import os

def textArea():
    print("Enter something for chatGPT to ask:\n")
    st = input()
    element = WebDriverWait(driver, 10).until(EC.visibility_of_all_elements_located((By.TAG_NAME, 'textarea')))
    txtArea = driver.find_elements(By.TAG_NAME, 'textarea')[0]
    txtArea.send_keys(st)
    txtArea.send_keys(Keys.RETURN)
    numP = len(driver.find_elements(By.TAG_NAME, 'p'))
    return numP

def response(numP):
    time.sleep(4)
    # ele = driver.find_elements(By.CSS_SELECTOR, "")
    # element = WebDriverWait(driver, 10).until(EC.staleness_of(ele))
    print("\nResponse from GPT:\n")
    lent = numP + 1
    txP = len(driver.find_elements(By.TAG_NAME, 'p'))
    while txP >= lent:
        ele = driver.find_elements(By.CSS_SELECTOR, ".text-base.gap-4.p-4.flex.m-auto p")
        WebDriverWait(driver, 10).until(EC.staleness_of(ele))

    fnEl = driver.find_elements(By.CSS_SELECTOR, ".text-base.gap-4.p-4.flex.m-auto")[-1]
    fnEl = fnEl.find_elements(By.TAG_NAME, 'p')
    for pTxt in fnEl:
        print(pTxt.text)
    print("\n")

def cycle():
    while True:
        numP = textArea()
        response(numP)

if __name__ == "__main__":
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-agent={UserAgent.random}")
    options.add_argument("user-data-dir=./")
    # options.add_experimental_option("detach", True)
    options.add_experimental_option("excludeSwitches", ["enable-logging"])

    driver = uc.Chrome(chrome_options=options)

    load_dotenv()
    em = os.getenv("EMAIL_ID")
    ps = os.getenv("PASSWORD")
    loginAuth.enter_gpt(em, ps, driver=driver)
    cycle()

