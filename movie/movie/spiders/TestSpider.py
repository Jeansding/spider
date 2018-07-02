#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
from scrapy.selector import Selector
from scrapy.spiders import Spider


class TestSpider(Spider):
    name = 'test'
    start_urls = 'https://movie.douban.com/subject/1292213/'

    def parse(self, response):
        selector = Selector(response)
        return selector.xpath('//span[@class="related-info"]/span[@class="indent"]/span/text()').extract()
