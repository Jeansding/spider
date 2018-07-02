# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import urllib.parse
username = urllib.parse.quote_plus('root')
password = urllib.parse.quote_plus('123456')

class QiubaiPipeline(object):
    pass

    # def __init__(self):
    #     self.connection = pymongo.MongoClient('mongodb://%s:%s@192.168.50.50' % (username, password))
    #     self.db = self.connection.jeans  # 切换到scrapy数据库
    #     self.collection = self.db.qiubai  # 获取到qiubai集合
    #
    # def process_item(self, item, spider):
    #     if not self.connection or not item:
    #         return
    #     self.collection.save(item)
    #
    #
    # def __del__(self):
    #     if self.connection:
    #         self.connection.close()
