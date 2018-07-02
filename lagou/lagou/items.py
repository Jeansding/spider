# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import re
import scrapy
from scrapy.loader.processors import TakeFirst, MapCompose, Join
from scrapy.loader import ItemLoader

class FirstItemLoader(ItemLoader):
    # 自定义itemloader，继承scrapy的ItemLoader类
    default_output_processor = TakeFirst()

def remove_splash(value):
    # 去掉工作城市的斜线
    return value.replace("/", "")

class LagouJobItem(scrapy.Item):
    # 拉勾网职位信息
    title = scrapy.Field()
    url = scrapy.Field()
    url_object_id = scrapy.Field()
    salary = scrapy.Field()
    job_city = scrapy.Field(input_processor=MapCompose(remove_splash))
    work_years = scrapy.Field(input_processor=MapCompose(remove_splash))
    degree_need = scrapy.Field(input_processor=MapCompose(remove_splash))
    job_type = scrapy.Field()
    publish_time = scrapy.Field()
    job_advantage = scrapy.Field()
    job_desc = scrapy.Field()
    job_addr = scrapy.Field()
    company_name = scrapy.Field()
    company_url = scrapy.Field()
    tags = scrapy.Field(input_processor=Join(","))
    crawl_time = scrapy.Field()