# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class JobspiderItem(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()
    job_company_name = scrapy.Field()
    job_place = scrapy.Field()
    job_salary = scrapy.Field()
    job_time = scrapy.Field()
    job_type = scrapy.Field()
    fan_kui_lv = scrapy.Field()