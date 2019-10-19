from selenium import webdriver
import time

driver = webdriver.Chrome()
l1 = r'https://ru.wikibooks.org/wiki'
l2 = r'https://stepik.org/lesson/24461/step/9?auth=login&unit=6767'

class BasePage():
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    def open(self):
        self.browser.get(self.url)


page = BasePage(driver, l1)
time.sleep(5)
page.open()
