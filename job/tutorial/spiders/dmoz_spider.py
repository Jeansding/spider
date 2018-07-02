# -*- coding: utf-8 -*-
from scrapy.loader import ItemLoader
import scrapy
from scrapy.spiders import CrawlSpider,Rule
from scrapy.linkextractors import LinkExtractor
from tutorial.items import ManhuaItem
# scrapy crawl demo -o file.csv

class DemoSpider(CrawlSpider):
    name = "demo"
    # 这里爬取两个网站，一个是自然语言处理工程师，一个是机器学习工程师
    start_urls = [
        #"http://search.51job.com/list/000000,000000,0000,00,9,99,%25E8%2587%25AA%25E7%2584%25B6%25E8%25AF%25AD%25E8%25A8%2580,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare=",
        #"http://search.51job.com/list/000000,000000,0000,00,9,99,%25E7%25AE%2597%25E6%25B3%2595%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        #"http://search.51job.com/list/000000,000000,0000,00,9,99,AI%25E5%25B7%25A5%25E7%25A8%258B%25E5%25B8%2588,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        #所有职位10万
        #"http://search.51job.com/list/000000,000000,0000,00,9,99,%2520,2,1.html?lang=c&stype=&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&providesalary=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        #月薪2万以上
        #"http://search.51job.com/list/000000,000000,0000,00,9,09,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        #月薪五万以上
        "http://search.51job.com/list/000000,000000,0000,00,9,12,%2B,2,1.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=21&dibiaoid=0&address=&line=&specialarea=00&from=&welfare="
        ]
    rules = {
        Rule(LinkExtractor(allow="http:\/\/search.51job.com\/list\/", restrict_xpaths="//div[@class='p_in']"),
             callback="paser_item", follow=True),
        # Rule(LinkExtractor(allow=""))
    }

    def paser_item(self, response):
        divs = response.xpath("//div[@class='el']")
        item = ManhuaItem()

        for div in divs:
            try:
                item['duty'] = div.xpath("./p/span/a/text()")[0].extract().strip()
                item['time'] = div.xpath("./span[4]/text()").extract()
                item['name'] = div.xpath("./span[1]/a/text()").extract()
                item['location'] = div.xpath("./span[2]/text()").extract()
                item['sallary'] = div.xpath("./span[3]/text()").extract()
                yield item
            except Exception:
                pass