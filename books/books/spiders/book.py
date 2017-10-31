# -*- coding: utf-8 -*-

import scrapy
from ..items import BooksItem
from scrapy.linkextractors import LinkExtractor
from scrapy import Request


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):

        # 提取一页中所有书的链接
        # book = response.css('article.product_pod h3 a::attr(href)').extract()
        # for i in book:
        #     i = response.urljoin(i)
        #     yield Request(url=i, callback=self.parseBook)


        # 提取一页中所有书的链接   使用 LinkExtractor
        le = LinkExtractor(restrict_css='.product_pod h3 a')
        links = le.extract_links(response)
        for i in links:
            yield Request(url=i.url, callback=self.parseBook)

        # 获取下一页链接
        # nextUrl = response.css('.next a::attr(href)').extract_first('nextUrl not found')
        # if nextUrl != 'nextUrl not found':
        #     yield Request(url=response.urljoin(nextUrl), callback=self.parse)

        # 获取下一页链接   使用 LinkExtractor
        le = LinkExtractor(restrict_css='.next')
        links = le.extract_links(response)

        if links:
            nextUrl = links[0].url
            yield Request(nextUrl, callback=self.parse)

    def parseBook(self, response):
        book = BooksItem()

        book['name'] = response.css('.product_main h1::text').extract_first('title not found')
        book['price'] = response.css('.product_main .price_color::text').extract_first('price not found')

        yield book
