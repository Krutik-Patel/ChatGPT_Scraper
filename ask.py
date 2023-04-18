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

def response():
    print("\nResponse from GPT:\n")
    time.sleep(2)
    last_par = 1
    lastP = driver.find_element(By.XPATH, f"((//div[@class='flex flex-grow flex-col gap-3'])[last()]//p)[{last_par}]")
    sz_lst = len(driver.find_elements(By.XPATH, "(//div[@class='flex flex-grow flex-col gap-3'])[last()]//p"))
    # print(sz_lst)
    while last_par <= sz_lst:
        lent = -1
        curr = len(lastP.text)
        while lent < curr:
            lent = curr
            time.sleep(1)
            lastP = driver.find_element(By.XPATH, f"((//div[@class='flex flex-grow flex-col gap-3'])[last()]//p)[{last_par}]")
            curr = len(lastP.text)
        print(lastP.text)
        print("\n")
        time.sleep(3)
        sz_lst = len(driver.find_elements(By.XPATH, "(//div[@class='flex flex-grow flex-col gap-3'])[last()]//p"))
        last_par += 1


    print("\nEnd of Response===================")

def cycle():
    while True:
        textArea()
        response()

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

