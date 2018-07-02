# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    targetUrl = scrapy.Field()
    docName = scrapy.Field()

    jobClass = scrapy.Field()
    jobUrl = scrapy.Field()

    jobName = scrapy.Field()
    jobPlace = scrapy.Field()
    jobMoney = scrapy.Field()
    jobNeed = scrapy.Field()
    jobCompany = scrapy.Field()
    jobType = scrapy.Field()
    jobSpesk = scrapy.Field()
    pass
