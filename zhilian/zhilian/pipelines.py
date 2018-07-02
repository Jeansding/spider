# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import  xlsxwriter

class ZhilianFistPipeline(object):
    # def open_spider(self, spider):
    def open_spider(self, spider):
        print('++++++++++++             ++++++++++++')
        print('++++++++++++    start    ++++++++++++')
        # 打开excel文件命名为url.xls
        # self.xls =xlsxwriter.Workbook('url.xlsx')
        # self.worksheet = self.xls.add_worksheet('myurls')
        # self.id = 0
        self.fp = open('myurls', 'w')
        print('++++++++++++      ok     ++++++++++++')
        pass

    def process_item(self, item, spider):
        if '.htm' in item['url']:
            pass
        elif 'http://jobs.zhaopin.com/' in item['url']:
            print('++++++++++++             ++++++++++++')
            print('++++++++++++    存储中    ++++++++++++')
            # id  =  'A' + str(self.id + 1)
            # # print('*****************', id, '***************************************')
            # self.worksheet.write(id, item['url'])
            # self.id = self.id +1
            self.fp.writelines(item['url'] + "\n")
            print('++++++++++++     ok      ++++++++++++')

            return item
        else:
            pass

            # def spider_closed(self, spider):

    # def spider_closed(self, spider):
    def spider_closed(self, spider):
        print('++++++++++++           ++++++++++++')
        print('++++++++++++    结束    ++++++++++++')
        self.fp.close()
        print('++++++++++++    ok    ++++++++++++')