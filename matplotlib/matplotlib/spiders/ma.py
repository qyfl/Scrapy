# -*- coding: utf-8 -*-

import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy import Request
from ..items import MatplotlibItem

class MaSpider(scrapy.Spider):
    name = 'ma'
    allowed_domains = ['matplotlib.org']
    start_urls = ['http://matplotlib.org/examples/index.html']

    def parse(self, response):

        le = LinkExtractor(restrict_css='.toctree-wrapper .toctree-l1 .reference')
        for i in le.extract_links(response):
            yield Request(url=i.url, callback=self.parseFile)


    def parseFile(self, response):
        le = LinkExtractor(restrict_css='.reference.external')

        link = response.css('.reference.external::attr(href)').extract_first('url not found')
        link = response.urljoin(link)

        source = MatplotlibItem()
        source['file_urls'] = [link]

        return source