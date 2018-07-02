# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class MovieItem(Item):
    title = Field()
    movieInfo = Field()
    star = Field()
    quote = Field()
    url = Field()
    intro = Field()
    pass
