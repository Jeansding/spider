# -*- coding: utf-8 -*-


BOT_NAME = 'zhilian_fist'

SPIDER_MODULES = ['zhilian_fist.spiders']
NEWSPIDER_MODULE = 'zhilian_fist.spiders'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DEFAULT_REQUEST_HEADERS = {
    'Host': 'jobs.zhaopin.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:53.0) Gecko/20100101 Firefox/53.0'
}

ITEM_PIPELINES = {
    'zhilian_fist.pipelines.ZhilianFistPipeline': 300,
}