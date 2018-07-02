#!/usr/bin/env python3
# -*- coding:utf-8 -*- 
# Author: lionel
import random

from scrapy.conf import settings
import logging

logger = logging.getLogger('movie.middlewares.proxy')


class StaticProxyMiddleWare(object):
    def process_request(self, request, spider):
        proxy = settings.get('PROXY')
        logger.info("process request %s using proxy %s" % (request, proxy))
        request.meta['proxy'] = proxy
        pass


class RandomProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = random.choice(settings.get('PROXY_LIST'))
        logger.info("process request %s using proxy %s" % (request, proxy))
        request.meta['proxy'] = proxy
