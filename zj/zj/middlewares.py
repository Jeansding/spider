# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/spider-middleware.html

# from scrapy import signals


class JobUserMiddleware(object):
    """This middleware allows spiders to override the user_agent"""

    def __init__(self, user_agent='Scrapy',name=''):
        self.user_agent = UserAgent()

    @classmethod
    def from_crawler(cls, crawler):
        # o = cls(crawler.settings['USER_AGENT'],'张三')
        # cls后的数据会自动赋值给构造函数的对应参数

        o = cls()
        # crawler.signals.connect(o.spider_opened, signal=signals.spider_opened)
        return o

    def spider_opened(self, spider):
        # =右边代码的含义是从spider中获得user_agent的属性,
        # 如果没有默认为self.user_agent的内容
        # self.user_agent = getattr(spider, 'user_agent', self.user_agent)
        pass

    def process_request(self, request, spider):
        if self.user_agent:
            request.headers.setdefault(b'User-Agent', self.user_agent.random)
