import time

import selenium

from selenium import webdriver

class youtubesec:
    def __init__(self):
        site = "https://www.ytroulette.com/?i=136&c=0"
        chromedriver = "C:\chromedriver.exe"
        site = "https://www.ytroulette.com/"
        self.driver = selenium.webdriver.Chrome(chromedriver)
        self.driver.get(site)
        time.sleep(3)
        self.driver.find_element_by_xpath('''/html/body/div[4]/div/div/div[2]/div[1]/div[1]/button''').click()
        time.sleep(3)
        self.driver.find_element_by_xpath('''/html/body/div[4]/div/div/div[2]/div[1]/div[1]/ul/h3/li[5]/a''').click()
        while True:
            time.sleep(10)
            self.driver.find_element_by_xpath('''/html/body/div[4]/div/div/div[2]/div[1]/div[2]/button''').click()
            time.sleep(0.2)
            self.driver.find_element_by_xpath('''/html/body/nav''').click()

youtubesec();

