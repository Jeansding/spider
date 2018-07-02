# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#Item是需要的数据进行格式化，方便后期处理
class MyItem(scrapy.Item):
    user = scrapy.Field()
    content = scrapy.Field()
    godComment = scrapy.Field()
