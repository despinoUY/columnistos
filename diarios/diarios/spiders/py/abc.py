# -*- coding: utf-8 -*-
import scrapy
from scrapy.loader import ItemLoader

from diarios.items import DiariosItem


class AbcSpider(scrapy.Spider):
    name = 'abc'
    allowed_domains = ['www.abc.com.py']
    start_urls = ['http://www.abc.com.py/edicion-impresa/opinion']
    custom_settings = {
        'ROBOTSTXT_OBEY': False,
    }

    def parse(self, response):
        """
        @url http://www.abc.com.py/edicion-impresa/opinion
        @returns items 1 14
        @returns requests 0 0
        @scrapes author title url
        """
        selectors = response.xpath('//*[@class="listed"]/ul/li')
        for selector in selectors:
            yield self.parse_article(selector, response)

    def parse_article(self, selector, response):
        loader = ItemLoader(DiariosItem(), selector=selector)
        #
        loader.add_xpath('author', './/h3//text()')
        loader.add_xpath('title', './/h2//a//text()')
        loader.add_xpath('url', './/h2//@href')
        return loader.load_item()
