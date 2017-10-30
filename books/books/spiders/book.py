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

        # le = LinkExtractor(restrict_css='article.product_pod h3')
        #
        # for link in le.extract_links(response):
        #     yield Request(link.url, callback=self.parseBook)

        # le = LinkExtractor(restrict_css='ul.pager li.next')
        # link = le.extract_links(response)
        # if link:
        #     nextUrl = link[0].url
        #     yield Request(nextUrl, callback=self.parse)
        book = BooksItem()
        books = response.css('article.product_pod')
        for i in books:

            book['name'] = i.css('h3 a::attr(title)').extract_first('name is not found')
            book['price'] = i.css('.product_price .price_color::text').extract_first('price is not found')

            yield book

    # def parseBook(self, response):
    #         book = BooksItem()
    #         book['name'] = book.css('h3 a::attr(title)').extract_first('name is not found')
    #         book['price'] = book.css('.product_price .price_color::text').extract_first('price is not found')
    #
    #         yield book
