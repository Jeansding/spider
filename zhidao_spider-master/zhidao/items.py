# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ZhidaoItem(scrapy.Item):
    # define the fields for your item here like:
    question_id = scrapy.Field()
    question_title = scrapy.Field()
    best_answer = scrapy.Field()
    answers = scrapy.Field()
    question_content = scrapy.Field()
    team_id = scrapy.Field()
    pass
