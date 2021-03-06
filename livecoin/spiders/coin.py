# -*- coding: utf-8 -*-
import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from scrapy.selector import Selector

class CoinSpider(scrapy.Spider):
    name = 'coin'
    allowed_domains = ['www.livecoin.net/en']
    start_urls = ['http://www.livecoin.net/en']

    def __init__(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")

        driver = webdriver.Chrome(executable_path="./chromedriver", options=chrome_options)
        driver.set_window_size(1920, 1080)
        driver.get('http://www.livecoin.net/en')

        rur_tab = driver.find_elements_by_class_name("filterPanelItem___2z5Gb")
        rur_tab[0].click()

        self.html = driver.page_source
        driver.close()



    def parse(self, response):
        resp = Selector(text=self.html)

        for currency in resp.xpath("//div[contains(@class, 'ReactVirtualized__Table__row tableRow___3EtiS ')]"):
            yield {
                'currency': currency.xpath(".//div[1]/div/text()").get(),
                'volumn(24hr)': currency.xpath(".//div[2]/span/text()").get()
            }