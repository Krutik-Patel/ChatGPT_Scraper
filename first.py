from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from fake_useragent import UserAgent
from . import loginAuth
import undetected_chromedriver as uc
import time

options = webdriver.ChromeOptions()
options.add_argument(f"user-agent={UserAgent.random}")
options.add_argument("user-data-dir=./")
options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-logging"])


driver = uc.Chrome(chrome_options=options)

