# -*- coding: utf-8 -*-

import scrapy
from scrapy.http import Request, FormRequest


class WebSpider(scrapy.Spider):
    name = 'web'
    allowed_domains = ['example.webscraping.com']
    start_urls = ['http://60.191.71.142:7080/worksheetAPI/http/do.jhtml?router=homeService.initLogin']

    loginUrl = 'http://60.191.71.142:7080/worksheetAPI/http/do.jhtml?router=homeService.initLogin'

    def start_requests(self):
        yield Request(url=self.loginUrl,callback=self.login)
        pass

    def login(self, response):
        fd = {'email':'374643063@qq.com', 'password':'zhangdaosheng'}

        yield FormRequest.from_response(response, formdata=fd, callback=self.parse)

    def parse(self, response):

        request = FormRequest.from_response()
        if 'qyfl' in response.text:
            yield from super().start_requests()
        