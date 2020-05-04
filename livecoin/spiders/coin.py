# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    # start_urls = ['http://www.livecoin.net/en']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(executable_path="./chromedriver")
        driver.get('http://www.livecoin.net/en')

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[4]

        self.html = driver.page_source
        driver.close()



    def parse(self, response):
        pass
