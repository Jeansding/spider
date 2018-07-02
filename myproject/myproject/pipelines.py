# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class MyprojectPipeline(object):

    #定义开始爬虫的行为
    def open_spider(self,spider):
        self.file=open('xxx.json','wb')
        self.exporter=CustomJsonLinesItemExporter(self.file)
        self.exporter.start_exporting()
    #定义爬虫结束的行为
    def close_spider(self,spider):
        self.exporter.finish_exporting()
        self.file.close()
    #定义爬虫过程中的行为
    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item