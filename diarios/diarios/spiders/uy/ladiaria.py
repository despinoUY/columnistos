# -*- coding: utf-8 -*-
import scrapy
import logging
from scrapy.loader import ItemLoader

from diarios.items import DiariosItem


class LaDiariaSpider(scrapy.Spider):
    name = 'ladiaria'
    allowed_domains = ['findesemana.ladiaria.com.uy']
    start_urls = ['https://findesemana.ladiaria.com.uy/seccion/posturas/']

    def parse(self, response):
        """
        @url https://findesemana.ladiaria.com.uy/seccion/posturas/
        @returns items 0 10
        @returns requests 0 0
        @scrapes author title url
        """
        # cintillo
        selectors = response.css('.section_module').xpath("//div[contains(@class,'ld-card')]")

        logging.info(selectors)

        for selector in selectors:
            yield self.parse_article(selector, response)


    def parse_article(self, selector, response):

        loader = ItemLoader(DiariosItem(), selector=selector)

        loader.add_xpath('title',  "./div[contains(@class,'ld-card__body')]/h3[contains(@class,'ld-card__title')]/a/text()")
        loader.add_xpath('author', "./div[contains(@class,'ld-card__body')]/h3[contains(@class,'ld-card__title')]/a/text()")


        loader.add_xpath('url', "./div[contains(@class,'ld-card__body')]/h3[contains(@class,'ld-card__title')]/a/@href")
        loader.add_xpath('site', "./div[contains(@class,'ld-card__body')]/h3[contains(@class,'ld-card__title')]/a/text()")
        #loader.add_xpath('last_seen', "./div[contains(@class,'listing-author-name')]/text()")


        #loader.add_xpath('author', response.css('.listing-author-name').xpath('text()'))

        #logging.info(response.css('.listing-author-name').xpath('text()').extract())

        return loader.load_item()
