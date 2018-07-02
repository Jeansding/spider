# -*- coding: utf-8 -*-
import scrapy
from scrapy_sample.items import ImageItem

# cd C:\Users\Mengcao.Quan\spider\scrapy_sample\scrapy_sample
#  scrapy crawl meizitu
class MeizituSpider(scrapy.Spider):
    name = 'meizitu'
    start_urls=[]
    for i in range(4001,5585):
        start_urls.append('http://www.meizitu.com/a/'+str(i)+'.html')

    def parse(self, response):
        yield ImageItem(image_urls=response.css('div#picture img::attr(src)').extract())
