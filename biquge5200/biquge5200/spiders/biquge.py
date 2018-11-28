# -*- coding: utf-8 -*-
import scrapy


class BiqugeSpider(scrapy.Spider):
    name = 'biquge'
    allowed_domains = ['dingdian']
    start_urls = ['http://dingdian/']

    def parse(self, response):
        pass
