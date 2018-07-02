# -*- coding: utf-8 -*-
# Author:   BinBin
# Email:    289594665@qq.com
# Time :    2017/07/27

import scrapy
from scrapy import Field

class ArticleItem(scrapy.Item):
    article_title = Field()
    article_author = Field()
    article_src = Field()
    article_url = Field()
    article_type = Field()
    article_content = Field()
    article_summary = Field()
    article_icon = Field()
    article_time = Field()
