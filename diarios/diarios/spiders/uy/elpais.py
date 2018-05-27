# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.loader import ItemLoader

from diarios.items import DiariosItem


class ElPaisSpider(scrapy.Spider):
    name = 'elpais'
    allowed_domains = ['www.elpais.com.uy']
    start_urls = ['https://www.elpais.com.uy/opinion']

    def parse(self, response):
        """
        @url https://www.elpais.com.uy/opinion
        @returns items 0 10
        @returns requests 0 0
        @scrapes author title url
        """
        # cintillo
        selectors = response.css('.opinion-columnistas-listing').xpath("//div[contains(@class,'listing-item')][.//div[contains(@class,'listing-author-name')]]")

        for selector in selectors:
            yield self.parse_article(selector, response)


    def parse_article(self, selector, response):

        loader = ItemLoader(DiariosItem(), selector=selector)

        loader.add_xpath('title', "./h3[contains(@class,'listing-title')]/a/text()")
        loader.add_xpath('author', "./div[contains(@class,'listing-author-name')]/text()")


        loader.add_xpath('url', "./h3[contains(@class,'listing-title')]/a/@href")
        loader.add_xpath('site', "./div[contains(@class,'listing-author-name')]/text()")
        loader.add_xpath('added', "./div[contains(@class,'listing-date')]/data-time")
        #loader.add_xpath('last_seen', "./div[contains(@class,'listing-author-name')]/text()")


        #loader.add_xpath('author', response.css('.listing-author-name').xpath('text()'))

        #logging.info(response.css('.listing-author-name').xpath('text()').extract())

        return loader.load_item()
