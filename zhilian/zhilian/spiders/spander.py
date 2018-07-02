# -*- coding:utf-8 -*-
import scrapy
from zhilian.items import ZhilianFistItem
#scrapy crawl zhilian_url -o file.csv

class zhilian_url(scrapy.Spider):
    name = 'zhilian_url'
    start_urls = ['http://jobs.zhaopin.com/']

    def parse(self, response):
        myurl = ZhilianFistItem()

        urls = response.xpath('/html/body/div/div/div/a[@target="_blank"]/@href').extract()
        # if len(urls) == 0:
        #     print('+++++++++++++++++++     空空空空空空空     +++++++++++++++++++++++++')
        for url in urls:
            myurl['url'] = url
            # print('---------begin-----------------------------------------')
            # print(url)
            # print('---------end-----------------------------------------')
            yield myurl

    pass

