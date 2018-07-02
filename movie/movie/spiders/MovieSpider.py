#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel

from scrapy.spiders import Spider
from scrapy.http import Request
from scrapy.selector import Selector

from movie.items import MovieItem

from bs4 import BeautifulSoup

# scrapy crawl movie
class MovieSpider(Spider):
    name = 'movie'
    url = 'https://movie.douban.com/top250'
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        selector = Selector(response)
        movies = selector.xpath('//div[@class="info"]')
        for movie in movies:
            item = MovieItem()
            title = movie.xpath('div[@class="hd"]/a/span/text()').extract()
            fullTitle = ''
            for each in title:
                fullTitle += each
            movieInfo = movie.xpath('div[@class="bd"]/p/text()').extract()
            star = movie.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = movie.xpath('div[@class="bd"]/p/span/text()').extract()
            url1 = movie.xpath('div[@class="hd"]/a/@href').extract()[0]
            if quote:
                quote = quote[0]
            else:
                quote = ''
            item['title'] = fullTitle
            item['movieInfo'] = ';'.join(movieInfo).replace(' ', '').replace('\n', '')
            item['star'] = star[0]
            item['quote'] = quote
            item['url'] = url1
            print(url1)
            yield Request(url1, callback=self.parseContent, meta={'item': item})
        nextPage = selector.xpath('//span[@class="next"]/link/@href').extract()
        if nextPage:
            nextPage = nextPage[0]
            print(self.url + str(nextPage))
            yield Request(self.url + str(nextPage), callback=self.parse)

    def parseContent(self, response):
        selector = Selector(response)
        item = response.meta['item']
        content = selector.xpath('//span[@class="related-info"]/span[@class="indent"]/span/text()').extract()
        if content:
            item['intro'] = content[0].strip()
        else:
            content = selector.xpath('//span[@class="all hidden"]/text()').extract()
            if content:
                item['intro'] = content[0]
            else:
                item['intro'] = ''
        yield item
