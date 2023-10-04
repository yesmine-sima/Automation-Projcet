from selenium import webdriver
import time

webdriver = webdriver.Firefox()
webdriver.maximize_window()
time.sleep(5)
webdriver.get('https://getmusic.cc/')
time.sleep(5)


