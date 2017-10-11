__author__ = 'pioc'

from selenium import webdriver


class Browser(object):

    driver = webdriver.Chrome(executable_path='C:\chromedriver')
    driver.maximize_window()
    driver.implicitly_wait(2)
