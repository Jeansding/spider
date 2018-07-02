# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class CompanyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    
    firstUrl = scrapy.Field()
    firstName = scrapy.Field()
    hangye = scrapy.Field()

    lianxiren = scrapy.Field()
    telephone = scrapy.Field()
    companyName = scrapy.Field()
    youbian = scrapy.Field()
    zhuye = scrapy.Field()

    companyType = scrapy.Field()
    companyProduct = scrapy.Field()
    companyLocal = scrapy.Field()
    pass
