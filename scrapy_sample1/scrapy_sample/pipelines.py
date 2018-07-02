# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


import pymongo


class BudejieMongoPipeline(object):
    "将百思不得姐段子保存到MongoDB中"
    collection_name = 'jokes'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE', 'jeans')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item


import pymysql


class BudejiePostgrePipeline(object):
    "将百思不得姐段子保存到MySQL中"

    def __init__(self):
        self.connection = pymysql.connect(host='192.168.50.90', port=3306, user='root', passwd='hunteron', db='test', charset='utf8')
        self.connection.autocommit = True

    def open_spider(self, spider):
        self.cursor = self.connection.cursor()

    def close_spider(self, spider):
        self.cursor.close()
        self.connection.close()

    def process_item(self, item, spider):
        self.cursor.execute('insert into joke(author,content) values(%s,%s)', (item['username'], item['content']))
        return item


from scrapy.pipelines.images import ImagesPipeline
from scrapy.http import Request


class RawFilenameImagePipeline(ImagesPipeline):
    def file_path(self, request, response=None, info=None):
        if not isinstance(request, Request):
            url = request
        else:
            url = request.url
        beg = url.rfind('/') + 1
        end = url.rfind('.')
        if end == -1:
            return 'full/{}.jpg'.format(url[beg:])
        else:
            return 'full/{}.jpg'.format(url[beg:end])


class RefererImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        requests = super().get_media_requests(item, info)
        for req in requests:
            req.headers.appendlist("referer", item['referer'])
        return requests


class CsdnBlogBackupPipeline(object):
    def process_item(self, item, spider):
        dirname = 'blogs'
        import os
        import codecs
        if not os.path.exists(dirname):
            os.mkdir(dirname)
        with codecs.open('{}{}{}.md'.format(dirname,os.sep,item["title"]), 'w', encoding='utf-8') as f:
            f.write(item['content'])
            f.close()
        return item
