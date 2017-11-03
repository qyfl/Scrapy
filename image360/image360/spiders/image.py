# -*- coding: utf-8 -*-

import json

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Request


class ImageSpider(scrapy.Spider):
    name = 'image'
    # allowed_domains = ['http://image.so.com/z?ch=beauty']

    base_url = 'http://image.so.com/zj?ch=beauty&sn=%s&listtype=new&temp=1'
    start_index = 0
    MAX_DOWNLOAD_NUM = 1000

    start_urls = [base_url % 0]

    def parse(self, response):
        infos = json.loads(response.body.decode('utf-8'))

        yield {'image_urls': [info['qhimg_url'] for info in infos['list']]}

        self.start_index += infos['count']

        if infos['count'] > 0 and self.start_index < self.MAX_DOWNLOAD_NUM:
            yield Request(url=self.base_url % self.start_index, callback=self.parse)
