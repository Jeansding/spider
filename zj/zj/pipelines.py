# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#pipeline:俗称管道,用于接收爬虫返回的item数据.

class JobspiderPipeline(object):
    def process_item(self, item, spider):
        return item


class ToCsvPipeline(object):
    def process_item(self, item, spider):
        with open("job.csv", "a", encoding="gb18030") as f:
            job_name = item['job_name']
            job_company_name = item['job_company_name']
            job_place = item['job_place']
            job_salary = item['job_salary']
            job_time = item['job_time']
            job_type = item['job_type']
            fan_kui_lv = item['fan_kui_lv']
            job_info = [job_name, job_company_name, job_place, job_salary, job_time, job_type, fan_kui_lv, "\n"]
            f.write(",".join(job_info))
        #把item传递给下一个pipeline做处理
        return item