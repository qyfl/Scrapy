# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request, FormRequest


class WebSpider(scrapy.Spider):
    name = 'web'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://example.webscraping.com/places/default/user/login?_next=/places/default/index']

    def parse(self, response):

        
        pass
